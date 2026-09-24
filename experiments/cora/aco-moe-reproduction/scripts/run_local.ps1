param(
    [ValidateSet('probe','data','adapter','policy','eval')]
    [string]$Stage = 'probe'
)
$ErrorActionPreference = 'Stop'
Set-Location (Split-Path $PSScriptRoot -Parent)
$env:MUJOCO_GL = 'glfw'
$env:PYTHONUNBUFFERED = '1'
$env:PYTHONIOENCODING = 'utf-8'
$env:OMP_NUM_THREADS = '4'
$env:MKL_NUM_THREADS = '4'
$pythonLocal = Join-Path (Get-Location) '.venv/Scripts/python.exe'
$runRoot = 'runs/local_initial'
New-Item -ItemType Directory -Force -Path $runRoot | Out-Null
function Run-Python([string[]]$Arguments, [string]$LogName) {
    $timerLocal = [System.Diagnostics.Stopwatch]::StartNew()
    & $pythonLocal @Arguments 2>&1 | Tee-Object -FilePath "$runRoot/$LogName.log"
    $codeLocal = $LASTEXITCODE
    $timerLocal.Stop()
    @{stage=$LogName; seconds=$timerLocal.Elapsed.TotalSeconds; exit_code=$codeLocal;
        completed_at=(Get-Date -Format o); arguments=$Arguments} | ConvertTo-Json -Compress |
        Add-Content "$runRoot/timings.jsonl" -Encoding utf8
    if ($codeLocal -ne 0) { throw "Python failed: $LogName (exit $codeLocal)" }
}
switch ($Stage) {
    'probe' { Run-Python @('-m','scripts.local_probe') 'probe' }
    'data' {
        Run-Python @('-m','scripts.generate_vdcs_dataset','--out_h5_dir','data/local_initial',
            '--tasks','walker_walk','--samples_per_task','100','--size','64','64',
            '--max_episode_steps','20','--train_ratio','0.8','--seed','0') 'data'
    }
    'adapter' {
        Run-Python @('-m','scripts.train_aco_moe',
            '--data_roots','data/local_initial/walker_walk_vdcs_seg64_split',
            '--output_dir','checkpoints/local_initial/adapter','--log_dir','logs/local_initial/adapter',
            '--base_channels','16','--num_experts','7','--batch_size','4','--val_batch_size','4',
            '--num_workers','0','--steps','101','--lambda_final','1',
            '--print_freq','20','--val_freq','50','--save_freq','100','--vis_freq','50') 'adapter'
    }
    'policy' {
        Run-Python @('dreamer.py','--configs','dmc_vision','local_initial',
            '--task','dmc_walker_walk','--logdir','logdir/local_initial/clean','--seed','0') 'policy'
    }
    'eval' {
        $policyPath = 'logdir/local_initial/clean/latest.pt'
        if (-not (Test-Path $policyPath)) { throw 'Train the policy stage first.' }
        $beforeHash = (Get-FileHash -LiteralPath $policyPath -Algorithm SHA256).Hash
        foreach ($condition in @('clean','corrupted','aco')) {
            $argumentsLocal = @('dreamer.py','--configs','dmc_vision','local_initial')
            if ($condition -ne 'clean') { $argumentsLocal += 'adapt_vdcs_markov_temporal' }
            $argumentsLocal += @('--eval_only','True','--policy_checkpoint',$policyPath,
                '--logdir',"logdir/local_initial/eval_$condition",'--seed','10','--eval_episode_num','1')
            if ($condition -eq 'corrupted') { $argumentsLocal += @('--use_dual_stream_unet_restore','False') }
            if ($condition -eq 'aco') {
                $argumentsLocal += @('--dual_stream_unet_checkpoint','checkpoints/local_initial/adapter/moe_unet_best.pth')
            }
            Run-Python $argumentsLocal "eval_$condition"
        }
        $afterHash = (Get-FileHash -LiteralPath $policyPath -Algorithm SHA256).Hash
        if ($beforeHash -ne $afterHash) { throw 'Policy checkpoint changed during evaluation.' }
        @{policy_sha256=$afterHash; unchanged=$true} | ConvertTo-Json |
            Set-Content "$runRoot/frozen_policy_check.json" -Encoding utf8
    }
}
