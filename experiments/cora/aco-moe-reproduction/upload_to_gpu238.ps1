param(
    [string]$Destination = "/home/gpuadmin/CST/CORA/aco-moe-reproduction",
    [switch]$UpdateExisting
)

$ErrorActionPreference = "Stop"
$ProjectRoot = $PSScriptRoot
$Archive = Join-Path $env:TEMP "aco-moe-reproduction.tar.gz"
$RemoteArchive = "/tmp/aco-moe-reproduction-$([guid]::NewGuid().ToString('N')).tar.gz"

Write-Host "Inspecting remote destination: $Destination"
$exists = ssh gpu-238 "if test -e '$Destination'; then echo EXISTS; find '$Destination' -mindepth 1 -maxdepth 2 -type d | head -n 30; else echo MISSING; fi"
$exists | ForEach-Object { Write-Host $_ }
if (($exists -contains "EXISTS") -and -not $UpdateExisting) {
    throw "Destination exists. Inspect it above, then rerun with -UpdateExisting if it belongs to this project."
}

if (Test-Path -LiteralPath $Archive) { Remove-Item -LiteralPath $Archive -Force }
try {
    Push-Location $ProjectRoot
    tar --exclude=.git --exclude=.venv --exclude=data --exclude=checkpoints `
        --exclude=logdir --exclude=logs --exclude=runs --exclude='*.pyc' `
        --exclude=__pycache__ -czf $Archive .
    if ($LASTEXITCODE -ne 0) { throw "Failed to create source archive." }
    scp $Archive "gpu-238:$RemoteArchive"
    if ($LASTEXITCODE -ne 0) { throw "Failed to upload source archive." }
    ssh gpu-238 "mkdir -p '$Destination' && tar -xzf '$RemoteArchive' -C '$Destination' && rm -f '$RemoteArchive'"
    if ($LASTEXITCODE -ne 0) { throw "Failed to extract source archive." }
    Write-Host "Uploaded source to $Destination"
    Write-Host "Next: cd $Destination && bash reproduction/00_preflight.sh"
}
finally {
    Pop-Location
    if (Test-Path -LiteralPath $Archive) { Remove-Item -LiteralPath $Archive -Force }
}
