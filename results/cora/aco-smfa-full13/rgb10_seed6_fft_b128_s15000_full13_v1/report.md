# Full13 seed6 results

All 13 types are training-seen. Former OOD6 use fallback_v1; this is not a zero-shot OOD experiment.

One training seed per model. +/- denotes episode SD, not training-seed uncertainty. Pooled cross-task SD also contains task differences.

## Overall control

| Protocol | Raw | ACO | SMFA |
|---|---:|---:|---:|
| markov | 483.41 +/- 353.71 (n=100) | 319.03 +/- 317.42 (n=100) | 640.65 +/- 335.70 (n=100) |
| single/all | 460.57 +/- 396.01 (n=650) | 316.72 +/- 364.93 (n=650) | 641.44 +/- 380.33 (n=650) |

Clean: 734.21 +/- 334.50 (n=50)

## Image restoration

| Model / group | n | PSNR-Y | SSIM-Y | PSNR-RGB | SSIM-RGB |
|---|---:|---:|---:|---:|---:|
| aco/all | 130000 | 23.2963 | 0.767038 | 19.6705 | 0.641638 |
| aco/task/walker_walk | 13000 | 22.4618 | 0.772798 | 19.1970 | 0.646981 |
| aco/degradation/rain | 10000 | 24.7413 | 0.835628 | 18.2279 | 0.730117 |
| aco/walker_walk/rain | 1000 | 24.6112 | 0.860330 | 18.3278 | 0.744309 |
| aco/degradation/fog | 10000 | 18.9914 | 0.843650 | 17.7505 | 0.598502 |
| aco/walker_walk/fog | 1000 | 18.5871 | 0.833364 | 17.3587 | 0.591917 |
| aco/degradation/snow | 10000 | 20.0476 | 0.690882 | 16.6378 | 0.631568 |
| aco/walker_walk/snow | 1000 | 20.1774 | 0.724476 | 16.7996 | 0.653744 |
| aco/degradation/motion_blur | 10000 | 24.5244 | 0.820118 | 22.2663 | 0.768999 |
| aco/walker_walk/motion_blur | 1000 | 21.6298 | 0.790855 | 20.2500 | 0.747147 |
| aco/degradation/gaussian_noise | 10000 | 22.4808 | 0.520071 | 17.8192 | 0.294491 |
| aco/walker_walk/gaussian_noise | 1000 | 22.1648 | 0.556991 | 17.8458 | 0.336302 |
| aco/degradation/low_light | 10000 | 22.4758 | 0.403812 | 18.2810 | 0.237396 |
| aco/walker_walk/low_light | 1000 | 21.1359 | 0.389677 | 17.8671 | 0.231863 |
| aco/degradation/jpeg | 10000 | 23.7391 | 0.859207 | 19.0507 | 0.705202 |
| aco/walker_walk/jpeg | 1000 | 23.3178 | 0.865785 | 18.8405 | 0.700232 |
| aco/degradation/defocus_blur | 10000 | 25.3838 | 0.848859 | 23.1878 | 0.800171 |
| aco/walker_walk/defocus_blur | 1000 | 22.3784 | 0.828110 | 21.0712 | 0.783242 |
| aco/degradation/frost | 10000 | 23.2027 | 0.928226 | 18.4600 | 0.856172 |
| aco/walker_walk/frost | 1000 | 22.2099 | 0.925227 | 18.4233 | 0.860247 |
| aco/degradation/occlusion_patch | 10000 | 25.7248 | 0.887738 | 23.7004 | 0.867573 |
| aco/walker_walk/occlusion_patch | 1000 | 24.5957 | 0.881773 | 22.6137 | 0.856532 |
| aco/degradation/saturation | 10000 | 23.4195 | 0.948201 | 19.9015 | 0.690671 |
| aco/walker_walk/saturation | 1000 | 23.5128 | 0.948450 | 19.4959 | 0.694432 |
| aco/degradation/shadow | 10000 | 26.4734 | 0.954664 | 23.4654 | 0.929545 |
| aco/walker_walk/shadow | 1000 | 26.2531 | 0.956986 | 23.6465 | 0.934324 |
| aco/degradation/shot_noise | 10000 | 21.6466 | 0.430443 | 16.9682 | 0.230893 |
| aco/walker_walk/shot_noise | 1000 | 21.4290 | 0.484351 | 17.0203 | 0.276456 |
| aco/task/walker_run | 13000 | 22.4214 | 0.771785 | 19.1717 | 0.644871 |
| aco/walker_run/rain | 1000 | 24.6090 | 0.859267 | 18.3263 | 0.741049 |
| aco/walker_run/fog | 1000 | 18.5730 | 0.831760 | 17.3394 | 0.588065 |
| aco/walker_run/snow | 1000 | 20.1706 | 0.725419 | 16.7994 | 0.653340 |
| aco/walker_run/motion_blur | 1000 | 21.5148 | 0.785650 | 20.1703 | 0.741499 |
| aco/walker_run/gaussian_noise | 1000 | 22.1253 | 0.556208 | 17.8365 | 0.336799 |
| aco/walker_run/low_light | 1000 | 21.0785 | 0.390731 | 17.8364 | 0.230871 |
| aco/walker_run/jpeg | 1000 | 23.2599 | 0.862343 | 18.8239 | 0.694395 |
| aco/walker_run/defocus_blur | 1000 | 22.2376 | 0.825592 | 20.9459 | 0.780030 |
| aco/walker_run/frost | 1000 | 22.2170 | 0.924301 | 18.4320 | 0.856951 |
| aco/walker_run/occlusion_patch | 1000 | 24.4852 | 0.880489 | 22.5098 | 0.854558 |
| aco/walker_run/saturation | 1000 | 23.5255 | 0.947814 | 19.4992 | 0.693349 |
| aco/walker_run/shadow | 1000 | 26.2765 | 0.956964 | 23.6856 | 0.933975 |
| aco/walker_run/shot_noise | 1000 | 21.4049 | 0.486668 | 17.0282 | 0.278443 |
| aco/task/walker_stand | 13000 | 22.4849 | 0.771043 | 19.2912 | 0.639287 |
| aco/walker_stand/rain | 1000 | 24.5441 | 0.857309 | 18.3772 | 0.725188 |
| aco/walker_stand/fog | 1000 | 18.8412 | 0.820165 | 17.5601 | 0.557071 |
| aco/walker_stand/snow | 1000 | 20.1328 | 0.716669 | 16.8360 | 0.641156 |
| aco/walker_stand/motion_blur | 1000 | 21.7314 | 0.801284 | 20.3845 | 0.757682 |
| aco/walker_stand/gaussian_noise | 1000 | 21.9514 | 0.544466 | 17.7806 | 0.324156 |
| aco/walker_stand/low_light | 1000 | 21.0218 | 0.386658 | 17.7969 | 0.222560 |
| aco/walker_stand/jpeg | 1000 | 23.1873 | 0.862989 | 18.9184 | 0.693689 |
| aco/walker_stand/defocus_blur | 1000 | 22.4562 | 0.841174 | 21.1981 | 0.796928 |
| aco/walker_stand/frost | 1000 | 22.0500 | 0.921524 | 18.4382 | 0.847219 |
| aco/walker_stand/occlusion_patch | 1000 | 24.8270 | 0.884120 | 22.7851 | 0.855935 |
| aco/walker_stand/saturation | 1000 | 23.6638 | 0.946366 | 19.6547 | 0.682229 |
| aco/walker_stand/shadow | 1000 | 26.5933 | 0.958605 | 24.0123 | 0.934813 |
| aco/walker_stand/shot_noise | 1000 | 21.3027 | 0.482231 | 17.0439 | 0.272106 |
| aco/task/hopper_stand | 13000 | 23.9228 | 0.770626 | 19.9049 | 0.647113 |
| aco/hopper_stand/rain | 1000 | 26.3972 | 0.874423 | 18.0993 | 0.760614 |
| aco/hopper_stand/fog | 1000 | 18.9058 | 0.849281 | 17.4801 | 0.644164 |
| aco/hopper_stand/snow | 1000 | 21.5320 | 0.741071 | 16.8682 | 0.651477 |
| aco/hopper_stand/motion_blur | 1000 | 26.1660 | 0.855919 | 23.6872 | 0.809593 |
| aco/hopper_stand/gaussian_noise | 1000 | 23.0209 | 0.485078 | 18.2527 | 0.252948 |
| aco/hopper_stand/low_light | 1000 | 23.4426 | 0.399177 | 19.0888 | 0.227252 |
| aco/hopper_stand/jpeg | 1000 | 24.1927 | 0.857479 | 19.8369 | 0.726202 |
| aco/hopper_stand/defocus_blur | 1000 | 26.8177 | 0.875369 | 24.6071 | 0.832049 |
| aco/hopper_stand/frost | 1000 | 25.2742 | 0.937645 | 18.0780 | 0.841987 |
| aco/hopper_stand/occlusion_patch | 1000 | 25.6324 | 0.879295 | 23.7128 | 0.861149 |
| aco/hopper_stand/saturation | 1000 | 21.7915 | 0.942283 | 18.8797 | 0.701265 |
| aco/hopper_stand/shadow | 1000 | 25.8876 | 0.950868 | 23.0253 | 0.925339 |
| aco/hopper_stand/shot_noise | 1000 | 21.9359 | 0.370251 | 17.1476 | 0.178435 |
| aco/task/quadruped_run | 13000 | 23.4011 | 0.749309 | 19.5770 | 0.615687 |
| aco/quadruped_run/rain | 1000 | 27.0438 | 0.839328 | 18.5718 | 0.675018 |
| aco/quadruped_run/fog | 1000 | 18.3867 | 0.841565 | 17.3314 | 0.593161 |
| aco/quadruped_run/snow | 1000 | 21.3898 | 0.712628 | 17.3578 | 0.648268 |
| aco/quadruped_run/motion_blur | 1000 | 23.0032 | 0.748665 | 21.2121 | 0.691278 |
| aco/quadruped_run/gaussian_noise | 1000 | 21.9008 | 0.523404 | 17.6325 | 0.305430 |
| aco/quadruped_run/low_light | 1000 | 21.8523 | 0.364034 | 17.9002 | 0.216151 |
| aco/quadruped_run/jpeg | 1000 | 23.1961 | 0.803055 | 18.7830 | 0.658641 |
| aco/quadruped_run/defocus_blur | 1000 | 24.0022 | 0.778111 | 22.2750 | 0.719600 |
| aco/quadruped_run/frost | 1000 | 25.8940 | 0.896195 | 19.1992 | 0.772119 |
| aco/quadruped_run/occlusion_patch | 1000 | 25.2369 | 0.879988 | 23.1683 | 0.855930 |
| aco/quadruped_run/saturation | 1000 | 23.9476 | 0.947446 | 20.1543 | 0.693734 |
| aco/quadruped_run/shadow | 1000 | 27.1317 | 0.957182 | 24.0602 | 0.932244 |
| aco/quadruped_run/shot_noise | 1000 | 21.2293 | 0.449413 | 16.8556 | 0.242356 |
| aco/task/finger_turn_hard | 13000 | 22.5601 | 0.770189 | 19.3469 | 0.639266 |
| aco/finger_turn_hard/rain | 1000 | 23.6466 | 0.854631 | 18.2584 | 0.754087 |
| aco/finger_turn_hard/fog | 1000 | 19.0350 | 0.811268 | 17.8085 | 0.558229 |
| aco/finger_turn_hard/snow | 1000 | 19.4916 | 0.724055 | 16.5789 | 0.664102 |
| aco/finger_turn_hard/motion_blur | 1000 | 22.2715 | 0.754149 | 20.4067 | 0.687836 |
| aco/finger_turn_hard/gaussian_noise | 1000 | 22.0133 | 0.564486 | 17.7114 | 0.346431 |
| aco/finger_turn_hard/low_light | 1000 | 21.6240 | 0.442693 | 17.9533 | 0.268357 |
| aco/finger_turn_hard/jpeg | 1000 | 23.1536 | 0.852830 | 18.7884 | 0.658796 |
| aco/finger_turn_hard/defocus_blur | 1000 | 22.9828 | 0.804593 | 21.4721 | 0.751479 |
| aco/finger_turn_hard/frost | 1000 | 21.5367 | 0.919783 | 18.3286 | 0.861971 |
| aco/finger_turn_hard/occlusion_patch | 1000 | 25.6196 | 0.892702 | 23.3729 | 0.866638 |
| aco/finger_turn_hard/saturation | 1000 | 23.6546 | 0.941404 | 19.8028 | 0.669124 |
| aco/finger_turn_hard/shadow | 1000 | 26.8682 | 0.953823 | 24.0176 | 0.930125 |
| aco/finger_turn_hard/shot_noise | 1000 | 21.3839 | 0.496041 | 17.0103 | 0.293286 |
| aco/task/cartpole_swingup_sparse | 13000 | 24.1910 | 0.761392 | 19.9985 | 0.640262 |
| aco/cartpole_swingup_sparse/rain | 1000 | 26.0965 | 0.887364 | 17.9933 | 0.781673 |
| aco/cartpole_swingup_sparse/fog | 1000 | 19.1302 | 0.844177 | 17.6525 | 0.638124 |
| aco/cartpole_swingup_sparse/snow | 1000 | 21.4040 | 0.760163 | 16.8041 | 0.689231 |
| aco/cartpole_swingup_sparse/motion_blur | 1000 | 27.2244 | 0.769312 | 23.8170 | 0.704128 |
| aco/cartpole_swingup_sparse/gaussian_noise | 1000 | 22.9877 | 0.520875 | 18.1628 | 0.288000 |
| aco/cartpole_swingup_sparse/low_light | 1000 | 23.5556 | 0.388416 | 18.9593 | 0.226438 |
| aco/cartpole_swingup_sparse/jpeg | 1000 | 24.3803 | 0.836489 | 19.9253 | 0.716531 |
| aco/cartpole_swingup_sparse/defocus_blur | 1000 | 28.2368 | 0.780836 | 25.1275 | 0.726142 |
| aco/cartpole_swingup_sparse/frost | 1000 | 25.6873 | 0.933937 | 18.1044 | 0.833590 |
| aco/cartpole_swingup_sparse/occlusion_patch | 1000 | 26.0084 | 0.886110 | 24.2501 | 0.871122 |
| aco/cartpole_swingup_sparse/saturation | 1000 | 22.0101 | 0.936564 | 19.2375 | 0.714619 |
| aco/cartpole_swingup_sparse/shadow | 1000 | 25.8664 | 0.947258 | 22.8693 | 0.923042 |
| aco/cartpole_swingup_sparse/shot_noise | 1000 | 21.8956 | 0.406589 | 17.0780 | 0.210760 |
| aco/task/cup_catch | 13000 | 24.2450 | 0.759752 | 20.6110 | 0.628401 |
| aco/cup_catch/rain | 1000 | 24.0791 | 0.825177 | 18.3126 | 0.715749 |
| aco/cup_catch/fog | 1000 | 19.2034 | 0.799786 | 18.1728 | 0.517468 |
| aco/cup_catch/snow | 1000 | 19.3989 | 0.659171 | 16.5380 | 0.600777 |
| aco/cup_catch/motion_blur | 1000 | 28.9146 | 0.859958 | 25.3334 | 0.802396 |
| aco/cup_catch/gaussian_noise | 1000 | 21.8229 | 0.459623 | 17.6395 | 0.239502 |
| aco/cup_catch/low_light | 1000 | 25.3041 | 0.448605 | 19.6658 | 0.255619 |
| aco/cup_catch/jpeg | 1000 | 23.2900 | 0.838857 | 19.3564 | 0.696613 |
| aco/cup_catch/defocus_blur | 1000 | 30.2033 | 0.874541 | 26.3574 | 0.820644 |
| aco/cup_catch/frost | 1000 | 21.5396 | 0.916359 | 18.4423 | 0.862216 |
| aco/cup_catch/occlusion_patch | 1000 | 27.4488 | 0.898077 | 25.1197 | 0.871612 |
| aco/cup_catch/saturation | 1000 | 24.1138 | 0.945141 | 20.9642 | 0.654749 |
| aco/cup_catch/shadow | 1000 | 28.5791 | 0.961981 | 25.0040 | 0.935925 |
| aco/cup_catch/shot_noise | 1000 | 21.2868 | 0.389495 | 17.0365 | 0.195943 |
| aco/task/reacher_easy | 13000 | 23.3850 | 0.772441 | 19.6252 | 0.656876 |
| aco/reacher_easy/rain | 1000 | 23.1676 | 0.753491 | 18.0165 | 0.705278 |
| aco/reacher_easy/fog | 1000 | 19.4726 | 0.901260 | 18.3079 | 0.645594 |
| aco/reacher_easy/snow | 1000 | 18.3839 | 0.576386 | 15.8911 | 0.558850 |
| aco/reacher_easy/motion_blur | 1000 | 25.4224 | 0.914000 | 23.0198 | 0.867718 |
| aco/reacher_easy/gaussian_noise | 1000 | 23.2234 | 0.498447 | 17.6078 | 0.263421 |
| aco/reacher_easy/low_light | 1000 | 22.8648 | 0.424285 | 17.8204 | 0.254373 |
| aco/reacher_easy/jpeg | 1000 | 24.3684 | 0.902677 | 18.4318 | 0.743088 |
| aco/reacher_easy/defocus_blur | 1000 | 26.2247 | 0.935273 | 23.7611 | 0.887955 |
| aco/reacher_easy/frost | 1000 | 22.8325 | 0.953584 | 18.5855 | 0.913449 |
| aco/reacher_easy/occlusion_patch | 1000 | 26.4680 | 0.895483 | 24.4667 | 0.889209 |
| aco/reacher_easy/saturation | 1000 | 23.9529 | 0.962319 | 20.4599 | 0.701885 |
| aco/reacher_easy/shadow | 1000 | 25.4657 | 0.950349 | 22.0769 | 0.922122 |
| aco/reacher_easy/shot_noise | 1000 | 22.1586 | 0.374173 | 16.6828 | 0.186443 |
| aco/task/reacher_hard | 13000 | 23.8896 | 0.771050 | 19.9815 | 0.657640 |
| aco/reacher_hard/rain | 1000 | 23.2179 | 0.744959 | 17.9958 | 0.698203 |
| aco/reacher_hard/fog | 1000 | 19.7794 | 0.903879 | 18.4931 | 0.651231 |
| aco/reacher_hard/snow | 1000 | 18.3951 | 0.568783 | 15.9053 | 0.554734 |
| aco/reacher_hard/motion_blur | 1000 | 27.3660 | 0.921391 | 24.3817 | 0.880711 |
| aco/reacher_hard/gaussian_noise | 1000 | 23.5977 | 0.491129 | 17.7227 | 0.251916 |
| aco/reacher_hard/low_light | 1000 | 22.8785 | 0.403848 | 17.9214 | 0.240480 |
| aco/reacher_hard/jpeg | 1000 | 25.0449 | 0.909569 | 18.8024 | 0.763832 |
| aco/reacher_hard/defocus_blur | 1000 | 28.2985 | 0.944986 | 25.0628 | 0.903638 |
| aco/reacher_hard/frost | 1000 | 22.7859 | 0.953709 | 18.5683 | 0.911975 |
| aco/reacher_hard/occlusion_patch | 1000 | 26.9264 | 0.899340 | 25.0047 | 0.893048 |
| aco/reacher_hard/saturation | 1000 | 24.0223 | 0.964220 | 20.8671 | 0.701320 |
| aco/reacher_hard/shadow | 1000 | 25.8127 | 0.952627 | 22.2559 | 0.923540 |
| aco/reacher_hard/shot_noise | 1000 | 22.4389 | 0.365216 | 16.7783 | 0.174698 |
| aco/clean_input | 10000 | 26.3518 | 0.915467 | 21.2298 | 0.807752 |
| aco/original7 | 70000 | 22.4286 | 0.710481 | 18.5762 | 0.566611 |
| aco/added6 | 60000 | 24.3085 | 0.833022 | 20.9472 | 0.729171 |
| smfa/all | 130000 | 34.6888 | 0.929250 | 32.2636 | 0.904155 |
| smfa/task/walker_walk | 13000 | 33.3565 | 0.921090 | 31.1536 | 0.896315 |
| smfa/degradation/rain | 10000 | 36.1677 | 0.947048 | 34.5242 | 0.929279 |
| smfa/walker_walk/rain | 1000 | 33.9908 | 0.938346 | 32.5799 | 0.919160 |
| smfa/degradation/fog | 10000 | 40.7732 | 0.990707 | 38.7427 | 0.983840 |
| smfa/walker_walk/fog | 1000 | 40.1199 | 0.990780 | 38.3275 | 0.984454 |
| smfa/degradation/snow | 10000 | 34.1885 | 0.925289 | 32.5997 | 0.898476 |
| smfa/walker_walk/snow | 1000 | 32.0824 | 0.910834 | 30.6691 | 0.880944 |
| smfa/degradation/motion_blur | 10000 | 27.5415 | 0.809709 | 25.4737 | 0.790342 |
| smfa/walker_walk/motion_blur | 1000 | 25.2642 | 0.766189 | 23.4864 | 0.751121 |
| smfa/degradation/gaussian_noise | 10000 | 37.3634 | 0.948936 | 34.5445 | 0.918236 |
| smfa/walker_walk/gaussian_noise | 1000 | 36.7214 | 0.946528 | 34.0517 | 0.914724 |
| smfa/degradation/low_light | 10000 | 32.1732 | 0.901482 | 29.6473 | 0.847777 |
| smfa/walker_walk/low_light | 1000 | 31.5556 | 0.906838 | 29.2215 | 0.855971 |
| smfa/degradation/jpeg | 10000 | 33.9443 | 0.936973 | 30.0866 | 0.890537 |
| smfa/walker_walk/jpeg | 1000 | 32.8251 | 0.934549 | 29.0914 | 0.882808 |
| smfa/degradation/defocus_blur | 10000 | 28.0631 | 0.822527 | 26.0424 | 0.801057 |
| smfa/walker_walk/defocus_blur | 1000 | 26.1294 | 0.791656 | 24.4134 | 0.771882 |
| smfa/degradation/frost | 10000 | 38.2889 | 0.971632 | 36.1731 | 0.958608 |
| smfa/walker_walk/frost | 1000 | 36.4660 | 0.968328 | 34.5227 | 0.953967 |
| smfa/degradation/occlusion_patch | 10000 | 32.5769 | 0.929507 | 30.0562 | 0.910575 |
| smfa/walker_walk/occlusion_patch | 1000 | 29.9973 | 0.917760 | 27.9014 | 0.901727 |
| smfa/degradation/saturation | 10000 | 41.2580 | 0.993251 | 38.1110 | 0.982364 |
| smfa/walker_walk/saturation | 1000 | 41.2241 | 0.993842 | 38.3177 | 0.984142 |
| smfa/degradation/shadow | 10000 | 33.2595 | 0.975306 | 30.9251 | 0.958184 |
| smfa/walker_walk/shadow | 1000 | 32.8647 | 0.979181 | 30.7308 | 0.964849 |
| smfa/degradation/shot_noise | 10000 | 35.3558 | 0.927884 | 32.4999 | 0.884742 |
| smfa/walker_walk/shot_noise | 1000 | 34.3940 | 0.929346 | 31.6832 | 0.886344 |
| smfa/task/walker_run | 13000 | 33.2258 | 0.919667 | 31.0318 | 0.894441 |
| smfa/walker_run/rain | 1000 | 33.9415 | 0.937160 | 32.5297 | 0.917842 |
| smfa/walker_run/fog | 1000 | 39.8501 | 0.990558 | 38.1081 | 0.984154 |
| smfa/walker_run/snow | 1000 | 31.9663 | 0.908138 | 30.5589 | 0.877707 |
| smfa/walker_run/motion_blur | 1000 | 25.0197 | 0.759929 | 23.2763 | 0.743868 |
| smfa/walker_run/gaussian_noise | 1000 | 36.6452 | 0.945940 | 33.9704 | 0.913827 |
| smfa/walker_run/low_light | 1000 | 31.6182 | 0.907031 | 29.2854 | 0.856346 |
| smfa/walker_run/jpeg | 1000 | 32.7258 | 0.932800 | 28.9596 | 0.879105 |
| smfa/walker_run/defocus_blur | 1000 | 25.9409 | 0.787112 | 24.2517 | 0.766285 |
| smfa/walker_run/frost | 1000 | 36.1959 | 0.967555 | 34.2278 | 0.952852 |
| smfa/walker_run/occlusion_patch | 1000 | 29.7510 | 0.916650 | 27.6840 | 0.900561 |
| smfa/walker_run/saturation | 1000 | 40.8858 | 0.993660 | 38.0114 | 0.983566 |
| smfa/walker_run/shadow | 1000 | 33.0119 | 0.979557 | 30.8823 | 0.965121 |
| smfa/walker_run/shot_noise | 1000 | 34.3836 | 0.929577 | 31.6673 | 0.886494 |
| smfa/task/walker_stand | 13000 | 33.2131 | 0.921723 | 30.9837 | 0.895122 |
| smfa/walker_stand/rain | 1000 | 34.5578 | 0.938997 | 33.0739 | 0.918078 |
| smfa/walker_stand/fog | 1000 | 40.1647 | 0.990094 | 38.3827 | 0.983422 |
| smfa/walker_stand/snow | 1000 | 32.6481 | 0.914069 | 31.1788 | 0.882203 |
| smfa/walker_stand/motion_blur | 1000 | 25.0720 | 0.770627 | 23.3131 | 0.755637 |
| smfa/walker_stand/gaussian_noise | 1000 | 36.1117 | 0.943264 | 33.3699 | 0.907560 |
| smfa/walker_stand/low_light | 1000 | 31.7070 | 0.908772 | 29.4215 | 0.856881 |
| smfa/walker_stand/jpeg | 1000 | 32.3702 | 0.932175 | 28.8383 | 0.879517 |
| smfa/walker_stand/defocus_blur | 1000 | 25.9878 | 0.800425 | 24.2763 | 0.779358 |
| smfa/walker_stand/frost | 1000 | 34.3088 | 0.962799 | 32.0776 | 0.940564 |
| smfa/walker_stand/occlusion_patch | 1000 | 29.8210 | 0.918823 | 27.6980 | 0.900984 |
| smfa/walker_stand/saturation | 1000 | 41.2244 | 0.993038 | 38.2531 | 0.983002 |
| smfa/walker_stand/shadow | 1000 | 33.4187 | 0.979678 | 31.2629 | 0.964723 |
| smfa/walker_stand/shot_noise | 1000 | 34.3780 | 0.929645 | 31.6420 | 0.884658 |
| smfa/task/hopper_stand | 13000 | 34.5620 | 0.924129 | 32.4163 | 0.896614 |
| smfa/hopper_stand/rain | 1000 | 36.0909 | 0.940213 | 34.6687 | 0.922000 |
| smfa/hopper_stand/fog | 1000 | 40.8054 | 0.988901 | 39.3183 | 0.982356 |
| smfa/hopper_stand/snow | 1000 | 34.5464 | 0.915266 | 33.1127 | 0.886355 |
| smfa/hopper_stand/motion_blur | 1000 | 29.6661 | 0.844366 | 27.5280 | 0.829101 |
| smfa/hopper_stand/gaussian_noise | 1000 | 37.3692 | 0.933916 | 35.0181 | 0.898339 |
| smfa/hopper_stand/low_light | 1000 | 32.1313 | 0.870369 | 29.9314 | 0.809029 |
| smfa/hopper_stand/jpeg | 1000 | 34.7471 | 0.926131 | 31.1251 | 0.871982 |
| smfa/hopper_stand/defocus_blur | 1000 | 30.1692 | 0.850270 | 28.1055 | 0.834764 |
| smfa/hopper_stand/frost | 1000 | 36.9538 | 0.960904 | 35.2320 | 0.947058 |
| smfa/hopper_stand/occlusion_patch | 1000 | 33.5904 | 0.932028 | 31.1169 | 0.913914 |
| smfa/hopper_stand/saturation | 1000 | 40.7685 | 0.993360 | 38.4017 | 0.982697 |
| smfa/hopper_stand/shadow | 1000 | 27.0149 | 0.955665 | 24.8894 | 0.929344 |
| smfa/hopper_stand/shot_noise | 1000 | 35.4533 | 0.902281 | 32.9638 | 0.849049 |
| smfa/task/quadruped_run | 13000 | 33.3233 | 0.900639 | 31.0764 | 0.875070 |
| smfa/quadruped_run/rain | 1000 | 33.1030 | 0.893626 | 31.6691 | 0.872430 |
| smfa/quadruped_run/fog | 1000 | 39.7760 | 0.989501 | 37.9166 | 0.983678 |
| smfa/quadruped_run/snow | 1000 | 31.1884 | 0.853939 | 29.8101 | 0.824588 |
| smfa/quadruped_run/motion_blur | 1000 | 26.6023 | 0.738029 | 24.5330 | 0.708738 |
| smfa/quadruped_run/gaussian_noise | 1000 | 36.4327 | 0.938277 | 33.7979 | 0.909930 |
| smfa/quadruped_run/low_light | 1000 | 31.8085 | 0.884560 | 29.3385 | 0.833173 |
| smfa/quadruped_run/jpeg | 1000 | 32.5142 | 0.918982 | 28.5902 | 0.872292 |
| smfa/quadruped_run/defocus_blur | 1000 | 27.0221 | 0.733843 | 24.9737 | 0.705619 |
| smfa/quadruped_run/frost | 1000 | 35.9714 | 0.956756 | 34.3570 | 0.944763 |
| smfa/quadruped_run/occlusion_patch | 1000 | 31.3453 | 0.911676 | 29.1354 | 0.895033 |
| smfa/quadruped_run/saturation | 1000 | 39.3704 | 0.991961 | 36.8133 | 0.980767 |
| smfa/quadruped_run/shadow | 1000 | 33.4364 | 0.976209 | 31.1146 | 0.961358 |
| smfa/quadruped_run/shot_noise | 1000 | 34.6321 | 0.920942 | 31.9432 | 0.883540 |
| smfa/task/finger_turn_hard | 13000 | 34.8593 | 0.930467 | 31.9704 | 0.904112 |
| smfa/finger_turn_hard/rain | 1000 | 37.1365 | 0.963751 | 35.1008 | 0.945646 |
| smfa/finger_turn_hard/fog | 1000 | 41.7021 | 0.992488 | 38.9313 | 0.985109 |
| smfa/finger_turn_hard/snow | 1000 | 35.0188 | 0.951270 | 33.0954 | 0.923044 |
| smfa/finger_turn_hard/motion_blur | 1000 | 26.8131 | 0.773460 | 24.4894 | 0.746426 |
| smfa/finger_turn_hard/gaussian_noise | 1000 | 37.2206 | 0.949868 | 33.8456 | 0.917791 |
| smfa/finger_turn_hard/low_light | 1000 | 32.3799 | 0.907725 | 29.3508 | 0.858614 |
| smfa/finger_turn_hard/jpeg | 1000 | 33.8497 | 0.935484 | 29.4172 | 0.885564 |
| smfa/finger_turn_hard/defocus_blur | 1000 | 27.9685 | 0.810699 | 25.5838 | 0.780183 |
| smfa/finger_turn_hard/frost | 1000 | 39.8071 | 0.978127 | 37.2402 | 0.965399 |
| smfa/finger_turn_hard/occlusion_patch | 1000 | 31.0813 | 0.925015 | 28.3999 | 0.907483 |
| smfa/finger_turn_hard/saturation | 1000 | 40.9248 | 0.993751 | 36.5922 | 0.980635 |
| smfa/finger_turn_hard/shadow | 1000 | 34.3754 | 0.980730 | 31.9026 | 0.964187 |
| smfa/finger_turn_hard/shot_noise | 1000 | 34.8936 | 0.933707 | 31.6657 | 0.893373 |
| smfa/task/cartpole_swingup_sparse | 13000 | 34.7785 | 0.912493 | 32.4930 | 0.887740 |
| smfa/cartpole_swingup_sparse/rain | 1000 | 35.8466 | 0.938440 | 34.3959 | 0.922862 |
| smfa/cartpole_swingup_sparse/fog | 1000 | 41.5295 | 0.991259 | 39.7630 | 0.985948 |
| smfa/cartpole_swingup_sparse/snow | 1000 | 34.2183 | 0.909646 | 32.7855 | 0.885979 |
| smfa/cartpole_swingup_sparse/motion_blur | 1000 | 29.7216 | 0.767813 | 27.4865 | 0.739505 |
| smfa/cartpole_swingup_sparse/gaussian_noise | 1000 | 37.0537 | 0.939046 | 34.4622 | 0.909889 |
| smfa/cartpole_swingup_sparse/low_light | 1000 | 31.8928 | 0.867835 | 29.5143 | 0.817838 |
| smfa/cartpole_swingup_sparse/jpeg | 1000 | 34.7849 | 0.930544 | 31.1611 | 0.889842 |
| smfa/cartpole_swingup_sparse/defocus_blur | 1000 | 29.9476 | 0.764816 | 27.7577 | 0.737247 |
| smfa/cartpole_swingup_sparse/frost | 1000 | 37.8346 | 0.969768 | 36.2197 | 0.960294 |
| smfa/cartpole_swingup_sparse/occlusion_patch | 1000 | 34.0510 | 0.924703 | 31.6328 | 0.907515 |
| smfa/cartpole_swingup_sparse/saturation | 1000 | 42.3290 | 0.994225 | 39.2352 | 0.984573 |
| smfa/cartpole_swingup_sparse/shadow | 1000 | 27.6145 | 0.957091 | 25.3753 | 0.935718 |
| smfa/cartpole_swingup_sparse/shot_noise | 1000 | 35.2965 | 0.907221 | 32.6203 | 0.863416 |
| smfa/task/cup_catch | 13000 | 37.4094 | 0.939130 | 34.8431 | 0.915252 |
| smfa/cup_catch/rain | 1000 | 38.0833 | 0.955264 | 36.4315 | 0.936234 |
| smfa/cup_catch/fog | 1000 | 42.9493 | 0.990969 | 40.8130 | 0.983552 |
| smfa/cup_catch/snow | 1000 | 36.4834 | 0.941659 | 34.9497 | 0.916301 |
| smfa/cup_catch/motion_blur | 1000 | 31.8646 | 0.863634 | 29.3105 | 0.844589 |
| smfa/cup_catch/gaussian_noise | 1000 | 38.5970 | 0.942359 | 35.7062 | 0.909437 |
| smfa/cup_catch/low_light | 1000 | 34.0447 | 0.897394 | 31.2536 | 0.844254 |
| smfa/cup_catch/jpeg | 1000 | 35.5016 | 0.933725 | 32.0467 | 0.898890 |
| smfa/cup_catch/defocus_blur | 1000 | 31.6324 | 0.856289 | 29.1916 | 0.838973 |
| smfa/cup_catch/frost | 1000 | 40.3559 | 0.971702 | 38.2070 | 0.957859 |
| smfa/cup_catch/occlusion_patch | 1000 | 37.4284 | 0.952465 | 34.2757 | 0.931608 |
| smfa/cup_catch/saturation | 1000 | 43.4056 | 0.992686 | 40.4642 | 0.981460 |
| smfa/cup_catch/shadow | 1000 | 38.4553 | 0.983009 | 35.8761 | 0.968806 |
| smfa/cup_catch/shot_noise | 1000 | 37.5209 | 0.927532 | 34.4351 | 0.886315 |
| smfa/task/reacher_easy | 13000 | 35.7713 | 0.961976 | 32.9672 | 0.937946 |
| smfa/reacher_easy/rain | 1000 | 39.1496 | 0.981708 | 37.0899 | 0.968716 |
| smfa/reacher_easy/fog | 1000 | 40.2743 | 0.990766 | 37.5508 | 0.982219 |
| smfa/reacher_easy/snow | 1000 | 36.3971 | 0.972460 | 34.5158 | 0.952165 |
| smfa/reacher_easy/motion_blur | 1000 | 27.7226 | 0.910716 | 25.5974 | 0.891932 |
| smfa/reacher_easy/gaussian_noise | 1000 | 38.5313 | 0.974580 | 35.3646 | 0.949579 |
| smfa/reacher_easy/low_light | 1000 | 32.1917 | 0.932016 | 29.2138 | 0.870135 |
| smfa/reacher_easy/jpeg | 1000 | 35.3082 | 0.965906 | 31.0107 | 0.927624 |
| smfa/reacher_easy/defocus_blur | 1000 | 27.9754 | 0.921282 | 25.9750 | 0.900264 |
| smfa/reacher_easy/frost | 1000 | 42.0993 | 0.989875 | 39.4421 | 0.981268 |
| smfa/reacher_easy/occlusion_patch | 1000 | 33.6628 | 0.945456 | 30.5977 | 0.920986 |
| smfa/reacher_easy/saturation | 1000 | 40.2388 | 0.992511 | 36.6239 | 0.980803 |
| smfa/reacher_easy/shadow | 1000 | 35.4954 | 0.980406 | 32.7445 | 0.962301 |
| smfa/reacher_easy/shot_noise | 1000 | 35.9805 | 0.948009 | 32.8479 | 0.905301 |
| smfa/task/reacher_hard | 13000 | 36.3883 | 0.961187 | 33.7003 | 0.938940 |
| smfa/reacher_hard/rain | 1000 | 39.7766 | 0.982974 | 37.7025 | 0.969821 |
| smfa/reacher_hard/fog | 1000 | 40.5609 | 0.991756 | 38.3153 | 0.983509 |
| smfa/reacher_hard/snow | 1000 | 37.3362 | 0.975608 | 35.3212 | 0.955470 |
| smfa/reacher_hard/motion_blur | 1000 | 27.6693 | 0.902323 | 25.7168 | 0.892503 |
| smfa/reacher_hard/gaussian_noise | 1000 | 38.9512 | 0.975579 | 35.8586 | 0.951280 |
| smfa/reacher_hard/low_light | 1000 | 32.4024 | 0.932278 | 29.9426 | 0.875533 |
| smfa/reacher_hard/jpeg | 1000 | 34.8160 | 0.959435 | 30.6257 | 0.917750 |
| smfa/reacher_hard/defocus_blur | 1000 | 27.8572 | 0.908880 | 25.8957 | 0.895994 |
| smfa/reacher_hard/frost | 1000 | 42.8966 | 0.990507 | 40.2048 | 0.982059 |
| smfa/reacher_hard/occlusion_patch | 1000 | 35.0406 | 0.950497 | 32.1199 | 0.925939 |
| smfa/reacher_hard/saturation | 1000 | 42.2082 | 0.993479 | 38.3974 | 0.981992 |
| smfa/reacher_hard/shadow | 1000 | 36.9076 | 0.981533 | 34.4724 | 0.965437 |
| smfa/reacher_hard/shot_noise | 1000 | 36.6252 | 0.950585 | 33.5311 | 0.908934 |
| smfa/clean_input | 10000 | 43.3198 | 0.994815 | 40.6373 | 0.989506 |
| smfa/original7 | 70000 | 34.5931 | 0.922878 | 32.2312 | 0.894070 |
| smfa/added6 | 60000 | 34.8003 | 0.936685 | 32.3013 | 0.915922 |

## All control aggregates

| Group | Mean +/- episode SD |
|---|---:|
| markov/raw | 483.41 +/- 353.71 (n=100) |
| single/all/raw | 460.57 +/- 396.01 (n=650) |
| single/original7/raw | 421.83 +/- 394.21 (n=350) |
| single/added6/raw | 505.77 +/- 393.96 (n=300) |
| single/rain/raw | 519.09 +/- 402.32 (n=50) |
| single/fog/raw | 568.59 +/- 365.03 (n=50) |
| single/snow/raw | 98.93 +/- 174.62 (n=50) |
| single/motion_blur/raw | 365.09 +/- 369.70 (n=50) |
| single/gaussian_noise/raw | 649.19 +/- 368.10 (n=50) |
| single/low_light/raw | 105.77 +/- 149.96 (n=50) |
| single/jpeg/raw | 646.18 +/- 373.12 (n=50) |
| single/defocus_blur/raw | 356.63 +/- 354.00 (n=50) |
| single/frost/raw | 627.26 +/- 389.05 (n=50) |
| single/occlusion_patch/raw | 337.05 +/- 359.22 (n=50) |
| single/saturation/raw | 637.99 +/- 378.81 (n=50) |
| single/shadow/raw | 561.88 +/- 382.10 (n=50) |
| single/shot_noise/raw | 513.79 +/- 404.91 (n=50) |
| task/walker_walk/single_mean/raw | 624.63 +/- 327.00 (n=65) |
| task/walker_walk/markov/raw | 506.91 +/- 202.69 (n=10) |
| task/walker_walk/rain/raw | 917.35 +/- 51.45 (n=5) |
| task/walker_walk/fog/raw | 569.88 +/- 124.06 (n=5) |
| task/walker_walk/snow/raw | 46.30 +/- 14.70 (n=5) |
| task/walker_walk/motion_blur/raw | 359.22 +/- 146.85 (n=5) |
| task/walker_walk/gaussian_noise/raw | 950.12 +/- 12.49 (n=5) |
| task/walker_walk/low_light/raw | 193.45 +/- 37.22 (n=5) |
| task/walker_walk/jpeg/raw | 944.90 +/- 31.20 (n=5) |
| task/walker_walk/defocus_blur/raw | 421.07 +/- 118.62 (n=5) |
| task/walker_walk/frost/raw | 905.61 +/- 30.90 (n=5) |
| task/walker_walk/occlusion_patch/raw | 393.57 +/- 266.20 (n=5) |
| task/walker_walk/saturation/raw | 910.55 +/- 45.66 (n=5) |
| task/walker_walk/shadow/raw | 695.43 +/- 301.02 (n=5) |
| task/walker_walk/shot_noise/raw | 812.80 +/- 99.68 (n=5) |
| task/walker_run/single_mean/raw | 328.29 +/- 215.57 (n=65) |
| task/walker_run/markov/raw | 238.31 +/- 56.58 (n=10) |
| task/walker_run/rain/raw | 472.24 +/- 129.45 (n=5) |
| task/walker_run/fog/raw | 219.73 +/- 17.88 (n=5) |
| task/walker_run/snow/raw | 56.31 +/- 10.24 (n=5) |
| task/walker_run/motion_blur/raw | 192.39 +/- 38.64 (n=5) |
| task/walker_run/gaussian_noise/raw | 555.58 +/- 168.94 (n=5) |
| task/walker_run/low_light/raw | 36.10 +/- 7.63 (n=5) |
| task/walker_run/jpeg/raw | 675.16 +/- 26.67 (n=5) |
| task/walker_run/defocus_blur/raw | 269.49 +/- 52.44 (n=5) |
| task/walker_run/frost/raw | 325.73 +/- 75.21 (n=5) |
| task/walker_run/occlusion_patch/raw | 162.59 +/- 15.34 (n=5) |
| task/walker_run/saturation/raw | 667.27 +/- 53.25 (n=5) |
| task/walker_run/shadow/raw | 375.56 +/- 112.74 (n=5) |
| task/walker_run/shot_noise/raw | 259.59 +/- 49.95 (n=5) |
| task/walker_stand/single_mean/raw | 842.35 +/- 200.20 (n=65) |
| task/walker_stand/markov/raw | 863.96 +/- 102.88 (n=10) |
| task/walker_stand/rain/raw | 956.35 +/- 13.93 (n=5) |
| task/walker_stand/fog/raw | 786.90 +/- 67.21 (n=5) |
| task/walker_stand/snow/raw | 356.58 +/- 57.89 (n=5) |
| task/walker_stand/motion_blur/raw | 839.98 +/- 121.05 (n=5) |
| task/walker_stand/gaussian_noise/raw | 974.82 +/- 12.66 (n=5) |
| task/walker_stand/low_light/raw | 478.56 +/- 90.52 (n=5) |
| task/walker_stand/jpeg/raw | 971.24 +/- 17.63 (n=5) |
| task/walker_stand/defocus_blur/raw | 867.85 +/- 100.90 (n=5) |
| task/walker_stand/frost/raw | 951.76 +/- 23.71 (n=5) |
| task/walker_stand/occlusion_patch/raw | 888.73 +/- 68.00 (n=5) |
| task/walker_stand/saturation/raw | 966.17 +/- 15.89 (n=5) |
| task/walker_stand/shadow/raw | 954.04 +/- 24.77 (n=5) |
| task/walker_stand/shot_noise/raw | 957.60 +/- 25.74 (n=5) |
| task/hopper_stand/single_mean/raw | 397.44 +/- 374.84 (n=65) |
| task/hopper_stand/markov/raw | 398.89 +/- 159.79 (n=10) |
| task/hopper_stand/rain/raw | 420.79 +/- 251.16 (n=5) |
| task/hopper_stand/fog/raw | 511.95 +/- 304.16 (n=5) |
| task/hopper_stand/snow/raw | 2.43 +/- 5.44 (n=5) |
| task/hopper_stand/motion_blur/raw | 78.41 +/- 50.51 (n=5) |
| task/hopper_stand/gaussian_noise/raw | 722.15 +/- 403.76 (n=5) |
| task/hopper_stand/low_light/raw | 2.25 +/- 5.03 (n=5) |
| task/hopper_stand/jpeg/raw | 597.18 +/- 342.73 (n=5) |
| task/hopper_stand/defocus_blur/raw | 67.61 +/- 55.23 (n=5) |
| task/hopper_stand/frost/raw | 649.04 +/- 373.78 (n=5) |
| task/hopper_stand/occlusion_patch/raw | 251.41 +/- 274.28 (n=5) |
| task/hopper_stand/saturation/raw | 664.33 +/- 375.89 (n=5) |
| task/hopper_stand/shadow/raw | 531.20 +/- 385.42 (n=5) |
| task/hopper_stand/shot_noise/raw | 667.91 +/- 375.20 (n=5) |
| task/quadruped_run/single_mean/raw | 441.94 +/- 156.30 (n=65) |
| task/quadruped_run/markov/raw | 469.00 +/- 96.10 (n=10) |
| task/quadruped_run/rain/raw | 529.34 +/- 33.25 (n=5) |
| task/quadruped_run/fog/raw | 317.64 +/- 263.99 (n=5) |
| task/quadruped_run/snow/raw | 238.06 +/- 134.87 (n=5) |
| task/quadruped_run/motion_blur/raw | 516.07 +/- 22.56 (n=5) |
| task/quadruped_run/gaussian_noise/raw | 538.64 +/- 22.49 (n=5) |
| task/quadruped_run/low_light/raw | 162.37 +/- 66.99 (n=5) |
| task/quadruped_run/jpeg/raw | 519.71 +/- 40.91 (n=5) |
| task/quadruped_run/defocus_blur/raw | 503.10 +/- 63.14 (n=5) |
| task/quadruped_run/frost/raw | 534.25 +/- 22.56 (n=5) |
| task/quadruped_run/occlusion_patch/raw | 420.83 +/- 187.13 (n=5) |
| task/quadruped_run/saturation/raw | 480.54 +/- 63.81 (n=5) |
| task/quadruped_run/shadow/raw | 450.12 +/- 131.25 (n=5) |
| task/quadruped_run/shot_noise/raw | 534.59 +/- 26.47 (n=5) |
| task/finger_turn_hard/single_mean/raw | 421.97 +/- 452.11 (n=65) |
| task/finger_turn_hard/markov/raw | 414.50 +/- 424.04 (n=10) |
| task/finger_turn_hard/rain/raw | 895.40 +/- 113.42 (n=5) |
| task/finger_turn_hard/fog/raw | 561.80 +/- 514.41 (n=5) |
| task/finger_turn_hard/snow/raw | 0.00 +/- 0.00 (n=5) |
| task/finger_turn_hard/motion_blur/raw | 32.40 +/- 37.69 (n=5) |
| task/finger_turn_hard/gaussian_noise/raw | 419.40 +/- 488.42 (n=5) |
| task/finger_turn_hard/low_light/raw | 0.00 +/- 0.00 (n=5) |
| task/finger_turn_hard/jpeg/raw | 694.80 +/- 393.87 (n=5) |
| task/finger_turn_hard/defocus_blur/raw | 72.20 +/- 95.32 (n=5) |
| task/finger_turn_hard/frost/raw | 761.60 +/- 414.08 (n=5) |
| task/finger_turn_hard/occlusion_patch/raw | 573.40 +/- 517.86 (n=5) |
| task/finger_turn_hard/saturation/raw | 557.60 +/- 509.04 (n=5) |
| task/finger_turn_hard/shadow/raw | 352.00 +/- 460.68 (n=5) |
| task/finger_turn_hard/shot_noise/raw | 565.00 +/- 514.54 (n=5) |
| task/cartpole_swingup_sparse/single_mean/raw | 152.17 +/- 250.25 (n=65) |
| task/cartpole_swingup_sparse/markov/raw | 64.10 +/- 79.71 (n=10) |
| task/cartpole_swingup_sparse/rain/raw | 3.00 +/- 6.71 (n=5) |
| task/cartpole_swingup_sparse/fog/raw | 752.00 +/- 180.60 (n=5) |
| task/cartpole_swingup_sparse/snow/raw | 0.00 +/- 0.00 (n=5) |
| task/cartpole_swingup_sparse/motion_blur/raw | 9.20 +/- 9.12 (n=5) |
| task/cartpole_swingup_sparse/gaussian_noise/raw | 384.00 +/- 164.15 (n=5) |
| task/cartpole_swingup_sparse/low_light/raw | 31.60 +/- 24.42 (n=5) |
| task/cartpole_swingup_sparse/jpeg/raw | 104.20 +/- 21.00 (n=5) |
| task/cartpole_swingup_sparse/defocus_blur/raw | 14.80 +/- 12.83 (n=5) |
| task/cartpole_swingup_sparse/frost/raw | 178.60 +/- 341.21 (n=5) |
| task/cartpole_swingup_sparse/occlusion_patch/raw | 25.40 +/- 27.16 (n=5) |
| task/cartpole_swingup_sparse/saturation/raw | 174.60 +/- 179.37 (n=5) |
| task/cartpole_swingup_sparse/shadow/raw | 296.80 +/- 269.55 (n=5) |
| task/cartpole_swingup_sparse/shot_noise/raw | 4.00 +/- 5.66 (n=5) |
| task/cup_catch/single_mean/raw | 623.94 +/- 448.77 (n=65) |
| task/cup_catch/markov/raw | 836.90 +/- 182.13 (n=10) |
| task/cup_catch/rain/raw | 7.40 +/- 7.09 (n=5) |
| task/cup_catch/fog/raw | 976.80 +/- 11.30 (n=5) |
| task/cup_catch/snow/raw | 188.80 +/- 411.02 (n=5) |
| task/cup_catch/motion_blur/raw | 949.00 +/- 61.82 (n=5) |
| task/cup_catch/gaussian_noise/raw | 955.20 +/- 40.03 (n=5) |
| task/cup_catch/low_light/raw | 6.00 +/- 8.94 (n=5) |
| task/cup_catch/jpeg/raw | 971.00 +/- 18.77 (n=5) |
| task/cup_catch/defocus_blur/raw | 571.40 +/- 522.27 (n=5) |
| task/cup_catch/frost/raw | 977.00 +/- 11.00 (n=5) |
| task/cup_catch/occlusion_patch/raw | 216.40 +/- 284.85 (n=5) |
| task/cup_catch/saturation/raw | 967.60 +/- 24.06 (n=5) |
| task/cup_catch/shadow/raw | 976.80 +/- 11.86 (n=5) |
| task/cup_catch/shot_noise/raw | 347.80 +/- 403.12 (n=5) |
| task/reacher_easy/single_mean/raw | 758.92 +/- 380.10 (n=65) |
| task/reacher_easy/markov/raw | 964.30 +/- 27.88 (n=10) |
| task/reacher_easy/rain/raw | 982.20 +/- 14.87 (n=5) |
| task/reacher_easy/fog/raw | 981.80 +/- 15.90 (n=5) |
| task/reacher_easy/snow/raw | 100.20 +/- 107.28 (n=5) |
| task/reacher_easy/motion_blur/raw | 667.80 +/- 423.62 (n=5) |
| task/reacher_easy/gaussian_noise/raw | 982.40 +/- 14.84 (n=5) |
| task/reacher_easy/low_light/raw | 141.20 +/- 80.26 (n=5) |
| task/reacher_easy/jpeg/raw | 981.20 +/- 16.63 (n=5) |
| task/reacher_easy/defocus_blur/raw | 674.40 +/- 442.58 (n=5) |
| task/reacher_easy/frost/raw | 981.80 +/- 15.90 (n=5) |
| task/reacher_easy/occlusion_patch/raw | 430.80 +/- 497.86 (n=5) |
| task/reacher_easy/saturation/raw | 982.00 +/- 15.22 (n=5) |
| task/reacher_easy/shadow/raw | 978.60 +/- 17.62 (n=5) |
| task/reacher_easy/shot_noise/raw | 981.60 +/- 15.24 (n=5) |
| task/reacher_hard/single_mean/raw | 14.06 +/- 57.86 (n=65) |
| task/reacher_hard/markov/raw | 77.20 +/- 224.18 (n=10) |
| task/reacher_hard/rain/raw | 6.80 +/- 15.21 (n=5) |
| task/reacher_hard/fog/raw | 7.40 +/- 16.55 (n=5) |
| task/reacher_hard/snow/raw | 0.60 +/- 1.34 (n=5) |
| task/reacher_hard/motion_blur/raw | 6.40 +/- 7.83 (n=5) |
| task/reacher_hard/gaussian_noise/raw | 9.60 +/- 19.31 (n=5) |
| task/reacher_hard/low_light/raw | 6.20 +/- 12.77 (n=5) |
| task/reacher_hard/jpeg/raw | 2.40 +/- 3.58 (n=5) |
| task/reacher_hard/defocus_blur/raw | 104.40 +/- 200.14 (n=5) |
| task/reacher_hard/frost/raw | 7.20 +/- 12.85 (n=5) |
| task/reacher_hard/occlusion_patch/raw | 7.40 +/- 12.24 (n=5) |
| task/reacher_hard/saturation/raw | 9.20 +/- 19.47 (n=5) |
| task/reacher_hard/shadow/raw | 8.20 +/- 18.34 (n=5) |
| task/reacher_hard/shot_noise/raw | 7.00 +/- 14.56 (n=5) |
| markov/aco | 319.03 +/- 317.42 (n=100) |
| single/all/aco | 316.72 +/- 364.93 (n=650) |
| single/original7/aco | 249.42 +/- 331.98 (n=350) |
| single/added6/aco | 395.24 +/- 385.91 (n=300) |
| single/rain/aco | 279.34 +/- 375.81 (n=50) |
| single/fog/aco | 328.97 +/- 350.48 (n=50) |
| single/snow/aco | 231.02 +/- 345.77 (n=50) |
| single/motion_blur/aco | 499.64 +/- 401.77 (n=50) |
| single/gaussian_noise/aco | 130.15 +/- 227.51 (n=50) |
| single/low_light/aco | 88.86 +/- 137.12 (n=50) |
| single/jpeg/aco | 188.00 +/- 230.43 (n=50) |
| single/defocus_blur/aco | 615.29 +/- 360.20 (n=50) |
| single/frost/aco | 335.74 +/- 368.39 (n=50) |
| single/occlusion_patch/aco | 483.43 +/- 381.84 (n=50) |
| single/saturation/aco | 277.77 +/- 367.87 (n=50) |
| single/shadow/aco | 566.70 +/- 364.16 (n=50) |
| single/shot_noise/aco | 92.51 +/- 176.05 (n=50) |
| task/walker_walk/single_mean/aco | 314.41 +/- 350.89 (n=65) |
| task/walker_walk/markov/aco | 207.12 +/- 76.28 (n=10) |
| task/walker_walk/rain/aco | 100.04 +/- 47.19 (n=5) |
| task/walker_walk/fog/aco | 191.74 +/- 65.18 (n=5) |
| task/walker_walk/snow/aco | 80.72 +/- 27.42 (n=5) |
| task/walker_walk/motion_blur/aco | 903.32 +/- 44.82 (n=5) |
| task/walker_walk/gaussian_noise/aco | 35.43 +/- 13.90 (n=5) |
| task/walker_walk/low_light/aco | 51.46 +/- 11.05 (n=5) |
| task/walker_walk/jpeg/aco | 75.42 +/- 28.82 (n=5) |
| task/walker_walk/defocus_blur/aco | 921.96 +/- 25.72 (n=5) |
| task/walker_walk/frost/aco | 217.44 +/- 69.49 (n=5) |
| task/walker_walk/occlusion_patch/aco | 678.42 +/- 263.89 (n=5) |
| task/walker_walk/saturation/aco | 100.97 +/- 45.89 (n=5) |
| task/walker_walk/shadow/aco | 695.43 +/- 272.59 (n=5) |
| task/walker_walk/shot_noise/aco | 34.94 +/- 9.31 (n=5) |
| task/walker_run/single_mean/aco | 148.98 +/- 145.25 (n=65) |
| task/walker_run/markov/aco | 102.23 +/- 20.62 (n=10) |
| task/walker_run/rain/aco | 68.65 +/- 17.31 (n=5) |
| task/walker_run/fog/aco | 166.37 +/- 17.75 (n=5) |
| task/walker_run/snow/aco | 39.36 +/- 19.21 (n=5) |
| task/walker_run/motion_blur/aco | 288.32 +/- 57.87 (n=5) |
| task/walker_run/gaussian_noise/aco | 32.82 +/- 10.08 (n=5) |
| task/walker_run/low_light/aco | 38.58 +/- 19.13 (n=5) |
| task/walker_run/jpeg/aco | 46.52 +/- 20.97 (n=5) |
| task/walker_run/defocus_blur/aco | 454.35 +/- 67.17 (n=5) |
| task/walker_run/frost/aco | 80.69 +/- 15.07 (n=5) |
| task/walker_run/occlusion_patch/aco | 198.96 +/- 28.52 (n=5) |
| task/walker_run/saturation/aco | 111.10 +/- 32.24 (n=5) |
| task/walker_run/shadow/aco | 372.16 +/- 166.92 (n=5) |
| task/walker_run/shot_noise/aco | 38.86 +/- 13.26 (n=5) |
| task/walker_stand/single_mean/aco | 691.77 +/- 262.24 (n=65) |
| task/walker_stand/markov/aco | 617.99 +/- 117.23 (n=10) |
| task/walker_stand/rain/aco | 889.56 +/- 70.69 (n=5) |
| task/walker_stand/fog/aco | 613.22 +/- 152.62 (n=5) |
| task/walker_stand/snow/aco | 705.44 +/- 184.29 (n=5) |
| task/walker_stand/motion_blur/aco | 919.34 +/- 51.36 (n=5) |
| task/walker_stand/gaussian_noise/aco | 296.39 +/- 86.45 (n=5) |
| task/walker_stand/low_light/aco | 376.32 +/- 88.27 (n=5) |
| task/walker_stand/jpeg/aco | 550.78 +/- 76.90 (n=5) |
| task/walker_stand/defocus_blur/aco | 956.31 +/- 22.54 (n=5) |
| task/walker_stand/frost/aco | 872.82 +/- 125.10 (n=5) |
| task/walker_stand/occlusion_patch/aco | 938.17 +/- 41.08 (n=5) |
| task/walker_stand/saturation/aco | 678.29 +/- 88.18 (n=5) |
| task/walker_stand/shadow/aco | 939.02 +/- 37.78 (n=5) |
| task/walker_stand/shot_noise/aco | 257.33 +/- 63.75 (n=5) |
| task/hopper_stand/single_mean/aco | 161.66 +/- 246.27 (n=65) |
| task/hopper_stand/markov/aco | 142.68 +/- 87.43 (n=10) |
| task/hopper_stand/rain/aco | 5.31 +/- 7.27 (n=5) |
| task/hopper_stand/fog/aco | 25.71 +/- 25.63 (n=5) |
| task/hopper_stand/snow/aco | 2.09 +/- 4.67 (n=5) |
| task/hopper_stand/motion_blur/aco | 284.73 +/- 182.12 (n=5) |
| task/hopper_stand/gaussian_noise/aco | 2.44 +/- 5.46 (n=5) |
| task/hopper_stand/low_light/aco | 2.24 +/- 5.00 (n=5) |
| task/hopper_stand/jpeg/aco | 303.59 +/- 189.67 (n=5) |
| task/hopper_stand/defocus_blur/aco | 476.16 +/- 276.76 (n=5) |
| task/hopper_stand/frost/aco | 121.98 +/- 83.41 (n=5) |
| task/hopper_stand/occlusion_patch/aco | 370.41 +/- 378.19 (n=5) |
| task/hopper_stand/saturation/aco | 39.34 +/- 32.73 (n=5) |
| task/hopper_stand/shadow/aco | 465.38 +/- 365.87 (n=5) |
| task/hopper_stand/shot_noise/aco | 2.25 +/- 5.03 (n=5) |
| task/quadruped_run/single_mean/aco | 348.83 +/- 157.29 (n=65) |
| task/quadruped_run/markov/aco | 338.37 +/- 143.20 (n=10) |
| task/quadruped_run/rain/aco | 220.86 +/- 69.69 (n=5) |
| task/quadruped_run/fog/aco | 423.07 +/- 135.29 (n=5) |
| task/quadruped_run/snow/aco | 176.14 +/- 57.12 (n=5) |
| task/quadruped_run/motion_blur/aco | 461.92 +/- 88.89 (n=5) |
| task/quadruped_run/gaussian_noise/aco | 329.81 +/- 52.37 (n=5) |
| task/quadruped_run/low_light/aco | 267.57 +/- 122.24 (n=5) |
| task/quadruped_run/jpeg/aco | 390.07 +/- 44.79 (n=5) |
| task/quadruped_run/defocus_blur/aco | 467.76 +/- 130.72 (n=5) |
| task/quadruped_run/frost/aco | 414.42 +/- 91.27 (n=5) |
| task/quadruped_run/occlusion_patch/aco | 423.50 +/- 187.29 (n=5) |
| task/quadruped_run/saturation/aco | 225.43 +/- 292.58 (n=5) |
| task/quadruped_run/shadow/aco | 438.01 +/- 112.13 (n=5) |
| task/quadruped_run/shot_noise/aco | 296.26 +/- 171.01 (n=5) |
| task/finger_turn_hard/single_mean/aco | 241.85 +/- 380.57 (n=65) |
| task/finger_turn_hard/markov/aco | 275.20 +/- 304.64 (n=10) |
| task/finger_turn_hard/rain/aco | 353.60 +/- 484.51 (n=5) |
| task/finger_turn_hard/fog/aco | 191.20 +/- 418.62 (n=5) |
| task/finger_turn_hard/snow/aco | 187.40 +/- 405.21 (n=5) |
| task/finger_turn_hard/motion_blur/aco | 154.60 +/- 309.34 (n=5) |
| task/finger_turn_hard/gaussian_noise/aco | 53.80 +/- 120.30 (n=5) |
| task/finger_turn_hard/low_light/aco | 0.00 +/- 0.00 (n=5) |
| task/finger_turn_hard/jpeg/aco | 52.40 +/- 31.18 (n=5) |
| task/finger_turn_hard/defocus_blur/aco | 604.80 +/- 396.87 (n=5) |
| task/finger_turn_hard/frost/aco | 512.00 +/- 477.61 (n=5) |
| task/finger_turn_hard/occlusion_patch/aco | 655.80 +/- 410.66 (n=5) |
| task/finger_turn_hard/saturation/aco | 2.00 +/- 4.47 (n=5) |
| task/finger_turn_hard/shadow/aco | 376.40 +/- 495.78 (n=5) |
| task/finger_turn_hard/shot_noise/aco | 0.00 +/- 0.00 (n=5) |
| task/cartpole_swingup_sparse/single_mean/aco | 122.74 +/- 199.34 (n=65) |
| task/cartpole_swingup_sparse/markov/aco | 19.40 +/- 30.54 (n=10) |
| task/cartpole_swingup_sparse/rain/aco | 22.80 +/- 14.94 (n=5) |
| task/cartpole_swingup_sparse/fog/aco | 286.80 +/- 180.98 (n=5) |
| task/cartpole_swingup_sparse/snow/aco | 0.00 +/- 0.00 (n=5) |
| task/cartpole_swingup_sparse/motion_blur/aco | 34.40 +/- 10.92 (n=5) |
| task/cartpole_swingup_sparse/gaussian_noise/aco | 0.00 +/- 0.00 (n=5) |
| task/cartpole_swingup_sparse/low_light/aco | 1.40 +/- 3.13 (n=5) |
| task/cartpole_swingup_sparse/jpeg/aco | 37.80 +/- 19.23 (n=5) |
| task/cartpole_swingup_sparse/defocus_blur/aco | 317.80 +/- 275.14 (n=5) |
| task/cartpole_swingup_sparse/frost/aco | 42.60 +/- 36.06 (n=5) |
| task/cartpole_swingup_sparse/occlusion_patch/aco | 336.60 +/- 335.83 (n=5) |
| task/cartpole_swingup_sparse/saturation/aco | 58.60 +/- 49.16 (n=5) |
| task/cartpole_swingup_sparse/shadow/aco | 456.80 +/- 113.65 (n=5) |
| task/cartpole_swingup_sparse/shot_noise/aco | 0.00 +/- 0.00 (n=5) |
| task/cup_catch/single_mean/aco | 660.23 +/- 447.21 (n=65) |
| task/cup_catch/markov/aco | 838.40 +/- 200.30 (n=10) |
| task/cup_catch/rain/aco | 976.60 +/- 12.58 (n=5) |
| task/cup_catch/fog/aco | 782.60 +/- 437.57 (n=5) |
| task/cup_catch/snow/aco | 971.80 +/- 17.80 (n=5) |
| task/cup_catch/motion_blur/aco | 971.80 +/- 14.34 (n=5) |
| task/cup_catch/gaussian_noise/aco | 3.80 +/- 5.22 (n=5) |
| task/cup_catch/low_light/aco | 11.20 +/- 13.52 (n=5) |
| task/cup_catch/jpeg/aco | 77.00 +/- 163.28 (n=5) |
| task/cup_catch/defocus_blur/aco | 974.60 +/- 13.01 (n=5) |
| task/cup_catch/frost/aco | 976.60 +/- 12.80 (n=5) |
| task/cup_catch/occlusion_patch/aco | 944.40 +/- 57.76 (n=5) |
| task/cup_catch/saturation/aco | 954.60 +/- 34.72 (n=5) |
| task/cup_catch/shadow/aco | 935.60 +/- 74.16 (n=5) |
| task/cup_catch/shot_noise/aco | 2.40 +/- 4.34 (n=5) |
| task/reacher_easy/single_mean/aco | 464.34 +/- 435.93 (n=65) |
| task/reacher_easy/markov/aco | 626.70 +/- 343.26 (n=10) |
| task/reacher_easy/rain/aco | 118.40 +/- 124.10 (n=5) |
| task/reacher_easy/fog/aco | 591.80 +/- 532.52 (n=5) |
| task/reacher_easy/snow/aco | 122.00 +/- 113.52 (n=5) |
| task/reacher_easy/motion_blur/aco | 976.60 +/- 20.60 (n=5) |
| task/reacher_easy/gaussian_noise/aco | 537.60 +/- 454.79 (n=5) |
| task/reacher_easy/low_light/aco | 124.80 +/- 117.53 (n=5) |
| task/reacher_easy/jpeg/aco | 345.60 +/- 403.41 (n=5) |
| task/reacher_easy/defocus_blur/aco | 978.60 +/- 21.49 (n=5) |
| task/reacher_easy/frost/aco | 107.00 +/- 127.12 (n=5) |
| task/reacher_easy/occlusion_patch/aco | 277.00 +/- 401.69 (n=5) |
| task/reacher_easy/saturation/aco | 592.40 +/- 519.48 (n=5) |
| task/reacher_easy/shadow/aco | 980.40 +/- 16.04 (n=5) |
| task/reacher_easy/shot_noise/aco | 284.20 +/- 394.89 (n=5) |
| task/reacher_hard/single_mean/aco | 12.43 +/- 24.91 (n=65) |
| task/reacher_hard/markov/aco | 22.20 +/- 58.07 (n=10) |
| task/reacher_hard/rain/aco | 37.60 +/- 74.42 (n=5) |
| task/reacher_hard/fog/aco | 17.20 +/- 16.83 (n=5) |
| task/reacher_hard/snow/aco | 25.20 +/- 34.86 (n=5) |
| task/reacher_hard/motion_blur/aco | 1.40 +/- 1.95 (n=5) |
| task/reacher_hard/gaussian_noise/aco | 9.40 +/- 14.10 (n=5) |
| task/reacher_hard/low_light/aco | 15.00 +/- 13.27 (n=5) |
| task/reacher_hard/jpeg/aco | 0.80 +/- 1.79 (n=5) |
| task/reacher_hard/defocus_blur/aco | 0.60 +/- 1.34 (n=5) |
| task/reacher_hard/frost/aco | 11.80 +/- 16.47 (n=5) |
| task/reacher_hard/occlusion_patch/aco | 11.00 +/- 12.39 (n=5) |
| task/reacher_hard/saturation/aco | 15.00 +/- 7.81 (n=5) |
| task/reacher_hard/shadow/aco | 7.80 +/- 17.44 (n=5) |
| task/reacher_hard/shot_noise/aco | 8.80 +/- 11.21 (n=5) |
| markov/smfa | 640.65 +/- 335.70 (n=100) |
| single/all/smfa | 641.44 +/- 380.33 (n=650) |
| single/original7/smfa | 652.03 +/- 378.29 (n=350) |
| single/added6/smfa | 629.09 +/- 382.96 (n=300) |
| single/rain/smfa | 722.01 +/- 346.92 (n=50) |
| single/fog/smfa | 732.79 +/- 336.43 (n=50) |
| single/snow/smfa | 714.48 +/- 358.34 (n=50) |
| single/motion_blur/smfa | 349.14 +/- 380.23 (n=50) |
| single/gaussian_noise/smfa | 745.64 +/- 329.91 (n=50) |
| single/low_light/smfa | 694.88 +/- 364.89 (n=50) |
| single/jpeg/smfa | 605.25 +/- 385.31 (n=50) |
| single/defocus_blur/smfa | 434.28 +/- 406.60 (n=50) |
| single/frost/smfa | 739.01 +/- 335.50 (n=50) |
| single/occlusion_patch/smfa | 490.56 +/- 385.56 (n=50) |
| single/saturation/smfa | 730.30 +/- 347.16 (n=50) |
| single/shadow/smfa | 660.49 +/- 367.21 (n=50) |
| single/shot_noise/smfa | 719.92 +/- 349.98 (n=50) |
| task/walker_walk/single_mean/smfa | 873.47 +/- 210.21 (n=65) |
| task/walker_walk/markov/smfa | 870.16 +/- 79.72 (n=10) |
| task/walker_walk/rain/smfa | 955.90 +/- 14.12 (n=5) |
| task/walker_walk/fog/smfa | 958.59 +/- 16.78 (n=5) |
| task/walker_walk/snow/smfa | 958.21 +/- 9.71 (n=5) |
| task/walker_walk/motion_blur/smfa | 478.63 +/- 225.44 (n=5) |
| task/walker_walk/gaussian_noise/smfa | 943.53 +/- 35.66 (n=5) |
| task/walker_walk/low_light/smfa | 965.70 +/- 3.62 (n=5) |
| task/walker_walk/jpeg/smfa | 938.80 +/- 33.56 (n=5) |
| task/walker_walk/defocus_blur/smfa | 883.19 +/- 29.16 (n=5) |
| task/walker_walk/frost/smfa | 961.08 +/- 7.88 (n=5) |
| task/walker_walk/occlusion_patch/smfa | 440.88 +/- 371.39 (n=5) |
| task/walker_walk/saturation/smfa | 958.83 +/- 7.88 (n=5) |
| task/walker_walk/shadow/smfa | 950.24 +/- 32.24 (n=5) |
| task/walker_walk/shot_noise/smfa | 961.46 +/- 2.71 (n=5) |
| task/walker_run/single_mean/smfa | 625.44 +/- 177.29 (n=65) |
| task/walker_run/markov/smfa | 589.84 +/- 110.75 (n=10) |
| task/walker_run/rain/smfa | 722.41 +/- 26.34 (n=5) |
| task/walker_run/fog/smfa | 715.28 +/- 52.61 (n=5) |
| task/walker_run/snow/smfa | 718.35 +/- 52.99 (n=5) |
| task/walker_run/motion_blur/smfa | 272.12 +/- 46.15 (n=5) |
| task/walker_run/gaussian_noise/smfa | 753.90 +/- 19.82 (n=5) |
| task/walker_run/low_light/smfa | 682.41 +/- 52.33 (n=5) |
| task/walker_run/jpeg/smfa | 670.91 +/- 71.48 (n=5) |
| task/walker_run/defocus_blur/smfa | 413.79 +/- 31.75 (n=5) |
| task/walker_run/frost/smfa | 707.66 +/- 51.85 (n=5) |
| task/walker_run/occlusion_patch/smfa | 275.42 +/- 65.01 (n=5) |
| task/walker_run/saturation/smfa | 743.76 +/- 12.15 (n=5) |
| task/walker_run/shadow/smfa | 712.99 +/- 26.45 (n=5) |
| task/walker_run/shot_noise/smfa | 741.67 +/- 4.47 (n=5) |
| task/walker_stand/single_mean/smfa | 962.01 +/- 28.45 (n=65) |
| task/walker_stand/markov/smfa | 959.88 +/- 24.18 (n=10) |
| task/walker_stand/rain/smfa | 974.80 +/- 15.06 (n=5) |
| task/walker_stand/fog/smfa | 975.18 +/- 8.41 (n=5) |
| task/walker_stand/snow/smfa | 966.46 +/- 14.50 (n=5) |
| task/walker_stand/motion_blur/smfa | 928.28 +/- 49.11 (n=5) |
| task/walker_stand/gaussian_noise/smfa | 968.46 +/- 17.31 (n=5) |
| task/walker_stand/low_light/smfa | 975.22 +/- 10.38 (n=5) |
| task/walker_stand/jpeg/smfa | 968.28 +/- 12.04 (n=5) |
| task/walker_stand/defocus_blur/smfa | 954.40 +/- 27.58 (n=5) |
| task/walker_stand/frost/smfa | 966.21 +/- 17.47 (n=5) |
| task/walker_stand/occlusion_patch/smfa | 926.63 +/- 62.59 (n=5) |
| task/walker_stand/saturation/smfa | 974.41 +/- 7.88 (n=5) |
| task/walker_stand/shadow/smfa | 962.34 +/- 14.37 (n=5) |
| task/walker_stand/shot_noise/smfa | 965.44 +/- 13.29 (n=5) |
| task/hopper_stand/single_mean/smfa | 578.54 +/- 402.88 (n=65) |
| task/hopper_stand/markov/smfa | 539.82 +/- 207.55 (n=10) |
| task/hopper_stand/rain/smfa | 700.29 +/- 392.28 (n=5) |
| task/hopper_stand/fog/smfa | 732.77 +/- 409.66 (n=5) |
| task/hopper_stand/snow/smfa | 715.27 +/- 401.77 (n=5) |
| task/hopper_stand/motion_blur/smfa | 111.37 +/- 64.47 (n=5) |
| task/hopper_stand/gaussian_noise/smfa | 715.26 +/- 400.98 (n=5) |
| task/hopper_stand/low_light/smfa | 722.88 +/- 404.14 (n=5) |
| task/hopper_stand/jpeg/smfa | 406.05 +/- 255.74 (n=5) |
| task/hopper_stand/defocus_blur/smfa | 91.68 +/- 80.08 (n=5) |
| task/hopper_stand/frost/smfa | 719.52 +/- 403.08 (n=5) |
| task/hopper_stand/occlusion_patch/smfa | 441.47 +/- 457.53 (n=5) |
| task/hopper_stand/saturation/smfa | 730.10 +/- 408.14 (n=5) |
| task/hopper_stand/shadow/smfa | 725.94 +/- 406.00 (n=5) |
| task/hopper_stand/shot_noise/smfa | 708.39 +/- 397.44 (n=5) |
| task/quadruped_run/single_mean/smfa | 473.66 +/- 129.53 (n=65) |
| task/quadruped_run/markov/smfa | 453.43 +/- 144.91 (n=10) |
| task/quadruped_run/rain/smfa | 506.70 +/- 37.80 (n=5) |
| task/quadruped_run/fog/smfa | 498.25 +/- 41.19 (n=5) |
| task/quadruped_run/snow/smfa | 426.46 +/- 213.66 (n=5) |
| task/quadruped_run/motion_blur/smfa | 319.62 +/- 269.59 (n=5) |
| task/quadruped_run/gaussian_noise/smfa | 532.45 +/- 29.95 (n=5) |
| task/quadruped_run/low_light/smfa | 466.79 +/- 121.71 (n=5) |
| task/quadruped_run/jpeg/smfa | 511.66 +/- 73.86 (n=5) |
| task/quadruped_run/defocus_blur/smfa | 413.17 +/- 230.50 (n=5) |
| task/quadruped_run/frost/smfa | 483.39 +/- 61.50 (n=5) |
| task/quadruped_run/occlusion_patch/smfa | 509.84 +/- 49.23 (n=5) |
| task/quadruped_run/saturation/smfa | 528.70 +/- 33.04 (n=5) |
| task/quadruped_run/shadow/smfa | 491.36 +/- 71.68 (n=5) |
| task/quadruped_run/shot_noise/smfa | 469.23 +/- 94.83 (n=5) |
| task/finger_turn_hard/single_mean/smfa | 495.62 +/- 447.55 (n=65) |
| task/finger_turn_hard/markov/smfa | 687.50 +/- 366.07 (n=10) |
| task/finger_turn_hard/rain/smfa | 561.80 +/- 511.68 (n=5) |
| task/finger_turn_hard/fog/smfa | 653.20 +/- 421.97 (n=5) |
| task/finger_turn_hard/snow/smfa | 564.20 +/- 515.20 (n=5) |
| task/finger_turn_hard/motion_blur/smfa | 60.20 +/- 75.01 (n=5) |
| task/finger_turn_hard/gaussian_noise/smfa | 756.00 +/- 423.10 (n=5) |
| task/finger_turn_hard/low_light/smfa | 376.40 +/- 515.50 (n=5) |
| task/finger_turn_hard/jpeg/smfa | 505.80 +/- 474.62 (n=5) |
| task/finger_turn_hard/defocus_blur/smfa | 244.00 +/- 330.17 (n=5) |
| task/finger_turn_hard/frost/smfa | 752.40 +/- 419.75 (n=5) |
| task/finger_turn_hard/occlusion_patch/smfa | 502.80 +/- 462.55 (n=5) |
| task/finger_turn_hard/saturation/smfa | 565.00 +/- 515.83 (n=5) |
| task/finger_turn_hard/shadow/smfa | 338.00 +/- 455.81 (n=5) |
| task/finger_turn_hard/shot_noise/smfa | 563.20 +/- 514.24 (n=5) |
| task/cartpole_swingup_sparse/single_mean/smfa | 593.11 +/- 342.57 (n=65) |
| task/cartpole_swingup_sparse/markov/smfa | 367.60 +/- 169.68 (n=10) |
| task/cartpole_swingup_sparse/rain/smfa | 830.00 +/- 5.34 (n=5) |
| task/cartpole_swingup_sparse/fog/smfa | 826.80 +/- 11.45 (n=5) |
| task/cartpole_swingup_sparse/snow/smfa | 825.00 +/- 9.51 (n=5) |
| task/cartpole_swingup_sparse/motion_blur/smfa | 5.60 +/- 7.80 (n=5) |
| task/cartpole_swingup_sparse/gaussian_noise/smfa | 817.20 +/- 14.52 (n=5) |
| task/cartpole_swingup_sparse/low_light/smfa | 790.80 +/- 39.59 (n=5) |
| task/cartpole_swingup_sparse/jpeg/smfa | 89.00 +/- 47.39 (n=5) |
| task/cartpole_swingup_sparse/defocus_blur/smfa | 7.80 +/- 8.01 (n=5) |
| task/cartpole_swingup_sparse/frost/smfa | 831.80 +/- 4.66 (n=5) |
| task/cartpole_swingup_sparse/occlusion_patch/smfa | 578.40 +/- 324.52 (n=5) |
| task/cartpole_swingup_sparse/saturation/smfa | 833.20 +/- 3.03 (n=5) |
| task/cartpole_swingup_sparse/shadow/smfa | 454.80 +/- 203.49 (n=5) |
| task/cartpole_swingup_sparse/shot_noise/smfa | 820.00 +/- 10.89 (n=5) |
| task/cup_catch/single_mean/smfa | 913.20 +/- 237.76 (n=65) |
| task/cup_catch/markov/smfa | 960.50 +/- 29.55 (n=10) |
| task/cup_catch/rain/smfa | 977.20 +/- 12.21 (n=5) |
| task/cup_catch/fog/smfa | 977.60 +/- 11.80 (n=5) |
| task/cup_catch/snow/smfa | 977.40 +/- 11.17 (n=5) |
| task/cup_catch/motion_blur/smfa | 583.40 +/- 532.80 (n=5) |
| task/cup_catch/gaussian_noise/smfa | 977.60 +/- 11.80 (n=5) |
| task/cup_catch/low_light/smfa | 977.00 +/- 11.05 (n=5) |
| task/cup_catch/jpeg/smfa | 975.60 +/- 10.92 (n=5) |
| task/cup_catch/defocus_blur/smfa | 539.60 +/- 502.52 (n=5) |
| task/cup_catch/frost/smfa | 977.40 +/- 11.57 (n=5) |
| task/cup_catch/occlusion_patch/smfa | 976.60 +/- 11.06 (n=5) |
| task/cup_catch/saturation/smfa | 977.20 +/- 11.26 (n=5) |
| task/cup_catch/shadow/smfa | 977.60 +/- 11.80 (n=5) |
| task/cup_catch/shot_noise/smfa | 977.40 +/- 11.57 (n=5) |
| task/reacher_easy/single_mean/smfa | 891.00 +/- 275.22 (n=65) |
| task/reacher_easy/markov/smfa | 971.40 +/- 16.83 (n=10) |
| task/reacher_easy/rain/smfa | 982.20 +/- 14.87 (n=5) |
| task/reacher_easy/fog/smfa | 982.40 +/- 14.84 (n=5) |
| task/reacher_easy/snow/smfa | 982.80 +/- 14.17 (n=5) |
| task/reacher_easy/motion_blur/smfa | 730.00 +/- 421.51 (n=5) |
| task/reacher_easy/gaussian_noise/smfa | 982.20 +/- 15.19 (n=5) |
| task/reacher_easy/low_light/smfa | 981.20 +/- 16.63 (n=5) |
| task/reacher_easy/jpeg/smfa | 981.20 +/- 16.36 (n=5) |
| task/reacher_easy/defocus_blur/smfa | 787.40 +/- 440.31 (n=5) |
| task/reacher_easy/frost/smfa | 982.20 +/- 15.19 (n=5) |
| task/reacher_easy/occlusion_patch/smfa | 246.60 +/- 412.01 (n=5) |
| task/reacher_easy/saturation/smfa | 981.60 +/- 15.99 (n=5) |
| task/reacher_easy/shadow/smfa | 981.60 +/- 16.26 (n=5) |
| task/reacher_easy/shot_noise/smfa | 981.60 +/- 16.26 (n=5) |
| task/reacher_hard/single_mean/smfa | 8.38 +/- 15.21 (n=65) |
| task/reacher_hard/markov/smfa | 6.40 +/- 8.13 (n=10) |
| task/reacher_hard/rain/smfa | 8.80 +/- 18.05 (n=5) |
| task/reacher_hard/fog/smfa | 7.80 +/- 16.35 (n=5) |
| task/reacher_hard/snow/smfa | 10.60 +/- 20.42 (n=5) |
| task/reacher_hard/motion_blur/smfa | 2.20 +/- 3.90 (n=5) |
| task/reacher_hard/gaussian_noise/smfa | 9.80 +/- 19.75 (n=5) |
| task/reacher_hard/low_light/smfa | 10.40 +/- 17.05 (n=5) |
| task/reacher_hard/jpeg/smfa | 5.20 +/- 10.55 (n=5) |
| task/reacher_hard/defocus_blur/smfa | 7.80 +/- 5.72 (n=5) |
| task/reacher_hard/frost/smfa | 8.40 +/- 14.45 (n=5) |
| task/reacher_hard/occlusion_patch/smfa | 7.00 +/- 9.75 (n=5) |
| task/reacher_hard/saturation/smfa | 10.20 +/- 20.64 (n=5) |
| task/reacher_hard/shadow/smfa | 10.00 +/- 22.36 (n=5) |
| task/reacher_hard/shot_noise/smfa | 10.80 +/- 23.05 (n=5) |
| clean | 734.21 +/- 334.50 (n=50) |

## All episodes

| Task | Mode | Type | Method | Seed | Return |
|---|---|---|---|---:|---:|
| walker_walk | clean | - | clean | 400000 | 961.430612 |
| walker_walk | clean | - | clean | 400001 | 954.905707 |
| walker_walk | clean | - | clean | 400002 | 967.383273 |
| walker_walk | clean | - | clean | 400003 | 969.821523 |
| walker_walk | clean | - | clean | 400004 | 961.640520 |
| walker_walk | markov | - | raw | 400000 | 258.340205 |
| walker_walk | markov | - | raw | 400001 | 212.277286 |
| walker_walk | markov | - | raw | 400002 | 464.627102 |
| walker_walk | markov | - | raw | 400003 | 585.583843 |
| walker_walk | markov | - | raw | 400004 | 359.270610 |
| walker_walk | markov | - | raw | 400005 | 605.049430 |
| walker_walk | markov | - | raw | 400006 | 754.421924 |
| walker_walk | markov | - | raw | 400007 | 407.459231 |
| walker_walk | markov | - | raw | 400008 | 594.258480 |
| walker_walk | markov | - | raw | 400009 | 827.798172 |
| walker_walk | single | rain | raw | 400000 | 945.505850 |
| walker_walk | single | rain | raw | 400001 | 944.606476 |
| walker_walk | single | rain | raw | 400002 | 952.071677 |
| walker_walk | single | rain | raw | 400003 | 915.761709 |
| walker_walk | single | rain | raw | 400004 | 828.790157 |
| walker_walk | single | fog | raw | 400000 | 577.161561 |
| walker_walk | single | fog | raw | 400001 | 577.364150 |
| walker_walk | single | fog | raw | 400002 | 397.657100 |
| walker_walk | single | fog | raw | 400003 | 747.089224 |
| walker_walk | single | fog | raw | 400004 | 550.126694 |
| walker_walk | single | snow | raw | 400000 | 30.439189 |
| walker_walk | single | snow | raw | 400001 | 69.892645 |
| walker_walk | single | snow | raw | 400002 | 46.131753 |
| walker_walk | single | snow | raw | 400003 | 46.209860 |
| walker_walk | single | snow | raw | 400004 | 38.815946 |
| walker_walk | single | motion_blur | raw | 400000 | 436.020055 |
| walker_walk | single | motion_blur | raw | 400001 | 316.331495 |
| walker_walk | single | motion_blur | raw | 400002 | 275.616975 |
| walker_walk | single | motion_blur | raw | 400003 | 571.539304 |
| walker_walk | single | motion_blur | raw | 400004 | 196.592173 |
| walker_walk | single | gaussian_noise | raw | 400000 | 962.570536 |
| walker_walk | single | gaussian_noise | raw | 400001 | 961.064199 |
| walker_walk | single | gaussian_noise | raw | 400002 | 931.826807 |
| walker_walk | single | gaussian_noise | raw | 400003 | 946.774997 |
| walker_walk | single | gaussian_noise | raw | 400004 | 948.349572 |
| walker_walk | single | low_light | raw | 400000 | 172.295054 |
| walker_walk | single | low_light | raw | 400001 | 207.180153 |
| walker_walk | single | low_light | raw | 400002 | 212.700505 |
| walker_walk | single | low_light | raw | 400003 | 234.774833 |
| walker_walk | single | low_light | raw | 400004 | 140.288299 |
| walker_walk | single | jpeg | raw | 400000 | 969.637492 |
| walker_walk | single | jpeg | raw | 400001 | 891.451154 |
| walker_walk | single | jpeg | raw | 400002 | 955.070915 |
| walker_walk | single | jpeg | raw | 400003 | 962.805727 |
| walker_walk | single | jpeg | raw | 400004 | 945.549422 |
| walker_walk | single | defocus_blur | raw | 400000 | 408.626115 |
| walker_walk | single | defocus_blur | raw | 400001 | 595.513118 |
| walker_walk | single | defocus_blur | raw | 400002 | 468.048766 |
| walker_walk | single | defocus_blur | raw | 400003 | 287.825265 |
| walker_walk | single | defocus_blur | raw | 400004 | 345.330404 |
| walker_walk | single | frost | raw | 400000 | 940.650614 |
| walker_walk | single | frost | raw | 400001 | 908.154265 |
| walker_walk | single | frost | raw | 400002 | 865.100608 |
| walker_walk | single | frost | raw | 400003 | 928.746960 |
| walker_walk | single | frost | raw | 400004 | 885.378856 |
| walker_walk | single | occlusion_patch | raw | 400000 | 73.496383 |
| walker_walk | single | occlusion_patch | raw | 400001 | 738.700657 |
| walker_walk | single | occlusion_patch | raw | 400002 | 505.109915 |
| walker_walk | single | occlusion_patch | raw | 400003 | 466.906561 |
| walker_walk | single | occlusion_patch | raw | 400004 | 183.627111 |
| walker_walk | single | saturation | raw | 400000 | 923.419382 |
| walker_walk | single | saturation | raw | 400001 | 951.903608 |
| walker_walk | single | saturation | raw | 400002 | 946.115946 |
| walker_walk | single | saturation | raw | 400003 | 841.507233 |
| walker_walk | single | saturation | raw | 400004 | 889.797618 |
| walker_walk | single | shadow | raw | 400000 | 422.699750 |
| walker_walk | single | shadow | raw | 400001 | 316.510516 |
| walker_walk | single | shadow | raw | 400002 | 952.557782 |
| walker_walk | single | shadow | raw | 400003 | 876.290380 |
| walker_walk | single | shadow | raw | 400004 | 909.104166 |
| walker_walk | single | shot_noise | raw | 400000 | 862.448549 |
| walker_walk | single | shot_noise | raw | 400001 | 651.810256 |
| walker_walk | single | shot_noise | raw | 400002 | 876.373329 |
| walker_walk | single | shot_noise | raw | 400003 | 892.279782 |
| walker_walk | single | shot_noise | raw | 400004 | 781.084889 |
| walker_walk | markov | - | aco | 400000 | 156.146777 |
| walker_walk | markov | - | aco | 400001 | 212.367616 |
| walker_walk | markov | - | aco | 400002 | 332.515757 |
| walker_walk | markov | - | aco | 400003 | 134.202464 |
| walker_walk | markov | - | aco | 400004 | 180.806004 |
| walker_walk | markov | - | aco | 400005 | 304.892612 |
| walker_walk | markov | - | aco | 400006 | 104.593436 |
| walker_walk | markov | - | aco | 400007 | 202.539922 |
| walker_walk | markov | - | aco | 400008 | 282.760610 |
| walker_walk | markov | - | aco | 400009 | 160.335358 |
| walker_walk | single | rain | aco | 400000 | 76.721660 |
| walker_walk | single | rain | aco | 400001 | 177.514865 |
| walker_walk | single | rain | aco | 400002 | 51.655635 |
| walker_walk | single | rain | aco | 400003 | 96.007856 |
| walker_walk | single | rain | aco | 400004 | 98.305371 |
| walker_walk | single | fog | aco | 400000 | 298.253981 |
| walker_walk | single | fog | aco | 400001 | 162.864002 |
| walker_walk | single | fog | aco | 400002 | 202.383208 |
| walker_walk | single | fog | aco | 400003 | 167.671926 |
| walker_walk | single | fog | aco | 400004 | 127.540266 |
| walker_walk | single | snow | aco | 400000 | 55.796916 |
| walker_walk | single | snow | aco | 400001 | 110.231159 |
| walker_walk | single | snow | aco | 400002 | 53.097461 |
| walker_walk | single | snow | aco | 400003 | 76.663895 |
| walker_walk | single | snow | aco | 400004 | 107.829211 |
| walker_walk | single | motion_blur | aco | 400000 | 884.887089 |
| walker_walk | single | motion_blur | aco | 400001 | 931.239473 |
| walker_walk | single | motion_blur | aco | 400002 | 946.826747 |
| walker_walk | single | motion_blur | aco | 400003 | 919.373872 |
| walker_walk | single | motion_blur | aco | 400004 | 834.283027 |
| walker_walk | single | gaussian_noise | aco | 400000 | 39.343207 |
| walker_walk | single | gaussian_noise | aco | 400001 | 44.524045 |
| walker_walk | single | gaussian_noise | aco | 400002 | 51.097073 |
| walker_walk | single | gaussian_noise | aco | 400003 | 18.074073 |
| walker_walk | single | gaussian_noise | aco | 400004 | 24.099861 |
| walker_walk | single | low_light | aco | 400000 | 45.914502 |
| walker_walk | single | low_light | aco | 400001 | 67.594989 |
| walker_walk | single | low_light | aco | 400002 | 44.763798 |
| walker_walk | single | low_light | aco | 400003 | 41.006161 |
| walker_walk | single | low_light | aco | 400004 | 58.010023 |
| walker_walk | single | jpeg | aco | 400000 | 112.640248 |
| walker_walk | single | jpeg | aco | 400001 | 72.088269 |
| walker_walk | single | jpeg | aco | 400002 | 88.494547 |
| walker_walk | single | jpeg | aco | 400003 | 70.039174 |
| walker_walk | single | jpeg | aco | 400004 | 33.862717 |
| walker_walk | single | defocus_blur | aco | 400000 | 880.180459 |
| walker_walk | single | defocus_blur | aco | 400001 | 930.636213 |
| walker_walk | single | defocus_blur | aco | 400002 | 927.975858 |
| walker_walk | single | defocus_blur | aco | 400003 | 920.964147 |
| walker_walk | single | defocus_blur | aco | 400004 | 950.034569 |
| walker_walk | single | frost | aco | 400000 | 171.567329 |
| walker_walk | single | frost | aco | 400001 | 203.018416 |
| walker_walk | single | frost | aco | 400002 | 165.863681 |
| walker_walk | single | frost | aco | 400003 | 209.813908 |
| walker_walk | single | frost | aco | 400004 | 336.951275 |
| walker_walk | single | occlusion_patch | aco | 400000 | 373.380815 |
| walker_walk | single | occlusion_patch | aco | 400001 | 936.212078 |
| walker_walk | single | occlusion_patch | aco | 400002 | 772.766278 |
| walker_walk | single | occlusion_patch | aco | 400003 | 888.366058 |
| walker_walk | single | occlusion_patch | aco | 400004 | 421.373312 |
| walker_walk | single | saturation | aco | 400000 | 124.027743 |
| walker_walk | single | saturation | aco | 400001 | 99.640878 |
| walker_walk | single | saturation | aco | 400002 | 61.240775 |
| walker_walk | single | saturation | aco | 400003 | 165.418492 |
| walker_walk | single | saturation | aco | 400004 | 54.511926 |
| walker_walk | single | shadow | aco | 400000 | 457.357847 |
| walker_walk | single | shadow | aco | 400001 | 348.207364 |
| walker_walk | single | shadow | aco | 400002 | 898.497987 |
| walker_walk | single | shadow | aco | 400003 | 939.856151 |
| walker_walk | single | shadow | aco | 400004 | 833.240455 |
| walker_walk | single | shot_noise | aco | 400000 | 40.951797 |
| walker_walk | single | shot_noise | aco | 400001 | 47.859161 |
| walker_walk | single | shot_noise | aco | 400002 | 29.463378 |
| walker_walk | single | shot_noise | aco | 400003 | 31.668494 |
| walker_walk | single | shot_noise | aco | 400004 | 24.777678 |
| walker_walk | markov | - | smfa | 400000 | 929.931338 |
| walker_walk | markov | - | smfa | 400001 | 824.326056 |
| walker_walk | markov | - | smfa | 400002 | 891.247419 |
| walker_walk | markov | - | smfa | 400003 | 926.121760 |
| walker_walk | markov | - | smfa | 400004 | 842.500665 |
| walker_walk | markov | - | smfa | 400005 | 674.608764 |
| walker_walk | markov | - | smfa | 400006 | 932.876698 |
| walker_walk | markov | - | smfa | 400007 | 846.013880 |
| walker_walk | markov | - | smfa | 400008 | 912.605995 |
| walker_walk | markov | - | smfa | 400009 | 921.325129 |
| walker_walk | single | rain | smfa | 400000 | 953.440907 |
| walker_walk | single | rain | smfa | 400001 | 940.563541 |
| walker_walk | single | rain | smfa | 400002 | 969.669061 |
| walker_walk | single | rain | smfa | 400003 | 971.297912 |
| walker_walk | single | rain | smfa | 400004 | 944.536893 |
| walker_walk | single | fog | smfa | 400000 | 966.020877 |
| walker_walk | single | fog | smfa | 400001 | 965.530438 |
| walker_walk | single | fog | smfa | 400002 | 928.820902 |
| walker_walk | single | fog | smfa | 400003 | 969.270407 |
| walker_walk | single | fog | smfa | 400004 | 963.318885 |
| walker_walk | single | snow | smfa | 400000 | 951.633101 |
| walker_walk | single | snow | smfa | 400001 | 953.500655 |
| walker_walk | single | snow | smfa | 400002 | 969.891806 |
| walker_walk | single | snow | smfa | 400003 | 967.386324 |
| walker_walk | single | snow | smfa | 400004 | 948.650398 |
| walker_walk | single | motion_blur | smfa | 400000 | 413.119947 |
| walker_walk | single | motion_blur | smfa | 400001 | 598.864710 |
| walker_walk | single | motion_blur | smfa | 400002 | 505.169429 |
| walker_walk | single | motion_blur | smfa | 400003 | 738.446540 |
| walker_walk | single | motion_blur | smfa | 400004 | 137.560877 |
| walker_walk | single | gaussian_noise | smfa | 400000 | 951.392303 |
| walker_walk | single | gaussian_noise | smfa | 400001 | 880.569780 |
| walker_walk | single | gaussian_noise | smfa | 400002 | 962.287274 |
| walker_walk | single | gaussian_noise | smfa | 400003 | 966.624549 |
| walker_walk | single | gaussian_noise | smfa | 400004 | 956.787247 |
| walker_walk | single | low_light | smfa | 400000 | 966.890840 |
| walker_walk | single | low_light | smfa | 400001 | 964.925240 |
| walker_walk | single | low_light | smfa | 400002 | 966.109296 |
| walker_walk | single | low_light | smfa | 400003 | 970.291616 |
| walker_walk | single | low_light | smfa | 400004 | 960.293997 |
| walker_walk | single | jpeg | smfa | 400000 | 879.125839 |
| walker_walk | single | jpeg | smfa | 400001 | 959.384341 |
| walker_walk | single | jpeg | smfa | 400002 | 952.358445 |
| walker_walk | single | jpeg | smfa | 400003 | 949.318086 |
| walker_walk | single | jpeg | smfa | 400004 | 953.825127 |
| walker_walk | single | defocus_blur | smfa | 400000 | 917.389386 |
| walker_walk | single | defocus_blur | smfa | 400001 | 902.405613 |
| walker_walk | single | defocus_blur | smfa | 400002 | 842.054661 |
| walker_walk | single | defocus_blur | smfa | 400003 | 883.968681 |
| walker_walk | single | defocus_blur | smfa | 400004 | 870.126625 |
| walker_walk | single | frost | smfa | 400000 | 950.056681 |
| walker_walk | single | frost | smfa | 400001 | 956.292238 |
| walker_walk | single | frost | smfa | 400002 | 968.353450 |
| walker_walk | single | frost | smfa | 400003 | 968.073976 |
| walker_walk | single | frost | smfa | 400004 | 962.638496 |
| walker_walk | single | occlusion_patch | smfa | 400000 | 173.532716 |
| walker_walk | single | occlusion_patch | smfa | 400001 | 907.032709 |
| walker_walk | single | occlusion_patch | smfa | 400002 | 782.446466 |
| walker_walk | single | occlusion_patch | smfa | 400003 | 158.870935 |
| walker_walk | single | occlusion_patch | smfa | 400004 | 182.526914 |
| walker_walk | single | saturation | smfa | 400000 | 953.294737 |
| walker_walk | single | saturation | smfa | 400001 | 957.711207 |
| walker_walk | single | saturation | smfa | 400002 | 950.304217 |
| walker_walk | single | saturation | smfa | 400003 | 970.189764 |
| walker_walk | single | saturation | smfa | 400004 | 962.645930 |
| walker_walk | single | shadow | smfa | 400000 | 970.529093 |
| walker_walk | single | shadow | smfa | 400001 | 951.279624 |
| walker_walk | single | shadow | smfa | 400002 | 962.480930 |
| walker_walk | single | shadow | smfa | 400003 | 972.409300 |
| walker_walk | single | shadow | smfa | 400004 | 894.521608 |
| walker_walk | single | shot_noise | smfa | 400000 | 962.120211 |
| walker_walk | single | shot_noise | smfa | 400001 | 957.998015 |
| walker_walk | single | shot_noise | smfa | 400002 | 964.018013 |
| walker_walk | single | shot_noise | smfa | 400003 | 959.306102 |
| walker_walk | single | shot_noise | smfa | 400004 | 963.862410 |
| walker_run | clean | - | clean | 401000 | 694.962176 |
| walker_run | clean | - | clean | 401001 | 764.742759 |
| walker_run | clean | - | clean | 401002 | 729.363152 |
| walker_run | clean | - | clean | 401003 | 720.556912 |
| walker_run | clean | - | clean | 401004 | 751.811506 |
| walker_run | markov | - | raw | 401000 | 95.024611 |
| walker_run | markov | - | raw | 401001 | 252.732275 |
| walker_run | markov | - | raw | 401002 | 289.286731 |
| walker_run | markov | - | raw | 401003 | 223.992984 |
| walker_run | markov | - | raw | 401004 | 230.775575 |
| walker_run | markov | - | raw | 401005 | 249.454004 |
| walker_run | markov | - | raw | 401006 | 283.689046 |
| walker_run | markov | - | raw | 401007 | 247.628532 |
| walker_run | markov | - | raw | 401008 | 220.910402 |
| walker_run | markov | - | raw | 401009 | 289.650639 |
| walker_run | single | rain | raw | 401000 | 359.476694 |
| walker_run | single | rain | raw | 401001 | 581.514230 |
| walker_run | single | rain | raw | 401002 | 632.096006 |
| walker_run | single | rain | raw | 401003 | 441.988188 |
| walker_run | single | rain | raw | 401004 | 346.145380 |
| walker_run | single | fog | raw | 401000 | 223.279676 |
| walker_run | single | fog | raw | 401001 | 203.626799 |
| walker_run | single | fog | raw | 401002 | 212.682234 |
| walker_run | single | fog | raw | 401003 | 249.100860 |
| walker_run | single | fog | raw | 401004 | 209.976768 |
| walker_run | single | snow | raw | 401000 | 56.037486 |
| walker_run | single | snow | raw | 401001 | 45.070144 |
| walker_run | single | snow | raw | 401002 | 53.249654 |
| walker_run | single | snow | raw | 401003 | 73.023743 |
| walker_run | single | snow | raw | 401004 | 54.181204 |
| walker_run | single | motion_blur | raw | 401000 | 185.876513 |
| walker_run | single | motion_blur | raw | 401001 | 137.700028 |
| walker_run | single | motion_blur | raw | 401002 | 189.351367 |
| walker_run | single | motion_blur | raw | 401003 | 245.332397 |
| walker_run | single | motion_blur | raw | 401004 | 203.687134 |
| walker_run | single | gaussian_noise | raw | 401000 | 533.705755 |
| walker_run | single | gaussian_noise | raw | 401001 | 633.667892 |
| walker_run | single | gaussian_noise | raw | 401002 | 271.720966 |
| walker_run | single | gaussian_noise | raw | 401003 | 692.759660 |
| walker_run | single | gaussian_noise | raw | 401004 | 646.068948 |
| walker_run | single | low_light | raw | 401000 | 37.988397 |
| walker_run | single | low_light | raw | 401001 | 37.260634 |
| walker_run | single | low_light | raw | 401002 | 39.072210 |
| walker_run | single | low_light | raw | 401003 | 43.129047 |
| walker_run | single | low_light | raw | 401004 | 23.074188 |
| walker_run | single | jpeg | raw | 401000 | 656.979176 |
| walker_run | single | jpeg | raw | 401001 | 686.582775 |
| walker_run | single | jpeg | raw | 401002 | 642.046292 |
| walker_run | single | jpeg | raw | 401003 | 710.793893 |
| walker_run | single | jpeg | raw | 401004 | 679.382011 |
| walker_run | single | defocus_blur | raw | 401000 | 284.705219 |
| walker_run | single | defocus_blur | raw | 401001 | 196.646559 |
| walker_run | single | defocus_blur | raw | 401002 | 240.879489 |
| walker_run | single | defocus_blur | raw | 401003 | 334.086250 |
| walker_run | single | defocus_blur | raw | 401004 | 291.148605 |
| walker_run | single | frost | raw | 401000 | 400.081002 |
| walker_run | single | frost | raw | 401001 | 199.924328 |
| walker_run | single | frost | raw | 401002 | 342.680185 |
| walker_run | single | frost | raw | 401003 | 329.048497 |
| walker_run | single | frost | raw | 401004 | 356.919442 |
| walker_run | single | occlusion_patch | raw | 401000 | 183.222506 |
| walker_run | single | occlusion_patch | raw | 401001 | 155.863069 |
| walker_run | single | occlusion_patch | raw | 401002 | 143.682061 |
| walker_run | single | occlusion_patch | raw | 401003 | 172.179644 |
| walker_run | single | occlusion_patch | raw | 401004 | 158.022612 |
| walker_run | single | saturation | raw | 401000 | 581.357194 |
| walker_run | single | saturation | raw | 401001 | 716.646679 |
| walker_run | single | saturation | raw | 401002 | 654.698147 |
| walker_run | single | saturation | raw | 401003 | 700.784401 |
| walker_run | single | saturation | raw | 401004 | 682.872576 |
| walker_run | single | shadow | raw | 401000 | 411.900082 |
| walker_run | single | shadow | raw | 401001 | 310.751825 |
| walker_run | single | shadow | raw | 401002 | 447.109979 |
| walker_run | single | shadow | raw | 401003 | 494.155355 |
| walker_run | single | shadow | raw | 401004 | 213.902549 |
| walker_run | single | shot_noise | raw | 401000 | 212.685774 |
| walker_run | single | shot_noise | raw | 401001 | 220.860701 |
| walker_run | single | shot_noise | raw | 401002 | 250.647688 |
| walker_run | single | shot_noise | raw | 401003 | 336.286537 |
| walker_run | single | shot_noise | raw | 401004 | 277.468461 |
| walker_run | markov | - | aco | 401000 | 106.993026 |
| walker_run | markov | - | aco | 401001 | 118.705953 |
| walker_run | markov | - | aco | 401002 | 130.562992 |
| walker_run | markov | - | aco | 401003 | 72.470804 |
| walker_run | markov | - | aco | 401004 | 131.157689 |
| walker_run | markov | - | aco | 401005 | 86.443501 |
| walker_run | markov | - | aco | 401006 | 112.527691 |
| walker_run | markov | - | aco | 401007 | 87.575649 |
| walker_run | markov | - | aco | 401008 | 91.779270 |
| walker_run | markov | - | aco | 401009 | 84.128116 |
| walker_run | single | rain | aco | 401000 | 51.753009 |
| walker_run | single | rain | aco | 401001 | 86.325564 |
| walker_run | single | rain | aco | 401002 | 48.860692 |
| walker_run | single | rain | aco | 401003 | 74.391320 |
| walker_run | single | rain | aco | 401004 | 81.920238 |
| walker_run | single | fog | aco | 401000 | 139.626371 |
| walker_run | single | fog | aco | 401001 | 185.486837 |
| walker_run | single | fog | aco | 401002 | 178.587534 |
| walker_run | single | fog | aco | 401003 | 160.960463 |
| walker_run | single | fog | aco | 401004 | 167.187999 |
| walker_run | single | snow | aco | 401000 | 12.919733 |
| walker_run | single | snow | aco | 401001 | 63.377092 |
| walker_run | single | snow | aco | 401002 | 28.828356 |
| walker_run | single | snow | aco | 401003 | 44.130086 |
| walker_run | single | snow | aco | 401004 | 47.526774 |
| walker_run | single | motion_blur | aco | 401000 | 296.712585 |
| walker_run | single | motion_blur | aco | 401001 | 240.779369 |
| walker_run | single | motion_blur | aco | 401002 | 221.982723 |
| walker_run | single | motion_blur | aco | 401003 | 317.568438 |
| walker_run | single | motion_blur | aco | 401004 | 364.536563 |
| walker_run | single | gaussian_noise | aco | 401000 | 17.346364 |
| walker_run | single | gaussian_noise | aco | 401001 | 44.013957 |
| walker_run | single | gaussian_noise | aco | 401002 | 29.403302 |
| walker_run | single | gaussian_noise | aco | 401003 | 36.253969 |
| walker_run | single | gaussian_noise | aco | 401004 | 37.083362 |
| walker_run | single | low_light | aco | 401000 | 27.192971 |
| walker_run | single | low_light | aco | 401001 | 27.576340 |
| walker_run | single | low_light | aco | 401002 | 23.227966 |
| walker_run | single | low_light | aco | 401003 | 68.980980 |
| walker_run | single | low_light | aco | 401004 | 45.916398 |
| walker_run | single | jpeg | aco | 401000 | 40.927212 |
| walker_run | single | jpeg | aco | 401001 | 58.464039 |
| walker_run | single | jpeg | aco | 401002 | 12.927635 |
| walker_run | single | jpeg | aco | 401003 | 66.658275 |
| walker_run | single | jpeg | aco | 401004 | 53.640898 |
| walker_run | single | defocus_blur | aco | 401000 | 551.732452 |
| walker_run | single | defocus_blur | aco | 401001 | 383.456320 |
| walker_run | single | defocus_blur | aco | 401002 | 473.259156 |
| walker_run | single | defocus_blur | aco | 401003 | 398.845002 |
| walker_run | single | defocus_blur | aco | 401004 | 464.435717 |
| walker_run | single | frost | aco | 401000 | 98.263710 |
| walker_run | single | frost | aco | 401001 | 65.349609 |
| walker_run | single | frost | aco | 401002 | 69.158946 |
| walker_run | single | frost | aco | 401003 | 95.026447 |
| walker_run | single | frost | aco | 401004 | 75.643332 |
| walker_run | single | occlusion_patch | aco | 401000 | 201.196795 |
| walker_run | single | occlusion_patch | aco | 401001 | 181.353135 |
| walker_run | single | occlusion_patch | aco | 401002 | 194.602836 |
| walker_run | single | occlusion_patch | aco | 401003 | 171.916917 |
| walker_run | single | occlusion_patch | aco | 401004 | 245.735644 |
| walker_run | single | saturation | aco | 401000 | 114.067129 |
| walker_run | single | saturation | aco | 401001 | 88.659487 |
| walker_run | single | saturation | aco | 401002 | 147.282324 |
| walker_run | single | saturation | aco | 401003 | 69.597273 |
| walker_run | single | saturation | aco | 401004 | 135.878823 |
| walker_run | single | shadow | aco | 401000 | 250.063273 |
| walker_run | single | shadow | aco | 401001 | 342.485372 |
| walker_run | single | shadow | aco | 401002 | 352.169066 |
| walker_run | single | shadow | aco | 401003 | 658.678974 |
| walker_run | single | shadow | aco | 401004 | 257.389051 |
| walker_run | single | shot_noise | aco | 401000 | 53.682548 |
| walker_run | single | shot_noise | aco | 401001 | 41.186757 |
| walker_run | single | shot_noise | aco | 401002 | 19.601742 |
| walker_run | single | shot_noise | aco | 401003 | 32.668414 |
| walker_run | single | shot_noise | aco | 401004 | 47.182545 |
| walker_run | markov | - | smfa | 401000 | 612.748495 |
| walker_run | markov | - | smfa | 401001 | 609.658139 |
| walker_run | markov | - | smfa | 401002 | 394.283714 |
| walker_run | markov | - | smfa | 401003 | 611.037321 |
| walker_run | markov | - | smfa | 401004 | 511.354800 |
| walker_run | markov | - | smfa | 401005 | 679.942365 |
| walker_run | markov | - | smfa | 401006 | 422.830401 |
| walker_run | markov | - | smfa | 401007 | 657.995173 |
| walker_run | markov | - | smfa | 401008 | 700.260998 |
| walker_run | markov | - | smfa | 401009 | 698.330266 |
| walker_run | single | rain | smfa | 401000 | 740.649447 |
| walker_run | single | rain | smfa | 401001 | 701.380623 |
| walker_run | single | rain | smfa | 401002 | 702.876885 |
| walker_run | single | rain | smfa | 401003 | 759.734346 |
| walker_run | single | rain | smfa | 401004 | 707.388172 |
| walker_run | single | fog | smfa | 401000 | 622.321449 |
| walker_run | single | fog | smfa | 401001 | 741.981383 |
| walker_run | single | fog | smfa | 401002 | 741.177726 |
| walker_run | single | fog | smfa | 401003 | 746.237212 |
| walker_run | single | fog | smfa | 401004 | 724.695250 |
| walker_run | single | snow | smfa | 401000 | 632.074282 |
| walker_run | single | snow | smfa | 401001 | 762.186371 |
| walker_run | single | snow | smfa | 401002 | 733.183337 |
| walker_run | single | snow | smfa | 401003 | 757.307137 |
| walker_run | single | snow | smfa | 401004 | 707.017292 |
| walker_run | single | motion_blur | smfa | 401000 | 335.483418 |
| walker_run | single | motion_blur | smfa | 401001 | 226.133071 |
| walker_run | single | motion_blur | smfa | 401002 | 231.250634 |
| walker_run | single | motion_blur | smfa | 401003 | 268.956674 |
| walker_run | single | motion_blur | smfa | 401004 | 298.781476 |
| walker_run | single | gaussian_noise | smfa | 401000 | 760.045712 |
| walker_run | single | gaussian_noise | smfa | 401001 | 767.812565 |
| walker_run | single | gaussian_noise | smfa | 401002 | 722.171021 |
| walker_run | single | gaussian_noise | smfa | 401003 | 771.269747 |
| walker_run | single | gaussian_noise | smfa | 401004 | 748.216204 |
| walker_run | single | low_light | smfa | 401000 | 732.945004 |
| walker_run | single | low_light | smfa | 401001 | 673.397011 |
| walker_run | single | low_light | smfa | 401002 | 610.746553 |
| walker_run | single | low_light | smfa | 401003 | 734.420153 |
| walker_run | single | low_light | smfa | 401004 | 660.555976 |
| walker_run | single | jpeg | smfa | 401000 | 696.606753 |
| walker_run | single | jpeg | smfa | 401001 | 719.768028 |
| walker_run | single | jpeg | smfa | 401002 | 546.704155 |
| walker_run | single | jpeg | smfa | 401003 | 714.847304 |
| walker_run | single | jpeg | smfa | 401004 | 676.603985 |
| walker_run | single | defocus_blur | smfa | 401000 | 429.528268 |
| walker_run | single | defocus_blur | smfa | 401001 | 381.271877 |
| walker_run | single | defocus_blur | smfa | 401002 | 377.900933 |
| walker_run | single | defocus_blur | smfa | 401003 | 445.222225 |
| walker_run | single | defocus_blur | smfa | 401004 | 435.008361 |
| walker_run | single | frost | smfa | 401000 | 634.780760 |
| walker_run | single | frost | smfa | 401001 | 754.529132 |
| walker_run | single | frost | smfa | 401002 | 704.415243 |
| walker_run | single | frost | smfa | 401003 | 759.739712 |
| walker_run | single | frost | smfa | 401004 | 684.811901 |
| walker_run | single | occlusion_patch | smfa | 401000 | 218.274173 |
| walker_run | single | occlusion_patch | smfa | 401001 | 278.408761 |
| walker_run | single | occlusion_patch | smfa | 401002 | 245.725448 |
| walker_run | single | occlusion_patch | smfa | 401003 | 249.388783 |
| walker_run | single | occlusion_patch | smfa | 401004 | 385.300254 |
| walker_run | single | saturation | smfa | 401000 | 745.072961 |
| walker_run | single | saturation | smfa | 401001 | 742.317646 |
| walker_run | single | saturation | smfa | 401002 | 725.204645 |
| walker_run | single | saturation | smfa | 401003 | 758.930476 |
| walker_run | single | saturation | smfa | 401004 | 747.292524 |
| walker_run | single | shadow | smfa | 401000 | 688.530454 |
| walker_run | single | shadow | smfa | 401001 | 753.199487 |
| walker_run | single | shadow | smfa | 401002 | 696.260324 |
| walker_run | single | shadow | smfa | 401003 | 725.793884 |
| walker_run | single | shadow | smfa | 401004 | 701.150840 |
| walker_run | single | shot_noise | smfa | 401000 | 738.912162 |
| walker_run | single | shot_noise | smfa | 401001 | 747.804874 |
| walker_run | single | shot_noise | smfa | 401002 | 740.628340 |
| walker_run | single | shot_noise | smfa | 401003 | 736.570830 |
| walker_run | single | shot_noise | smfa | 401004 | 744.448994 |
| walker_stand | clean | - | clean | 402000 | 983.884201 |
| walker_stand | clean | - | clean | 402001 | 983.957855 |
| walker_stand | clean | - | clean | 402002 | 947.099468 |
| walker_stand | clean | - | clean | 402003 | 899.024025 |
| walker_stand | clean | - | clean | 402004 | 972.692843 |
| walker_stand | markov | - | raw | 402000 | 783.149967 |
| walker_stand | markov | - | raw | 402001 | 954.741792 |
| walker_stand | markov | - | raw | 402002 | 658.189583 |
| walker_stand | markov | - | raw | 402003 | 913.244302 |
| walker_stand | markov | - | raw | 402004 | 856.062366 |
| walker_stand | markov | - | raw | 402005 | 927.005247 |
| walker_stand | markov | - | raw | 402006 | 851.809231 |
| walker_stand | markov | - | raw | 402007 | 934.686247 |
| walker_stand | markov | - | raw | 402008 | 766.361827 |
| walker_stand | markov | - | raw | 402009 | 994.391614 |
| walker_stand | single | rain | raw | 402000 | 967.991135 |
| walker_stand | single | rain | raw | 402001 | 933.301096 |
| walker_stand | single | rain | raw | 402002 | 964.414570 |
| walker_stand | single | rain | raw | 402003 | 962.419034 |
| walker_stand | single | rain | raw | 402004 | 953.609526 |
| walker_stand | single | fog | raw | 402000 | 741.490035 |
| walker_stand | single | fog | raw | 402001 | 755.406504 |
| walker_stand | single | fog | raw | 402002 | 905.725364 |
| walker_stand | single | fog | raw | 402003 | 762.857340 |
| walker_stand | single | fog | raw | 402004 | 769.025061 |
| walker_stand | single | snow | raw | 402000 | 278.472577 |
| walker_stand | single | snow | raw | 402001 | 427.655095 |
| walker_stand | single | snow | raw | 402002 | 375.767218 |
| walker_stand | single | snow | raw | 402003 | 380.602540 |
| walker_stand | single | snow | raw | 402004 | 320.408726 |
| walker_stand | single | motion_blur | raw | 402000 | 803.012505 |
| walker_stand | single | motion_blur | raw | 402001 | 866.243427 |
| walker_stand | single | motion_blur | raw | 402002 | 963.761512 |
| walker_stand | single | motion_blur | raw | 402003 | 651.455779 |
| walker_stand | single | motion_blur | raw | 402004 | 915.408807 |
| walker_stand | single | gaussian_noise | raw | 402000 | 954.923406 |
| walker_stand | single | gaussian_noise | raw | 402001 | 983.126486 |
| walker_stand | single | gaussian_noise | raw | 402002 | 985.399539 |
| walker_stand | single | gaussian_noise | raw | 402003 | 980.986910 |
| walker_stand | single | gaussian_noise | raw | 402004 | 969.681099 |
| walker_stand | single | low_light | raw | 402000 | 380.865247 |
| walker_stand | single | low_light | raw | 402001 | 597.827427 |
| walker_stand | single | low_light | raw | 402002 | 457.252100 |
| walker_stand | single | low_light | raw | 402003 | 413.018816 |
| walker_stand | single | low_light | raw | 402004 | 543.828784 |
| walker_stand | single | jpeg | raw | 402000 | 983.208334 |
| walker_stand | single | jpeg | raw | 402001 | 983.324949 |
| walker_stand | single | jpeg | raw | 402002 | 982.511905 |
| walker_stand | single | jpeg | raw | 402003 | 943.517484 |
| walker_stand | single | jpeg | raw | 402004 | 963.636519 |
| walker_stand | single | defocus_blur | raw | 402000 | 962.907064 |
| walker_stand | single | defocus_blur | raw | 402001 | 960.986318 |
| walker_stand | single | defocus_blur | raw | 402002 | 804.298511 |
| walker_stand | single | defocus_blur | raw | 402003 | 730.682608 |
| walker_stand | single | defocus_blur | raw | 402004 | 880.368208 |
| walker_stand | single | frost | raw | 402000 | 978.102032 |
| walker_stand | single | frost | raw | 402001 | 958.883422 |
| walker_stand | single | frost | raw | 402002 | 964.618794 |
| walker_stand | single | frost | raw | 402003 | 940.118233 |
| walker_stand | single | frost | raw | 402004 | 917.063510 |
| walker_stand | single | occlusion_patch | raw | 402000 | 978.609855 |
| walker_stand | single | occlusion_patch | raw | 402001 | 933.000710 |
| walker_stand | single | occlusion_patch | raw | 402002 | 884.450651 |
| walker_stand | single | occlusion_patch | raw | 402003 | 825.430055 |
| walker_stand | single | occlusion_patch | raw | 402004 | 822.154226 |
| walker_stand | single | saturation | raw | 402000 | 982.550552 |
| walker_stand | single | saturation | raw | 402001 | 980.421778 |
| walker_stand | single | saturation | raw | 402002 | 960.966388 |
| walker_stand | single | saturation | raw | 402003 | 963.158422 |
| walker_stand | single | saturation | raw | 402004 | 943.745116 |
| walker_stand | single | shadow | raw | 402000 | 960.476772 |
| walker_stand | single | shadow | raw | 402001 | 982.120234 |
| walker_stand | single | shadow | raw | 402002 | 919.016952 |
| walker_stand | single | shadow | raw | 402003 | 940.206397 |
| walker_stand | single | shadow | raw | 402004 | 968.395746 |
| walker_stand | single | shot_noise | raw | 402000 | 963.564038 |
| walker_stand | single | shot_noise | raw | 402001 | 982.657440 |
| walker_stand | single | shot_noise | raw | 402002 | 930.333464 |
| walker_stand | single | shot_noise | raw | 402003 | 980.591772 |
| walker_stand | single | shot_noise | raw | 402004 | 930.863987 |
| walker_stand | markov | - | aco | 402000 | 404.636832 |
| walker_stand | markov | - | aco | 402001 | 498.613331 |
| walker_stand | markov | - | aco | 402002 | 589.789206 |
| walker_stand | markov | - | aco | 402003 | 760.303451 |
| walker_stand | markov | - | aco | 402004 | 556.678028 |
| walker_stand | markov | - | aco | 402005 | 799.356389 |
| walker_stand | markov | - | aco | 402006 | 623.606577 |
| walker_stand | markov | - | aco | 402007 | 618.586146 |
| walker_stand | markov | - | aco | 402008 | 633.215329 |
| walker_stand | markov | - | aco | 402009 | 695.080688 |
| walker_stand | single | rain | aco | 402000 | 915.328586 |
| walker_stand | single | rain | aco | 402001 | 947.246536 |
| walker_stand | single | rain | aco | 402002 | 779.551621 |
| walker_stand | single | rain | aco | 402003 | 944.917402 |
| walker_stand | single | rain | aco | 402004 | 860.776238 |
| walker_stand | single | fog | aco | 402000 | 460.900692 |
| walker_stand | single | fog | aco | 402001 | 477.245572 |
| walker_stand | single | fog | aco | 402002 | 803.638275 |
| walker_stand | single | fog | aco | 402003 | 734.366360 |
| walker_stand | single | fog | aco | 402004 | 589.949301 |
| walker_stand | single | snow | aco | 402000 | 590.036642 |
| walker_stand | single | snow | aco | 402001 | 825.075170 |
| walker_stand | single | snow | aco | 402002 | 854.649153 |
| walker_stand | single | snow | aco | 402003 | 821.332017 |
| walker_stand | single | snow | aco | 402004 | 436.123615 |
| walker_stand | single | motion_blur | aco | 402000 | 897.755263 |
| walker_stand | single | motion_blur | aco | 402001 | 979.366800 |
| walker_stand | single | motion_blur | aco | 402002 | 848.812477 |
| walker_stand | single | motion_blur | aco | 402003 | 913.085656 |
| walker_stand | single | motion_blur | aco | 402004 | 957.664635 |
| walker_stand | single | gaussian_noise | aco | 402000 | 384.168670 |
| walker_stand | single | gaussian_noise | aco | 402001 | 184.258112 |
| walker_stand | single | gaussian_noise | aco | 402002 | 339.790530 |
| walker_stand | single | gaussian_noise | aco | 402003 | 348.285890 |
| walker_stand | single | gaussian_noise | aco | 402004 | 225.423947 |
| walker_stand | single | low_light | aco | 402000 | 330.974707 |
| walker_stand | single | low_light | aco | 402001 | 477.706708 |
| walker_stand | single | low_light | aco | 402002 | 277.495259 |
| walker_stand | single | low_light | aco | 402003 | 333.872876 |
| walker_stand | single | low_light | aco | 402004 | 461.554186 |
| walker_stand | single | jpeg | aco | 402000 | 624.673715 |
| walker_stand | single | jpeg | aco | 402001 | 461.833272 |
| walker_stand | single | jpeg | aco | 402002 | 548.258436 |
| walker_stand | single | jpeg | aco | 402003 | 488.425647 |
| walker_stand | single | jpeg | aco | 402004 | 630.704038 |
| walker_stand | single | defocus_blur | aco | 402000 | 977.829943 |
| walker_stand | single | defocus_blur | aco | 402001 | 949.293829 |
| walker_stand | single | defocus_blur | aco | 402002 | 947.894646 |
| walker_stand | single | defocus_blur | aco | 402003 | 980.011919 |
| walker_stand | single | defocus_blur | aco | 402004 | 926.517241 |
| walker_stand | single | frost | aco | 402000 | 820.412102 |
| walker_stand | single | frost | aco | 402001 | 959.062378 |
| walker_stand | single | frost | aco | 402002 | 936.525881 |
| walker_stand | single | frost | aco | 402003 | 676.407310 |
| walker_stand | single | frost | aco | 402004 | 971.716333 |
| walker_stand | single | occlusion_patch | aco | 402000 | 979.554352 |
| walker_stand | single | occlusion_patch | aco | 402001 | 978.802195 |
| walker_stand | single | occlusion_patch | aco | 402002 | 896.386465 |
| walker_stand | single | occlusion_patch | aco | 402003 | 938.450531 |
| walker_stand | single | occlusion_patch | aco | 402004 | 897.659460 |
| walker_stand | single | saturation | aco | 402000 | 634.218981 |
| walker_stand | single | saturation | aco | 402001 | 830.581915 |
| walker_stand | single | saturation | aco | 402002 | 641.237240 |
| walker_stand | single | saturation | aco | 402003 | 674.825289 |
| walker_stand | single | saturation | aco | 402004 | 610.595281 |
| walker_stand | single | shadow | aco | 402000 | 928.015286 |
| walker_stand | single | shadow | aco | 402001 | 978.652161 |
| walker_stand | single | shadow | aco | 402002 | 879.605509 |
| walker_stand | single | shadow | aco | 402003 | 957.077568 |
| walker_stand | single | shadow | aco | 402004 | 951.739129 |
| walker_stand | single | shot_noise | aco | 402000 | 240.181962 |
| walker_stand | single | shot_noise | aco | 402001 | 209.048209 |
| walker_stand | single | shot_noise | aco | 402002 | 213.281864 |
| walker_stand | single | shot_noise | aco | 402003 | 258.699498 |
| walker_stand | single | shot_noise | aco | 402004 | 365.456970 |
| walker_stand | markov | - | smfa | 402000 | 980.111156 |
| walker_stand | markov | - | smfa | 402001 | 981.372060 |
| walker_stand | markov | - | smfa | 402002 | 940.926816 |
| walker_stand | markov | - | smfa | 402003 | 965.851736 |
| walker_stand | markov | - | smfa | 402004 | 932.250306 |
| walker_stand | markov | - | smfa | 402005 | 951.942038 |
| walker_stand | markov | - | smfa | 402006 | 995.636765 |
| walker_stand | markov | - | smfa | 402007 | 951.307092 |
| walker_stand | markov | - | smfa | 402008 | 921.328623 |
| walker_stand | markov | - | smfa | 402009 | 978.029570 |
| walker_stand | single | rain | smfa | 402000 | 982.629008 |
| walker_stand | single | rain | smfa | 402001 | 984.860266 |
| walker_stand | single | rain | smfa | 402002 | 980.790953 |
| walker_stand | single | rain | smfa | 402003 | 977.401178 |
| walker_stand | single | rain | smfa | 402004 | 948.312281 |
| walker_stand | single | fog | smfa | 402000 | 976.751009 |
| walker_stand | single | fog | smfa | 402001 | 981.838962 |
| walker_stand | single | fog | smfa | 402002 | 982.217020 |
| walker_stand | single | fog | smfa | 402003 | 961.627888 |
| walker_stand | single | fog | smfa | 402004 | 973.471690 |
| walker_stand | single | snow | smfa | 402000 | 976.351179 |
| walker_stand | single | snow | smfa | 402001 | 983.887249 |
| walker_stand | single | snow | smfa | 402002 | 946.912867 |
| walker_stand | single | snow | smfa | 402003 | 958.850904 |
| walker_stand | single | snow | smfa | 402004 | 966.292628 |
| walker_stand | single | motion_blur | smfa | 402000 | 898.962483 |
| walker_stand | single | motion_blur | smfa | 402001 | 980.410410 |
| walker_stand | single | motion_blur | smfa | 402002 | 962.702444 |
| walker_stand | single | motion_blur | smfa | 402003 | 859.363698 |
| walker_stand | single | motion_blur | smfa | 402004 | 939.955564 |
| walker_stand | single | gaussian_noise | smfa | 402000 | 976.380445 |
| walker_stand | single | gaussian_noise | smfa | 402001 | 983.918572 |
| walker_stand | single | gaussian_noise | smfa | 402002 | 982.033113 |
| walker_stand | single | gaussian_noise | smfa | 402003 | 946.134129 |
| walker_stand | single | gaussian_noise | smfa | 402004 | 953.817929 |
| walker_stand | single | low_light | smfa | 402000 | 977.691177 |
| walker_stand | single | low_light | smfa | 402001 | 984.430891 |
| walker_stand | single | low_light | smfa | 402002 | 981.193191 |
| walker_stand | single | low_light | smfa | 402003 | 975.026361 |
| walker_stand | single | low_light | smfa | 402004 | 957.772695 |
| walker_stand | single | jpeg | smfa | 402000 | 959.470678 |
| walker_stand | single | jpeg | smfa | 402001 | 981.141529 |
| walker_stand | single | jpeg | smfa | 402002 | 981.592412 |
| walker_stand | single | jpeg | smfa | 402003 | 957.458640 |
| walker_stand | single | jpeg | smfa | 402004 | 961.749296 |
| walker_stand | single | defocus_blur | smfa | 402000 | 982.521937 |
| walker_stand | single | defocus_blur | smfa | 402001 | 982.154126 |
| walker_stand | single | defocus_blur | smfa | 402002 | 942.906508 |
| walker_stand | single | defocus_blur | smfa | 402003 | 918.710145 |
| walker_stand | single | defocus_blur | smfa | 402004 | 945.687956 |
| walker_stand | single | frost | smfa | 402000 | 972.557943 |
| walker_stand | single | frost | smfa | 402001 | 942.769973 |
| walker_stand | single | frost | smfa | 402002 | 982.666620 |
| walker_stand | single | frost | smfa | 402003 | 979.956921 |
| walker_stand | single | frost | smfa | 402004 | 953.119490 |
| walker_stand | single | occlusion_patch | smfa | 402000 | 982.994562 |
| walker_stand | single | occlusion_patch | smfa | 402001 | 962.535470 |
| walker_stand | single | occlusion_patch | smfa | 402002 | 968.944542 |
| walker_stand | single | occlusion_patch | smfa | 402003 | 845.940038 |
| walker_stand | single | occlusion_patch | smfa | 402004 | 872.757956 |
| walker_stand | single | saturation | smfa | 402000 | 964.919492 |
| walker_stand | single | saturation | smfa | 402001 | 984.105171 |
| walker_stand | single | saturation | smfa | 402002 | 968.996273 |
| walker_stand | single | saturation | smfa | 402003 | 980.262384 |
| walker_stand | single | saturation | smfa | 402004 | 973.747111 |
| walker_stand | single | shadow | smfa | 402000 | 956.350180 |
| walker_stand | single | shadow | smfa | 402001 | 957.257079 |
| walker_stand | single | shadow | smfa | 402002 | 944.869807 |
| walker_stand | single | shadow | smfa | 402003 | 981.683143 |
| walker_stand | single | shadow | smfa | 402004 | 971.544711 |
| walker_stand | single | shot_noise | smfa | 402000 | 978.772203 |
| walker_stand | single | shot_noise | smfa | 402001 | 966.824135 |
| walker_stand | single | shot_noise | smfa | 402002 | 965.973019 |
| walker_stand | single | shot_noise | smfa | 402003 | 943.490535 |
| walker_stand | single | shot_noise | smfa | 402004 | 972.153506 |
| hopper_stand | clean | - | clean | 403000 | 909.121270 |
| hopper_stand | clean | - | clean | 403001 | 909.294773 |
| hopper_stand | clean | - | clean | 403002 | 914.618452 |
| hopper_stand | clean | - | clean | 403003 | 916.120909 |
| hopper_stand | clean | - | clean | 403004 | 0.000000 |
| hopper_stand | markov | - | raw | 403000 | 556.273014 |
| hopper_stand | markov | - | raw | 403001 | 309.243793 |
| hopper_stand | markov | - | raw | 403002 | 370.719877 |
| hopper_stand | markov | - | raw | 403003 | 385.280302 |
| hopper_stand | markov | - | raw | 403004 | 0.000000 |
| hopper_stand | markov | - | raw | 403005 | 405.910855 |
| hopper_stand | markov | - | raw | 403006 | 441.137957 |
| hopper_stand | markov | - | raw | 403007 | 514.935418 |
| hopper_stand | markov | - | raw | 403008 | 507.123877 |
| hopper_stand | markov | - | raw | 403009 | 498.229974 |
| hopper_stand | single | rain | raw | 403000 | 404.416632 |
| hopper_stand | single | rain | raw | 403001 | 502.723722 |
| hopper_stand | single | rain | raw | 403002 | 547.428486 |
| hopper_stand | single | rain | raw | 403003 | 649.366779 |
| hopper_stand | single | rain | raw | 403004 | 0.000000 |
| hopper_stand | single | fog | raw | 403000 | 652.279298 |
| hopper_stand | single | fog | raw | 403001 | 549.535018 |
| hopper_stand | single | fog | raw | 403002 | 803.589514 |
| hopper_stand | single | fog | raw | 403003 | 554.338265 |
| hopper_stand | single | fog | raw | 403004 | 0.000000 |
| hopper_stand | single | snow | raw | 403000 | 0.000000 |
| hopper_stand | single | snow | raw | 403001 | 12.161607 |
| hopper_stand | single | snow | raw | 403002 | 0.000000 |
| hopper_stand | single | snow | raw | 403003 | 0.000000 |
| hopper_stand | single | snow | raw | 403004 | 0.000000 |
| hopper_stand | single | motion_blur | raw | 403000 | 77.855201 |
| hopper_stand | single | motion_blur | raw | 403001 | 140.893998 |
| hopper_stand | single | motion_blur | raw | 403002 | 83.866562 |
| hopper_stand | single | motion_blur | raw | 403003 | 89.446534 |
| hopper_stand | single | motion_blur | raw | 403004 | 0.000000 |
| hopper_stand | single | gaussian_noise | raw | 403000 | 898.898379 |
| hopper_stand | single | gaussian_noise | raw | 403001 | 894.200280 |
| hopper_stand | single | gaussian_noise | raw | 403002 | 913.471203 |
| hopper_stand | single | gaussian_noise | raw | 403003 | 904.194184 |
| hopper_stand | single | gaussian_noise | raw | 403004 | 0.000000 |
| hopper_stand | single | low_light | raw | 403000 | 0.000000 |
| hopper_stand | single | low_light | raw | 403001 | 11.239557 |
| hopper_stand | single | low_light | raw | 403002 | 0.000000 |
| hopper_stand | single | low_light | raw | 403003 | 0.000000 |
| hopper_stand | single | low_light | raw | 403004 | 0.000000 |
| hopper_stand | single | jpeg | raw | 403000 | 873.804209 |
| hopper_stand | single | jpeg | raw | 403001 | 712.934779 |
| hopper_stand | single | jpeg | raw | 403002 | 733.847340 |
| hopper_stand | single | jpeg | raw | 403003 | 665.301814 |
| hopper_stand | single | jpeg | raw | 403004 | 0.000000 |
| hopper_stand | single | defocus_blur | raw | 403000 | 20.012813 |
| hopper_stand | single | defocus_blur | raw | 403001 | 84.080940 |
| hopper_stand | single | defocus_blur | raw | 403002 | 127.449201 |
| hopper_stand | single | defocus_blur | raw | 403003 | 106.531318 |
| hopper_stand | single | defocus_blur | raw | 403004 | 0.000000 |
| hopper_stand | single | frost | raw | 403000 | 906.909078 |
| hopper_stand | single | frost | raw | 403001 | 775.703937 |
| hopper_stand | single | frost | raw | 403002 | 881.491039 |
| hopper_stand | single | frost | raw | 403003 | 681.092640 |
| hopper_stand | single | frost | raw | 403004 | 0.000000 |
| hopper_stand | single | occlusion_patch | raw | 403000 | 278.277202 |
| hopper_stand | single | occlusion_patch | raw | 403001 | 663.348304 |
| hopper_stand | single | occlusion_patch | raw | 403002 | 315.416784 |
| hopper_stand | single | occlusion_patch | raw | 403003 | 0.000000 |
| hopper_stand | single | occlusion_patch | raw | 403004 | 0.000000 |
| hopper_stand | single | saturation | raw | 403000 | 904.404387 |
| hopper_stand | single | saturation | raw | 403001 | 834.545737 |
| hopper_stand | single | saturation | raw | 403002 | 741.490283 |
| hopper_stand | single | saturation | raw | 403003 | 841.203158 |
| hopper_stand | single | saturation | raw | 403004 | 0.000000 |
| hopper_stand | single | shadow | raw | 403000 | 610.370278 |
| hopper_stand | single | shadow | raw | 403001 | 850.955501 |
| hopper_stand | single | shadow | raw | 403002 | 909.390981 |
| hopper_stand | single | shadow | raw | 403003 | 285.262725 |
| hopper_stand | single | shadow | raw | 403004 | 0.000000 |
| hopper_stand | single | shot_noise | raw | 403000 | 892.291012 |
| hopper_stand | single | shot_noise | raw | 403001 | 793.695844 |
| hopper_stand | single | shot_noise | raw | 403002 | 839.605269 |
| hopper_stand | single | shot_noise | raw | 403003 | 813.974075 |
| hopper_stand | single | shot_noise | raw | 403004 | 0.000000 |
| hopper_stand | markov | - | aco | 403000 | 195.117130 |
| hopper_stand | markov | - | aco | 403001 | 103.301061 |
| hopper_stand | markov | - | aco | 403002 | 78.401784 |
| hopper_stand | markov | - | aco | 403003 | 298.837712 |
| hopper_stand | markov | - | aco | 403004 | 0.000000 |
| hopper_stand | markov | - | aco | 403005 | 70.058356 |
| hopper_stand | markov | - | aco | 403006 | 233.263213 |
| hopper_stand | markov | - | aco | 403007 | 185.213894 |
| hopper_stand | markov | - | aco | 403008 | 137.684573 |
| hopper_stand | markov | - | aco | 403009 | 124.964153 |
| hopper_stand | single | rain | aco | 403000 | 0.000000 |
| hopper_stand | single | rain | aco | 403001 | 13.124718 |
| hopper_stand | single | rain | aco | 403002 | 0.000000 |
| hopper_stand | single | rain | aco | 403003 | 13.420998 |
| hopper_stand | single | rain | aco | 403004 | 0.000000 |
| hopper_stand | single | fog | aco | 403000 | 7.746620 |
| hopper_stand | single | fog | aco | 403001 | 29.552215 |
| hopper_stand | single | fog | aco | 403002 | 25.156553 |
| hopper_stand | single | fog | aco | 403003 | 66.074495 |
| hopper_stand | single | fog | aco | 403004 | 0.000000 |
| hopper_stand | single | snow | aco | 403000 | 0.000000 |
| hopper_stand | single | snow | aco | 403001 | 10.435597 |
| hopper_stand | single | snow | aco | 403002 | 0.000000 |
| hopper_stand | single | snow | aco | 403003 | 0.000000 |
| hopper_stand | single | snow | aco | 403004 | 0.000000 |
| hopper_stand | single | motion_blur | aco | 403000 | 318.989213 |
| hopper_stand | single | motion_blur | aco | 403001 | 276.829603 |
| hopper_stand | single | motion_blur | aco | 403002 | 321.783504 |
| hopper_stand | single | motion_blur | aco | 403003 | 506.059818 |
| hopper_stand | single | motion_blur | aco | 403004 | 0.000000 |
| hopper_stand | single | gaussian_noise | aco | 403000 | 0.000000 |
| hopper_stand | single | gaussian_noise | aco | 403001 | 12.212797 |
| hopper_stand | single | gaussian_noise | aco | 403002 | 0.000000 |
| hopper_stand | single | gaussian_noise | aco | 403003 | 0.000000 |
| hopper_stand | single | gaussian_noise | aco | 403004 | 0.000000 |
| hopper_stand | single | low_light | aco | 403000 | 0.000000 |
| hopper_stand | single | low_light | aco | 403001 | 11.187634 |
| hopper_stand | single | low_light | aco | 403002 | 0.000000 |
| hopper_stand | single | low_light | aco | 403003 | 0.000000 |
| hopper_stand | single | low_light | aco | 403004 | 0.000000 |
| hopper_stand | single | jpeg | aco | 403000 | 353.021761 |
| hopper_stand | single | jpeg | aco | 403001 | 485.557054 |
| hopper_stand | single | jpeg | aco | 403002 | 257.321103 |
| hopper_stand | single | jpeg | aco | 403003 | 422.049429 |
| hopper_stand | single | jpeg | aco | 403004 | 0.000000 |
| hopper_stand | single | defocus_blur | aco | 403000 | 552.400354 |
| hopper_stand | single | defocus_blur | aco | 403001 | 646.438946 |
| hopper_stand | single | defocus_blur | aco | 403002 | 494.852944 |
| hopper_stand | single | defocus_blur | aco | 403003 | 687.089544 |
| hopper_stand | single | defocus_blur | aco | 403004 | 0.000000 |
| hopper_stand | single | frost | aco | 403000 | 93.608698 |
| hopper_stand | single | frost | aco | 403001 | 217.854890 |
| hopper_stand | single | frost | aco | 403002 | 122.110812 |
| hopper_stand | single | frost | aco | 403003 | 176.331149 |
| hopper_stand | single | frost | aco | 403004 | 0.000000 |
| hopper_stand | single | occlusion_patch | aco | 403000 | 875.745676 |
| hopper_stand | single | occlusion_patch | aco | 403001 | 640.638496 |
| hopper_stand | single | occlusion_patch | aco | 403002 | 278.412014 |
| hopper_stand | single | occlusion_patch | aco | 403003 | 57.272003 |
| hopper_stand | single | occlusion_patch | aco | 403004 | 0.000000 |
| hopper_stand | single | saturation | aco | 403000 | 32.125973 |
| hopper_stand | single | saturation | aco | 403001 | 88.096020 |
| hopper_stand | single | saturation | aco | 403002 | 50.598393 |
| hopper_stand | single | saturation | aco | 403003 | 25.895262 |
| hopper_stand | single | saturation | aco | 403004 | 0.000000 |
| hopper_stand | single | shadow | aco | 403000 | 264.810218 |
| hopper_stand | single | shadow | aco | 403001 | 850.929193 |
| hopper_stand | single | shadow | aco | 403002 | 818.501589 |
| hopper_stand | single | shadow | aco | 403003 | 392.679024 |
| hopper_stand | single | shadow | aco | 403004 | 0.000000 |
| hopper_stand | single | shot_noise | aco | 403000 | 0.000000 |
| hopper_stand | single | shot_noise | aco | 403001 | 11.254809 |
| hopper_stand | single | shot_noise | aco | 403002 | 0.000000 |
| hopper_stand | single | shot_noise | aco | 403003 | 0.000000 |
| hopper_stand | single | shot_noise | aco | 403004 | 0.000000 |
| hopper_stand | markov | - | smfa | 403000 | 657.078029 |
| hopper_stand | markov | - | smfa | 403001 | 515.266215 |
| hopper_stand | markov | - | smfa | 403002 | 608.643093 |
| hopper_stand | markov | - | smfa | 403003 | 634.547244 |
| hopper_stand | markov | - | smfa | 403004 | 0.000000 |
| hopper_stand | markov | - | smfa | 403005 | 590.136348 |
| hopper_stand | markov | - | smfa | 403006 | 708.510446 |
| hopper_stand | markov | - | smfa | 403007 | 564.851793 |
| hopper_stand | markov | - | smfa | 403008 | 693.411440 |
| hopper_stand | markov | - | smfa | 403009 | 425.709005 |
| hopper_stand | single | rain | smfa | 403000 | 909.908714 |
| hopper_stand | single | rain | smfa | 403001 | 886.953657 |
| hopper_stand | single | rain | smfa | 403002 | 843.727449 |
| hopper_stand | single | rain | smfa | 403003 | 860.840011 |
| hopper_stand | single | rain | smfa | 403004 | 0.000000 |
| hopper_stand | single | fog | smfa | 403000 | 910.586291 |
| hopper_stand | single | fog | smfa | 403001 | 923.522981 |
| hopper_stand | single | fog | smfa | 403002 | 915.030803 |
| hopper_stand | single | fog | smfa | 403003 | 914.698801 |
| hopper_stand | single | fog | smfa | 403004 | 0.000000 |
| hopper_stand | single | snow | smfa | 403000 | 903.893704 |
| hopper_stand | single | snow | smfa | 403001 | 933.659051 |
| hopper_stand | single | snow | smfa | 403002 | 909.868932 |
| hopper_stand | single | snow | smfa | 403003 | 828.944723 |
| hopper_stand | single | snow | smfa | 403004 | 0.000000 |
| hopper_stand | single | motion_blur | smfa | 403000 | 165.745087 |
| hopper_stand | single | motion_blur | smfa | 403001 | 128.451313 |
| hopper_stand | single | motion_blur | smfa | 403002 | 140.717126 |
| hopper_stand | single | motion_blur | smfa | 403003 | 121.911955 |
| hopper_stand | single | motion_blur | smfa | 403004 | 0.000000 |
| hopper_stand | single | gaussian_noise | smfa | 403000 | 909.476126 |
| hopper_stand | single | gaussian_noise | smfa | 403001 | 841.780594 |
| hopper_stand | single | gaussian_noise | smfa | 403002 | 914.185405 |
| hopper_stand | single | gaussian_noise | smfa | 403003 | 910.849298 |
| hopper_stand | single | gaussian_noise | smfa | 403004 | 0.000000 |
| hopper_stand | single | low_light | smfa | 403000 | 902.561993 |
| hopper_stand | single | low_light | smfa | 403001 | 907.353491 |
| hopper_stand | single | low_light | smfa | 403002 | 909.882390 |
| hopper_stand | single | low_light | smfa | 403003 | 894.588546 |
| hopper_stand | single | low_light | smfa | 403004 | 0.000000 |
| hopper_stand | single | jpeg | smfa | 403000 | 604.124302 |
| hopper_stand | single | jpeg | smfa | 403001 | 644.275224 |
| hopper_stand | single | jpeg | smfa | 403002 | 378.831152 |
| hopper_stand | single | jpeg | smfa | 403003 | 403.036590 |
| hopper_stand | single | jpeg | smfa | 403004 | 0.000000 |
| hopper_stand | single | defocus_blur | smfa | 403000 | 71.495054 |
| hopper_stand | single | defocus_blur | smfa | 403001 | 220.757346 |
| hopper_stand | single | defocus_blur | smfa | 403002 | 79.098819 |
| hopper_stand | single | defocus_blur | smfa | 403003 | 87.053774 |
| hopper_stand | single | defocus_blur | smfa | 403004 | 0.000000 |
| hopper_stand | single | frost | smfa | 403000 | 908.074790 |
| hopper_stand | single | frost | smfa | 403001 | 919.394932 |
| hopper_stand | single | frost | smfa | 403002 | 915.581931 |
| hopper_stand | single | frost | smfa | 403003 | 854.549492 |
| hopper_stand | single | frost | smfa | 403004 | 0.000000 |
| hopper_stand | single | occlusion_patch | smfa | 403000 | 908.215489 |
| hopper_stand | single | occlusion_patch | smfa | 403001 | 929.379698 |
| hopper_stand | single | occlusion_patch | smfa | 403002 | 350.497164 |
| hopper_stand | single | occlusion_patch | smfa | 403003 | 19.255924 |
| hopper_stand | single | occlusion_patch | smfa | 403004 | 0.000000 |
| hopper_stand | single | saturation | smfa | 403000 | 911.535835 |
| hopper_stand | single | saturation | smfa | 403001 | 910.566619 |
| hopper_stand | single | saturation | smfa | 403002 | 913.892300 |
| hopper_stand | single | saturation | smfa | 403003 | 914.522046 |
| hopper_stand | single | saturation | smfa | 403004 | 0.000000 |
| hopper_stand | single | shadow | smfa | 403000 | 906.262785 |
| hopper_stand | single | shadow | smfa | 403001 | 921.190649 |
| hopper_stand | single | shadow | smfa | 403002 | 914.250354 |
| hopper_stand | single | shadow | smfa | 403003 | 887.973960 |
| hopper_stand | single | shadow | smfa | 403004 | 0.000000 |
| hopper_stand | single | shot_noise | smfa | 403000 | 907.225966 |
| hopper_stand | single | shot_noise | smfa | 403001 | 918.546006 |
| hopper_stand | single | shot_noise | smfa | 403002 | 830.661241 |
| hopper_stand | single | shot_noise | smfa | 403003 | 885.511013 |
| hopper_stand | single | shot_noise | smfa | 403004 | 0.000000 |
| quadruped_run | clean | - | clean | 404000 | 557.328063 |
| quadruped_run | clean | - | clean | 404001 | 528.285726 |
| quadruped_run | clean | - | clean | 404002 | 532.484092 |
| quadruped_run | clean | - | clean | 404003 | 347.202242 |
| quadruped_run | clean | - | clean | 404004 | 550.739673 |
| quadruped_run | markov | - | raw | 404000 | 566.127604 |
| quadruped_run | markov | - | raw | 404001 | 484.471694 |
| quadruped_run | markov | - | raw | 404002 | 493.658079 |
| quadruped_run | markov | - | raw | 404003 | 535.672151 |
| quadruped_run | markov | - | raw | 404004 | 546.965919 |
| quadruped_run | markov | - | raw | 404005 | 502.423206 |
| quadruped_run | markov | - | raw | 404006 | 523.105437 |
| quadruped_run | markov | - | raw | 404007 | 272.936417 |
| quadruped_run | markov | - | raw | 404008 | 431.261981 |
| quadruped_run | markov | - | raw | 404009 | 333.333284 |
| quadruped_run | single | rain | raw | 404000 | 561.197139 |
| quadruped_run | single | rain | raw | 404001 | 491.654210 |
| quadruped_run | single | rain | raw | 404002 | 505.048929 |
| quadruped_run | single | rain | raw | 404003 | 522.651645 |
| quadruped_run | single | rain | raw | 404004 | 566.126606 |
| quadruped_run | single | fog | raw | 404000 | 543.345447 |
| quadruped_run | single | fog | raw | 404001 | 57.480649 |
| quadruped_run | single | fog | raw | 404002 | 416.188937 |
| quadruped_run | single | fog | raw | 404003 | 13.213309 |
| quadruped_run | single | fog | raw | 404004 | 557.961276 |
| quadruped_run | single | snow | raw | 404000 | 66.338491 |
| quadruped_run | single | snow | raw | 404001 | 370.013201 |
| quadruped_run | single | snow | raw | 404002 | 129.157991 |
| quadruped_run | single | snow | raw | 404003 | 273.972608 |
| quadruped_run | single | snow | raw | 404004 | 350.795399 |
| quadruped_run | single | motion_blur | raw | 404000 | 503.938784 |
| quadruped_run | single | motion_blur | raw | 404001 | 499.688092 |
| quadruped_run | single | motion_blur | raw | 404002 | 505.615944 |
| quadruped_run | single | motion_blur | raw | 404003 | 516.142411 |
| quadruped_run | single | motion_blur | raw | 404004 | 554.945186 |
| quadruped_run | single | gaussian_noise | raw | 404000 | 541.612419 |
| quadruped_run | single | gaussian_noise | raw | 404001 | 520.759228 |
| quadruped_run | single | gaussian_noise | raw | 404002 | 517.129305 |
| quadruped_run | single | gaussian_noise | raw | 404003 | 539.983709 |
| quadruped_run | single | gaussian_noise | raw | 404004 | 573.701868 |
| quadruped_run | single | low_light | raw | 404000 | 146.908290 |
| quadruped_run | single | low_light | raw | 404001 | 222.679877 |
| quadruped_run | single | low_light | raw | 404002 | 241.913065 |
| quadruped_run | single | low_light | raw | 404003 | 97.818238 |
| quadruped_run | single | low_light | raw | 404004 | 102.537850 |
| quadruped_run | single | jpeg | raw | 404000 | 564.654425 |
| quadruped_run | single | jpeg | raw | 404001 | 495.383250 |
| quadruped_run | single | jpeg | raw | 404002 | 554.149623 |
| quadruped_run | single | jpeg | raw | 404003 | 465.903977 |
| quadruped_run | single | jpeg | raw | 404004 | 518.437123 |
| quadruped_run | single | defocus_blur | raw | 404000 | 558.425285 |
| quadruped_run | single | defocus_blur | raw | 404001 | 463.440907 |
| quadruped_run | single | defocus_blur | raw | 404002 | 513.212132 |
| quadruped_run | single | defocus_blur | raw | 404003 | 416.467604 |
| quadruped_run | single | defocus_blur | raw | 404004 | 563.971828 |
| quadruped_run | single | frost | raw | 404000 | 565.344902 |
| quadruped_run | single | frost | raw | 404001 | 521.274481 |
| quadruped_run | single | frost | raw | 404002 | 514.132812 |
| quadruped_run | single | frost | raw | 404003 | 519.532737 |
| quadruped_run | single | frost | raw | 404004 | 550.955878 |
| quadruped_run | single | occlusion_patch | raw | 404000 | 562.530349 |
| quadruped_run | single | occlusion_patch | raw | 404001 | 242.616795 |
| quadruped_run | single | occlusion_patch | raw | 404002 | 549.210091 |
| quadruped_run | single | occlusion_patch | raw | 404003 | 191.148628 |
| quadruped_run | single | occlusion_patch | raw | 404004 | 558.633481 |
| quadruped_run | single | saturation | raw | 404000 | 385.298854 |
| quadruped_run | single | saturation | raw | 404001 | 491.831262 |
| quadruped_run | single | saturation | raw | 404002 | 502.763422 |
| quadruped_run | single | saturation | raw | 404003 | 462.956040 |
| quadruped_run | single | saturation | raw | 404004 | 559.835285 |
| quadruped_run | single | shadow | raw | 404000 | 529.539278 |
| quadruped_run | single | shadow | raw | 404001 | 226.841979 |
| quadruped_run | single | shadow | raw | 404002 | 551.191681 |
| quadruped_run | single | shadow | raw | 404003 | 499.938460 |
| quadruped_run | single | shadow | raw | 404004 | 443.070872 |
| quadruped_run | single | shot_noise | raw | 404000 | 524.060866 |
| quadruped_run | single | shot_noise | raw | 404001 | 538.578541 |
| quadruped_run | single | shot_noise | raw | 404002 | 545.870414 |
| quadruped_run | single | shot_noise | raw | 404003 | 496.606756 |
| quadruped_run | single | shot_noise | raw | 404004 | 567.832351 |
| quadruped_run | markov | - | aco | 404000 | 88.512704 |
| quadruped_run | markov | - | aco | 404001 | 376.888605 |
| quadruped_run | markov | - | aco | 404002 | 357.569327 |
| quadruped_run | markov | - | aco | 404003 | 357.002015 |
| quadruped_run | markov | - | aco | 404004 | 549.598090 |
| quadruped_run | markov | - | aco | 404005 | 385.101934 |
| quadruped_run | markov | - | aco | 404006 | 268.287580 |
| quadruped_run | markov | - | aco | 404007 | 121.416141 |
| quadruped_run | markov | - | aco | 404008 | 457.312137 |
| quadruped_run | markov | - | aco | 404009 | 422.034718 |
| quadruped_run | single | rain | aco | 404000 | 217.448234 |
| quadruped_run | single | rain | aco | 404001 | 341.389789 |
| quadruped_run | single | rain | aco | 404002 | 192.741735 |
| quadruped_run | single | rain | aco | 404003 | 168.146626 |
| quadruped_run | single | rain | aco | 404004 | 184.554392 |
| quadruped_run | single | fog | aco | 404000 | 488.800136 |
| quadruped_run | single | fog | aco | 404001 | 308.221814 |
| quadruped_run | single | fog | aco | 404002 | 524.860937 |
| quadruped_run | single | fog | aco | 404003 | 248.490061 |
| quadruped_run | single | fog | aco | 404004 | 544.965213 |
| quadruped_run | single | snow | aco | 404000 | 141.608477 |
| quadruped_run | single | snow | aco | 404001 | 238.798196 |
| quadruped_run | single | snow | aco | 404002 | 218.189730 |
| quadruped_run | single | snow | aco | 404003 | 98.024348 |
| quadruped_run | single | snow | aco | 404004 | 184.097238 |
| quadruped_run | single | motion_blur | aco | 404000 | 387.759714 |
| quadruped_run | single | motion_blur | aco | 404001 | 514.303104 |
| quadruped_run | single | motion_blur | aco | 404002 | 500.889892 |
| quadruped_run | single | motion_blur | aco | 404003 | 349.167831 |
| quadruped_run | single | motion_blur | aco | 404004 | 557.467299 |
| quadruped_run | single | gaussian_noise | aco | 404000 | 396.492338 |
| quadruped_run | single | gaussian_noise | aco | 404001 | 338.078550 |
| quadruped_run | single | gaussian_noise | aco | 404002 | 339.215206 |
| quadruped_run | single | gaussian_noise | aco | 404003 | 325.090268 |
| quadruped_run | single | gaussian_noise | aco | 404004 | 250.166995 |
| quadruped_run | single | low_light | aco | 404000 | 398.646673 |
| quadruped_run | single | low_light | aco | 404001 | 150.049123 |
| quadruped_run | single | low_light | aco | 404002 | 326.814643 |
| quadruped_run | single | low_light | aco | 404003 | 337.524999 |
| quadruped_run | single | low_light | aco | 404004 | 124.816995 |
| quadruped_run | single | jpeg | aco | 404000 | 344.972427 |
| quadruped_run | single | jpeg | aco | 404001 | 337.777287 |
| quadruped_run | single | jpeg | aco | 404002 | 416.517848 |
| quadruped_run | single | jpeg | aco | 404003 | 420.997997 |
| quadruped_run | single | jpeg | aco | 404004 | 430.083912 |
| quadruped_run | single | defocus_blur | aco | 404000 | 248.100613 |
| quadruped_run | single | defocus_blur | aco | 404001 | 521.291611 |
| quadruped_run | single | defocus_blur | aco | 404002 | 536.489501 |
| quadruped_run | single | defocus_blur | aco | 404003 | 454.158599 |
| quadruped_run | single | defocus_blur | aco | 404004 | 578.778711 |
| quadruped_run | single | frost | aco | 404000 | 420.146128 |
| quadruped_run | single | frost | aco | 404001 | 388.254203 |
| quadruped_run | single | frost | aco | 404002 | 425.475593 |
| quadruped_run | single | frost | aco | 404003 | 291.762406 |
| quadruped_run | single | frost | aco | 404004 | 546.472980 |
| quadruped_run | single | occlusion_patch | aco | 404000 | 560.566640 |
| quadruped_run | single | occlusion_patch | aco | 404001 | 237.298964 |
| quadruped_run | single | occlusion_patch | aco | 404002 | 549.469818 |
| quadruped_run | single | occlusion_patch | aco | 404003 | 200.646949 |
| quadruped_run | single | occlusion_patch | aco | 404004 | 569.492804 |
| quadruped_run | single | saturation | aco | 404000 | 545.694230 |
| quadruped_run | single | saturation | aco | 404001 | 16.070840 |
| quadruped_run | single | saturation | aco | 404002 | 11.952354 |
| quadruped_run | single | saturation | aco | 404003 | 7.299707 |
| quadruped_run | single | saturation | aco | 404004 | 546.149769 |
| quadruped_run | single | shadow | aco | 404000 | 516.892267 |
| quadruped_run | single | shadow | aco | 404001 | 486.986639 |
| quadruped_run | single | shadow | aco | 404002 | 477.381377 |
| quadruped_run | single | shadow | aco | 404003 | 468.704527 |
| quadruped_run | single | shadow | aco | 404004 | 240.079301 |
| quadruped_run | single | shot_noise | aco | 404000 | 57.641325 |
| quadruped_run | single | shot_noise | aco | 404001 | 273.104494 |
| quadruped_run | single | shot_noise | aco | 404002 | 452.008900 |
| quadruped_run | single | shot_noise | aco | 404003 | 227.595026 |
| quadruped_run | single | shot_noise | aco | 404004 | 470.971966 |
| quadruped_run | markov | - | smfa | 404000 | 49.302328 |
| quadruped_run | markov | - | smfa | 404001 | 506.461670 |
| quadruped_run | markov | - | smfa | 404002 | 537.844343 |
| quadruped_run | markov | - | smfa | 404003 | 492.796243 |
| quadruped_run | markov | - | smfa | 404004 | 489.692490 |
| quadruped_run | markov | - | smfa | 404005 | 439.479553 |
| quadruped_run | markov | - | smfa | 404006 | 519.107932 |
| quadruped_run | markov | - | smfa | 404007 | 495.486956 |
| quadruped_run | markov | - | smfa | 404008 | 471.489080 |
| quadruped_run | markov | - | smfa | 404009 | 532.631263 |
| quadruped_run | single | rain | smfa | 404000 | 552.541012 |
| quadruped_run | single | rain | smfa | 404001 | 488.714414 |
| quadruped_run | single | rain | smfa | 404002 | 532.206895 |
| quadruped_run | single | rain | smfa | 404003 | 504.676327 |
| quadruped_run | single | rain | smfa | 404004 | 455.348882 |
| quadruped_run | single | fog | smfa | 404000 | 471.609344 |
| quadruped_run | single | fog | smfa | 404001 | 531.687126 |
| quadruped_run | single | fog | smfa | 404002 | 471.223720 |
| quadruped_run | single | fog | smfa | 404003 | 463.511621 |
| quadruped_run | single | fog | smfa | 404004 | 553.211175 |
| quadruped_run | single | snow | smfa | 404000 | 46.890954 |
| quadruped_run | single | snow | smfa | 404001 | 490.390358 |
| quadruped_run | single | snow | smfa | 404002 | 530.366804 |
| quadruped_run | single | snow | smfa | 404003 | 507.584238 |
| quadruped_run | single | snow | smfa | 404004 | 557.074873 |
| quadruped_run | single | motion_blur | smfa | 404000 | 497.664812 |
| quadruped_run | single | motion_blur | smfa | 404001 | 15.162224 |
| quadruped_run | single | motion_blur | smfa | 404002 | 486.134751 |
| quadruped_run | single | motion_blur | smfa | 404003 | 37.096621 |
| quadruped_run | single | motion_blur | smfa | 404004 | 562.055651 |
| quadruped_run | single | gaussian_noise | smfa | 404000 | 557.987746 |
| quadruped_run | single | gaussian_noise | smfa | 404001 | 492.660639 |
| quadruped_run | single | gaussian_noise | smfa | 404002 | 536.895711 |
| quadruped_run | single | gaussian_noise | smfa | 404003 | 512.004442 |
| quadruped_run | single | gaussian_noise | smfa | 404004 | 562.701408 |
| quadruped_run | single | low_light | smfa | 404000 | 527.187837 |
| quadruped_run | single | low_light | smfa | 404001 | 513.311234 |
| quadruped_run | single | low_light | smfa | 404002 | 256.581116 |
| quadruped_run | single | low_light | smfa | 404003 | 474.136686 |
| quadruped_run | single | low_light | smfa | 404004 | 562.714180 |
| quadruped_run | single | jpeg | smfa | 404000 | 561.329772 |
| quadruped_run | single | jpeg | smfa | 404001 | 390.475318 |
| quadruped_run | single | jpeg | smfa | 404002 | 538.597353 |
| quadruped_run | single | jpeg | smfa | 404003 | 495.557570 |
| quadruped_run | single | jpeg | smfa | 404004 | 572.341900 |
| quadruped_run | single | defocus_blur | smfa | 404000 | 564.734141 |
| quadruped_run | single | defocus_blur | smfa | 404001 | 442.715655 |
| quadruped_run | single | defocus_blur | smfa | 404002 | 497.110953 |
| quadruped_run | single | defocus_blur | smfa | 404003 | 9.996335 |
| quadruped_run | single | defocus_blur | smfa | 404004 | 551.314021 |
| quadruped_run | single | frost | smfa | 404000 | 396.849796 |
| quadruped_run | single | frost | smfa | 404001 | 516.198194 |
| quadruped_run | single | frost | smfa | 404002 | 479.813431 |
| quadruped_run | single | frost | smfa | 404003 | 462.479448 |
| quadruped_run | single | frost | smfa | 404004 | 561.588842 |
| quadruped_run | single | occlusion_patch | smfa | 404000 | 547.088600 |
| quadruped_run | single | occlusion_patch | smfa | 404001 | 498.968001 |
| quadruped_run | single | occlusion_patch | smfa | 404002 | 505.594373 |
| quadruped_run | single | occlusion_patch | smfa | 404003 | 435.816736 |
| quadruped_run | single | occlusion_patch | smfa | 404004 | 561.733355 |
| quadruped_run | single | saturation | smfa | 404000 | 558.619714 |
| quadruped_run | single | saturation | smfa | 404001 | 515.790681 |
| quadruped_run | single | saturation | smfa | 404002 | 531.847535 |
| quadruped_run | single | saturation | smfa | 404003 | 479.317787 |
| quadruped_run | single | saturation | smfa | 404004 | 557.940711 |
| quadruped_run | single | shadow | smfa | 404000 | 373.859178 |
| quadruped_run | single | shadow | smfa | 404001 | 513.200333 |
| quadruped_run | single | shadow | smfa | 404002 | 547.272081 |
| quadruped_run | single | shadow | smfa | 404003 | 476.923099 |
| quadruped_run | single | shadow | smfa | 404004 | 545.532067 |
| quadruped_run | single | shot_noise | smfa | 404000 | 325.675987 |
| quadruped_run | single | shot_noise | smfa | 404001 | 504.900244 |
| quadruped_run | single | shot_noise | smfa | 404002 | 537.837705 |
| quadruped_run | single | shot_noise | smfa | 404003 | 423.249976 |
| quadruped_run | single | shot_noise | smfa | 404004 | 554.485017 |
| finger_turn_hard | clean | - | clean | 405000 | 0.000000 |
| finger_turn_hard | clean | - | clean | 405001 | 929.000000 |
| finger_turn_hard | clean | - | clean | 405002 | 951.000000 |
| finger_turn_hard | clean | - | clean | 405003 | 506.000000 |
| finger_turn_hard | clean | - | clean | 405004 | 902.000000 |
| finger_turn_hard | markov | - | raw | 405000 | 8.000000 |
| finger_turn_hard | markov | - | raw | 405001 | 434.000000 |
| finger_turn_hard | markov | - | raw | 405002 | 944.000000 |
| finger_turn_hard | markov | - | raw | 405003 | 19.000000 |
| finger_turn_hard | markov | - | raw | 405004 | 163.000000 |
| finger_turn_hard | markov | - | raw | 405005 | 914.000000 |
| finger_turn_hard | markov | - | raw | 405006 | 755.000000 |
| finger_turn_hard | markov | - | raw | 405007 | 0.000000 |
| finger_turn_hard | markov | - | raw | 405008 | 908.000000 |
| finger_turn_hard | markov | - | raw | 405009 | 0.000000 |
| finger_turn_hard | single | rain | raw | 405000 | 980.000000 |
| finger_turn_hard | single | rain | raw | 405001 | 919.000000 |
| finger_turn_hard | single | rain | raw | 405002 | 953.000000 |
| finger_turn_hard | single | rain | raw | 405003 | 697.000000 |
| finger_turn_hard | single | rain | raw | 405004 | 928.000000 |
| finger_turn_hard | single | fog | raw | 405000 | 982.000000 |
| finger_turn_hard | single | fog | raw | 405001 | 873.000000 |
| finger_turn_hard | single | fog | raw | 405002 | 954.000000 |
| finger_turn_hard | single | fog | raw | 405003 | 0.000000 |
| finger_turn_hard | single | fog | raw | 405004 | 0.000000 |
| finger_turn_hard | single | snow | raw | 405000 | 0.000000 |
| finger_turn_hard | single | snow | raw | 405001 | 0.000000 |
| finger_turn_hard | single | snow | raw | 405002 | 0.000000 |
| finger_turn_hard | single | snow | raw | 405003 | 0.000000 |
| finger_turn_hard | single | snow | raw | 405004 | 0.000000 |
| finger_turn_hard | single | motion_blur | raw | 405000 | 0.000000 |
| finger_turn_hard | single | motion_blur | raw | 405001 | 70.000000 |
| finger_turn_hard | single | motion_blur | raw | 405002 | 0.000000 |
| finger_turn_hard | single | motion_blur | raw | 405003 | 16.000000 |
| finger_turn_hard | single | motion_blur | raw | 405004 | 76.000000 |
| finger_turn_hard | single | gaussian_noise | raw | 405000 | 204.000000 |
| finger_turn_hard | single | gaussian_noise | raw | 405001 | 0.000000 |
| finger_turn_hard | single | gaussian_noise | raw | 405002 | 960.000000 |
| finger_turn_hard | single | gaussian_noise | raw | 405003 | 0.000000 |
| finger_turn_hard | single | gaussian_noise | raw | 405004 | 933.000000 |
| finger_turn_hard | single | low_light | raw | 405000 | 0.000000 |
| finger_turn_hard | single | low_light | raw | 405001 | 0.000000 |
| finger_turn_hard | single | low_light | raw | 405002 | 0.000000 |
| finger_turn_hard | single | low_light | raw | 405003 | 0.000000 |
| finger_turn_hard | single | low_light | raw | 405004 | 0.000000 |
| finger_turn_hard | single | jpeg | raw | 405000 | 691.000000 |
| finger_turn_hard | single | jpeg | raw | 405001 | 883.000000 |
| finger_turn_hard | single | jpeg | raw | 405002 | 954.000000 |
| finger_turn_hard | single | jpeg | raw | 405003 | 15.000000 |
| finger_turn_hard | single | jpeg | raw | 405004 | 931.000000 |
| finger_turn_hard | single | defocus_blur | raw | 405000 | 30.000000 |
| finger_turn_hard | single | defocus_blur | raw | 405001 | 236.000000 |
| finger_turn_hard | single | defocus_blur | raw | 405002 | 3.000000 |
| finger_turn_hard | single | defocus_blur | raw | 405003 | 18.000000 |
| finger_turn_hard | single | defocus_blur | raw | 405004 | 74.000000 |
| finger_turn_hard | single | frost | raw | 405000 | 982.000000 |
| finger_turn_hard | single | frost | raw | 405001 | 929.000000 |
| finger_turn_hard | single | frost | raw | 405002 | 951.000000 |
| finger_turn_hard | single | frost | raw | 405003 | 22.000000 |
| finger_turn_hard | single | frost | raw | 405004 | 924.000000 |
| finger_turn_hard | single | occlusion_patch | raw | 405000 | 981.000000 |
| finger_turn_hard | single | occlusion_patch | raw | 405001 | 0.000000 |
| finger_turn_hard | single | occlusion_patch | raw | 405002 | 941.000000 |
| finger_turn_hard | single | occlusion_patch | raw | 405003 | 13.000000 |
| finger_turn_hard | single | occlusion_patch | raw | 405004 | 932.000000 |
| finger_turn_hard | single | saturation | raw | 405000 | 0.000000 |
| finger_turn_hard | single | saturation | raw | 405001 | 934.000000 |
| finger_turn_hard | single | saturation | raw | 405002 | 932.000000 |
| finger_turn_hard | single | saturation | raw | 405003 | 0.000000 |
| finger_turn_hard | single | saturation | raw | 405004 | 922.000000 |
| finger_turn_hard | single | shadow | raw | 405000 | 8.000000 |
| finger_turn_hard | single | shadow | raw | 405001 | 918.000000 |
| finger_turn_hard | single | shadow | raw | 405002 | 5.000000 |
| finger_turn_hard | single | shadow | raw | 405003 | 39.000000 |
| finger_turn_hard | single | shadow | raw | 405004 | 790.000000 |
| finger_turn_hard | single | shot_noise | raw | 405000 | 0.000000 |
| finger_turn_hard | single | shot_noise | raw | 405001 | 927.000000 |
| finger_turn_hard | single | shot_noise | raw | 405002 | 959.000000 |
| finger_turn_hard | single | shot_noise | raw | 405003 | 3.000000 |
| finger_turn_hard | single | shot_noise | raw | 405004 | 936.000000 |
| finger_turn_hard | markov | - | aco | 405000 | 0.000000 |
| finger_turn_hard | markov | - | aco | 405001 | 532.000000 |
| finger_turn_hard | markov | - | aco | 405002 | 8.000000 |
| finger_turn_hard | markov | - | aco | 405003 | 23.000000 |
| finger_turn_hard | markov | - | aco | 405004 | 221.000000 |
| finger_turn_hard | markov | - | aco | 405005 | 764.000000 |
| finger_turn_hard | markov | - | aco | 405006 | 623.000000 |
| finger_turn_hard | markov | - | aco | 405007 | 46.000000 |
| finger_turn_hard | markov | - | aco | 405008 | 535.000000 |
| finger_turn_hard | markov | - | aco | 405009 | 0.000000 |
| finger_turn_hard | single | rain | aco | 405000 | 0.000000 |
| finger_turn_hard | single | rain | aco | 405001 | 909.000000 |
| finger_turn_hard | single | rain | aco | 405002 | 0.000000 |
| finger_turn_hard | single | rain | aco | 405003 | 0.000000 |
| finger_turn_hard | single | rain | aco | 405004 | 859.000000 |
| finger_turn_hard | single | fog | aco | 405000 | 0.000000 |
| finger_turn_hard | single | fog | aco | 405001 | 0.000000 |
| finger_turn_hard | single | fog | aco | 405002 | 5.000000 |
| finger_turn_hard | single | fog | aco | 405003 | 940.000000 |
| finger_turn_hard | single | fog | aco | 405004 | 11.000000 |
| finger_turn_hard | single | snow | aco | 405000 | 0.000000 |
| finger_turn_hard | single | snow | aco | 405001 | 912.000000 |
| finger_turn_hard | single | snow | aco | 405002 | 0.000000 |
| finger_turn_hard | single | snow | aco | 405003 | 0.000000 |
| finger_turn_hard | single | snow | aco | 405004 | 25.000000 |
| finger_turn_hard | single | motion_blur | aco | 405000 | 0.000000 |
| finger_turn_hard | single | motion_blur | aco | 405001 | 44.000000 |
| finger_turn_hard | single | motion_blur | aco | 405002 | 22.000000 |
| finger_turn_hard | single | motion_blur | aco | 405003 | 0.000000 |
| finger_turn_hard | single | motion_blur | aco | 405004 | 707.000000 |
| finger_turn_hard | single | gaussian_noise | aco | 405000 | 269.000000 |
| finger_turn_hard | single | gaussian_noise | aco | 405001 | 0.000000 |
| finger_turn_hard | single | gaussian_noise | aco | 405002 | 0.000000 |
| finger_turn_hard | single | gaussian_noise | aco | 405003 | 0.000000 |
| finger_turn_hard | single | gaussian_noise | aco | 405004 | 0.000000 |
| finger_turn_hard | single | low_light | aco | 405000 | 0.000000 |
| finger_turn_hard | single | low_light | aco | 405001 | 0.000000 |
| finger_turn_hard | single | low_light | aco | 405002 | 0.000000 |
| finger_turn_hard | single | low_light | aco | 405003 | 0.000000 |
| finger_turn_hard | single | low_light | aco | 405004 | 0.000000 |
| finger_turn_hard | single | jpeg | aco | 405000 | 24.000000 |
| finger_turn_hard | single | jpeg | aco | 405001 | 81.000000 |
| finger_turn_hard | single | jpeg | aco | 405002 | 14.000000 |
| finger_turn_hard | single | jpeg | aco | 405003 | 66.000000 |
| finger_turn_hard | single | jpeg | aco | 405004 | 77.000000 |
| finger_turn_hard | single | defocus_blur | aco | 405000 | 982.000000 |
| finger_turn_hard | single | defocus_blur | aco | 405001 | 581.000000 |
| finger_turn_hard | single | defocus_blur | aco | 405002 | 946.000000 |
| finger_turn_hard | single | defocus_blur | aco | 405003 | 3.000000 |
| finger_turn_hard | single | defocus_blur | aco | 405004 | 512.000000 |
| finger_turn_hard | single | frost | aco | 405000 | 0.000000 |
| finger_turn_hard | single | frost | aco | 405001 | 927.000000 |
| finger_turn_hard | single | frost | aco | 405002 | 940.000000 |
| finger_turn_hard | single | frost | aco | 405003 | 0.000000 |
| finger_turn_hard | single | frost | aco | 405004 | 693.000000 |
| finger_turn_hard | single | occlusion_patch | aco | 405000 | 981.000000 |
| finger_turn_hard | single | occlusion_patch | aco | 405001 | 239.000000 |
| finger_turn_hard | single | occlusion_patch | aco | 405002 | 949.000000 |
| finger_turn_hard | single | occlusion_patch | aco | 405003 | 175.000000 |
| finger_turn_hard | single | occlusion_patch | aco | 405004 | 935.000000 |
| finger_turn_hard | single | saturation | aco | 405000 | 0.000000 |
| finger_turn_hard | single | saturation | aco | 405001 | 0.000000 |
| finger_turn_hard | single | saturation | aco | 405002 | 10.000000 |
| finger_turn_hard | single | saturation | aco | 405003 | 0.000000 |
| finger_turn_hard | single | saturation | aco | 405004 | 0.000000 |
| finger_turn_hard | single | shadow | aco | 405000 | 6.000000 |
| finger_turn_hard | single | shadow | aco | 405001 | 897.000000 |
| finger_turn_hard | single | shadow | aco | 405002 | 0.000000 |
| finger_turn_hard | single | shadow | aco | 405003 | 38.000000 |
| finger_turn_hard | single | shadow | aco | 405004 | 941.000000 |
| finger_turn_hard | single | shot_noise | aco | 405000 | 0.000000 |
| finger_turn_hard | single | shot_noise | aco | 405001 | 0.000000 |
| finger_turn_hard | single | shot_noise | aco | 405002 | 0.000000 |
| finger_turn_hard | single | shot_noise | aco | 405003 | 0.000000 |
| finger_turn_hard | single | shot_noise | aco | 405004 | 0.000000 |
| finger_turn_hard | markov | - | smfa | 405000 | 688.000000 |
| finger_turn_hard | markov | - | smfa | 405001 | 4.000000 |
| finger_turn_hard | markov | - | smfa | 405002 | 952.000000 |
| finger_turn_hard | markov | - | smfa | 405003 | 10.000000 |
| finger_turn_hard | markov | - | smfa | 405004 | 816.000000 |
| finger_turn_hard | markov | - | smfa | 405005 | 938.000000 |
| finger_turn_hard | markov | - | smfa | 405006 | 903.000000 |
| finger_turn_hard | markov | - | smfa | 405007 | 868.000000 |
| finger_turn_hard | markov | - | smfa | 405008 | 841.000000 |
| finger_turn_hard | markov | - | smfa | 405009 | 855.000000 |
| finger_turn_hard | single | rain | smfa | 405000 | 3.000000 |
| finger_turn_hard | single | rain | smfa | 405001 | 917.000000 |
| finger_turn_hard | single | rain | smfa | 405002 | 957.000000 |
| finger_turn_hard | single | rain | smfa | 405003 | 0.000000 |
| finger_turn_hard | single | rain | smfa | 405004 | 932.000000 |
| finger_turn_hard | single | fog | smfa | 405000 | 451.000000 |
| finger_turn_hard | single | fog | smfa | 405001 | 922.000000 |
| finger_turn_hard | single | fog | smfa | 405002 | 960.000000 |
| finger_turn_hard | single | fog | smfa | 405003 | 0.000000 |
| finger_turn_hard | single | fog | smfa | 405004 | 933.000000 |
| finger_turn_hard | single | snow | smfa | 405000 | 0.000000 |
| finger_turn_hard | single | snow | smfa | 405001 | 923.000000 |
| finger_turn_hard | single | snow | smfa | 405002 | 959.000000 |
| finger_turn_hard | single | snow | smfa | 405003 | 0.000000 |
| finger_turn_hard | single | snow | smfa | 405004 | 939.000000 |
| finger_turn_hard | single | motion_blur | smfa | 405000 | 2.000000 |
| finger_turn_hard | single | motion_blur | smfa | 405001 | 182.000000 |
| finger_turn_hard | single | motion_blur | smfa | 405002 | 30.000000 |
| finger_turn_hard | single | motion_blur | smfa | 405003 | 6.000000 |
| finger_turn_hard | single | motion_blur | smfa | 405004 | 81.000000 |
| finger_turn_hard | single | gaussian_noise | smfa | 405000 | 974.000000 |
| finger_turn_hard | single | gaussian_noise | smfa | 405001 | 919.000000 |
| finger_turn_hard | single | gaussian_noise | smfa | 405002 | 951.000000 |
| finger_turn_hard | single | gaussian_noise | smfa | 405003 | 0.000000 |
| finger_turn_hard | single | gaussian_noise | smfa | 405004 | 936.000000 |
| finger_turn_hard | single | low_light | smfa | 405000 | 0.000000 |
| finger_turn_hard | single | low_light | smfa | 405001 | 0.000000 |
| finger_turn_hard | single | low_light | smfa | 405002 | 955.000000 |
| finger_turn_hard | single | low_light | smfa | 405003 | 0.000000 |
| finger_turn_hard | single | low_light | smfa | 405004 | 927.000000 |
| finger_turn_hard | single | jpeg | smfa | 405000 | 666.000000 |
| finger_turn_hard | single | jpeg | smfa | 405001 | 0.000000 |
| finger_turn_hard | single | jpeg | smfa | 405002 | 957.000000 |
| finger_turn_hard | single | jpeg | smfa | 405003 | 0.000000 |
| finger_turn_hard | single | jpeg | smfa | 405004 | 906.000000 |
| finger_turn_hard | single | defocus_blur | smfa | 405000 | 6.000000 |
| finger_turn_hard | single | defocus_blur | smfa | 405001 | 620.000000 |
| finger_turn_hard | single | defocus_blur | smfa | 405002 | 3.000000 |
| finger_turn_hard | single | defocus_blur | smfa | 405003 | 591.000000 |
| finger_turn_hard | single | defocus_blur | smfa | 405004 | 0.000000 |
| finger_turn_hard | single | frost | smfa | 405000 | 952.000000 |
| finger_turn_hard | single | frost | smfa | 405001 | 919.000000 |
| finger_turn_hard | single | frost | smfa | 405002 | 956.000000 |
| finger_turn_hard | single | frost | smfa | 405003 | 2.000000 |
| finger_turn_hard | single | frost | smfa | 405004 | 933.000000 |
| finger_turn_hard | single | occlusion_patch | smfa | 405000 | 21.000000 |
| finger_turn_hard | single | occlusion_patch | smfa | 405001 | 0.000000 |
| finger_turn_hard | single | occlusion_patch | smfa | 405002 | 910.000000 |
| finger_turn_hard | single | occlusion_patch | smfa | 405003 | 653.000000 |
| finger_turn_hard | single | occlusion_patch | smfa | 405004 | 930.000000 |
| finger_turn_hard | single | saturation | smfa | 405000 | 0.000000 |
| finger_turn_hard | single | saturation | smfa | 405001 | 936.000000 |
| finger_turn_hard | single | saturation | smfa | 405002 | 954.000000 |
| finger_turn_hard | single | saturation | smfa | 405003 | 0.000000 |
| finger_turn_hard | single | saturation | smfa | 405004 | 935.000000 |
| finger_turn_hard | single | shadow | smfa | 405000 | 23.000000 |
| finger_turn_hard | single | shadow | smfa | 405001 | 925.000000 |
| finger_turn_hard | single | shadow | smfa | 405002 | 3.000000 |
| finger_turn_hard | single | shadow | smfa | 405003 | 0.000000 |
| finger_turn_hard | single | shadow | smfa | 405004 | 739.000000 |
| finger_turn_hard | single | shot_noise | smfa | 405000 | 0.000000 |
| finger_turn_hard | single | shot_noise | smfa | 405001 | 930.000000 |
| finger_turn_hard | single | shot_noise | smfa | 405002 | 956.000000 |
| finger_turn_hard | single | shot_noise | smfa | 405003 | 0.000000 |
| finger_turn_hard | single | shot_noise | smfa | 405004 | 930.000000 |
| cartpole_swingup_sparse | clean | - | clean | 406000 | 817.000000 |
| cartpole_swingup_sparse | clean | - | clean | 406001 | 835.000000 |
| cartpole_swingup_sparse | clean | - | clean | 406002 | 836.000000 |
| cartpole_swingup_sparse | clean | - | clean | 406003 | 836.000000 |
| cartpole_swingup_sparse | clean | - | clean | 406004 | 832.000000 |
| cartpole_swingup_sparse | markov | - | raw | 406000 | 36.000000 |
| cartpole_swingup_sparse | markov | - | raw | 406001 | 56.000000 |
| cartpole_swingup_sparse | markov | - | raw | 406002 | 20.000000 |
| cartpole_swingup_sparse | markov | - | raw | 406003 | 187.000000 |
| cartpole_swingup_sparse | markov | - | raw | 406004 | 60.000000 |
| cartpole_swingup_sparse | markov | - | raw | 406005 | 27.000000 |
| cartpole_swingup_sparse | markov | - | raw | 406006 | 232.000000 |
| cartpole_swingup_sparse | markov | - | raw | 406007 | 1.000000 |
| cartpole_swingup_sparse | markov | - | raw | 406008 | 17.000000 |
| cartpole_swingup_sparse | markov | - | raw | 406009 | 5.000000 |
| cartpole_swingup_sparse | single | rain | raw | 406000 | 0.000000 |
| cartpole_swingup_sparse | single | rain | raw | 406001 | 0.000000 |
| cartpole_swingup_sparse | single | rain | raw | 406002 | 15.000000 |
| cartpole_swingup_sparse | single | rain | raw | 406003 | 0.000000 |
| cartpole_swingup_sparse | single | rain | raw | 406004 | 0.000000 |
| cartpole_swingup_sparse | single | fog | raw | 406000 | 828.000000 |
| cartpole_swingup_sparse | single | fog | raw | 406001 | 836.000000 |
| cartpole_swingup_sparse | single | fog | raw | 406002 | 837.000000 |
| cartpole_swingup_sparse | single | fog | raw | 406003 | 429.000000 |
| cartpole_swingup_sparse | single | fog | raw | 406004 | 830.000000 |
| cartpole_swingup_sparse | single | snow | raw | 406000 | 0.000000 |
| cartpole_swingup_sparse | single | snow | raw | 406001 | 0.000000 |
| cartpole_swingup_sparse | single | snow | raw | 406002 | 0.000000 |
| cartpole_swingup_sparse | single | snow | raw | 406003 | 0.000000 |
| cartpole_swingup_sparse | single | snow | raw | 406004 | 0.000000 |
| cartpole_swingup_sparse | single | motion_blur | raw | 406000 | 18.000000 |
| cartpole_swingup_sparse | single | motion_blur | raw | 406001 | 20.000000 |
| cartpole_swingup_sparse | single | motion_blur | raw | 406002 | 4.000000 |
| cartpole_swingup_sparse | single | motion_blur | raw | 406003 | 4.000000 |
| cartpole_swingup_sparse | single | motion_blur | raw | 406004 | 0.000000 |
| cartpole_swingup_sparse | single | gaussian_noise | raw | 406000 | 309.000000 |
| cartpole_swingup_sparse | single | gaussian_noise | raw | 406001 | 374.000000 |
| cartpole_swingup_sparse | single | gaussian_noise | raw | 406002 | 493.000000 |
| cartpole_swingup_sparse | single | gaussian_noise | raw | 406003 | 160.000000 |
| cartpole_swingup_sparse | single | gaussian_noise | raw | 406004 | 584.000000 |
| cartpole_swingup_sparse | single | low_light | raw | 406000 | 18.000000 |
| cartpole_swingup_sparse | single | low_light | raw | 406001 | 25.000000 |
| cartpole_swingup_sparse | single | low_light | raw | 406002 | 28.000000 |
| cartpole_swingup_sparse | single | low_light | raw | 406003 | 74.000000 |
| cartpole_swingup_sparse | single | low_light | raw | 406004 | 13.000000 |
| cartpole_swingup_sparse | single | jpeg | raw | 406000 | 119.000000 |
| cartpole_swingup_sparse | single | jpeg | raw | 406001 | 109.000000 |
| cartpole_swingup_sparse | single | jpeg | raw | 406002 | 103.000000 |
| cartpole_swingup_sparse | single | jpeg | raw | 406003 | 69.000000 |
| cartpole_swingup_sparse | single | jpeg | raw | 406004 | 121.000000 |
| cartpole_swingup_sparse | single | defocus_blur | raw | 406000 | 8.000000 |
| cartpole_swingup_sparse | single | defocus_blur | raw | 406001 | 4.000000 |
| cartpole_swingup_sparse | single | defocus_blur | raw | 406002 | 5.000000 |
| cartpole_swingup_sparse | single | defocus_blur | raw | 406003 | 25.000000 |
| cartpole_swingup_sparse | single | defocus_blur | raw | 406004 | 32.000000 |
| cartpole_swingup_sparse | single | frost | raw | 406000 | 0.000000 |
| cartpole_swingup_sparse | single | frost | raw | 406001 | 0.000000 |
| cartpole_swingup_sparse | single | frost | raw | 406002 | 110.000000 |
| cartpole_swingup_sparse | single | frost | raw | 406003 | 0.000000 |
| cartpole_swingup_sparse | single | frost | raw | 406004 | 783.000000 |
| cartpole_swingup_sparse | single | occlusion_patch | raw | 406000 | 64.000000 |
| cartpole_swingup_sparse | single | occlusion_patch | raw | 406001 | 14.000000 |
| cartpole_swingup_sparse | single | occlusion_patch | raw | 406002 | 43.000000 |
| cartpole_swingup_sparse | single | occlusion_patch | raw | 406003 | 6.000000 |
| cartpole_swingup_sparse | single | occlusion_patch | raw | 406004 | 0.000000 |
| cartpole_swingup_sparse | single | saturation | raw | 406000 | 51.000000 |
| cartpole_swingup_sparse | single | saturation | raw | 406001 | 23.000000 |
| cartpole_swingup_sparse | single | saturation | raw | 406002 | 98.000000 |
| cartpole_swingup_sparse | single | saturation | raw | 406003 | 457.000000 |
| cartpole_swingup_sparse | single | saturation | raw | 406004 | 244.000000 |
| cartpole_swingup_sparse | single | shadow | raw | 406000 | 194.000000 |
| cartpole_swingup_sparse | single | shadow | raw | 406001 | 182.000000 |
| cartpole_swingup_sparse | single | shadow | raw | 406002 | 148.000000 |
| cartpole_swingup_sparse | single | shadow | raw | 406003 | 182.000000 |
| cartpole_swingup_sparse | single | shadow | raw | 406004 | 778.000000 |
| cartpole_swingup_sparse | single | shot_noise | raw | 406000 | 12.000000 |
| cartpole_swingup_sparse | single | shot_noise | raw | 406001 | 8.000000 |
| cartpole_swingup_sparse | single | shot_noise | raw | 406002 | 0.000000 |
| cartpole_swingup_sparse | single | shot_noise | raw | 406003 | 0.000000 |
| cartpole_swingup_sparse | single | shot_noise | raw | 406004 | 0.000000 |
| cartpole_swingup_sparse | markov | - | aco | 406000 | 21.000000 |
| cartpole_swingup_sparse | markov | - | aco | 406001 | 0.000000 |
| cartpole_swingup_sparse | markov | - | aco | 406002 | 0.000000 |
| cartpole_swingup_sparse | markov | - | aco | 406003 | 92.000000 |
| cartpole_swingup_sparse | markov | - | aco | 406004 | 8.000000 |
| cartpole_swingup_sparse | markov | - | aco | 406005 | 0.000000 |
| cartpole_swingup_sparse | markov | - | aco | 406006 | 55.000000 |
| cartpole_swingup_sparse | markov | - | aco | 406007 | 0.000000 |
| cartpole_swingup_sparse | markov | - | aco | 406008 | 8.000000 |
| cartpole_swingup_sparse | markov | - | aco | 406009 | 10.000000 |
| cartpole_swingup_sparse | single | rain | aco | 406000 | 40.000000 |
| cartpole_swingup_sparse | single | rain | aco | 406001 | 18.000000 |
| cartpole_swingup_sparse | single | rain | aco | 406002 | 28.000000 |
| cartpole_swingup_sparse | single | rain | aco | 406003 | 0.000000 |
| cartpole_swingup_sparse | single | rain | aco | 406004 | 28.000000 |
| cartpole_swingup_sparse | single | fog | aco | 406000 | 249.000000 |
| cartpole_swingup_sparse | single | fog | aco | 406001 | 517.000000 |
| cartpole_swingup_sparse | single | fog | aco | 406002 | 407.000000 |
| cartpole_swingup_sparse | single | fog | aco | 406003 | 49.000000 |
| cartpole_swingup_sparse | single | fog | aco | 406004 | 212.000000 |
| cartpole_swingup_sparse | single | snow | aco | 406000 | 0.000000 |
| cartpole_swingup_sparse | single | snow | aco | 406001 | 0.000000 |
| cartpole_swingup_sparse | single | snow | aco | 406002 | 0.000000 |
| cartpole_swingup_sparse | single | snow | aco | 406003 | 0.000000 |
| cartpole_swingup_sparse | single | snow | aco | 406004 | 0.000000 |
| cartpole_swingup_sparse | single | motion_blur | aco | 406000 | 50.000000 |
| cartpole_swingup_sparse | single | motion_blur | aco | 406001 | 24.000000 |
| cartpole_swingup_sparse | single | motion_blur | aco | 406002 | 26.000000 |
| cartpole_swingup_sparse | single | motion_blur | aco | 406003 | 31.000000 |
| cartpole_swingup_sparse | single | motion_blur | aco | 406004 | 41.000000 |
| cartpole_swingup_sparse | single | gaussian_noise | aco | 406000 | 0.000000 |
| cartpole_swingup_sparse | single | gaussian_noise | aco | 406001 | 0.000000 |
| cartpole_swingup_sparse | single | gaussian_noise | aco | 406002 | 0.000000 |
| cartpole_swingup_sparse | single | gaussian_noise | aco | 406003 | 0.000000 |
| cartpole_swingup_sparse | single | gaussian_noise | aco | 406004 | 0.000000 |
| cartpole_swingup_sparse | single | low_light | aco | 406000 | 7.000000 |
| cartpole_swingup_sparse | single | low_light | aco | 406001 | 0.000000 |
| cartpole_swingup_sparse | single | low_light | aco | 406002 | 0.000000 |
| cartpole_swingup_sparse | single | low_light | aco | 406003 | 0.000000 |
| cartpole_swingup_sparse | single | low_light | aco | 406004 | 0.000000 |
| cartpole_swingup_sparse | single | jpeg | aco | 406000 | 26.000000 |
| cartpole_swingup_sparse | single | jpeg | aco | 406001 | 39.000000 |
| cartpole_swingup_sparse | single | jpeg | aco | 406002 | 16.000000 |
| cartpole_swingup_sparse | single | jpeg | aco | 406003 | 41.000000 |
| cartpole_swingup_sparse | single | jpeg | aco | 406004 | 67.000000 |
| cartpole_swingup_sparse | single | defocus_blur | aco | 406000 | 219.000000 |
| cartpole_swingup_sparse | single | defocus_blur | aco | 406001 | 403.000000 |
| cartpole_swingup_sparse | single | defocus_blur | aco | 406002 | 748.000000 |
| cartpole_swingup_sparse | single | defocus_blur | aco | 406003 | 193.000000 |
| cartpole_swingup_sparse | single | defocus_blur | aco | 406004 | 26.000000 |
| cartpole_swingup_sparse | single | frost | aco | 406000 | 97.000000 |
| cartpole_swingup_sparse | single | frost | aco | 406001 | 49.000000 |
| cartpole_swingup_sparse | single | frost | aco | 406002 | 44.000000 |
| cartpole_swingup_sparse | single | frost | aco | 406003 | 0.000000 |
| cartpole_swingup_sparse | single | frost | aco | 406004 | 23.000000 |
| cartpole_swingup_sparse | single | occlusion_patch | aco | 406000 | 805.000000 |
| cartpole_swingup_sparse | single | occlusion_patch | aco | 406001 | 16.000000 |
| cartpole_swingup_sparse | single | occlusion_patch | aco | 406002 | 116.000000 |
| cartpole_swingup_sparse | single | occlusion_patch | aco | 406003 | 570.000000 |
| cartpole_swingup_sparse | single | occlusion_patch | aco | 406004 | 176.000000 |
| cartpole_swingup_sparse | single | saturation | aco | 406000 | 69.000000 |
| cartpole_swingup_sparse | single | saturation | aco | 406001 | 14.000000 |
| cartpole_swingup_sparse | single | saturation | aco | 406002 | 5.000000 |
| cartpole_swingup_sparse | single | saturation | aco | 406003 | 123.000000 |
| cartpole_swingup_sparse | single | saturation | aco | 406004 | 82.000000 |
| cartpole_swingup_sparse | single | shadow | aco | 406000 | 450.000000 |
| cartpole_swingup_sparse | single | shadow | aco | 406001 | 452.000000 |
| cartpole_swingup_sparse | single | shadow | aco | 406002 | 364.000000 |
| cartpole_swingup_sparse | single | shadow | aco | 406003 | 372.000000 |
| cartpole_swingup_sparse | single | shadow | aco | 406004 | 646.000000 |
| cartpole_swingup_sparse | single | shot_noise | aco | 406000 | 0.000000 |
| cartpole_swingup_sparse | single | shot_noise | aco | 406001 | 0.000000 |
| cartpole_swingup_sparse | single | shot_noise | aco | 406002 | 0.000000 |
| cartpole_swingup_sparse | single | shot_noise | aco | 406003 | 0.000000 |
| cartpole_swingup_sparse | single | shot_noise | aco | 406004 | 0.000000 |
| cartpole_swingup_sparse | markov | - | smfa | 406000 | 334.000000 |
| cartpole_swingup_sparse | markov | - | smfa | 406001 | 566.000000 |
| cartpole_swingup_sparse | markov | - | smfa | 406002 | 342.000000 |
| cartpole_swingup_sparse | markov | - | smfa | 406003 | 149.000000 |
| cartpole_swingup_sparse | markov | - | smfa | 406004 | 427.000000 |
| cartpole_swingup_sparse | markov | - | smfa | 406005 | 217.000000 |
| cartpole_swingup_sparse | markov | - | smfa | 406006 | 321.000000 |
| cartpole_swingup_sparse | markov | - | smfa | 406007 | 432.000000 |
| cartpole_swingup_sparse | markov | - | smfa | 406008 | 193.000000 |
| cartpole_swingup_sparse | markov | - | smfa | 406009 | 695.000000 |
| cartpole_swingup_sparse | single | rain | smfa | 406000 | 831.000000 |
| cartpole_swingup_sparse | single | rain | smfa | 406001 | 822.000000 |
| cartpole_swingup_sparse | single | rain | smfa | 406002 | 833.000000 |
| cartpole_swingup_sparse | single | rain | smfa | 406003 | 836.000000 |
| cartpole_swingup_sparse | single | rain | smfa | 406004 | 828.000000 |
| cartpole_swingup_sparse | single | fog | smfa | 406000 | 829.000000 |
| cartpole_swingup_sparse | single | fog | smfa | 406001 | 829.000000 |
| cartpole_swingup_sparse | single | fog | smfa | 406002 | 807.000000 |
| cartpole_swingup_sparse | single | fog | smfa | 406003 | 836.000000 |
| cartpole_swingup_sparse | single | fog | smfa | 406004 | 833.000000 |
| cartpole_swingup_sparse | single | snow | smfa | 406000 | 832.000000 |
| cartpole_swingup_sparse | single | snow | smfa | 406001 | 835.000000 |
| cartpole_swingup_sparse | single | snow | smfa | 406002 | 821.000000 |
| cartpole_swingup_sparse | single | snow | smfa | 406003 | 811.000000 |
| cartpole_swingup_sparse | single | snow | smfa | 406004 | 826.000000 |
| cartpole_swingup_sparse | single | motion_blur | smfa | 406000 | 16.000000 |
| cartpole_swingup_sparse | single | motion_blur | smfa | 406001 | 0.000000 |
| cartpole_swingup_sparse | single | motion_blur | smfa | 406002 | 12.000000 |
| cartpole_swingup_sparse | single | motion_blur | smfa | 406003 | 0.000000 |
| cartpole_swingup_sparse | single | motion_blur | smfa | 406004 | 0.000000 |
| cartpole_swingup_sparse | single | gaussian_noise | smfa | 406000 | 829.000000 |
| cartpole_swingup_sparse | single | gaussian_noise | smfa | 406001 | 809.000000 |
| cartpole_swingup_sparse | single | gaussian_noise | smfa | 406002 | 802.000000 |
| cartpole_swingup_sparse | single | gaussian_noise | smfa | 406003 | 836.000000 |
| cartpole_swingup_sparse | single | gaussian_noise | smfa | 406004 | 810.000000 |
| cartpole_swingup_sparse | single | low_light | smfa | 406000 | 771.000000 |
| cartpole_swingup_sparse | single | low_light | smfa | 406001 | 804.000000 |
| cartpole_swingup_sparse | single | low_light | smfa | 406002 | 733.000000 |
| cartpole_swingup_sparse | single | low_light | smfa | 406003 | 835.000000 |
| cartpole_swingup_sparse | single | low_light | smfa | 406004 | 811.000000 |
| cartpole_swingup_sparse | single | jpeg | smfa | 406000 | 27.000000 |
| cartpole_swingup_sparse | single | jpeg | smfa | 406001 | 101.000000 |
| cartpole_swingup_sparse | single | jpeg | smfa | 406002 | 53.000000 |
| cartpole_swingup_sparse | single | jpeg | smfa | 406003 | 131.000000 |
| cartpole_swingup_sparse | single | jpeg | smfa | 406004 | 133.000000 |
| cartpole_swingup_sparse | single | defocus_blur | smfa | 406000 | 7.000000 |
| cartpole_swingup_sparse | single | defocus_blur | smfa | 406001 | 16.000000 |
| cartpole_swingup_sparse | single | defocus_blur | smfa | 406002 | 0.000000 |
| cartpole_swingup_sparse | single | defocus_blur | smfa | 406003 | 0.000000 |
| cartpole_swingup_sparse | single | defocus_blur | smfa | 406004 | 16.000000 |
| cartpole_swingup_sparse | single | frost | smfa | 406000 | 836.000000 |
| cartpole_swingup_sparse | single | frost | smfa | 406001 | 829.000000 |
| cartpole_swingup_sparse | single | frost | smfa | 406002 | 826.000000 |
| cartpole_swingup_sparse | single | frost | smfa | 406003 | 837.000000 |
| cartpole_swingup_sparse | single | frost | smfa | 406004 | 831.000000 |
| cartpole_swingup_sparse | single | occlusion_patch | smfa | 406000 | 833.000000 |
| cartpole_swingup_sparse | single | occlusion_patch | smfa | 406001 | 43.000000 |
| cartpole_swingup_sparse | single | occlusion_patch | smfa | 406002 | 626.000000 |
| cartpole_swingup_sparse | single | occlusion_patch | smfa | 406003 | 553.000000 |
| cartpole_swingup_sparse | single | occlusion_patch | smfa | 406004 | 837.000000 |
| cartpole_swingup_sparse | single | saturation | smfa | 406000 | 831.000000 |
| cartpole_swingup_sparse | single | saturation | smfa | 406001 | 836.000000 |
| cartpole_swingup_sparse | single | saturation | smfa | 406002 | 837.000000 |
| cartpole_swingup_sparse | single | saturation | smfa | 406003 | 831.000000 |
| cartpole_swingup_sparse | single | saturation | smfa | 406004 | 831.000000 |
| cartpole_swingup_sparse | single | shadow | smfa | 406000 | 283.000000 |
| cartpole_swingup_sparse | single | shadow | smfa | 406001 | 404.000000 |
| cartpole_swingup_sparse | single | shadow | smfa | 406002 | 448.000000 |
| cartpole_swingup_sparse | single | shadow | smfa | 406003 | 338.000000 |
| cartpole_swingup_sparse | single | shadow | smfa | 406004 | 801.000000 |
| cartpole_swingup_sparse | single | shot_noise | smfa | 406000 | 814.000000 |
| cartpole_swingup_sparse | single | shot_noise | smfa | 406001 | 818.000000 |
| cartpole_swingup_sparse | single | shot_noise | smfa | 406002 | 839.000000 |
| cartpole_swingup_sparse | single | shot_noise | smfa | 406003 | 812.000000 |
| cartpole_swingup_sparse | single | shot_noise | smfa | 406004 | 817.000000 |
| cup_catch | clean | - | clean | 407000 | 972.000000 |
| cup_catch | clean | - | clean | 407001 | 964.000000 |
| cup_catch | clean | - | clean | 407002 | 991.000000 |
| cup_catch | clean | - | clean | 407003 | 988.000000 |
| cup_catch | clean | - | clean | 407004 | 972.000000 |
| cup_catch | markov | - | raw | 407000 | 950.000000 |
| cup_catch | markov | - | raw | 407001 | 964.000000 |
| cup_catch | markov | - | raw | 407002 | 982.000000 |
| cup_catch | markov | - | raw | 407003 | 783.000000 |
| cup_catch | markov | - | raw | 407004 | 970.000000 |
| cup_catch | markov | - | raw | 407005 | 361.000000 |
| cup_catch | markov | - | raw | 407006 | 811.000000 |
| cup_catch | markov | - | raw | 407007 | 857.000000 |
| cup_catch | markov | - | raw | 407008 | 835.000000 |
| cup_catch | markov | - | raw | 407009 | 856.000000 |
| cup_catch | single | rain | raw | 407000 | 0.000000 |
| cup_catch | single | rain | raw | 407001 | 1.000000 |
| cup_catch | single | rain | raw | 407002 | 11.000000 |
| cup_catch | single | rain | raw | 407003 | 8.000000 |
| cup_catch | single | rain | raw | 407004 | 17.000000 |
| cup_catch | single | fog | raw | 407000 | 972.000000 |
| cup_catch | single | fog | raw | 407001 | 963.000000 |
| cup_catch | single | fog | raw | 407002 | 988.000000 |
| cup_catch | single | fog | raw | 407003 | 989.000000 |
| cup_catch | single | fog | raw | 407004 | 972.000000 |
| cup_catch | single | snow | raw | 407000 | 924.000000 |
| cup_catch | single | snow | raw | 407001 | 0.000000 |
| cup_catch | single | snow | raw | 407002 | 10.000000 |
| cup_catch | single | snow | raw | 407003 | 10.000000 |
| cup_catch | single | snow | raw | 407004 | 0.000000 |
| cup_catch | single | motion_blur | raw | 407000 | 970.000000 |
| cup_catch | single | motion_blur | raw | 407001 | 840.000000 |
| cup_catch | single | motion_blur | raw | 407002 | 990.000000 |
| cup_catch | single | motion_blur | raw | 407003 | 982.000000 |
| cup_catch | single | motion_blur | raw | 407004 | 963.000000 |
| cup_catch | single | gaussian_noise | raw | 407000 | 972.000000 |
| cup_catch | single | gaussian_noise | raw | 407001 | 961.000000 |
| cup_catch | single | gaussian_noise | raw | 407002 | 886.000000 |
| cup_catch | single | gaussian_noise | raw | 407003 | 989.000000 |
| cup_catch | single | gaussian_noise | raw | 407004 | 968.000000 |
| cup_catch | single | low_light | raw | 407000 | 0.000000 |
| cup_catch | single | low_light | raw | 407001 | 0.000000 |
| cup_catch | single | low_light | raw | 407002 | 10.000000 |
| cup_catch | single | low_light | raw | 407003 | 20.000000 |
| cup_catch | single | low_light | raw | 407004 | 0.000000 |
| cup_catch | single | jpeg | raw | 407000 | 971.000000 |
| cup_catch | single | jpeg | raw | 407001 | 963.000000 |
| cup_catch | single | jpeg | raw | 407002 | 990.000000 |
| cup_catch | single | jpeg | raw | 407003 | 987.000000 |
| cup_catch | single | jpeg | raw | 407004 | 944.000000 |
| cup_catch | single | defocus_blur | raw | 407000 | 0.000000 |
| cup_catch | single | defocus_blur | raw | 407001 | 0.000000 |
| cup_catch | single | defocus_blur | raw | 407002 | 982.000000 |
| cup_catch | single | defocus_blur | raw | 407003 | 964.000000 |
| cup_catch | single | defocus_blur | raw | 407004 | 911.000000 |
| cup_catch | single | frost | raw | 407000 | 972.000000 |
| cup_catch | single | frost | raw | 407001 | 964.000000 |
| cup_catch | single | frost | raw | 407002 | 989.000000 |
| cup_catch | single | frost | raw | 407003 | 988.000000 |
| cup_catch | single | frost | raw | 407004 | 972.000000 |
| cup_catch | single | occlusion_patch | raw | 407000 | 18.000000 |
| cup_catch | single | occlusion_patch | raw | 407001 | 0.000000 |
| cup_catch | single | occlusion_patch | raw | 407002 | 431.000000 |
| cup_catch | single | occlusion_patch | raw | 407003 | 610.000000 |
| cup_catch | single | occlusion_patch | raw | 407004 | 23.000000 |
| cup_catch | single | saturation | raw | 407000 | 971.000000 |
| cup_catch | single | saturation | raw | 407001 | 963.000000 |
| cup_catch | single | saturation | raw | 407002 | 988.000000 |
| cup_catch | single | saturation | raw | 407003 | 987.000000 |
| cup_catch | single | saturation | raw | 407004 | 929.000000 |
| cup_catch | single | shadow | raw | 407000 | 972.000000 |
| cup_catch | single | shadow | raw | 407001 | 962.000000 |
| cup_catch | single | shadow | raw | 407002 | 989.000000 |
| cup_catch | single | shadow | raw | 407003 | 989.000000 |
| cup_catch | single | shadow | raw | 407004 | 972.000000 |
| cup_catch | single | shot_noise | raw | 407000 | 853.000000 |
| cup_catch | single | shot_noise | raw | 407001 | 77.000000 |
| cup_catch | single | shot_noise | raw | 407002 | 719.000000 |
| cup_catch | single | shot_noise | raw | 407003 | 57.000000 |
| cup_catch | single | shot_noise | raw | 407004 | 33.000000 |
| cup_catch | markov | - | aco | 407000 | 960.000000 |
| cup_catch | markov | - | aco | 407001 | 872.000000 |
| cup_catch | markov | - | aco | 407002 | 991.000000 |
| cup_catch | markov | - | aco | 407003 | 312.000000 |
| cup_catch | markov | - | aco | 407004 | 873.000000 |
| cup_catch | markov | - | aco | 407005 | 933.000000 |
| cup_catch | markov | - | aco | 407006 | 740.000000 |
| cup_catch | markov | - | aco | 407007 | 812.000000 |
| cup_catch | markov | - | aco | 407008 | 920.000000 |
| cup_catch | markov | - | aco | 407009 | 971.000000 |
| cup_catch | single | rain | aco | 407000 | 971.000000 |
| cup_catch | single | rain | aco | 407001 | 961.000000 |
| cup_catch | single | rain | aco | 407002 | 991.000000 |
| cup_catch | single | rain | aco | 407003 | 988.000000 |
| cup_catch | single | rain | aco | 407004 | 972.000000 |
| cup_catch | single | fog | aco | 407000 | 969.000000 |
| cup_catch | single | fog | aco | 407001 | 0.000000 |
| cup_catch | single | fog | aco | 407002 | 990.000000 |
| cup_catch | single | fog | aco | 407003 | 982.000000 |
| cup_catch | single | fog | aco | 407004 | 972.000000 |
| cup_catch | single | snow | aco | 407000 | 972.000000 |
| cup_catch | single | snow | aco | 407001 | 955.000000 |
| cup_catch | single | snow | aco | 407002 | 991.000000 |
| cup_catch | single | snow | aco | 407003 | 988.000000 |
| cup_catch | single | snow | aco | 407004 | 953.000000 |
| cup_catch | single | motion_blur | aco | 407000 | 956.000000 |
| cup_catch | single | motion_blur | aco | 407001 | 963.000000 |
| cup_catch | single | motion_blur | aco | 407002 | 991.000000 |
| cup_catch | single | motion_blur | aco | 407003 | 982.000000 |
| cup_catch | single | motion_blur | aco | 407004 | 967.000000 |
| cup_catch | single | gaussian_noise | aco | 407000 | 0.000000 |
| cup_catch | single | gaussian_noise | aco | 407001 | 0.000000 |
| cup_catch | single | gaussian_noise | aco | 407002 | 10.000000 |
| cup_catch | single | gaussian_noise | aco | 407003 | 9.000000 |
| cup_catch | single | gaussian_noise | aco | 407004 | 0.000000 |
| cup_catch | single | low_light | aco | 407000 | 0.000000 |
| cup_catch | single | low_light | aco | 407001 | 31.000000 |
| cup_catch | single | low_light | aco | 407002 | 6.000000 |
| cup_catch | single | low_light | aco | 407003 | 19.000000 |
| cup_catch | single | low_light | aco | 407004 | 0.000000 |
| cup_catch | single | jpeg | aco | 407000 | 0.000000 |
| cup_catch | single | jpeg | aco | 407001 | 369.000000 |
| cup_catch | single | jpeg | aco | 407002 | 9.000000 |
| cup_catch | single | jpeg | aco | 407003 | 7.000000 |
| cup_catch | single | jpeg | aco | 407004 | 0.000000 |
| cup_catch | single | defocus_blur | aco | 407000 | 970.000000 |
| cup_catch | single | defocus_blur | aco | 407001 | 963.000000 |
| cup_catch | single | defocus_blur | aco | 407002 | 989.000000 |
| cup_catch | single | defocus_blur | aco | 407003 | 988.000000 |
| cup_catch | single | defocus_blur | aco | 407004 | 963.000000 |
| cup_catch | single | frost | aco | 407000 | 972.000000 |
| cup_catch | single | frost | aco | 407001 | 960.000000 |
| cup_catch | single | frost | aco | 407002 | 991.000000 |
| cup_catch | single | frost | aco | 407003 | 988.000000 |
| cup_catch | single | frost | aco | 407004 | 972.000000 |
| cup_catch | single | occlusion_patch | aco | 407000 | 968.000000 |
| cup_catch | single | occlusion_patch | aco | 407001 | 966.000000 |
| cup_catch | single | occlusion_patch | aco | 407002 | 842.000000 |
| cup_catch | single | occlusion_patch | aco | 407003 | 983.000000 |
| cup_catch | single | occlusion_patch | aco | 407004 | 963.000000 |
| cup_catch | single | saturation | aco | 407000 | 921.000000 |
| cup_catch | single | saturation | aco | 407001 | 914.000000 |
| cup_catch | single | saturation | aco | 407002 | 988.000000 |
| cup_catch | single | saturation | aco | 407003 | 982.000000 |
| cup_catch | single | saturation | aco | 407004 | 968.000000 |
| cup_catch | single | shadow | aco | 407000 | 971.000000 |
| cup_catch | single | shadow | aco | 407001 | 806.000000 |
| cup_catch | single | shadow | aco | 407002 | 943.000000 |
| cup_catch | single | shadow | aco | 407003 | 987.000000 |
| cup_catch | single | shadow | aco | 407004 | 971.000000 |
| cup_catch | single | shot_noise | aco | 407000 | 0.000000 |
| cup_catch | single | shot_noise | aco | 407001 | 0.000000 |
| cup_catch | single | shot_noise | aco | 407002 | 10.000000 |
| cup_catch | single | shot_noise | aco | 407003 | 2.000000 |
| cup_catch | single | shot_noise | aco | 407004 | 0.000000 |
| cup_catch | markov | - | smfa | 407000 | 971.000000 |
| cup_catch | markov | - | smfa | 407001 | 964.000000 |
| cup_catch | markov | - | smfa | 407002 | 981.000000 |
| cup_catch | markov | - | smfa | 407003 | 988.000000 |
| cup_catch | markov | - | smfa | 407004 | 973.000000 |
| cup_catch | markov | - | smfa | 407005 | 967.000000 |
| cup_catch | markov | - | smfa | 407006 | 890.000000 |
| cup_catch | markov | - | smfa | 407007 | 927.000000 |
| cup_catch | markov | - | smfa | 407008 | 973.000000 |
| cup_catch | markov | - | smfa | 407009 | 971.000000 |
| cup_catch | single | rain | smfa | 407000 | 971.000000 |
| cup_catch | single | rain | smfa | 407001 | 963.000000 |
| cup_catch | single | rain | smfa | 407002 | 991.000000 |
| cup_catch | single | rain | smfa | 407003 | 989.000000 |
| cup_catch | single | rain | smfa | 407004 | 972.000000 |
| cup_catch | single | fog | smfa | 407000 | 972.000000 |
| cup_catch | single | fog | smfa | 407001 | 964.000000 |
| cup_catch | single | fog | smfa | 407002 | 991.000000 |
| cup_catch | single | fog | smfa | 407003 | 989.000000 |
| cup_catch | single | fog | smfa | 407004 | 972.000000 |
| cup_catch | single | snow | smfa | 407000 | 972.000000 |
| cup_catch | single | snow | smfa | 407001 | 964.000000 |
| cup_catch | single | snow | smfa | 407002 | 990.000000 |
| cup_catch | single | snow | smfa | 407003 | 988.000000 |
| cup_catch | single | snow | smfa | 407004 | 973.000000 |
| cup_catch | single | motion_blur | smfa | 407000 | 0.000000 |
| cup_catch | single | motion_blur | smfa | 407001 | 0.000000 |
| cup_catch | single | motion_blur | smfa | 407002 | 987.000000 |
| cup_catch | single | motion_blur | smfa | 407003 | 983.000000 |
| cup_catch | single | motion_blur | smfa | 407004 | 947.000000 |
| cup_catch | single | gaussian_noise | smfa | 407000 | 972.000000 |
| cup_catch | single | gaussian_noise | smfa | 407001 | 964.000000 |
| cup_catch | single | gaussian_noise | smfa | 407002 | 991.000000 |
| cup_catch | single | gaussian_noise | smfa | 407003 | 989.000000 |
| cup_catch | single | gaussian_noise | smfa | 407004 | 972.000000 |
| cup_catch | single | low_light | smfa | 407000 | 972.000000 |
| cup_catch | single | low_light | smfa | 407001 | 964.000000 |
| cup_catch | single | low_light | smfa | 407002 | 990.000000 |
| cup_catch | single | low_light | smfa | 407003 | 987.000000 |
| cup_catch | single | low_light | smfa | 407004 | 972.000000 |
| cup_catch | single | jpeg | smfa | 407000 | 972.000000 |
| cup_catch | single | jpeg | smfa | 407001 | 962.000000 |
| cup_catch | single | jpeg | smfa | 407002 | 991.000000 |
| cup_catch | single | jpeg | smfa | 407003 | 981.000000 |
| cup_catch | single | jpeg | smfa | 407004 | 972.000000 |
| cup_catch | single | defocus_blur | smfa | 407000 | 0.000000 |
| cup_catch | single | defocus_blur | smfa | 407001 | 737.000000 |
| cup_catch | single | defocus_blur | smfa | 407002 | 984.000000 |
| cup_catch | single | defocus_blur | smfa | 407003 | 977.000000 |
| cup_catch | single | defocus_blur | smfa | 407004 | 0.000000 |
| cup_catch | single | frost | smfa | 407000 | 972.000000 |
| cup_catch | single | frost | smfa | 407001 | 964.000000 |
| cup_catch | single | frost | smfa | 407002 | 991.000000 |
| cup_catch | single | frost | smfa | 407003 | 988.000000 |
| cup_catch | single | frost | smfa | 407004 | 972.000000 |
| cup_catch | single | occlusion_patch | smfa | 407000 | 972.000000 |
| cup_catch | single | occlusion_patch | smfa | 407001 | 963.000000 |
| cup_catch | single | occlusion_patch | smfa | 407002 | 989.000000 |
| cup_catch | single | occlusion_patch | smfa | 407003 | 987.000000 |
| cup_catch | single | occlusion_patch | smfa | 407004 | 972.000000 |
| cup_catch | single | saturation | smfa | 407000 | 972.000000 |
| cup_catch | single | saturation | smfa | 407001 | 964.000000 |
| cup_catch | single | saturation | smfa | 407002 | 989.000000 |
| cup_catch | single | saturation | smfa | 407003 | 989.000000 |
| cup_catch | single | saturation | smfa | 407004 | 972.000000 |
| cup_catch | single | shadow | smfa | 407000 | 972.000000 |
| cup_catch | single | shadow | smfa | 407001 | 964.000000 |
| cup_catch | single | shadow | smfa | 407002 | 991.000000 |
| cup_catch | single | shadow | smfa | 407003 | 989.000000 |
| cup_catch | single | shadow | smfa | 407004 | 972.000000 |
| cup_catch | single | shot_noise | smfa | 407000 | 972.000000 |
| cup_catch | single | shot_noise | smfa | 407001 | 964.000000 |
| cup_catch | single | shot_noise | smfa | 407002 | 991.000000 |
| cup_catch | single | shot_noise | smfa | 407003 | 988.000000 |
| cup_catch | single | shot_noise | smfa | 407004 | 972.000000 |
| reacher_easy | clean | - | clean | 408000 | 964.000000 |
| reacher_easy | clean | - | clean | 408001 | 981.000000 |
| reacher_easy | clean | - | clean | 408002 | 976.000000 |
| reacher_easy | clean | - | clean | 408003 | 1000.000000 |
| reacher_easy | clean | - | clean | 408004 | 993.000000 |
| reacher_easy | markov | - | raw | 408000 | 946.000000 |
| reacher_easy | markov | - | raw | 408001 | 973.000000 |
| reacher_easy | markov | - | raw | 408002 | 973.000000 |
| reacher_easy | markov | - | raw | 408003 | 1000.000000 |
| reacher_easy | markov | - | raw | 408004 | 993.000000 |
| reacher_easy | markov | - | raw | 408005 | 945.000000 |
| reacher_easy | markov | - | raw | 408006 | 966.000000 |
| reacher_easy | markov | - | raw | 408007 | 981.000000 |
| reacher_easy | markov | - | raw | 408008 | 903.000000 |
| reacher_easy | markov | - | raw | 408009 | 963.000000 |
| reacher_easy | single | rain | raw | 408000 | 962.000000 |
| reacher_easy | single | rain | raw | 408001 | 980.000000 |
| reacher_easy | single | rain | raw | 408002 | 976.000000 |
| reacher_easy | single | rain | raw | 408003 | 1000.000000 |
| reacher_easy | single | rain | raw | 408004 | 993.000000 |
| reacher_easy | single | fog | raw | 408000 | 959.000000 |
| reacher_easy | single | fog | raw | 408001 | 981.000000 |
| reacher_easy | single | fog | raw | 408002 | 976.000000 |
| reacher_easy | single | fog | raw | 408003 | 1000.000000 |
| reacher_easy | single | fog | raw | 408004 | 993.000000 |
| reacher_easy | single | snow | raw | 408000 | 224.000000 |
| reacher_easy | single | snow | raw | 408001 | 9.000000 |
| reacher_easy | single | snow | raw | 408002 | 210.000000 |
| reacher_easy | single | snow | raw | 408003 | 39.000000 |
| reacher_easy | single | snow | raw | 408004 | 19.000000 |
| reacher_easy | single | motion_blur | raw | 408000 | 0.000000 |
| reacher_easy | single | motion_blur | raw | 408001 | 979.000000 |
| reacher_easy | single | motion_blur | raw | 408002 | 962.000000 |
| reacher_easy | single | motion_blur | raw | 408003 | 491.000000 |
| reacher_easy | single | motion_blur | raw | 408004 | 907.000000 |
| reacher_easy | single | gaussian_noise | raw | 408000 | 962.000000 |
| reacher_easy | single | gaussian_noise | raw | 408001 | 981.000000 |
| reacher_easy | single | gaussian_noise | raw | 408002 | 976.000000 |
| reacher_easy | single | gaussian_noise | raw | 408003 | 1000.000000 |
| reacher_easy | single | gaussian_noise | raw | 408004 | 993.000000 |
| reacher_easy | single | low_light | raw | 408000 | 177.000000 |
| reacher_easy | single | low_light | raw | 408001 | 0.000000 |
| reacher_easy | single | low_light | raw | 408002 | 159.000000 |
| reacher_easy | single | low_light | raw | 408003 | 199.000000 |
| reacher_easy | single | low_light | raw | 408004 | 171.000000 |
| reacher_easy | single | jpeg | raw | 408000 | 957.000000 |
| reacher_easy | single | jpeg | raw | 408001 | 980.000000 |
| reacher_easy | single | jpeg | raw | 408002 | 976.000000 |
| reacher_easy | single | jpeg | raw | 408003 | 1000.000000 |
| reacher_easy | single | jpeg | raw | 408004 | 993.000000 |
| reacher_easy | single | defocus_blur | raw | 408000 | 0.000000 |
| reacher_easy | single | defocus_blur | raw | 408001 | 978.000000 |
| reacher_easy | single | defocus_blur | raw | 408002 | 959.000000 |
| reacher_easy | single | defocus_blur | raw | 408003 | 442.000000 |
| reacher_easy | single | defocus_blur | raw | 408004 | 993.000000 |
| reacher_easy | single | frost | raw | 408000 | 959.000000 |
| reacher_easy | single | frost | raw | 408001 | 981.000000 |
| reacher_easy | single | frost | raw | 408002 | 976.000000 |
| reacher_easy | single | frost | raw | 408003 | 1000.000000 |
| reacher_easy | single | frost | raw | 408004 | 993.000000 |
| reacher_easy | single | occlusion_patch | raw | 408000 | 42.000000 |
| reacher_easy | single | occlusion_patch | raw | 408001 | 977.000000 |
| reacher_easy | single | occlusion_patch | raw | 408002 | 970.000000 |
| reacher_easy | single | occlusion_patch | raw | 408003 | 148.000000 |
| reacher_easy | single | occlusion_patch | raw | 408004 | 17.000000 |
| reacher_easy | single | saturation | raw | 408000 | 961.000000 |
| reacher_easy | single | saturation | raw | 408001 | 980.000000 |
| reacher_easy | single | saturation | raw | 408002 | 976.000000 |
| reacher_easy | single | saturation | raw | 408003 | 1000.000000 |
| reacher_easy | single | saturation | raw | 408004 | 993.000000 |
| reacher_easy | single | shadow | raw | 408000 | 959.000000 |
| reacher_easy | single | shadow | raw | 408001 | 965.000000 |
| reacher_easy | single | shadow | raw | 408002 | 976.000000 |
| reacher_easy | single | shadow | raw | 408003 | 1000.000000 |
| reacher_easy | single | shadow | raw | 408004 | 993.000000 |
| reacher_easy | single | shot_noise | raw | 408000 | 962.000000 |
| reacher_easy | single | shot_noise | raw | 408001 | 980.000000 |
| reacher_easy | single | shot_noise | raw | 408002 | 973.000000 |
| reacher_easy | single | shot_noise | raw | 408003 | 1000.000000 |
| reacher_easy | single | shot_noise | raw | 408004 | 993.000000 |
| reacher_easy | markov | - | aco | 408000 | 406.000000 |
| reacher_easy | markov | - | aco | 408001 | 350.000000 |
| reacher_easy | markov | - | aco | 408002 | 827.000000 |
| reacher_easy | markov | - | aco | 408003 | 985.000000 |
| reacher_easy | markov | - | aco | 408004 | 32.000000 |
| reacher_easy | markov | - | aco | 408005 | 551.000000 |
| reacher_easy | markov | - | aco | 408006 | 942.000000 |
| reacher_easy | markov | - | aco | 408007 | 919.000000 |
| reacher_easy | markov | - | aco | 408008 | 294.000000 |
| reacher_easy | markov | - | aco | 408009 | 961.000000 |
| reacher_easy | single | rain | aco | 408000 | 309.000000 |
| reacher_easy | single | rain | aco | 408001 | 25.000000 |
| reacher_easy | single | rain | aco | 408002 | 0.000000 |
| reacher_easy | single | rain | aco | 408003 | 95.000000 |
| reacher_easy | single | rain | aco | 408004 | 163.000000 |
| reacher_easy | single | fog | aco | 408000 | 10.000000 |
| reacher_easy | single | fog | aco | 408001 | 7.000000 |
| reacher_easy | single | fog | aco | 408002 | 974.000000 |
| reacher_easy | single | fog | aco | 408003 | 976.000000 |
| reacher_easy | single | fog | aco | 408004 | 992.000000 |
| reacher_easy | single | snow | aco | 408000 | 284.000000 |
| reacher_easy | single | snow | aco | 408001 | 44.000000 |
| reacher_easy | single | snow | aco | 408002 | 7.000000 |
| reacher_easy | single | snow | aco | 408003 | 85.000000 |
| reacher_easy | single | snow | aco | 408004 | 190.000000 |
| reacher_easy | single | motion_blur | aco | 408000 | 945.000000 |
| reacher_easy | single | motion_blur | aco | 408001 | 980.000000 |
| reacher_easy | single | motion_blur | aco | 408002 | 971.000000 |
| reacher_easy | single | motion_blur | aco | 408003 | 1000.000000 |
| reacher_easy | single | motion_blur | aco | 408004 | 987.000000 |
| reacher_easy | single | gaussian_noise | aco | 408000 | 559.000000 |
| reacher_easy | single | gaussian_noise | aco | 408001 | 116.000000 |
| reacher_easy | single | gaussian_noise | aco | 408002 | 972.000000 |
| reacher_easy | single | gaussian_noise | aco | 408003 | 1000.000000 |
| reacher_easy | single | gaussian_noise | aco | 408004 | 41.000000 |
| reacher_easy | single | low_light | aco | 408000 | 0.000000 |
| reacher_easy | single | low_light | aco | 408001 | 121.000000 |
| reacher_easy | single | low_light | aco | 408002 | 160.000000 |
| reacher_easy | single | low_light | aco | 408003 | 302.000000 |
| reacher_easy | single | low_light | aco | 408004 | 41.000000 |
| reacher_easy | single | jpeg | aco | 408000 | 45.000000 |
| reacher_easy | single | jpeg | aco | 408001 | 49.000000 |
| reacher_easy | single | jpeg | aco | 408002 | 969.000000 |
| reacher_easy | single | jpeg | aco | 408003 | 537.000000 |
| reacher_easy | single | jpeg | aco | 408004 | 128.000000 |
| reacher_easy | single | defocus_blur | aco | 408000 | 944.000000 |
| reacher_easy | single | defocus_blur | aco | 408001 | 981.000000 |
| reacher_easy | single | defocus_blur | aco | 408002 | 976.000000 |
| reacher_easy | single | defocus_blur | aco | 408003 | 1000.000000 |
| reacher_easy | single | defocus_blur | aco | 408004 | 992.000000 |
| reacher_easy | single | frost | aco | 408000 | 306.000000 |
| reacher_easy | single | frost | aco | 408001 | 16.000000 |
| reacher_easy | single | frost | aco | 408002 | 0.000000 |
| reacher_easy | single | frost | aco | 408003 | 55.000000 |
| reacher_easy | single | frost | aco | 408004 | 158.000000 |
| reacher_easy | single | occlusion_patch | aco | 408000 | 0.000000 |
| reacher_easy | single | occlusion_patch | aco | 408001 | 189.000000 |
| reacher_easy | single | occlusion_patch | aco | 408002 | 976.000000 |
| reacher_easy | single | occlusion_patch | aco | 408003 | 201.000000 |
| reacher_easy | single | occlusion_patch | aco | 408004 | 19.000000 |
| reacher_easy | single | saturation | aco | 408000 | 0.000000 |
| reacher_easy | single | saturation | aco | 408001 | 946.000000 |
| reacher_easy | single | saturation | aco | 408002 | 970.000000 |
| reacher_easy | single | saturation | aco | 408003 | 998.000000 |
| reacher_easy | single | saturation | aco | 408004 | 48.000000 |
| reacher_easy | single | shadow | aco | 408000 | 958.000000 |
| reacher_easy | single | shadow | aco | 408001 | 977.000000 |
| reacher_easy | single | shadow | aco | 408002 | 976.000000 |
| reacher_easy | single | shadow | aco | 408003 | 1000.000000 |
| reacher_easy | single | shadow | aco | 408004 | 991.000000 |
| reacher_easy | single | shot_noise | aco | 408000 | 130.000000 |
| reacher_easy | single | shot_noise | aco | 408001 | 8.000000 |
| reacher_easy | single | shot_noise | aco | 408002 | 972.000000 |
| reacher_easy | single | shot_noise | aco | 408003 | 249.000000 |
| reacher_easy | single | shot_noise | aco | 408004 | 62.000000 |
| reacher_easy | markov | - | smfa | 408000 | 958.000000 |
| reacher_easy | markov | - | smfa | 408001 | 980.000000 |
| reacher_easy | markov | - | smfa | 408002 | 976.000000 |
| reacher_easy | markov | - | smfa | 408003 | 1000.000000 |
| reacher_easy | markov | - | smfa | 408004 | 993.000000 |
| reacher_easy | markov | - | smfa | 408005 | 942.000000 |
| reacher_easy | markov | - | smfa | 408006 | 966.000000 |
| reacher_easy | markov | - | smfa | 408007 | 970.000000 |
| reacher_easy | markov | - | smfa | 408008 | 965.000000 |
| reacher_easy | markov | - | smfa | 408009 | 964.000000 |
| reacher_easy | single | rain | smfa | 408000 | 962.000000 |
| reacher_easy | single | rain | smfa | 408001 | 980.000000 |
| reacher_easy | single | rain | smfa | 408002 | 976.000000 |
| reacher_easy | single | rain | smfa | 408003 | 1000.000000 |
| reacher_easy | single | rain | smfa | 408004 | 993.000000 |
| reacher_easy | single | fog | smfa | 408000 | 962.000000 |
| reacher_easy | single | fog | smfa | 408001 | 981.000000 |
| reacher_easy | single | fog | smfa | 408002 | 976.000000 |
| reacher_easy | single | fog | smfa | 408003 | 1000.000000 |
| reacher_easy | single | fog | smfa | 408004 | 993.000000 |
| reacher_easy | single | snow | smfa | 408000 | 964.000000 |
| reacher_easy | single | snow | smfa | 408001 | 981.000000 |
| reacher_easy | single | snow | smfa | 408002 | 976.000000 |
| reacher_easy | single | snow | smfa | 408003 | 1000.000000 |
| reacher_easy | single | snow | smfa | 408004 | 993.000000 |
| reacher_easy | single | motion_blur | smfa | 408000 | 0.000000 |
| reacher_easy | single | motion_blur | smfa | 408001 | 980.000000 |
| reacher_easy | single | motion_blur | smfa | 408002 | 964.000000 |
| reacher_easy | single | motion_blur | smfa | 408003 | 730.000000 |
| reacher_easy | single | motion_blur | smfa | 408004 | 976.000000 |
| reacher_easy | single | gaussian_noise | smfa | 408000 | 961.000000 |
| reacher_easy | single | gaussian_noise | smfa | 408001 | 981.000000 |
| reacher_easy | single | gaussian_noise | smfa | 408002 | 976.000000 |
| reacher_easy | single | gaussian_noise | smfa | 408003 | 1000.000000 |
| reacher_easy | single | gaussian_noise | smfa | 408004 | 993.000000 |
| reacher_easy | single | low_light | smfa | 408000 | 957.000000 |
| reacher_easy | single | low_light | smfa | 408001 | 980.000000 |
| reacher_easy | single | low_light | smfa | 408002 | 976.000000 |
| reacher_easy | single | low_light | smfa | 408003 | 1000.000000 |
| reacher_easy | single | low_light | smfa | 408004 | 993.000000 |
| reacher_easy | single | jpeg | smfa | 408000 | 958.000000 |
| reacher_easy | single | jpeg | smfa | 408001 | 980.000000 |
| reacher_easy | single | jpeg | smfa | 408002 | 975.000000 |
| reacher_easy | single | jpeg | smfa | 408003 | 1000.000000 |
| reacher_easy | single | jpeg | smfa | 408004 | 993.000000 |
| reacher_easy | single | defocus_blur | smfa | 408000 | 0.000000 |
| reacher_easy | single | defocus_blur | smfa | 408001 | 980.000000 |
| reacher_easy | single | defocus_blur | smfa | 408002 | 968.000000 |
| reacher_easy | single | defocus_blur | smfa | 408003 | 996.000000 |
| reacher_easy | single | defocus_blur | smfa | 408004 | 993.000000 |
| reacher_easy | single | frost | smfa | 408000 | 961.000000 |
| reacher_easy | single | frost | smfa | 408001 | 981.000000 |
| reacher_easy | single | frost | smfa | 408002 | 976.000000 |
| reacher_easy | single | frost | smfa | 408003 | 1000.000000 |
| reacher_easy | single | frost | smfa | 408004 | 993.000000 |
| reacher_easy | single | occlusion_patch | smfa | 408000 | 0.000000 |
| reacher_easy | single | occlusion_patch | smfa | 408001 | 141.000000 |
| reacher_easy | single | occlusion_patch | smfa | 408002 | 976.000000 |
| reacher_easy | single | occlusion_patch | smfa | 408003 | 102.000000 |
| reacher_easy | single | occlusion_patch | smfa | 408004 | 14.000000 |
| reacher_easy | single | saturation | smfa | 408000 | 959.000000 |
| reacher_easy | single | saturation | smfa | 408001 | 981.000000 |
| reacher_easy | single | saturation | smfa | 408002 | 975.000000 |
| reacher_easy | single | saturation | smfa | 408003 | 1000.000000 |
| reacher_easy | single | saturation | smfa | 408004 | 993.000000 |
| reacher_easy | single | shadow | smfa | 408000 | 958.000000 |
| reacher_easy | single | shadow | smfa | 408001 | 981.000000 |
| reacher_easy | single | shadow | smfa | 408002 | 976.000000 |
| reacher_easy | single | shadow | smfa | 408003 | 1000.000000 |
| reacher_easy | single | shadow | smfa | 408004 | 993.000000 |
| reacher_easy | single | shot_noise | smfa | 408000 | 958.000000 |
| reacher_easy | single | shot_noise | smfa | 408001 | 981.000000 |
| reacher_easy | single | shot_noise | smfa | 408002 | 976.000000 |
| reacher_easy | single | shot_noise | smfa | 408003 | 1000.000000 |
| reacher_easy | single | shot_noise | smfa | 408004 | 993.000000 |
| reacher_hard | clean | - | clean | 409000 | 37.000000 |
| reacher_hard | clean | - | clean | 409001 | 0.000000 |
| reacher_hard | clean | - | clean | 409002 | 0.000000 |
| reacher_hard | clean | - | clean | 409003 | 0.000000 |
| reacher_hard | clean | - | clean | 409004 | 0.000000 |
| reacher_hard | markov | - | raw | 409000 | 20.000000 |
| reacher_hard | markov | - | raw | 409001 | 0.000000 |
| reacher_hard | markov | - | raw | 409002 | 3.000000 |
| reacher_hard | markov | - | raw | 409003 | 0.000000 |
| reacher_hard | markov | - | raw | 409004 | 5.000000 |
| reacher_hard | markov | - | raw | 409005 | 6.000000 |
| reacher_hard | markov | - | raw | 409006 | 13.000000 |
| reacher_hard | markov | - | raw | 409007 | 6.000000 |
| reacher_hard | markov | - | raw | 409008 | 4.000000 |
| reacher_hard | markov | - | raw | 409009 | 715.000000 |
| reacher_hard | single | rain | raw | 409000 | 34.000000 |
| reacher_hard | single | rain | raw | 409001 | 0.000000 |
| reacher_hard | single | rain | raw | 409002 | 0.000000 |
| reacher_hard | single | rain | raw | 409003 | 0.000000 |
| reacher_hard | single | rain | raw | 409004 | 0.000000 |
| reacher_hard | single | fog | raw | 409000 | 37.000000 |
| reacher_hard | single | fog | raw | 409001 | 0.000000 |
| reacher_hard | single | fog | raw | 409002 | 0.000000 |
| reacher_hard | single | fog | raw | 409003 | 0.000000 |
| reacher_hard | single | fog | raw | 409004 | 0.000000 |
| reacher_hard | single | snow | raw | 409000 | 0.000000 |
| reacher_hard | single | snow | raw | 409001 | 0.000000 |
| reacher_hard | single | snow | raw | 409002 | 0.000000 |
| reacher_hard | single | snow | raw | 409003 | 3.000000 |
| reacher_hard | single | snow | raw | 409004 | 0.000000 |
| reacher_hard | single | motion_blur | raw | 409000 | 19.000000 |
| reacher_hard | single | motion_blur | raw | 409001 | 0.000000 |
| reacher_hard | single | motion_blur | raw | 409002 | 5.000000 |
| reacher_hard | single | motion_blur | raw | 409003 | 8.000000 |
| reacher_hard | single | motion_blur | raw | 409004 | 0.000000 |
| reacher_hard | single | gaussian_noise | raw | 409000 | 44.000000 |
| reacher_hard | single | gaussian_noise | raw | 409001 | 0.000000 |
| reacher_hard | single | gaussian_noise | raw | 409002 | 0.000000 |
| reacher_hard | single | gaussian_noise | raw | 409003 | 0.000000 |
| reacher_hard | single | gaussian_noise | raw | 409004 | 4.000000 |
| reacher_hard | single | low_light | raw | 409000 | 29.000000 |
| reacher_hard | single | low_light | raw | 409001 | 0.000000 |
| reacher_hard | single | low_light | raw | 409002 | 0.000000 |
| reacher_hard | single | low_light | raw | 409003 | 2.000000 |
| reacher_hard | single | low_light | raw | 409004 | 0.000000 |
| reacher_hard | single | jpeg | raw | 409000 | 8.000000 |
| reacher_hard | single | jpeg | raw | 409001 | 0.000000 |
| reacher_hard | single | jpeg | raw | 409002 | 4.000000 |
| reacher_hard | single | jpeg | raw | 409003 | 0.000000 |
| reacher_hard | single | jpeg | raw | 409004 | 0.000000 |
| reacher_hard | single | defocus_blur | raw | 409000 | 14.000000 |
| reacher_hard | single | defocus_blur | raw | 409001 | 462.000000 |
| reacher_hard | single | defocus_blur | raw | 409002 | 20.000000 |
| reacher_hard | single | defocus_blur | raw | 409003 | 26.000000 |
| reacher_hard | single | defocus_blur | raw | 409004 | 0.000000 |
| reacher_hard | single | frost | raw | 409000 | 30.000000 |
| reacher_hard | single | frost | raw | 409001 | 0.000000 |
| reacher_hard | single | frost | raw | 409002 | 2.000000 |
| reacher_hard | single | frost | raw | 409003 | 0.000000 |
| reacher_hard | single | frost | raw | 409004 | 4.000000 |
| reacher_hard | single | occlusion_patch | raw | 409000 | 4.000000 |
| reacher_hard | single | occlusion_patch | raw | 409001 | 29.000000 |
| reacher_hard | single | occlusion_patch | raw | 409002 | 4.000000 |
| reacher_hard | single | occlusion_patch | raw | 409003 | 0.000000 |
| reacher_hard | single | occlusion_patch | raw | 409004 | 0.000000 |
| reacher_hard | single | saturation | raw | 409000 | 44.000000 |
| reacher_hard | single | saturation | raw | 409001 | 0.000000 |
| reacher_hard | single | saturation | raw | 409002 | 0.000000 |
| reacher_hard | single | saturation | raw | 409003 | 2.000000 |
| reacher_hard | single | saturation | raw | 409004 | 0.000000 |
| reacher_hard | single | shadow | raw | 409000 | 41.000000 |
| reacher_hard | single | shadow | raw | 409001 | 0.000000 |
| reacher_hard | single | shadow | raw | 409002 | 0.000000 |
| reacher_hard | single | shadow | raw | 409003 | 0.000000 |
| reacher_hard | single | shadow | raw | 409004 | 0.000000 |
| reacher_hard | single | shot_noise | raw | 409000 | 33.000000 |
| reacher_hard | single | shot_noise | raw | 409001 | 0.000000 |
| reacher_hard | single | shot_noise | raw | 409002 | 2.000000 |
| reacher_hard | single | shot_noise | raw | 409003 | 0.000000 |
| reacher_hard | single | shot_noise | raw | 409004 | 0.000000 |
| reacher_hard | markov | - | aco | 409000 | 3.000000 |
| reacher_hard | markov | - | aco | 409001 | 0.000000 |
| reacher_hard | markov | - | aco | 409002 | 0.000000 |
| reacher_hard | markov | - | aco | 409003 | 13.000000 |
| reacher_hard | markov | - | aco | 409004 | 3.000000 |
| reacher_hard | markov | - | aco | 409005 | 10.000000 |
| reacher_hard | markov | - | aco | 409006 | 0.000000 |
| reacher_hard | markov | - | aco | 409007 | 3.000000 |
| reacher_hard | markov | - | aco | 409008 | 3.000000 |
| reacher_hard | markov | - | aco | 409009 | 187.000000 |
| reacher_hard | single | rain | aco | 409000 | 0.000000 |
| reacher_hard | single | rain | aco | 409001 | 170.000000 |
| reacher_hard | single | rain | aco | 409002 | 18.000000 |
| reacher_hard | single | rain | aco | 409003 | 0.000000 |
| reacher_hard | single | rain | aco | 409004 | 0.000000 |
| reacher_hard | single | fog | aco | 409000 | 9.000000 |
| reacher_hard | single | fog | aco | 409001 | 21.000000 |
| reacher_hard | single | fog | aco | 409002 | 7.000000 |
| reacher_hard | single | fog | aco | 409003 | 45.000000 |
| reacher_hard | single | fog | aco | 409004 | 4.000000 |
| reacher_hard | single | snow | aco | 409000 | 0.000000 |
| reacher_hard | single | snow | aco | 409001 | 70.000000 |
| reacher_hard | single | snow | aco | 409002 | 56.000000 |
| reacher_hard | single | snow | aco | 409003 | 0.000000 |
| reacher_hard | single | snow | aco | 409004 | 0.000000 |
| reacher_hard | single | motion_blur | aco | 409000 | 0.000000 |
| reacher_hard | single | motion_blur | aco | 409001 | 0.000000 |
| reacher_hard | single | motion_blur | aco | 409002 | 4.000000 |
| reacher_hard | single | motion_blur | aco | 409003 | 0.000000 |
| reacher_hard | single | motion_blur | aco | 409004 | 3.000000 |
| reacher_hard | single | gaussian_noise | aco | 409000 | 12.000000 |
| reacher_hard | single | gaussian_noise | aco | 409001 | 0.000000 |
| reacher_hard | single | gaussian_noise | aco | 409002 | 33.000000 |
| reacher_hard | single | gaussian_noise | aco | 409003 | 2.000000 |
| reacher_hard | single | gaussian_noise | aco | 409004 | 0.000000 |
| reacher_hard | single | low_light | aco | 409000 | 4.000000 |
| reacher_hard | single | low_light | aco | 409001 | 34.000000 |
| reacher_hard | single | low_light | aco | 409002 | 2.000000 |
| reacher_hard | single | low_light | aco | 409003 | 22.000000 |
| reacher_hard | single | low_light | aco | 409004 | 13.000000 |
| reacher_hard | single | jpeg | aco | 409000 | 0.000000 |
| reacher_hard | single | jpeg | aco | 409001 | 0.000000 |
| reacher_hard | single | jpeg | aco | 409002 | 4.000000 |
| reacher_hard | single | jpeg | aco | 409003 | 0.000000 |
| reacher_hard | single | jpeg | aco | 409004 | 0.000000 |
| reacher_hard | single | defocus_blur | aco | 409000 | 0.000000 |
| reacher_hard | single | defocus_blur | aco | 409001 | 0.000000 |
| reacher_hard | single | defocus_blur | aco | 409002 | 3.000000 |
| reacher_hard | single | defocus_blur | aco | 409003 | 0.000000 |
| reacher_hard | single | defocus_blur | aco | 409004 | 0.000000 |
| reacher_hard | single | frost | aco | 409000 | 0.000000 |
| reacher_hard | single | frost | aco | 409001 | 34.000000 |
| reacher_hard | single | frost | aco | 409002 | 25.000000 |
| reacher_hard | single | frost | aco | 409003 | 0.000000 |
| reacher_hard | single | frost | aco | 409004 | 0.000000 |
| reacher_hard | single | occlusion_patch | aco | 409000 | 24.000000 |
| reacher_hard | single | occlusion_patch | aco | 409001 | 0.000000 |
| reacher_hard | single | occlusion_patch | aco | 409002 | 3.000000 |
| reacher_hard | single | occlusion_patch | aco | 409003 | 25.000000 |
| reacher_hard | single | occlusion_patch | aco | 409004 | 3.000000 |
| reacher_hard | single | saturation | aco | 409000 | 11.000000 |
| reacher_hard | single | saturation | aco | 409001 | 4.000000 |
| reacher_hard | single | saturation | aco | 409002 | 24.000000 |
| reacher_hard | single | saturation | aco | 409003 | 20.000000 |
| reacher_hard | single | saturation | aco | 409004 | 16.000000 |
| reacher_hard | single | shadow | aco | 409000 | 39.000000 |
| reacher_hard | single | shadow | aco | 409001 | 0.000000 |
| reacher_hard | single | shadow | aco | 409002 | 0.000000 |
| reacher_hard | single | shadow | aco | 409003 | 0.000000 |
| reacher_hard | single | shadow | aco | 409004 | 0.000000 |
| reacher_hard | single | shot_noise | aco | 409000 | 16.000000 |
| reacher_hard | single | shot_noise | aco | 409001 | 0.000000 |
| reacher_hard | single | shot_noise | aco | 409002 | 25.000000 |
| reacher_hard | single | shot_noise | aco | 409003 | 3.000000 |
| reacher_hard | single | shot_noise | aco | 409004 | 0.000000 |
| reacher_hard | markov | - | smfa | 409000 | 23.000000 |
| reacher_hard | markov | - | smfa | 409001 | 0.000000 |
| reacher_hard | markov | - | smfa | 409002 | 5.000000 |
| reacher_hard | markov | - | smfa | 409003 | 0.000000 |
| reacher_hard | markov | - | smfa | 409004 | 0.000000 |
| reacher_hard | markov | - | smfa | 409005 | 6.000000 |
| reacher_hard | markov | - | smfa | 409006 | 17.000000 |
| reacher_hard | markov | - | smfa | 409007 | 2.000000 |
| reacher_hard | markov | - | smfa | 409008 | 11.000000 |
| reacher_hard | markov | - | smfa | 409009 | 0.000000 |
| reacher_hard | single | rain | smfa | 409000 | 41.000000 |
| reacher_hard | single | rain | smfa | 409001 | 0.000000 |
| reacher_hard | single | rain | smfa | 409002 | 0.000000 |
| reacher_hard | single | rain | smfa | 409003 | 0.000000 |
| reacher_hard | single | rain | smfa | 409004 | 3.000000 |
| reacher_hard | single | fog | smfa | 409000 | 37.000000 |
| reacher_hard | single | fog | smfa | 409001 | 0.000000 |
| reacher_hard | single | fog | smfa | 409002 | 2.000000 |
| reacher_hard | single | fog | smfa | 409003 | 0.000000 |
| reacher_hard | single | fog | smfa | 409004 | 0.000000 |
| reacher_hard | single | snow | smfa | 409000 | 47.000000 |
| reacher_hard | single | snow | smfa | 409001 | 0.000000 |
| reacher_hard | single | snow | smfa | 409002 | 2.000000 |
| reacher_hard | single | snow | smfa | 409003 | 0.000000 |
| reacher_hard | single | snow | smfa | 409004 | 4.000000 |
| reacher_hard | single | motion_blur | smfa | 409000 | 9.000000 |
| reacher_hard | single | motion_blur | smfa | 409001 | 0.000000 |
| reacher_hard | single | motion_blur | smfa | 409002 | 0.000000 |
| reacher_hard | single | motion_blur | smfa | 409003 | 2.000000 |
| reacher_hard | single | motion_blur | smfa | 409004 | 0.000000 |
| reacher_hard | single | gaussian_noise | smfa | 409000 | 45.000000 |
| reacher_hard | single | gaussian_noise | smfa | 409001 | 0.000000 |
| reacher_hard | single | gaussian_noise | smfa | 409002 | 0.000000 |
| reacher_hard | single | gaussian_noise | smfa | 409003 | 0.000000 |
| reacher_hard | single | gaussian_noise | smfa | 409004 | 4.000000 |
| reacher_hard | single | low_light | smfa | 409000 | 40.000000 |
| reacher_hard | single | low_light | smfa | 409001 | 0.000000 |
| reacher_hard | single | low_light | smfa | 409002 | 2.000000 |
| reacher_hard | single | low_light | smfa | 409003 | 0.000000 |
| reacher_hard | single | low_light | smfa | 409004 | 10.000000 |
| reacher_hard | single | jpeg | smfa | 409000 | 24.000000 |
| reacher_hard | single | jpeg | smfa | 409001 | 0.000000 |
| reacher_hard | single | jpeg | smfa | 409002 | 0.000000 |
| reacher_hard | single | jpeg | smfa | 409003 | 0.000000 |
| reacher_hard | single | jpeg | smfa | 409004 | 2.000000 |
| reacher_hard | single | defocus_blur | smfa | 409000 | 0.000000 |
| reacher_hard | single | defocus_blur | smfa | 409001 | 15.000000 |
| reacher_hard | single | defocus_blur | smfa | 409002 | 8.000000 |
| reacher_hard | single | defocus_blur | smfa | 409003 | 11.000000 |
| reacher_hard | single | defocus_blur | smfa | 409004 | 5.000000 |
| reacher_hard | single | frost | smfa | 409000 | 34.000000 |
| reacher_hard | single | frost | smfa | 409001 | 0.000000 |
| reacher_hard | single | frost | smfa | 409002 | 4.000000 |
| reacher_hard | single | frost | smfa | 409003 | 0.000000 |
| reacher_hard | single | frost | smfa | 409004 | 4.000000 |
| reacher_hard | single | occlusion_patch | smfa | 409000 | 20.000000 |
| reacher_hard | single | occlusion_patch | smfa | 409001 | 0.000000 |
| reacher_hard | single | occlusion_patch | smfa | 409002 | 0.000000 |
| reacher_hard | single | occlusion_patch | smfa | 409003 | 15.000000 |
| reacher_hard | single | occlusion_patch | smfa | 409004 | 0.000000 |
| reacher_hard | single | saturation | smfa | 409000 | 47.000000 |
| reacher_hard | single | saturation | smfa | 409001 | 0.000000 |
| reacher_hard | single | saturation | smfa | 409002 | 0.000000 |
| reacher_hard | single | saturation | smfa | 409003 | 0.000000 |
| reacher_hard | single | saturation | smfa | 409004 | 4.000000 |
| reacher_hard | single | shadow | smfa | 409000 | 50.000000 |
| reacher_hard | single | shadow | smfa | 409001 | 0.000000 |
| reacher_hard | single | shadow | smfa | 409002 | 0.000000 |
| reacher_hard | single | shadow | smfa | 409003 | 0.000000 |
| reacher_hard | single | shadow | smfa | 409004 | 0.000000 |
| reacher_hard | single | shot_noise | smfa | 409000 | 52.000000 |
| reacher_hard | single | shot_noise | smfa | 409001 | 0.000000 |
| reacher_hard | single | shot_noise | smfa | 409002 | 2.000000 |
| reacher_hard | single | shot_noise | smfa | 409003 | 0.000000 |
| reacher_hard | single | shot_noise | smfa | 409004 | 0.000000 |
