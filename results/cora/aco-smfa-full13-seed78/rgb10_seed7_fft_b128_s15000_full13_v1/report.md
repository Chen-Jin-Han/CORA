# Full13 seed6 results

All 13 types are training-seen. Former OOD6 use fallback_v1; this is not a zero-shot OOD experiment.

One training seed per model. +/- denotes episode SD, not training-seed uncertainty. Pooled cross-task SD also contains task differences.

## Overall control

| Protocol | Raw | ACO | SMFA |
|---|---:|---:|---:|
| markov | 483.41 +/- 353.71 (n=100) | 455.32 +/- 338.30 (n=100) | 646.41 +/- 339.97 (n=100) |
| single/all | 460.57 +/- 396.01 (n=650) | 462.43 +/- 401.21 (n=650) | 655.96 +/- 375.02 (n=650) |

Clean: 734.21 +/- 334.50 (n=50)

## Image restoration

| Model / group | n | PSNR-Y | SSIM-Y | PSNR-RGB | SSIM-RGB |
|---|---:|---:|---:|---:|---:|
| aco/all | 130000 | 26.4610 | 0.796784 | 22.2298 | 0.713717 |
| aco/task/walker_walk | 13000 | 25.4175 | 0.797786 | 21.6844 | 0.716142 |
| aco/degradation/rain | 10000 | 26.2746 | 0.917020 | 22.8589 | 0.833609 |
| aco/walker_walk/rain | 1000 | 24.8140 | 0.912308 | 21.8422 | 0.810869 |
| aco/degradation/fog | 10000 | 30.9914 | 0.984732 | 26.7566 | 0.943811 |
| aco/walker_walk/fog | 1000 | 30.7596 | 0.984701 | 26.5240 | 0.940726 |
| aco/degradation/snow | 10000 | 27.6725 | 0.869870 | 24.1244 | 0.802729 |
| aco/walker_walk/snow | 1000 | 26.5703 | 0.884157 | 23.4949 | 0.811463 |
| aco/degradation/motion_blur | 10000 | 24.3144 | 0.822449 | 20.9892 | 0.769240 |
| aco/walker_walk/motion_blur | 1000 | 21.7530 | 0.800257 | 19.4535 | 0.749440 |
| aco/degradation/gaussian_noise | 10000 | 24.9585 | 0.488518 | 20.0974 | 0.350763 |
| aco/walker_walk/gaussian_noise | 1000 | 24.5319 | 0.535962 | 19.9919 | 0.388320 |
| aco/degradation/low_light | 10000 | 21.6091 | 0.479297 | 16.5539 | 0.304196 |
| aco/walker_walk/low_light | 1000 | 19.4135 | 0.390085 | 15.9631 | 0.276432 |
| aco/degradation/jpeg | 10000 | 25.4319 | 0.775968 | 20.0470 | 0.615636 |
| aco/walker_walk/jpeg | 1000 | 23.3872 | 0.794350 | 19.3554 | 0.670302 |
| aco/degradation/defocus_blur | 10000 | 24.8294 | 0.845324 | 21.3498 | 0.791739 |
| aco/walker_walk/defocus_blur | 1000 | 22.2270 | 0.823487 | 19.8524 | 0.767343 |
| aco/degradation/frost | 10000 | 31.0366 | 0.954154 | 26.7626 | 0.918436 |
| aco/walker_walk/frost | 1000 | 30.9569 | 0.958904 | 26.8835 | 0.925059 |
| aco/degradation/occlusion_patch | 10000 | 26.4311 | 0.888214 | 22.4290 | 0.848475 |
| aco/walker_walk/occlusion_patch | 1000 | 27.2141 | 0.898893 | 22.7395 | 0.856668 |
| aco/degradation/saturation | 10000 | 32.1165 | 0.989194 | 25.9381 | 0.891773 |
| aco/walker_walk/saturation | 1000 | 31.3442 | 0.988301 | 25.0539 | 0.873206 |
| aco/degradation/shadow | 10000 | 24.9340 | 0.952393 | 22.4655 | 0.921187 |
| aco/walker_walk/shadow | 1000 | 24.2468 | 0.945140 | 22.1253 | 0.910471 |
| aco/degradation/shot_noise | 10000 | 23.3936 | 0.391061 | 18.6151 | 0.286733 |
| aco/walker_walk/shot_noise | 1000 | 23.2088 | 0.454666 | 18.6176 | 0.329547 |
| aco/task/walker_run | 13000 | 25.3463 | 0.797193 | 21.6483 | 0.714678 |
| aco/walker_run/rain | 1000 | 24.7602 | 0.912429 | 21.8002 | 0.809533 |
| aco/walker_run/fog | 1000 | 30.4277 | 0.983795 | 26.3193 | 0.936958 |
| aco/walker_run/snow | 1000 | 26.5257 | 0.884563 | 23.4751 | 0.811298 |
| aco/walker_run/motion_blur | 1000 | 21.6681 | 0.794472 | 19.3809 | 0.743010 |
| aco/walker_run/gaussian_noise | 1000 | 24.5150 | 0.538525 | 19.9821 | 0.389747 |
| aco/walker_run/low_light | 1000 | 19.4249 | 0.391215 | 16.0015 | 0.276532 |
| aco/walker_run/jpeg | 1000 | 23.2617 | 0.790208 | 19.3210 | 0.668145 |
| aco/walker_run/defocus_blur | 1000 | 22.1680 | 0.819833 | 19.7988 | 0.762118 |
| aco/walker_run/frost | 1000 | 31.0040 | 0.958897 | 26.9226 | 0.925375 |
| aco/walker_run/occlusion_patch | 1000 | 26.9445 | 0.896471 | 22.6169 | 0.853707 |
| aco/walker_run/saturation | 1000 | 31.3122 | 0.988237 | 25.0172 | 0.872187 |
| aco/walker_run/shadow | 1000 | 24.2642 | 0.944921 | 22.1455 | 0.909581 |
| aco/walker_run/shot_noise | 1000 | 23.2263 | 0.459947 | 18.6461 | 0.332624 |
| aco/task/walker_stand | 13000 | 25.3975 | 0.799883 | 21.6980 | 0.707785 |
| aco/walker_stand/rain | 1000 | 24.7907 | 0.911062 | 21.8409 | 0.790941 |
| aco/walker_stand/fog | 1000 | 30.0483 | 0.981258 | 26.1120 | 0.922837 |
| aco/walker_stand/snow | 1000 | 26.4974 | 0.885090 | 23.4876 | 0.797830 |
| aco/walker_stand/motion_blur | 1000 | 21.7683 | 0.812762 | 19.5003 | 0.758109 |
| aco/walker_stand/gaussian_noise | 1000 | 24.4393 | 0.531668 | 19.9848 | 0.378929 |
| aco/walker_stand/low_light | 1000 | 19.7494 | 0.403856 | 16.2897 | 0.282080 |
| aco/walker_stand/jpeg | 1000 | 23.6484 | 0.785141 | 19.4136 | 0.640008 |
| aco/walker_stand/defocus_blur | 1000 | 22.2184 | 0.836276 | 19.8941 | 0.776085 |
| aco/walker_stand/frost | 1000 | 30.7570 | 0.958385 | 26.7545 | 0.914097 |
| aco/walker_stand/occlusion_patch | 1000 | 27.1187 | 0.897639 | 22.7093 | 0.850524 |
| aco/walker_stand/saturation | 1000 | 31.2721 | 0.987665 | 24.9597 | 0.854954 |
| aco/walker_stand/shadow | 1000 | 24.5843 | 0.946662 | 22.3603 | 0.905938 |
| aco/walker_stand/shot_noise | 1000 | 23.2753 | 0.461016 | 18.7673 | 0.328879 |
| aco/task/hopper_stand | 13000 | 27.1630 | 0.793333 | 22.5967 | 0.722354 |
| aco/hopper_stand/rain | 1000 | 26.2084 | 0.920515 | 22.8878 | 0.861316 |
| aco/hopper_stand/fog | 1000 | 32.2269 | 0.991312 | 27.5581 | 0.970495 |
| aco/hopper_stand/snow | 1000 | 27.9176 | 0.867673 | 24.3046 | 0.813784 |
| aco/hopper_stand/motion_blur | 1000 | 25.7111 | 0.858898 | 22.1058 | 0.814839 |
| aco/hopper_stand/gaussian_noise | 1000 | 25.4297 | 0.423043 | 20.2289 | 0.305165 |
| aco/hopper_stand/low_light | 1000 | 22.4365 | 0.482502 | 16.0384 | 0.284666 |
| aco/hopper_stand/jpeg | 1000 | 27.7735 | 0.786477 | 21.3004 | 0.641367 |
| aco/hopper_stand/defocus_blur | 1000 | 26.2500 | 0.871906 | 22.3713 | 0.823305 |
| aco/hopper_stand/frost | 1000 | 32.8342 | 0.959090 | 27.9410 | 0.937472 |
| aco/hopper_stand/occlusion_patch | 1000 | 26.1148 | 0.880582 | 22.0602 | 0.842457 |
| aco/hopper_stand/saturation | 1000 | 31.0355 | 0.990567 | 25.5665 | 0.918893 |
| aco/hopper_stand/shadow | 1000 | 25.8248 | 0.967942 | 23.0538 | 0.946927 |
| aco/hopper_stand/shot_noise | 1000 | 23.3561 | 0.312826 | 18.3398 | 0.229912 |
| aco/task/quadruped_run | 13000 | 25.9623 | 0.765874 | 21.9602 | 0.672268 |
| aco/quadruped_run/rain | 1000 | 25.1533 | 0.844324 | 22.0645 | 0.735845 |
| aco/quadruped_run/fog | 1000 | 30.5775 | 0.984552 | 26.4536 | 0.932289 |
| aco/quadruped_run/snow | 1000 | 27.0371 | 0.801526 | 23.9060 | 0.738132 |
| aco/quadruped_run/motion_blur | 1000 | 23.5611 | 0.760717 | 20.5935 | 0.702837 |
| aco/quadruped_run/gaussian_noise | 1000 | 24.6351 | 0.536679 | 20.0974 | 0.391178 |
| aco/quadruped_run/low_light | 1000 | 20.1182 | 0.376255 | 16.2305 | 0.252286 |
| aco/quadruped_run/jpeg | 1000 | 26.2799 | 0.702117 | 20.3388 | 0.471920 |
| aco/quadruped_run/defocus_blur | 1000 | 24.3695 | 0.777626 | 21.0726 | 0.715195 |
| aco/quadruped_run/frost | 1000 | 28.0438 | 0.889059 | 24.8602 | 0.821703 |
| aco/quadruped_run/occlusion_patch | 1000 | 27.2092 | 0.894999 | 22.6984 | 0.853458 |
| aco/quadruped_run/saturation | 1000 | 31.7483 | 0.988016 | 25.4651 | 0.868028 |
| aco/quadruped_run/shadow | 1000 | 25.4347 | 0.953799 | 22.9317 | 0.929126 |
| aco/quadruped_run/shot_noise | 1000 | 23.3425 | 0.446696 | 18.7699 | 0.327486 |
| aco/task/finger_turn_hard | 13000 | 25.6483 | 0.789861 | 21.8256 | 0.704569 |
| aco/finger_turn_hard/rain | 1000 | 25.6487 | 0.932177 | 22.5028 | 0.836317 |
| aco/finger_turn_hard/fog | 1000 | 29.5975 | 0.974599 | 25.8698 | 0.923846 |
| aco/finger_turn_hard/snow | 1000 | 27.3288 | 0.910739 | 24.0274 | 0.838129 |
| aco/finger_turn_hard/motion_blur | 1000 | 22.3313 | 0.763102 | 19.7052 | 0.698159 |
| aco/finger_turn_hard/gaussian_noise | 1000 | 24.4883 | 0.538185 | 19.9628 | 0.394183 |
| aco/finger_turn_hard/low_light | 1000 | 20.3277 | 0.427467 | 16.6050 | 0.311335 |
| aco/finger_turn_hard/jpeg | 1000 | 23.6248 | 0.675541 | 19.2216 | 0.542143 |
| aco/finger_turn_hard/defocus_blur | 1000 | 22.8033 | 0.794857 | 20.1496 | 0.730053 |
| aco/finger_turn_hard/frost | 1000 | 30.7029 | 0.962404 | 26.5059 | 0.918193 |
| aco/finger_turn_hard/occlusion_patch | 1000 | 27.0172 | 0.898858 | 22.6663 | 0.855532 |
| aco/finger_turn_hard/saturation | 1000 | 31.2183 | 0.985233 | 25.0820 | 0.863545 |
| aco/finger_turn_hard/shadow | 1000 | 24.9654 | 0.946331 | 22.6176 | 0.909428 |
| aco/finger_turn_hard/shot_noise | 1000 | 23.3741 | 0.458695 | 18.8169 | 0.338533 |
| aco/task/cartpole_swingup_sparse | 13000 | 27.0789 | 0.775569 | 22.5601 | 0.699928 |
| aco/cartpole_swingup_sparse/rain | 1000 | 27.1713 | 0.916985 | 23.5707 | 0.867410 |
| aco/cartpole_swingup_sparse/fog | 1000 | 32.0865 | 0.985941 | 27.4401 | 0.962665 |
| aco/cartpole_swingup_sparse/snow | 1000 | 28.6505 | 0.866258 | 24.7723 | 0.825386 |
| aco/cartpole_swingup_sparse/motion_blur | 1000 | 25.0990 | 0.731053 | 21.4096 | 0.653747 |
| aco/cartpole_swingup_sparse/gaussian_noise | 1000 | 25.1089 | 0.468623 | 19.9592 | 0.359245 |
| aco/cartpole_swingup_sparse/low_light | 1000 | 21.7895 | 0.464889 | 16.0767 | 0.297261 |
| aco/cartpole_swingup_sparse/jpeg | 1000 | 27.9855 | 0.740278 | 20.7913 | 0.498915 |
| aco/cartpole_swingup_sparse/defocus_blur | 1000 | 24.7007 | 0.774218 | 21.6274 | 0.724857 |
| aco/cartpole_swingup_sparse/frost | 1000 | 33.0931 | 0.936123 | 28.2081 | 0.916862 |
| aco/cartpole_swingup_sparse/occlusion_patch | 1000 | 25.5574 | 0.878652 | 21.8400 | 0.844374 |
| aco/cartpole_swingup_sparse/saturation | 1000 | 31.5767 | 0.989940 | 26.0557 | 0.919538 |
| aco/cartpole_swingup_sparse/shadow | 1000 | 26.0655 | 0.971169 | 23.3526 | 0.951633 |
| aco/cartpole_swingup_sparse/shot_noise | 1000 | 23.1408 | 0.358262 | 18.1780 | 0.277165 |
| aco/task/cup_catch | 13000 | 27.4418 | 0.797005 | 22.8470 | 0.713743 |
| aco/cup_catch/rain | 1000 | 25.6555 | 0.918301 | 22.5216 | 0.809529 |
| aco/cup_catch/fog | 1000 | 29.8979 | 0.977968 | 26.1505 | 0.927606 |
| aco/cup_catch/snow | 1000 | 27.6376 | 0.893102 | 24.2832 | 0.813523 |
| aco/cup_catch/motion_blur | 1000 | 28.3932 | 0.856226 | 23.1994 | 0.801573 |
| aco/cup_catch/gaussian_noise | 1000 | 24.9852 | 0.448214 | 20.2619 | 0.323529 |
| aco/cup_catch/low_light | 1000 | 23.6999 | 0.444585 | 18.0990 | 0.321038 |
| aco/cup_catch/jpeg | 1000 | 27.5235 | 0.803764 | 21.3158 | 0.676893 |
| aco/cup_catch/defocus_blur | 1000 | 29.0626 | 0.865147 | 23.3869 | 0.810039 |
| aco/cup_catch/frost | 1000 | 31.1358 | 0.960238 | 26.8523 | 0.913668 |
| aco/cup_catch/occlusion_patch | 1000 | 27.3499 | 0.890064 | 23.0042 | 0.842632 |
| aco/cup_catch/saturation | 1000 | 31.3217 | 0.986260 | 25.2577 | 0.849346 |
| aco/cup_catch/shadow | 1000 | 26.2362 | 0.954184 | 23.4806 | 0.916324 |
| aco/cup_catch/shot_noise | 1000 | 23.8436 | 0.363008 | 19.1985 | 0.272965 |
| aco/task/reacher_easy | 13000 | 27.4389 | 0.824863 | 22.6122 | 0.741944 |
| aco/reacher_easy/rain | 1000 | 28.9219 | 0.948801 | 24.5804 | 0.905747 |
| aco/reacher_easy/fog | 1000 | 32.1720 | 0.991318 | 27.4968 | 0.959957 |
| aco/reacher_easy/snow | 1000 | 28.9495 | 0.851230 | 24.5461 | 0.788774 |
| aco/reacher_easy/motion_blur | 1000 | 26.1914 | 0.917927 | 22.0447 | 0.877157 |
| aco/reacher_easy/gaussian_noise | 1000 | 25.6256 | 0.434455 | 20.2227 | 0.292944 |
| aco/reacher_easy/low_light | 1000 | 24.4957 | 0.704890 | 17.0197 | 0.375657 |
| aco/reacher_easy/jpeg | 1000 | 25.4587 | 0.840501 | 19.4689 | 0.664116 |
| aco/reacher_easy/defocus_blur | 1000 | 27.0625 | 0.941444 | 22.4773 | 0.896606 |
| aco/reacher_easy/frost | 1000 | 30.8048 | 0.978202 | 26.2476 | 0.955293 |
| aco/reacher_easy/occlusion_patch | 1000 | 24.7726 | 0.872737 | 21.8425 | 0.842184 |
| aco/reacher_easy/saturation | 1000 | 34.7901 | 0.993130 | 28.2688 | 0.948520 |
| aco/reacher_easy/shadow | 1000 | 23.9388 | 0.948406 | 21.3665 | 0.919500 |
| aco/reacher_easy/shot_noise | 1000 | 23.5222 | 0.300182 | 18.3760 | 0.218819 |
| aco/task/reacher_hard | 13000 | 27.7158 | 0.826476 | 22.8658 | 0.743762 |
| aco/reacher_hard/rain | 1000 | 29.6217 | 0.953300 | 24.9780 | 0.908581 |
| aco/reacher_hard/fog | 1000 | 32.1200 | 0.991877 | 27.6422 | 0.960727 |
| aco/reacher_hard/snow | 1000 | 29.6100 | 0.854359 | 24.9470 | 0.788970 |
| aco/reacher_hard/motion_blur | 1000 | 26.6669 | 0.929079 | 22.4994 | 0.893525 |
| aco/reacher_hard/gaussian_noise | 1000 | 25.8259 | 0.429827 | 20.2823 | 0.284387 |
| aco/reacher_hard/low_light | 1000 | 24.6361 | 0.707229 | 17.2151 | 0.364671 |
| aco/reacher_hard/jpeg | 1000 | 25.3756 | 0.841301 | 19.9435 | 0.682553 |
| aco/reacher_hard/defocus_blur | 1000 | 27.4322 | 0.948444 | 22.8681 | 0.911788 |
| aco/reacher_hard/frost | 1000 | 31.0337 | 0.980239 | 26.4505 | 0.956636 |
| aco/reacher_hard/occlusion_patch | 1000 | 25.0128 | 0.873247 | 22.1125 | 0.843211 |
| aco/reacher_hard/saturation | 1000 | 35.5458 | 0.994594 | 28.6548 | 0.949511 |
| aco/reacher_hard/shadow | 1000 | 23.7790 | 0.945380 | 21.2209 | 0.912945 |
| aco/reacher_hard/shot_noise | 1000 | 23.6462 | 0.295308 | 18.4408 | 0.211402 |
| aco/clean_input | 10000 | 28.8445 | 0.843593 | 21.1405 | 0.627788 |
| aco/original7 | 70000 | 25.8932 | 0.762551 | 21.6325 | 0.659998 |
| aco/added6 | 60000 | 27.1235 | 0.836723 | 22.9267 | 0.776390 |
| smfa/all | 130000 | 34.6075 | 0.928539 | 32.1043 | 0.903184 |
| smfa/task/walker_walk | 13000 | 33.2784 | 0.920498 | 31.0378 | 0.896049 |
| smfa/degradation/rain | 10000 | 36.3911 | 0.946276 | 34.7065 | 0.927951 |
| smfa/walker_walk/rain | 1000 | 34.0677 | 0.933760 | 32.6377 | 0.913460 |
| smfa/degradation/fog | 10000 | 39.4200 | 0.988639 | 37.1387 | 0.980476 |
| smfa/walker_walk/fog | 1000 | 38.4365 | 0.988227 | 36.5327 | 0.980368 |
| smfa/degradation/snow | 10000 | 34.5333 | 0.924368 | 32.9127 | 0.896508 |
| smfa/walker_walk/snow | 1000 | 32.5959 | 0.910295 | 31.1172 | 0.879723 |
| smfa/degradation/motion_blur | 10000 | 27.5314 | 0.807301 | 25.4426 | 0.787774 |
| smfa/walker_walk/motion_blur | 1000 | 25.3368 | 0.763771 | 23.5471 | 0.748725 |
| smfa/degradation/gaussian_noise | 10000 | 37.4766 | 0.946601 | 34.4914 | 0.915215 |
| smfa/walker_walk/gaussian_noise | 1000 | 36.6730 | 0.946662 | 33.8918 | 0.914972 |
| smfa/degradation/low_light | 10000 | 32.8594 | 0.906269 | 30.2374 | 0.854017 |
| smfa/walker_walk/low_light | 1000 | 32.3461 | 0.911081 | 29.9869 | 0.862978 |
| smfa/degradation/jpeg | 10000 | 34.2913 | 0.937148 | 30.3258 | 0.893146 |
| smfa/walker_walk/jpeg | 1000 | 33.1525 | 0.934045 | 29.4066 | 0.886802 |
| smfa/degradation/defocus_blur | 10000 | 28.1561 | 0.821343 | 26.1194 | 0.799688 |
| smfa/walker_walk/defocus_blur | 1000 | 26.2544 | 0.789982 | 24.5269 | 0.770180 |
| smfa/degradation/frost | 10000 | 36.6674 | 0.967724 | 34.6736 | 0.953614 |
| smfa/walker_walk/frost | 1000 | 35.4970 | 0.966527 | 33.6076 | 0.951681 |
| smfa/degradation/occlusion_patch | 10000 | 32.4079 | 0.931869 | 29.8042 | 0.912521 |
| smfa/walker_walk/occlusion_patch | 1000 | 30.0096 | 0.920527 | 27.8142 | 0.905905 |
| smfa/degradation/saturation | 10000 | 40.9557 | 0.992784 | 37.6009 | 0.981075 |
| smfa/walker_walk/saturation | 1000 | 40.2919 | 0.992704 | 37.3179 | 0.982445 |
| smfa/degradation/shadow | 10000 | 33.9400 | 0.975677 | 31.5058 | 0.957699 |
| smfa/walker_walk/shadow | 1000 | 33.8758 | 0.979877 | 31.6823 | 0.964729 |
| smfa/degradation/shot_noise | 10000 | 35.2666 | 0.925013 | 32.3964 | 0.881712 |
| smfa/walker_walk/shot_noise | 1000 | 34.0819 | 0.929018 | 31.4222 | 0.886671 |
| smfa/task/walker_run | 13000 | 33.1696 | 0.918898 | 30.9334 | 0.893937 |
| smfa/walker_run/rain | 1000 | 33.9604 | 0.932758 | 32.5215 | 0.912203 |
| smfa/walker_run/fog | 1000 | 38.7175 | 0.988144 | 36.7966 | 0.980232 |
| smfa/walker_run/snow | 1000 | 32.4851 | 0.908082 | 31.0107 | 0.877165 |
| smfa/walker_run/motion_blur | 1000 | 25.0603 | 0.756796 | 23.3068 | 0.740536 |
| smfa/walker_run/gaussian_noise | 1000 | 36.4196 | 0.945315 | 33.6600 | 0.913150 |
| smfa/walker_run/low_light | 1000 | 32.3480 | 0.911107 | 29.9989 | 0.863366 |
| smfa/walker_run/jpeg | 1000 | 32.9522 | 0.932156 | 29.2313 | 0.883239 |
| smfa/walker_run/defocus_blur | 1000 | 26.0356 | 0.785256 | 24.3378 | 0.763840 |
| smfa/walker_run/frost | 1000 | 35.3316 | 0.965891 | 33.3936 | 0.950468 |
| smfa/walker_run/occlusion_patch | 1000 | 29.7527 | 0.919206 | 27.5937 | 0.904385 |
| smfa/walker_run/saturation | 1000 | 40.2995 | 0.992661 | 37.2787 | 0.982393 |
| smfa/walker_run/shadow | 1000 | 33.9090 | 0.979915 | 31.7213 | 0.964591 |
| smfa/walker_run/shot_noise | 1000 | 33.9328 | 0.928391 | 31.2839 | 0.885612 |
| smfa/task/walker_stand | 13000 | 32.5836 | 0.919250 | 30.3697 | 0.891861 |
| smfa/walker_stand/rain | 1000 | 33.8410 | 0.932748 | 32.3534 | 0.909123 |
| smfa/walker_stand/fog | 1000 | 37.5590 | 0.987034 | 35.6624 | 0.977659 |
| smfa/walker_stand/snow | 1000 | 33.0032 | 0.910835 | 31.4729 | 0.877899 |
| smfa/walker_stand/motion_blur | 1000 | 25.0728 | 0.768100 | 23.3004 | 0.752508 |
| smfa/walker_stand/gaussian_noise | 1000 | 34.8351 | 0.937973 | 32.1512 | 0.900419 |
| smfa/walker_stand/low_light | 1000 | 32.4581 | 0.913847 | 30.1176 | 0.864356 |
| smfa/walker_stand/jpeg | 1000 | 31.7603 | 0.927306 | 28.3716 | 0.876107 |
| smfa/walker_stand/defocus_blur | 1000 | 26.0587 | 0.798005 | 24.3401 | 0.777075 |
| smfa/walker_stand/frost | 1000 | 32.8936 | 0.959430 | 30.8374 | 0.935962 |
| smfa/walker_stand/occlusion_patch | 1000 | 29.3950 | 0.919648 | 27.2223 | 0.902181 |
| smfa/walker_stand/saturation | 1000 | 40.2413 | 0.992509 | 37.2938 | 0.982109 |
| smfa/walker_stand/shadow | 1000 | 33.3890 | 0.978341 | 31.2119 | 0.961089 |
| smfa/walker_stand/shot_noise | 1000 | 33.0804 | 0.924472 | 30.4712 | 0.877711 |
| smfa/task/hopper_stand | 13000 | 34.7939 | 0.924371 | 32.4595 | 0.897762 |
| smfa/hopper_stand/rain | 1000 | 36.5934 | 0.939367 | 35.1384 | 0.920070 |
| smfa/hopper_stand/fog | 1000 | 39.2029 | 0.986658 | 36.4033 | 0.977919 |
| smfa/hopper_stand/snow | 1000 | 35.2845 | 0.919611 | 33.7406 | 0.890048 |
| smfa/hopper_stand/motion_blur | 1000 | 29.6522 | 0.841901 | 27.4658 | 0.826176 |
| smfa/hopper_stand/gaussian_noise | 1000 | 38.0491 | 0.932542 | 35.5143 | 0.899870 |
| smfa/hopper_stand/low_light | 1000 | 33.2276 | 0.882682 | 30.8835 | 0.825039 |
| smfa/hopper_stand/jpeg | 1000 | 35.0821 | 0.922596 | 31.4062 | 0.875156 |
| smfa/hopper_stand/defocus_blur | 1000 | 30.1707 | 0.848816 | 28.0559 | 0.832517 |
| smfa/hopper_stand/frost | 1000 | 35.8027 | 0.954881 | 33.7781 | 0.938498 |
| smfa/hopper_stand/occlusion_patch | 1000 | 33.6563 | 0.934424 | 31.1054 | 0.916498 |
| smfa/hopper_stand/saturation | 1000 | 41.3168 | 0.992601 | 38.8456 | 0.981946 |
| smfa/hopper_stand/shadow | 1000 | 28.3696 | 0.957621 | 26.3081 | 0.933120 |
| smfa/hopper_stand/shot_noise | 1000 | 35.9128 | 0.903124 | 33.3285 | 0.854049 |
| smfa/task/quadruped_run | 13000 | 32.9888 | 0.901342 | 30.7219 | 0.875761 |
| smfa/quadruped_run/rain | 1000 | 33.1688 | 0.900365 | 31.7668 | 0.880610 |
| smfa/quadruped_run/fog | 1000 | 36.0314 | 0.984637 | 34.2365 | 0.976297 |
| smfa/quadruped_run/snow | 1000 | 31.4478 | 0.856752 | 30.0536 | 0.827662 |
| smfa/quadruped_run/motion_blur | 1000 | 26.5949 | 0.736817 | 24.5151 | 0.707423 |
| smfa/quadruped_run/gaussian_noise | 1000 | 36.4417 | 0.937777 | 33.7480 | 0.908421 |
| smfa/quadruped_run/low_light | 1000 | 32.0585 | 0.887252 | 29.6216 | 0.838430 |
| smfa/quadruped_run/jpeg | 1000 | 32.9979 | 0.922489 | 28.9160 | 0.877504 |
| smfa/quadruped_run/defocus_blur | 1000 | 27.0471 | 0.734223 | 24.9888 | 0.705044 |
| smfa/quadruped_run/frost | 1000 | 34.3279 | 0.954850 | 32.7387 | 0.941448 |
| smfa/quadruped_run/occlusion_patch | 1000 | 30.6311 | 0.912608 | 28.4495 | 0.895654 |
| smfa/quadruped_run/saturation | 1000 | 39.6164 | 0.991678 | 36.7313 | 0.980644 |
| smfa/quadruped_run/shadow | 1000 | 33.8407 | 0.977124 | 31.6347 | 0.961786 |
| smfa/quadruped_run/shot_noise | 1000 | 34.6499 | 0.920877 | 31.9837 | 0.883971 |
| smfa/task/finger_turn_hard | 13000 | 34.8224 | 0.929458 | 31.8325 | 0.902956 |
| smfa/finger_turn_hard/rain | 1000 | 37.3328 | 0.962998 | 35.2808 | 0.943324 |
| smfa/finger_turn_hard/fog | 1000 | 40.5582 | 0.989606 | 37.8563 | 0.980510 |
| smfa/finger_turn_hard/snow | 1000 | 35.2937 | 0.947849 | 33.3236 | 0.918303 |
| smfa/finger_turn_hard/motion_blur | 1000 | 26.7394 | 0.770974 | 24.4003 | 0.743801 |
| smfa/finger_turn_hard/gaussian_noise | 1000 | 37.6535 | 0.950962 | 33.8976 | 0.920664 |
| smfa/finger_turn_hard/low_light | 1000 | 32.9144 | 0.911420 | 29.6437 | 0.863486 |
| smfa/finger_turn_hard/jpeg | 1000 | 34.3248 | 0.935748 | 29.6839 | 0.888265 |
| smfa/finger_turn_hard/defocus_blur | 1000 | 28.0840 | 0.809469 | 25.6847 | 0.779582 |
| smfa/finger_turn_hard/frost | 1000 | 37.3009 | 0.973214 | 35.1641 | 0.959139 |
| smfa/finger_turn_hard/occlusion_patch | 1000 | 30.9052 | 0.925295 | 28.1933 | 0.908063 |
| smfa/finger_turn_hard/saturation | 1000 | 40.5402 | 0.992402 | 35.9039 | 0.976938 |
| smfa/finger_turn_hard/shadow | 1000 | 35.9135 | 0.978430 | 32.9974 | 0.960475 |
| smfa/finger_turn_hard/shot_noise | 1000 | 35.1309 | 0.934589 | 31.7930 | 0.895882 |
| smfa/task/cartpole_swingup_sparse | 13000 | 35.0126 | 0.913908 | 32.5599 | 0.889456 |
| smfa/cartpole_swingup_sparse/rain | 1000 | 36.5243 | 0.944092 | 35.0221 | 0.928289 |
| smfa/cartpole_swingup_sparse/fog | 1000 | 39.7808 | 0.988464 | 37.7828 | 0.982139 |
| smfa/cartpole_swingup_sparse/snow | 1000 | 34.9260 | 0.917661 | 33.4094 | 0.893709 |
| smfa/cartpole_swingup_sparse/motion_blur | 1000 | 29.8642 | 0.769114 | 27.5397 | 0.740875 |
| smfa/cartpole_swingup_sparse/gaussian_noise | 1000 | 37.5972 | 0.935525 | 34.6976 | 0.907751 |
| smfa/cartpole_swingup_sparse/low_light | 1000 | 32.7679 | 0.876198 | 30.1533 | 0.827072 |
| smfa/cartpole_swingup_sparse/jpeg | 1000 | 35.6111 | 0.931380 | 31.7797 | 0.893975 |
| smfa/cartpole_swingup_sparse/defocus_blur | 1000 | 30.0374 | 0.764150 | 27.7853 | 0.736390 |
| smfa/cartpole_swingup_sparse/frost | 1000 | 37.2368 | 0.967228 | 35.3744 | 0.956526 |
| smfa/cartpole_swingup_sparse/occlusion_patch | 1000 | 33.9898 | 0.927166 | 31.4461 | 0.909748 |
| smfa/cartpole_swingup_sparse/saturation | 1000 | 42.6982 | 0.993316 | 39.2925 | 0.982406 |
| smfa/cartpole_swingup_sparse/shadow | 1000 | 28.4342 | 0.960497 | 26.2317 | 0.940265 |
| smfa/cartpole_swingup_sparse/shot_noise | 1000 | 35.6955 | 0.906019 | 32.7647 | 0.863783 |
| smfa/task/cup_catch | 13000 | 36.7432 | 0.937657 | 34.1255 | 0.912344 |
| smfa/cup_catch/rain | 1000 | 38.0630 | 0.954279 | 36.4251 | 0.934547 |
| smfa/cup_catch/fog | 1000 | 40.4163 | 0.987771 | 38.3189 | 0.978827 |
| smfa/cup_catch/snow | 1000 | 36.3235 | 0.933293 | 34.7702 | 0.904234 |
| smfa/cup_catch/motion_blur | 1000 | 31.6175 | 0.862986 | 29.0268 | 0.842665 |
| smfa/cup_catch/gaussian_noise | 1000 | 38.9731 | 0.943068 | 35.8067 | 0.909346 |
| smfa/cup_catch/low_light | 1000 | 34.6203 | 0.901149 | 31.6209 | 0.846539 |
| smfa/cup_catch/jpeg | 1000 | 36.0220 | 0.933699 | 32.3457 | 0.897681 |
| smfa/cup_catch/defocus_blur | 1000 | 31.8932 | 0.859478 | 29.3709 | 0.841238 |
| smfa/cup_catch/frost | 1000 | 37.4470 | 0.966161 | 35.6308 | 0.951144 |
| smfa/cup_catch/occlusion_patch | 1000 | 36.5333 | 0.950829 | 33.4335 | 0.930148 |
| smfa/cup_catch/saturation | 1000 | 43.0506 | 0.992721 | 39.7848 | 0.979637 |
| smfa/cup_catch/shadow | 1000 | 35.1174 | 0.975371 | 32.6728 | 0.957458 |
| smfa/cup_catch/shot_noise | 1000 | 37.5848 | 0.928736 | 34.4245 | 0.887002 |
| smfa/task/reacher_easy | 13000 | 35.9068 | 0.960355 | 33.1156 | 0.935539 |
| smfa/reacher_easy/rain | 1000 | 39.5200 | 0.980032 | 37.4159 | 0.967919 |
| smfa/reacher_easy/fog | 1000 | 41.1074 | 0.992460 | 38.1266 | 0.984886 |
| smfa/reacher_easy/snow | 1000 | 36.2438 | 0.967989 | 34.5244 | 0.946423 |
| smfa/reacher_easy/motion_blur | 1000 | 27.7018 | 0.905714 | 25.5831 | 0.887264 |
| smfa/reacher_easy/gaussian_noise | 1000 | 38.6086 | 0.967542 | 35.4219 | 0.938013 |
| smfa/reacher_easy/low_light | 1000 | 32.8117 | 0.933683 | 29.8610 | 0.872837 |
| smfa/reacher_easy/jpeg | 1000 | 35.5813 | 0.968491 | 31.2035 | 0.930793 |
| smfa/reacher_easy/defocus_blur | 1000 | 28.0895 | 0.919454 | 26.1314 | 0.898206 |
| smfa/reacher_easy/frost | 1000 | 40.1034 | 0.984304 | 37.7911 | 0.975649 |
| smfa/reacher_easy/occlusion_patch | 1000 | 33.8851 | 0.951627 | 30.6542 | 0.923695 |
| smfa/reacher_easy/saturation | 1000 | 39.8333 | 0.993111 | 36.2334 | 0.981228 |
| smfa/reacher_easy/shadow | 1000 | 37.3721 | 0.983765 | 34.6380 | 0.965187 |
| smfa/reacher_easy/shot_noise | 1000 | 35.9304 | 0.936447 | 32.9187 | 0.889913 |
| smfa/task/reacher_hard | 13000 | 36.7752 | 0.959655 | 33.8867 | 0.936177 |
| smfa/reacher_hard/rain | 1000 | 40.8395 | 0.982357 | 38.5032 | 0.969965 |
| smfa/reacher_hard/fog | 1000 | 42.3905 | 0.993393 | 39.6708 | 0.985921 |
| smfa/reacher_hard/snow | 1000 | 37.7296 | 0.971314 | 35.7047 | 0.949917 |
| smfa/reacher_hard/motion_blur | 1000 | 27.6741 | 0.896837 | 25.7407 | 0.887769 |
| smfa/reacher_hard/gaussian_noise | 1000 | 39.5154 | 0.968644 | 36.1248 | 0.939538 |
| smfa/reacher_hard/low_light | 1000 | 33.0416 | 0.934274 | 30.4863 | 0.876062 |
| smfa/reacher_hard/jpeg | 1000 | 35.4287 | 0.963574 | 30.9138 | 0.921939 |
| smfa/reacher_hard/defocus_blur | 1000 | 27.8907 | 0.904595 | 25.9723 | 0.892809 |
| smfa/reacher_hard/frost | 1000 | 40.7332 | 0.984752 | 38.4205 | 0.975623 |
| smfa/reacher_hard/occlusion_patch | 1000 | 35.3210 | 0.957356 | 32.1300 | 0.928934 |
| smfa/reacher_hard/saturation | 1000 | 41.6689 | 0.994138 | 37.3269 | 0.981002 |
| smfa/reacher_hard/shadow | 1000 | 39.1785 | 0.985831 | 35.9594 | 0.968293 |
| smfa/reacher_hard/shot_noise | 1000 | 36.6661 | 0.938453 | 33.5735 | 0.892526 |
| smfa/clean_input | 10000 | 44.6843 | 0.995525 | 40.7921 | 0.988938 |
| smfa/original7 | 70000 | 34.6433 | 0.922372 | 32.1793 | 0.893584 |
| smfa/added6 | 60000 | 34.5656 | 0.935735 | 32.0167 | 0.914385 |

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
| markov/aco | 455.32 +/- 338.30 (n=100) |
| single/all/aco | 462.43 +/- 401.21 (n=650) |
| single/original7/aco | 435.52 +/- 404.30 (n=350) |
| single/added6/aco | 493.82 +/- 395.93 (n=300) |
| single/rain/aco | 711.14 +/- 337.52 (n=50) |
| single/fog/aco | 720.39 +/- 331.29 (n=50) |
| single/snow/aco | 653.04 +/- 380.41 (n=50) |
| single/motion_blur/aco | 389.46 +/- 388.09 (n=50) |
| single/gaussian_noise/aco | 193.88 +/- 300.34 (n=50) |
| single/low_light/aco | 92.34 +/- 164.07 (n=50) |
| single/jpeg/aco | 288.39 +/- 339.88 (n=50) |
| single/defocus_blur/aco | 410.08 +/- 385.57 (n=50) |
| single/frost/aco | 720.97 +/- 338.00 (n=50) |
| single/occlusion_patch/aco | 384.08 +/- 369.73 (n=50) |
| single/saturation/aco | 700.02 +/- 354.13 (n=50) |
| single/shadow/aco | 595.27 +/- 353.76 (n=50) |
| single/shot_noise/aco | 152.53 +/- 248.15 (n=50) |
| task/walker_walk/single_mean/aco | 591.43 +/- 373.93 (n=65) |
| task/walker_walk/markov/aco | 481.66 +/- 88.64 (n=10) |
| task/walker_walk/rain/aco | 935.66 +/- 30.67 (n=5) |
| task/walker_walk/fog/aco | 951.46 +/- 13.15 (n=5) |
| task/walker_walk/snow/aco | 957.12 +/- 8.80 (n=5) |
| task/walker_walk/motion_blur/aco | 332.64 +/- 92.70 (n=5) |
| task/walker_walk/gaussian_noise/aco | 40.56 +/- 8.79 (n=5) |
| task/walker_walk/low_light/aco | 47.55 +/- 12.17 (n=5) |
| task/walker_walk/jpeg/aco | 508.75 +/- 101.25 (n=5) |
| task/walker_walk/defocus_blur/aco | 417.49 +/- 100.36 (n=5) |
| task/walker_walk/frost/aco | 961.19 +/- 3.44 (n=5) |
| task/walker_walk/occlusion_patch/aco | 745.20 +/- 139.97 (n=5) |
| task/walker_walk/saturation/aco | 961.49 +/- 12.70 (n=5) |
| task/walker_walk/shadow/aco | 785.12 +/- 194.64 (n=5) |
| task/walker_walk/shot_noise/aco | 44.39 +/- 11.46 (n=5) |
| task/walker_run/single_mean/aco | 320.07 +/- 237.06 (n=65) |
| task/walker_run/markov/aco | 214.70 +/- 91.26 (n=10) |
| task/walker_run/rain/aco | 515.17 +/- 45.62 (n=5) |
| task/walker_run/fog/aco | 617.24 +/- 108.10 (n=5) |
| task/walker_run/snow/aco | 509.17 +/- 67.38 (n=5) |
| task/walker_run/motion_blur/aco | 174.19 +/- 28.86 (n=5) |
| task/walker_run/gaussian_noise/aco | 46.22 +/- 12.73 (n=5) |
| task/walker_run/low_light/aco | 21.38 +/- 11.68 (n=5) |
| task/walker_run/jpeg/aco | 174.14 +/- 28.54 (n=5) |
| task/walker_run/defocus_blur/aco | 146.66 +/- 29.61 (n=5) |
| task/walker_run/frost/aco | 693.01 +/- 80.27 (n=5) |
| task/walker_run/occlusion_patch/aco | 260.18 +/- 49.13 (n=5) |
| task/walker_run/saturation/aco | 499.34 +/- 57.41 (n=5) |
| task/walker_run/shadow/aco | 461.02 +/- 167.04 (n=5) |
| task/walker_run/shot_noise/aco | 43.23 +/- 10.38 (n=5) |
| task/walker_stand/single_mean/aco | 816.15 +/- 238.52 (n=65) |
| task/walker_stand/markov/aco | 814.67 +/- 112.57 (n=10) |
| task/walker_stand/rain/aco | 960.84 +/- 19.50 (n=5) |
| task/walker_stand/fog/aco | 964.66 +/- 26.22 (n=5) |
| task/walker_stand/snow/aco | 957.35 +/- 24.92 (n=5) |
| task/walker_stand/motion_blur/aco | 881.96 +/- 84.65 (n=5) |
| task/walker_stand/gaussian_noise/aco | 498.92 +/- 201.12 (n=5) |
| task/walker_stand/low_light/aco | 269.60 +/- 117.60 (n=5) |
| task/walker_stand/jpeg/aco | 841.59 +/- 113.88 (n=5) |
| task/walker_stand/defocus_blur/aco | 896.47 +/- 60.26 (n=5) |
| task/walker_stand/frost/aco | 962.99 +/- 23.75 (n=5) |
| task/walker_stand/occlusion_patch/aco | 960.89 +/- 18.35 (n=5) |
| task/walker_stand/saturation/aco | 968.74 +/- 13.84 (n=5) |
| task/walker_stand/shadow/aco | 944.30 +/- 41.52 (n=5) |
| task/walker_stand/shot_noise/aco | 501.71 +/- 95.93 (n=5) |
| task/hopper_stand/single_mean/aco | 382.80 +/- 391.49 (n=65) |
| task/hopper_stand/markov/aco | 414.60 +/- 168.85 (n=10) |
| task/hopper_stand/rain/aco | 712.13 +/- 398.29 (n=5) |
| task/hopper_stand/fog/aco | 704.16 +/- 394.84 (n=5) |
| task/hopper_stand/snow/aco | 717.35 +/- 401.05 (n=5) |
| task/hopper_stand/motion_blur/aco | 250.48 +/- 163.56 (n=5) |
| task/hopper_stand/gaussian_noise/aco | 34.07 +/- 41.27 (n=5) |
| task/hopper_stand/low_light/aco | 2.10 +/- 4.69 (n=5) |
| task/hopper_stand/jpeg/aco | 7.62 +/- 11.57 (n=5) |
| task/hopper_stand/defocus_blur/aco | 281.98 +/- 181.85 (n=5) |
| task/hopper_stand/frost/aco | 669.71 +/- 381.07 (n=5) |
| task/hopper_stand/occlusion_patch/aco | 282.55 +/- 189.83 (n=5) |
| task/hopper_stand/saturation/aco | 729.82 +/- 408.06 (n=5) |
| task/hopper_stand/shadow/aco | 582.14 +/- 349.90 (n=5) |
| task/hopper_stand/shot_noise/aco | 2.26 +/- 5.05 (n=5) |
| task/quadruped_run/single_mean/aco | 360.10 +/- 146.13 (n=65) |
| task/quadruped_run/markov/aco | 436.47 +/- 86.16 (n=10) |
| task/quadruped_run/rain/aco | 475.96 +/- 56.85 (n=5) |
| task/quadruped_run/fog/aco | 437.95 +/- 121.16 (n=5) |
| task/quadruped_run/snow/aco | 419.17 +/- 124.88 (n=5) |
| task/quadruped_run/motion_blur/aco | 280.75 +/- 86.65 (n=5) |
| task/quadruped_run/gaussian_noise/aco | 260.46 +/- 87.83 (n=5) |
| task/quadruped_run/low_light/aco | 227.20 +/- 115.11 (n=5) |
| task/quadruped_run/jpeg/aco | 241.64 +/- 133.71 (n=5) |
| task/quadruped_run/defocus_blur/aco | 237.62 +/- 51.30 (n=5) |
| task/quadruped_run/frost/aco | 429.35 +/- 77.18 (n=5) |
| task/quadruped_run/occlusion_patch/aco | 413.99 +/- 210.67 (n=5) |
| task/quadruped_run/saturation/aco | 505.60 +/- 67.35 (n=5) |
| task/quadruped_run/shadow/aco | 468.74 +/- 109.36 (n=5) |
| task/quadruped_run/shot_noise/aco | 282.87 +/- 163.36 (n=5) |
| task/finger_turn_hard/single_mean/aco | 311.14 +/- 405.23 (n=65) |
| task/finger_turn_hard/markov/aco | 386.40 +/- 364.18 (n=10) |
| task/finger_turn_hard/rain/aco | 721.80 +/- 403.50 (n=5) |
| task/finger_turn_hard/fog/aco | 729.60 +/- 299.05 (n=5) |
| task/finger_turn_hard/snow/aco | 188.80 +/- 414.92 (n=5) |
| task/finger_turn_hard/motion_blur/aco | 12.60 +/- 15.60 (n=5) |
| task/finger_turn_hard/gaussian_noise/aco | 127.00 +/- 283.98 (n=5) |
| task/finger_turn_hard/low_light/aco | 0.00 +/- 0.00 (n=5) |
| task/finger_turn_hard/jpeg/aco | 148.00 +/- 203.06 (n=5) |
| task/finger_turn_hard/defocus_blur/aco | 147.60 +/- 201.98 (n=5) |
| task/finger_turn_hard/frost/aco | 699.60 +/- 408.79 (n=5) |
| task/finger_turn_hard/occlusion_patch/aco | 374.80 +/- 492.12 (n=5) |
| task/finger_turn_hard/saturation/aco | 535.00 +/- 490.26 (n=5) |
| task/finger_turn_hard/shadow/aco | 360.00 +/- 469.24 (n=5) |
| task/finger_turn_hard/shot_noise/aco | 0.00 +/- 0.00 (n=5) |
| task/cartpole_swingup_sparse/single_mean/aco | 366.48 +/- 389.88 (n=65) |
| task/cartpole_swingup_sparse/markov/aco | 47.30 +/- 70.94 (n=10) |
| task/cartpole_swingup_sparse/rain/aco | 819.60 +/- 26.35 (n=5) |
| task/cartpole_swingup_sparse/fog/aco | 830.20 +/- 4.49 (n=5) |
| task/cartpole_swingup_sparse/snow/aco | 813.80 +/- 24.74 (n=5) |
| task/cartpole_swingup_sparse/motion_blur/aco | 17.00 +/- 10.42 (n=5) |
| task/cartpole_swingup_sparse/gaussian_noise/aco | 0.00 +/- 0.00 (n=5) |
| task/cartpole_swingup_sparse/low_light/aco | 0.00 +/- 0.00 (n=5) |
| task/cartpole_swingup_sparse/jpeg/aco | 3.40 +/- 3.44 (n=5) |
| task/cartpole_swingup_sparse/defocus_blur/aco | 19.00 +/- 12.61 (n=5) |
| task/cartpole_swingup_sparse/frost/aco | 826.80 +/- 4.49 (n=5) |
| task/cartpole_swingup_sparse/occlusion_patch/aco | 95.60 +/- 63.61 (n=5) |
| task/cartpole_swingup_sparse/saturation/aco | 830.40 +/- 7.64 (n=5) |
| task/cartpole_swingup_sparse/shadow/aco | 507.20 +/- 171.70 (n=5) |
| task/cartpole_swingup_sparse/shot_noise/aco | 1.20 +/- 2.68 (n=5) |
| task/cup_catch/single_mean/aco | 711.29 +/- 425.18 (n=65) |
| task/cup_catch/markov/aco | 819.40 +/- 168.85 (n=10) |
| task/cup_catch/rain/aco | 977.20 +/- 11.48 (n=5) |
| task/cup_catch/fog/aco | 977.40 +/- 11.57 (n=5) |
| task/cup_catch/snow/aco | 976.80 +/- 12.09 (n=5) |
| task/cup_catch/motion_blur/aco | 976.20 +/- 10.28 (n=5) |
| task/cup_catch/gaussian_noise/aco | 194.40 +/- 411.95 (n=5) |
| task/cup_catch/low_light/aco | 3.00 +/- 4.47 (n=5) |
| task/cup_catch/jpeg/aco | 884.40 +/- 122.94 (n=5) |
| task/cup_catch/defocus_blur/aco | 977.20 +/- 10.94 (n=5) |
| task/cup_catch/frost/aco | 977.60 +/- 11.80 (n=5) |
| task/cup_catch/occlusion_patch/aco | 356.20 +/- 476.62 (n=5) |
| task/cup_catch/saturation/aco | 976.80 +/- 11.88 (n=5) |
| task/cup_catch/shadow/aco | 965.20 +/- 14.34 (n=5) |
| task/cup_catch/shot_noise/aco | 4.40 +/- 6.07 (n=5) |
| task/reacher_easy/single_mean/aco | 752.69 +/- 368.71 (n=65) |
| task/reacher_easy/markov/aco | 926.60 +/- 114.69 (n=10) |
| task/reacher_easy/rain/aco | 982.00 +/- 15.54 (n=5) |
| task/reacher_easy/fog/aco | 982.40 +/- 14.84 (n=5) |
| task/reacher_easy/snow/aco | 982.00 +/- 15.22 (n=5) |
| task/reacher_easy/motion_blur/aco | 967.80 +/- 40.41 (n=5) |
| task/reacher_easy/gaussian_noise/aco | 736.40 +/- 356.47 (n=5) |
| task/reacher_easy/low_light/aco | 347.00 +/- 315.55 (n=5) |
| task/reacher_easy/jpeg/aco | 72.60 +/- 157.36 (n=5) |
| task/reacher_easy/defocus_blur/aco | 976.00 +/- 23.36 (n=5) |
| task/reacher_easy/frost/aco | 981.60 +/- 16.26 (n=5) |
| task/reacher_easy/occlusion_patch/aco | 344.00 +/- 449.17 (n=5) |
| task/reacher_easy/saturation/aco | 982.80 +/- 14.17 (n=5) |
| task/reacher_easy/shadow/aco | 786.00 +/- 435.80 (n=5) |
| task/reacher_easy/shot_noise/aco | 644.40 +/- 265.26 (n=5) |
| task/reacher_hard/single_mean/aco | 12.14 +/- 56.86 (n=65) |
| task/reacher_hard/markov/aco | 11.40 +/- 25.95 (n=10) |
| task/reacher_hard/rain/aco | 11.00 +/- 22.43 (n=5) |
| task/reacher_hard/fog/aco | 8.80 +/- 19.68 (n=5) |
| task/reacher_hard/snow/aco | 8.80 +/- 18.05 (n=5) |
| task/reacher_hard/motion_blur/aco | 1.00 +/- 1.41 (n=5) |
| task/reacher_hard/gaussian_noise/aco | 0.80 +/- 1.79 (n=5) |
| task/reacher_hard/low_light/aco | 5.60 +/- 5.59 (n=5) |
| task/reacher_hard/jpeg/aco | 1.80 +/- 3.03 (n=5) |
| task/reacher_hard/defocus_blur/aco | 0.80 +/- 1.30 (n=5) |
| task/reacher_hard/frost/aco | 7.80 +/- 15.82 (n=5) |
| task/reacher_hard/occlusion_patch/aco | 7.40 +/- 9.42 (n=5) |
| task/reacher_hard/saturation/aco | 10.20 +/- 22.81 (n=5) |
| task/reacher_hard/shadow/aco | 93.00 +/- 201.30 (n=5) |
| task/reacher_hard/shot_noise/aco | 0.80 +/- 1.79 (n=5) |
| markov/smfa | 646.41 +/- 339.97 (n=100) |
| single/all/smfa | 655.96 +/- 375.02 (n=650) |
| single/original7/smfa | 670.60 +/- 369.91 (n=350) |
| single/added6/smfa | 638.87 +/- 380.79 (n=300) |
| single/rain/smfa | 722.80 +/- 347.02 (n=50) |
| single/fog/smfa | 723.20 +/- 347.15 (n=50) |
| single/snow/smfa | 743.47 +/- 333.88 (n=50) |
| single/motion_blur/smfa | 434.88 +/- 395.35 (n=50) |
| single/gaussian_noise/smfa | 725.11 +/- 348.49 (n=50) |
| single/low_light/smfa | 731.76 +/- 339.38 (n=50) |
| single/jpeg/smfa | 612.98 +/- 389.00 (n=50) |
| single/defocus_blur/smfa | 442.11 +/- 412.81 (n=50) |
| single/frost/smfa | 726.32 +/- 348.65 (n=50) |
| single/occlusion_patch/smfa | 502.05 +/- 386.80 (n=50) |
| single/saturation/smfa | 745.60 +/- 331.14 (n=50) |
| single/shadow/smfa | 693.53 +/- 354.33 (n=50) |
| single/shot_noise/smfa | 723.63 +/- 345.83 (n=50) |
| task/walker_walk/single_mean/smfa | 903.69 +/- 159.11 (n=65) |
| task/walker_walk/markov/smfa | 909.20 +/- 59.05 (n=10) |
| task/walker_walk/rain/smfa | 961.50 +/- 6.98 (n=5) |
| task/walker_walk/fog/smfa | 958.13 +/- 4.39 (n=5) |
| task/walker_walk/snow/smfa | 957.76 +/- 8.99 (n=5) |
| task/walker_walk/motion_blur/smfa | 800.51 +/- 68.38 (n=5) |
| task/walker_walk/gaussian_noise/smfa | 951.77 +/- 16.84 (n=5) |
| task/walker_walk/low_light/smfa | 958.42 +/- 17.97 (n=5) |
| task/walker_walk/jpeg/smfa | 958.09 +/- 10.88 (n=5) |
| task/walker_walk/defocus_blur/smfa | 905.86 +/- 67.97 (n=5) |
| task/walker_walk/frost/smfa | 960.63 +/- 8.79 (n=5) |
| task/walker_walk/occlusion_patch/smfa | 457.24 +/- 307.39 (n=5) |
| task/walker_walk/saturation/smfa | 958.40 +/- 6.71 (n=5) |
| task/walker_walk/shadow/smfa | 966.04 +/- 7.98 (n=5) |
| task/walker_walk/shot_noise/smfa | 953.63 +/- 10.79 (n=5) |
| task/walker_run/single_mean/smfa | 635.47 +/- 165.38 (n=65) |
| task/walker_run/markov/smfa | 586.60 +/- 127.23 (n=10) |
| task/walker_run/rain/smfa | 726.15 +/- 38.83 (n=5) |
| task/walker_run/fog/smfa | 700.99 +/- 78.51 (n=5) |
| task/walker_run/snow/smfa | 742.06 +/- 18.51 (n=5) |
| task/walker_run/motion_blur/smfa | 344.67 +/- 18.27 (n=5) |
| task/walker_run/gaussian_noise/smfa | 738.63 +/- 21.50 (n=5) |
| task/walker_run/low_light/smfa | 706.54 +/- 58.56 (n=5) |
| task/walker_run/jpeg/smfa | 681.27 +/- 55.54 (n=5) |
| task/walker_run/defocus_blur/smfa | 504.43 +/- 43.77 (n=5) |
| task/walker_run/frost/smfa | 735.45 +/- 25.98 (n=5) |
| task/walker_run/occlusion_patch/smfa | 245.80 +/- 80.33 (n=5) |
| task/walker_run/saturation/smfa | 722.57 +/- 31.76 (n=5) |
| task/walker_run/shadow/smfa | 672.63 +/- 75.41 (n=5) |
| task/walker_run/shot_noise/smfa | 739.97 +/- 12.13 (n=5) |
| task/walker_stand/single_mean/smfa | 963.16 +/- 23.28 (n=65) |
| task/walker_stand/markov/smfa | 961.99 +/- 30.07 (n=10) |
| task/walker_stand/rain/smfa | 969.84 +/- 18.32 (n=5) |
| task/walker_stand/fog/smfa | 961.88 +/- 18.29 (n=5) |
| task/walker_stand/snow/smfa | 970.63 +/- 21.09 (n=5) |
| task/walker_stand/motion_blur/smfa | 948.25 +/- 43.86 (n=5) |
| task/walker_stand/gaussian_noise/smfa | 972.13 +/- 12.34 (n=5) |
| task/walker_stand/low_light/smfa | 976.77 +/- 13.90 (n=5) |
| task/walker_stand/jpeg/smfa | 964.45 +/- 25.15 (n=5) |
| task/walker_stand/defocus_blur/smfa | 953.41 +/- 24.77 (n=5) |
| task/walker_stand/frost/smfa | 972.35 +/- 14.74 (n=5) |
| task/walker_stand/occlusion_patch/smfa | 954.82 +/- 34.16 (n=5) |
| task/walker_stand/saturation/smfa | 948.73 +/- 20.91 (n=5) |
| task/walker_stand/shadow/smfa | 967.01 +/- 21.38 (n=5) |
| task/walker_stand/shot_noise/smfa | 960.82 +/- 20.70 (n=5) |
| task/hopper_stand/single_mean/smfa | 593.15 +/- 394.34 (n=65) |
| task/hopper_stand/markov/smfa | 565.91 +/- 212.21 (n=10) |
| task/hopper_stand/rain/smfa | 707.58 +/- 396.79 (n=5) |
| task/hopper_stand/fog/smfa | 731.43 +/- 408.92 (n=5) |
| task/hopper_stand/snow/smfa | 715.24 +/- 400.19 (n=5) |
| task/hopper_stand/motion_blur/smfa | 189.75 +/- 152.49 (n=5) |
| task/hopper_stand/gaussian_noise/smfa | 728.88 +/- 407.48 (n=5) |
| task/hopper_stand/low_light/smfa | 717.64 +/- 401.18 (n=5) |
| task/hopper_stand/jpeg/smfa | 515.84 +/- 305.25 (n=5) |
| task/hopper_stand/defocus_blur/smfa | 134.07 +/- 97.36 (n=5) |
| task/hopper_stand/frost/smfa | 730.63 +/- 408.50 (n=5) |
| task/hopper_stand/occlusion_patch/smfa | 410.88 +/- 463.95 (n=5) |
| task/hopper_stand/saturation/smfa | 732.14 +/- 409.35 (n=5) |
| task/hopper_stand/shadow/smfa | 689.63 +/- 387.65 (n=5) |
| task/hopper_stand/shot_noise/smfa | 707.25 +/- 396.94 (n=5) |
| task/quadruped_run/single_mean/smfa | 504.52 +/- 78.22 (n=65) |
| task/quadruped_run/markov/smfa | 492.91 +/- 49.30 (n=10) |
| task/quadruped_run/rain/smfa | 510.50 +/- 30.86 (n=5) |
| task/quadruped_run/fog/smfa | 526.20 +/- 41.39 (n=5) |
| task/quadruped_run/snow/smfa | 496.79 +/- 50.25 (n=5) |
| task/quadruped_run/motion_blur/smfa | 436.21 +/- 237.59 (n=5) |
| task/quadruped_run/gaussian_noise/smfa | 498.66 +/- 44.91 (n=5) |
| task/quadruped_run/low_light/smfa | 511.08 +/- 66.48 (n=5) |
| task/quadruped_run/jpeg/smfa | 540.71 +/- 22.24 (n=5) |
| task/quadruped_run/defocus_blur/smfa | 521.12 +/- 37.27 (n=5) |
| task/quadruped_run/frost/smfa | 505.58 +/- 30.26 (n=5) |
| task/quadruped_run/occlusion_patch/smfa | 440.41 +/- 66.88 (n=5) |
| task/quadruped_run/saturation/smfa | 534.32 +/- 34.12 (n=5) |
| task/quadruped_run/shadow/smfa | 517.53 +/- 57.27 (n=5) |
| task/quadruped_run/shot_noise/smfa | 519.66 +/- 52.22 (n=5) |
| task/finger_turn_hard/single_mean/smfa | 541.54 +/- 458.84 (n=65) |
| task/finger_turn_hard/markov/smfa | 622.00 +/- 432.45 (n=10) |
| task/finger_turn_hard/rain/smfa | 560.60 +/- 511.99 (n=5) |
| task/finger_turn_hard/fog/smfa | 563.20 +/- 514.22 (n=5) |
| task/finger_turn_hard/snow/smfa | 758.20 +/- 424.16 (n=5) |
| task/finger_turn_hard/motion_blur/smfa | 102.20 +/- 139.32 (n=5) |
| task/finger_turn_hard/gaussian_noise/smfa | 560.80 +/- 512.14 (n=5) |
| task/finger_turn_hard/low_light/smfa | 758.00 +/- 424.37 (n=5) |
| task/finger_turn_hard/jpeg/smfa | 379.80 +/- 515.51 (n=5) |
| task/finger_turn_hard/defocus_blur/smfa | 22.40 +/- 29.53 (n=5) |
| task/finger_turn_hard/frost/smfa | 561.00 +/- 512.30 (n=5) |
| task/finger_turn_hard/occlusion_patch/smfa | 689.00 +/- 407.62 (n=5) |
| task/finger_turn_hard/saturation/smfa | 760.40 +/- 425.68 (n=5) |
| task/finger_turn_hard/shadow/smfa | 760.80 +/- 425.62 (n=5) |
| task/finger_turn_hard/shot_noise/smfa | 563.60 +/- 514.59 (n=5) |
| task/cartpole_swingup_sparse/single_mean/smfa | 584.83 +/- 344.77 (n=65) |
| task/cartpole_swingup_sparse/markov/smfa | 375.30 +/- 134.87 (n=10) |
| task/cartpole_swingup_sparse/rain/smfa | 823.60 +/- 9.04 (n=5) |
| task/cartpole_swingup_sparse/fog/smfa | 821.60 +/- 10.64 (n=5) |
| task/cartpole_swingup_sparse/snow/smfa | 826.00 +/- 8.40 (n=5) |
| task/cartpole_swingup_sparse/motion_blur/smfa | 13.00 +/- 8.80 (n=5) |
| task/cartpole_swingup_sparse/gaussian_noise/smfa | 832.20 +/- 3.56 (n=5) |
| task/cartpole_swingup_sparse/low_light/smfa | 717.60 +/- 240.95 (n=5) |
| task/cartpole_swingup_sparse/jpeg/smfa | 128.20 +/- 48.26 (n=5) |
| task/cartpole_swingup_sparse/defocus_blur/smfa | 11.00 +/- 11.92 (n=5) |
| task/cartpole_swingup_sparse/frost/smfa | 829.80 +/- 4.60 (n=5) |
| task/cartpole_swingup_sparse/occlusion_patch/smfa | 551.20 +/- 337.89 (n=5) |
| task/cartpole_swingup_sparse/saturation/smfa | 831.80 +/- 1.48 (n=5) |
| task/cartpole_swingup_sparse/shadow/smfa | 393.00 +/- 250.90 (n=5) |
| task/cartpole_swingup_sparse/shot_noise/smfa | 823.80 +/- 16.41 (n=5) |
| task/cup_catch/single_mean/smfa | 931.32 +/- 206.76 (n=65) |
| task/cup_catch/markov/smfa | 971.70 +/- 8.67 (n=10) |
| task/cup_catch/rain/smfa | 977.00 +/- 12.17 (n=5) |
| task/cup_catch/fog/smfa | 976.80 +/- 10.73 (n=5) |
| task/cup_catch/snow/smfa | 977.40 +/- 11.17 (n=5) |
| task/cup_catch/motion_blur/smfa | 780.40 +/- 436.36 (n=5) |
| task/cup_catch/gaussian_noise/smfa | 977.60 +/- 11.80 (n=5) |
| task/cup_catch/low_light/smfa | 977.20 +/- 11.28 (n=5) |
| task/cup_catch/jpeg/smfa | 976.20 +/- 11.17 (n=5) |
| task/cup_catch/defocus_blur/smfa | 578.20 +/- 528.09 (n=5) |
| task/cup_catch/frost/smfa | 977.40 +/- 11.57 (n=5) |
| task/cup_catch/occlusion_patch/smfa | 976.80 +/- 11.86 (n=5) |
| task/cup_catch/saturation/smfa | 977.20 +/- 11.69 (n=5) |
| task/cup_catch/shadow/smfa | 977.40 +/- 11.57 (n=5) |
| task/cup_catch/shot_noise/smfa | 977.60 +/- 11.80 (n=5) |
| task/reacher_easy/single_mean/smfa | 894.63 +/- 269.00 (n=65) |
| task/reacher_easy/markov/smfa | 972.10 +/- 16.29 (n=10) |
| task/reacher_easy/rain/smfa | 982.40 +/- 14.84 (n=5) |
| task/reacher_easy/fog/smfa | 982.80 +/- 14.17 (n=5) |
| task/reacher_easy/snow/smfa | 981.60 +/- 16.26 (n=5) |
| task/reacher_easy/motion_blur/smfa | 733.20 +/- 423.38 (n=5) |
| task/reacher_easy/gaussian_noise/smfa | 981.40 +/- 16.62 (n=5) |
| task/reacher_easy/low_light/smfa | 982.00 +/- 15.02 (n=5) |
| task/reacher_easy/jpeg/smfa | 981.40 +/- 16.35 (n=5) |
| task/reacher_easy/defocus_blur/smfa | 788.80 +/- 441.05 (n=5) |
| task/reacher_easy/frost/smfa | 981.80 +/- 15.64 (n=5) |
| task/reacher_easy/occlusion_patch/smfa | 288.80 +/- 425.38 (n=5) |
| task/reacher_easy/saturation/smfa | 982.20 +/- 15.19 (n=5) |
| task/reacher_easy/shadow/smfa | 981.60 +/- 16.26 (n=5) |
| task/reacher_easy/shot_noise/smfa | 982.20 +/- 15.19 (n=5) |
| task/reacher_hard/single_mean/smfa | 7.25 +/- 14.42 (n=65) |
| task/reacher_hard/markov/smfa | 6.40 +/- 11.08 (n=10) |
| task/reacher_hard/rain/smfa | 8.80 +/- 17.53 (n=5) |
| task/reacher_hard/fog/smfa | 9.00 +/- 16.85 (n=5) |
| task/reacher_hard/snow/smfa | 9.00 +/- 16.85 (n=5) |
| task/reacher_hard/motion_blur/smfa | 0.60 +/- 0.89 (n=5) |
| task/reacher_hard/gaussian_noise/smfa | 9.00 +/- 17.97 (n=5) |
| task/reacher_hard/low_light/smfa | 12.40 +/- 20.51 (n=5) |
| task/reacher_hard/jpeg/smfa | 3.80 +/- 8.50 (n=5) |
| task/reacher_hard/defocus_blur/smfa | 1.80 +/- 1.64 (n=5) |
| task/reacher_hard/frost/smfa | 8.60 +/- 17.08 (n=5) |
| task/reacher_hard/occlusion_patch/smfa | 5.60 +/- 12.52 (n=5) |
| task/reacher_hard/saturation/smfa | 8.20 +/- 18.34 (n=5) |
| task/reacher_hard/shadow/smfa | 9.60 +/- 19.31 (n=5) |
| task/reacher_hard/shot_noise/smfa | 7.80 +/- 17.44 (n=5) |
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
| walker_walk | markov | - | aco | 400000 | 560.481292 |
| walker_walk | markov | - | aco | 400001 | 455.900677 |
| walker_walk | markov | - | aco | 400002 | 340.703006 |
| walker_walk | markov | - | aco | 400003 | 430.814535 |
| walker_walk | markov | - | aco | 400004 | 581.015837 |
| walker_walk | markov | - | aco | 400005 | 624.674219 |
| walker_walk | markov | - | aco | 400006 | 505.558829 |
| walker_walk | markov | - | aco | 400007 | 381.202796 |
| walker_walk | markov | - | aco | 400008 | 464.743089 |
| walker_walk | markov | - | aco | 400009 | 471.458005 |
| walker_walk | single | rain | aco | 400000 | 881.244919 |
| walker_walk | single | rain | aco | 400001 | 945.182553 |
| walker_walk | single | rain | aco | 400002 | 946.543056 |
| walker_walk | single | rain | aco | 400003 | 949.899838 |
| walker_walk | single | rain | aco | 400004 | 955.408900 |
| walker_walk | single | fog | aco | 400000 | 930.416424 |
| walker_walk | single | fog | aco | 400001 | 952.184911 |
| walker_walk | single | fog | aco | 400002 | 953.222136 |
| walker_walk | single | fog | aco | 400003 | 966.780589 |
| walker_walk | single | fog | aco | 400004 | 954.680449 |
| walker_walk | single | snow | aco | 400000 | 972.225549 |
| walker_walk | single | snow | aco | 400001 | 952.882839 |
| walker_walk | single | snow | aco | 400002 | 951.519490 |
| walker_walk | single | snow | aco | 400003 | 951.473196 |
| walker_walk | single | snow | aco | 400004 | 957.480068 |
| walker_walk | single | motion_blur | aco | 400000 | 328.782352 |
| walker_walk | single | motion_blur | aco | 400001 | 365.141768 |
| walker_walk | single | motion_blur | aco | 400002 | 318.000828 |
| walker_walk | single | motion_blur | aco | 400003 | 454.080460 |
| walker_walk | single | motion_blur | aco | 400004 | 197.207195 |
| walker_walk | single | gaussian_noise | aco | 400000 | 44.507619 |
| walker_walk | single | gaussian_noise | aco | 400001 | 53.143884 |
| walker_walk | single | gaussian_noise | aco | 400002 | 31.760236 |
| walker_walk | single | gaussian_noise | aco | 400003 | 32.970632 |
| walker_walk | single | gaussian_noise | aco | 400004 | 40.418440 |
| walker_walk | single | low_light | aco | 400000 | 60.639050 |
| walker_walk | single | low_light | aco | 400001 | 28.915581 |
| walker_walk | single | low_light | aco | 400002 | 43.496974 |
| walker_walk | single | low_light | aco | 400003 | 49.917356 |
| walker_walk | single | low_light | aco | 400004 | 54.778091 |
| walker_walk | single | jpeg | aco | 400000 | 343.643490 |
| walker_walk | single | jpeg | aco | 400001 | 506.212020 |
| walker_walk | single | jpeg | aco | 400002 | 611.277498 |
| walker_walk | single | jpeg | aco | 400003 | 564.827940 |
| walker_walk | single | jpeg | aco | 400004 | 517.805543 |
| walker_walk | single | defocus_blur | aco | 400000 | 449.014577 |
| walker_walk | single | defocus_blur | aco | 400001 | 580.316206 |
| walker_walk | single | defocus_blur | aco | 400002 | 348.143504 |
| walker_walk | single | defocus_blur | aco | 400003 | 363.895733 |
| walker_walk | single | defocus_blur | aco | 400004 | 346.081401 |
| walker_walk | single | frost | aco | 400000 | 964.683683 |
| walker_walk | single | frost | aco | 400001 | 958.135176 |
| walker_walk | single | frost | aco | 400002 | 958.198358 |
| walker_walk | single | frost | aco | 400003 | 959.835385 |
| walker_walk | single | frost | aco | 400004 | 965.075782 |
| walker_walk | single | occlusion_patch | aco | 400000 | 663.847963 |
| walker_walk | single | occlusion_patch | aco | 400001 | 847.949826 |
| walker_walk | single | occlusion_patch | aco | 400002 | 917.237594 |
| walker_walk | single | occlusion_patch | aco | 400003 | 728.716094 |
| walker_walk | single | occlusion_patch | aco | 400004 | 568.234654 |
| walker_walk | single | saturation | aco | 400000 | 974.082762 |
| walker_walk | single | saturation | aco | 400001 | 941.680553 |
| walker_walk | single | saturation | aco | 400002 | 963.409735 |
| walker_walk | single | saturation | aco | 400003 | 970.324920 |
| walker_walk | single | saturation | aco | 400004 | 957.928407 |
| walker_walk | single | shadow | aco | 400000 | 700.320069 |
| walker_walk | single | shadow | aco | 400001 | 481.850492 |
| walker_walk | single | shadow | aco | 400002 | 927.122444 |
| walker_walk | single | shadow | aco | 400003 | 877.054817 |
| walker_walk | single | shadow | aco | 400004 | 939.265683 |
| walker_walk | single | shot_noise | aco | 400000 | 46.632779 |
| walker_walk | single | shot_noise | aco | 400001 | 43.956350 |
| walker_walk | single | shot_noise | aco | 400002 | 29.437441 |
| walker_walk | single | shot_noise | aco | 400003 | 61.207091 |
| walker_walk | single | shot_noise | aco | 400004 | 40.711524 |
| walker_walk | markov | - | smfa | 400000 | 931.366433 |
| walker_walk | markov | - | smfa | 400001 | 802.492354 |
| walker_walk | markov | - | smfa | 400002 | 890.815644 |
| walker_walk | markov | - | smfa | 400003 | 927.682635 |
| walker_walk | markov | - | smfa | 400004 | 804.843011 |
| walker_walk | markov | - | smfa | 400005 | 947.150345 |
| walker_walk | markov | - | smfa | 400006 | 968.533020 |
| walker_walk | markov | - | smfa | 400007 | 935.386082 |
| walker_walk | markov | - | smfa | 400008 | 950.634745 |
| walker_walk | markov | - | smfa | 400009 | 933.134666 |
| walker_walk | single | rain | smfa | 400000 | 954.471995 |
| walker_walk | single | rain | smfa | 400001 | 955.712474 |
| walker_walk | single | rain | smfa | 400002 | 971.256811 |
| walker_walk | single | rain | smfa | 400003 | 965.503635 |
| walker_walk | single | rain | smfa | 400004 | 960.544131 |
| walker_walk | single | fog | smfa | 400000 | 953.135381 |
| walker_walk | single | fog | smfa | 400001 | 958.616693 |
| walker_walk | single | fog | smfa | 400002 | 956.321162 |
| walker_walk | single | fog | smfa | 400003 | 965.067132 |
| walker_walk | single | fog | smfa | 400004 | 957.522366 |
| walker_walk | single | snow | smfa | 400000 | 954.366135 |
| walker_walk | single | snow | smfa | 400001 | 960.999948 |
| walker_walk | single | snow | smfa | 400002 | 944.241314 |
| walker_walk | single | snow | smfa | 400003 | 968.132223 |
| walker_walk | single | snow | smfa | 400004 | 961.082710 |
| walker_walk | single | motion_blur | smfa | 400000 | 686.940245 |
| walker_walk | single | motion_blur | smfa | 400001 | 832.447542 |
| walker_walk | single | motion_blur | smfa | 400002 | 865.585895 |
| walker_walk | single | motion_blur | smfa | 400003 | 823.131002 |
| walker_walk | single | motion_blur | smfa | 400004 | 794.438716 |
| walker_walk | single | gaussian_noise | smfa | 400000 | 961.655523 |
| walker_walk | single | gaussian_noise | smfa | 400001 | 958.929998 |
| walker_walk | single | gaussian_noise | smfa | 400002 | 932.170541 |
| walker_walk | single | gaussian_noise | smfa | 400003 | 970.347733 |
| walker_walk | single | gaussian_noise | smfa | 400004 | 935.766815 |
| walker_walk | single | low_light | smfa | 400000 | 969.032344 |
| walker_walk | single | low_light | smfa | 400001 | 926.812473 |
| walker_walk | single | low_light | smfa | 400002 | 967.190377 |
| walker_walk | single | low_light | smfa | 400003 | 968.344409 |
| walker_walk | single | low_light | smfa | 400004 | 960.727697 |
| walker_walk | single | jpeg | smfa | 400000 | 940.310742 |
| walker_walk | single | jpeg | smfa | 400001 | 958.108594 |
| walker_walk | single | jpeg | smfa | 400002 | 961.449331 |
| walker_walk | single | jpeg | smfa | 400003 | 969.908014 |
| walker_walk | single | jpeg | smfa | 400004 | 960.688018 |
| walker_walk | single | defocus_blur | smfa | 400000 | 972.522080 |
| walker_walk | single | defocus_blur | smfa | 400001 | 919.808718 |
| walker_walk | single | defocus_blur | smfa | 400002 | 930.533082 |
| walker_walk | single | defocus_blur | smfa | 400003 | 915.244921 |
| walker_walk | single | defocus_blur | smfa | 400004 | 791.206134 |
| walker_walk | single | frost | smfa | 400000 | 967.647554 |
| walker_walk | single | frost | smfa | 400001 | 951.613030 |
| walker_walk | single | frost | smfa | 400002 | 952.045707 |
| walker_walk | single | frost | smfa | 400003 | 970.872239 |
| walker_walk | single | frost | smfa | 400004 | 960.958866 |
| walker_walk | single | occlusion_patch | smfa | 400000 | 204.377203 |
| walker_walk | single | occlusion_patch | smfa | 400001 | 840.831755 |
| walker_walk | single | occlusion_patch | smfa | 400002 | 740.948143 |
| walker_walk | single | occlusion_patch | smfa | 400003 | 265.792092 |
| walker_walk | single | occlusion_patch | smfa | 400004 | 234.259105 |
| walker_walk | single | saturation | smfa | 400000 | 952.558118 |
| walker_walk | single | saturation | smfa | 400001 | 952.938058 |
| walker_walk | single | saturation | smfa | 400002 | 958.652693 |
| walker_walk | single | saturation | smfa | 400003 | 969.167444 |
| walker_walk | single | saturation | smfa | 400004 | 958.702104 |
| walker_walk | single | shadow | smfa | 400000 | 975.042308 |
| walker_walk | single | shadow | smfa | 400001 | 954.088447 |
| walker_walk | single | shadow | smfa | 400002 | 967.490267 |
| walker_walk | single | shadow | smfa | 400003 | 970.519750 |
| walker_walk | single | shadow | smfa | 400004 | 963.054059 |
| walker_walk | single | shot_noise | smfa | 400000 | 951.138301 |
| walker_walk | single | shot_noise | smfa | 400001 | 960.053621 |
| walker_walk | single | shot_noise | smfa | 400002 | 963.499465 |
| walker_walk | single | shot_noise | smfa | 400003 | 936.106600 |
| walker_walk | single | shot_noise | smfa | 400004 | 957.375260 |
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
| walker_run | markov | - | aco | 401000 | 147.881231 |
| walker_run | markov | - | aco | 401001 | 225.699907 |
| walker_run | markov | - | aco | 401002 | 162.299178 |
| walker_run | markov | - | aco | 401003 | 244.532964 |
| walker_run | markov | - | aco | 401004 | 265.367877 |
| walker_run | markov | - | aco | 401005 | 121.009913 |
| walker_run | markov | - | aco | 401006 | 428.884083 |
| walker_run | markov | - | aco | 401007 | 191.065061 |
| walker_run | markov | - | aco | 401008 | 237.434820 |
| walker_run | markov | - | aco | 401009 | 122.845509 |
| walker_run | single | rain | aco | 401000 | 532.674156 |
| walker_run | single | rain | aco | 401001 | 529.560343 |
| walker_run | single | rain | aco | 401002 | 437.072154 |
| walker_run | single | rain | aco | 401003 | 520.308503 |
| walker_run | single | rain | aco | 401004 | 556.248000 |
| walker_run | single | fog | aco | 401000 | 700.623168 |
| walker_run | single | fog | aco | 401001 | 668.197970 |
| walker_run | single | fog | aco | 401002 | 628.713371 |
| walker_run | single | fog | aco | 401003 | 429.383133 |
| walker_run | single | fog | aco | 401004 | 659.296984 |
| walker_run | single | snow | aco | 401000 | 513.957003 |
| walker_run | single | snow | aco | 401001 | 579.301262 |
| walker_run | single | snow | aco | 401002 | 399.367749 |
| walker_run | single | snow | aco | 401003 | 509.941647 |
| walker_run | single | snow | aco | 401004 | 543.282299 |
| walker_run | single | motion_blur | aco | 401000 | 129.257124 |
| walker_run | single | motion_blur | aco | 401001 | 185.833315 |
| walker_run | single | motion_blur | aco | 401002 | 191.656201 |
| walker_run | single | motion_blur | aco | 401003 | 162.767161 |
| walker_run | single | motion_blur | aco | 401004 | 201.435046 |
| walker_run | single | gaussian_noise | aco | 401000 | 45.115863 |
| walker_run | single | gaussian_noise | aco | 401001 | 47.999832 |
| walker_run | single | gaussian_noise | aco | 401002 | 27.281252 |
| walker_run | single | gaussian_noise | aco | 401003 | 63.034915 |
| walker_run | single | gaussian_noise | aco | 401004 | 47.680863 |
| walker_run | single | low_light | aco | 401000 | 10.676486 |
| walker_run | single | low_light | aco | 401001 | 38.691188 |
| walker_run | single | low_light | aco | 401002 | 10.353147 |
| walker_run | single | low_light | aco | 401003 | 23.337455 |
| walker_run | single | low_light | aco | 401004 | 23.857775 |
| walker_run | single | jpeg | aco | 401000 | 165.901433 |
| walker_run | single | jpeg | aco | 401001 | 203.664323 |
| walker_run | single | jpeg | aco | 401002 | 202.969599 |
| walker_run | single | jpeg | aco | 401003 | 159.883091 |
| walker_run | single | jpeg | aco | 401004 | 138.306001 |
| walker_run | single | defocus_blur | aco | 401000 | 97.826094 |
| walker_run | single | defocus_blur | aco | 401001 | 158.213434 |
| walker_run | single | defocus_blur | aco | 401002 | 140.535885 |
| walker_run | single | defocus_blur | aco | 401003 | 170.520958 |
| walker_run | single | defocus_blur | aco | 401004 | 166.178800 |
| walker_run | single | frost | aco | 401000 | 730.396740 |
| walker_run | single | frost | aco | 401001 | 550.817361 |
| walker_run | single | frost | aco | 401002 | 710.890374 |
| walker_run | single | frost | aco | 401003 | 741.732639 |
| walker_run | single | frost | aco | 401004 | 731.234214 |
| walker_run | single | occlusion_patch | aco | 401000 | 280.811069 |
| walker_run | single | occlusion_patch | aco | 401001 | 249.800536 |
| walker_run | single | occlusion_patch | aco | 401002 | 190.214678 |
| walker_run | single | occlusion_patch | aco | 401003 | 255.069696 |
| walker_run | single | occlusion_patch | aco | 401004 | 324.986224 |
| walker_run | single | saturation | aco | 401000 | 474.960928 |
| walker_run | single | saturation | aco | 401001 | 555.189153 |
| walker_run | single | saturation | aco | 401002 | 548.060950 |
| walker_run | single | saturation | aco | 401003 | 503.282264 |
| walker_run | single | saturation | aco | 401004 | 415.200664 |
| walker_run | single | shadow | aco | 401000 | 506.948745 |
| walker_run | single | shadow | aco | 401001 | 494.891487 |
| walker_run | single | shadow | aco | 401002 | 447.849449 |
| walker_run | single | shadow | aco | 401003 | 657.889000 |
| walker_run | single | shadow | aco | 401004 | 197.528574 |
| walker_run | single | shot_noise | aco | 401000 | 27.940167 |
| walker_run | single | shot_noise | aco | 401001 | 55.018987 |
| walker_run | single | shot_noise | aco | 401002 | 39.273702 |
| walker_run | single | shot_noise | aco | 401003 | 44.204207 |
| walker_run | single | shot_noise | aco | 401004 | 49.707632 |
| walker_run | markov | - | smfa | 401000 | 543.063597 |
| walker_run | markov | - | smfa | 401001 | 507.544708 |
| walker_run | markov | - | smfa | 401002 | 322.529906 |
| walker_run | markov | - | smfa | 401003 | 739.161120 |
| walker_run | markov | - | smfa | 401004 | 563.864330 |
| walker_run | markov | - | smfa | 401005 | 569.041107 |
| walker_run | markov | - | smfa | 401006 | 534.906158 |
| walker_run | markov | - | smfa | 401007 | 639.115761 |
| walker_run | markov | - | smfa | 401008 | 744.154819 |
| walker_run | markov | - | smfa | 401009 | 702.574934 |
| walker_run | single | rain | smfa | 401000 | 689.105889 |
| walker_run | single | rain | smfa | 401001 | 760.099187 |
| walker_run | single | rain | smfa | 401002 | 679.008861 |
| walker_run | single | rain | smfa | 401003 | 748.056843 |
| walker_run | single | rain | smfa | 401004 | 754.485656 |
| walker_run | single | fog | smfa | 401000 | 561.727258 |
| walker_run | single | fog | smfa | 401001 | 744.459745 |
| walker_run | single | fog | smfa | 401002 | 728.866294 |
| walker_run | single | fog | smfa | 401003 | 747.004067 |
| walker_run | single | fog | smfa | 401004 | 722.904347 |
| walker_run | single | snow | smfa | 401000 | 714.026403 |
| walker_run | single | snow | smfa | 401001 | 750.729323 |
| walker_run | single | snow | smfa | 401002 | 736.782422 |
| walker_run | single | snow | smfa | 401003 | 763.803928 |
| walker_run | single | snow | smfa | 401004 | 744.974715 |
| walker_run | single | motion_blur | smfa | 401000 | 343.951219 |
| walker_run | single | motion_blur | smfa | 401001 | 370.881614 |
| walker_run | single | motion_blur | smfa | 401002 | 344.276840 |
| walker_run | single | motion_blur | smfa | 401003 | 345.032372 |
| walker_run | single | motion_blur | smfa | 401004 | 319.232494 |
| walker_run | single | gaussian_noise | smfa | 401000 | 706.850976 |
| walker_run | single | gaussian_noise | smfa | 401001 | 759.079777 |
| walker_run | single | gaussian_noise | smfa | 401002 | 726.547249 |
| walker_run | single | gaussian_noise | smfa | 401003 | 749.852726 |
| walker_run | single | gaussian_noise | smfa | 401004 | 750.819569 |
| walker_run | single | low_light | smfa | 401000 | 611.194280 |
| walker_run | single | low_light | smfa | 401001 | 739.412107 |
| walker_run | single | low_light | smfa | 401002 | 690.031121 |
| walker_run | single | low_light | smfa | 401003 | 754.855541 |
| walker_run | single | low_light | smfa | 401004 | 737.194701 |
| walker_run | single | jpeg | smfa | 401000 | 714.298114 |
| walker_run | single | jpeg | smfa | 401001 | 708.654761 |
| walker_run | single | jpeg | smfa | 401002 | 588.493248 |
| walker_run | single | jpeg | smfa | 401003 | 723.590907 |
| walker_run | single | jpeg | smfa | 401004 | 671.336050 |
| walker_run | single | defocus_blur | smfa | 401000 | 537.528483 |
| walker_run | single | defocus_blur | smfa | 401001 | 495.873420 |
| walker_run | single | defocus_blur | smfa | 401002 | 480.198930 |
| walker_run | single | defocus_blur | smfa | 401003 | 449.912880 |
| walker_run | single | defocus_blur | smfa | 401004 | 558.619894 |
| walker_run | single | frost | smfa | 401000 | 752.120036 |
| walker_run | single | frost | smfa | 401001 | 723.454318 |
| walker_run | single | frost | smfa | 401002 | 731.942217 |
| walker_run | single | frost | smfa | 401003 | 768.514878 |
| walker_run | single | frost | smfa | 401004 | 701.202670 |
| walker_run | single | occlusion_patch | smfa | 401000 | 182.814136 |
| walker_run | single | occlusion_patch | smfa | 401001 | 259.421925 |
| walker_run | single | occlusion_patch | smfa | 401002 | 189.723901 |
| walker_run | single | occlusion_patch | smfa | 401003 | 218.015944 |
| walker_run | single | occlusion_patch | smfa | 401004 | 379.004728 |
| walker_run | single | saturation | smfa | 401000 | 697.950129 |
| walker_run | single | saturation | smfa | 401001 | 718.142534 |
| walker_run | single | saturation | smfa | 401002 | 704.799973 |
| walker_run | single | saturation | smfa | 401003 | 777.576770 |
| walker_run | single | saturation | smfa | 401004 | 714.364137 |
| walker_run | single | shadow | smfa | 401000 | 700.578506 |
| walker_run | single | shadow | smfa | 401001 | 708.321178 |
| walker_run | single | shadow | smfa | 401002 | 605.757264 |
| walker_run | single | shadow | smfa | 401003 | 764.290095 |
| walker_run | single | shadow | smfa | 401004 | 584.220479 |
| walker_run | single | shot_noise | smfa | 401000 | 745.671063 |
| walker_run | single | shot_noise | smfa | 401001 | 757.346108 |
| walker_run | single | shot_noise | smfa | 401002 | 731.611918 |
| walker_run | single | shot_noise | smfa | 401003 | 726.449390 |
| walker_run | single | shot_noise | smfa | 401004 | 738.762237 |
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
| walker_stand | markov | - | aco | 402000 | 819.611410 |
| walker_stand | markov | - | aco | 402001 | 719.222343 |
| walker_stand | markov | - | aco | 402002 | 805.763305 |
| walker_stand | markov | - | aco | 402003 | 753.038661 |
| walker_stand | markov | - | aco | 402004 | 559.439796 |
| walker_stand | markov | - | aco | 402005 | 887.958576 |
| walker_stand | markov | - | aco | 402006 | 914.568333 |
| walker_stand | markov | - | aco | 402007 | 898.354904 |
| walker_stand | markov | - | aco | 402008 | 873.939913 |
| walker_stand | markov | - | aco | 402009 | 914.796010 |
| walker_stand | single | rain | aco | 402000 | 967.044633 |
| walker_stand | single | rain | aco | 402001 | 984.477082 |
| walker_stand | single | rain | aco | 402002 | 959.266820 |
| walker_stand | single | rain | aco | 402003 | 930.550616 |
| walker_stand | single | rain | aco | 402004 | 962.862352 |
| walker_stand | single | fog | aco | 402000 | 982.361376 |
| walker_stand | single | fog | aco | 402001 | 983.500365 |
| walker_stand | single | fog | aco | 402002 | 980.891427 |
| walker_stand | single | fog | aco | 402003 | 923.668786 |
| walker_stand | single | fog | aco | 402004 | 952.884504 |
| walker_stand | single | snow | aco | 402000 | 981.631312 |
| walker_stand | single | snow | aco | 402001 | 983.883776 |
| walker_stand | single | snow | aco | 402002 | 934.888286 |
| walker_stand | single | snow | aco | 402003 | 931.275564 |
| walker_stand | single | snow | aco | 402004 | 955.071839 |
| walker_stand | single | motion_blur | aco | 402000 | 899.219009 |
| walker_stand | single | motion_blur | aco | 402001 | 752.821267 |
| walker_stand | single | motion_blur | aco | 402002 | 919.688143 |
| walker_stand | single | motion_blur | aco | 402003 | 980.332337 |
| walker_stand | single | motion_blur | aco | 402004 | 857.729929 |
| walker_stand | single | gaussian_noise | aco | 402000 | 152.756289 |
| walker_stand | single | gaussian_noise | aco | 402001 | 645.207100 |
| walker_stand | single | gaussian_noise | aco | 402002 | 500.251063 |
| walker_stand | single | gaussian_noise | aco | 402003 | 577.529440 |
| walker_stand | single | gaussian_noise | aco | 402004 | 618.834345 |
| walker_stand | single | low_light | aco | 402000 | 78.385801 |
| walker_stand | single | low_light | aco | 402001 | 286.941800 |
| walker_stand | single | low_light | aco | 402002 | 398.585541 |
| walker_stand | single | low_light | aco | 402003 | 312.184199 |
| walker_stand | single | low_light | aco | 402004 | 271.878987 |
| walker_stand | single | jpeg | aco | 402000 | 829.332250 |
| walker_stand | single | jpeg | aco | 402001 | 907.620847 |
| walker_stand | single | jpeg | aco | 402002 | 859.847704 |
| walker_stand | single | jpeg | aco | 402003 | 954.640845 |
| walker_stand | single | jpeg | aco | 402004 | 656.524097 |
| walker_stand | single | defocus_blur | aco | 402000 | 962.232665 |
| walker_stand | single | defocus_blur | aco | 402001 | 875.824667 |
| walker_stand | single | defocus_blur | aco | 402002 | 803.599422 |
| walker_stand | single | defocus_blur | aco | 402003 | 918.016894 |
| walker_stand | single | defocus_blur | aco | 402004 | 922.659059 |
| walker_stand | single | frost | aco | 402000 | 984.393566 |
| walker_stand | single | frost | aco | 402001 | 982.414821 |
| walker_stand | single | frost | aco | 402002 | 968.240345 |
| walker_stand | single | frost | aco | 402003 | 927.082602 |
| walker_stand | single | frost | aco | 402004 | 952.831891 |
| walker_stand | single | occlusion_patch | aco | 402000 | 979.947395 |
| walker_stand | single | occlusion_patch | aco | 402001 | 948.374550 |
| walker_stand | single | occlusion_patch | aco | 402002 | 977.187606 |
| walker_stand | single | occlusion_patch | aco | 402003 | 961.719025 |
| walker_stand | single | occlusion_patch | aco | 402004 | 937.208783 |
| walker_stand | single | saturation | aco | 402000 | 983.565090 |
| walker_stand | single | saturation | aco | 402001 | 949.691389 |
| walker_stand | single | saturation | aco | 402002 | 981.008636 |
| walker_stand | single | saturation | aco | 402003 | 964.140145 |
| walker_stand | single | saturation | aco | 402004 | 965.292944 |
| walker_stand | single | shadow | aco | 402000 | 941.524165 |
| walker_stand | single | shadow | aco | 402001 | 980.428599 |
| walker_stand | single | shadow | aco | 402002 | 876.802109 |
| walker_stand | single | shadow | aco | 402003 | 976.243831 |
| walker_stand | single | shadow | aco | 402004 | 946.486611 |
| walker_stand | single | shot_noise | aco | 402000 | 429.581838 |
| walker_stand | single | shot_noise | aco | 402001 | 446.384848 |
| walker_stand | single | shot_noise | aco | 402002 | 655.390227 |
| walker_stand | single | shot_noise | aco | 402003 | 440.702837 |
| walker_stand | single | shot_noise | aco | 402004 | 536.495065 |
| walker_stand | markov | - | smfa | 402000 | 980.202875 |
| walker_stand | markov | - | smfa | 402001 | 957.264511 |
| walker_stand | markov | - | smfa | 402002 | 945.158740 |
| walker_stand | markov | - | smfa | 402003 | 972.591942 |
| walker_stand | markov | - | smfa | 402004 | 972.680601 |
| walker_stand | markov | - | smfa | 402005 | 905.061972 |
| walker_stand | markov | - | smfa | 402006 | 997.851260 |
| walker_stand | markov | - | smfa | 402007 | 971.737595 |
| walker_stand | markov | - | smfa | 402008 | 922.415908 |
| walker_stand | markov | - | smfa | 402009 | 994.983536 |
| walker_stand | single | rain | smfa | 402000 | 984.271017 |
| walker_stand | single | rain | smfa | 402001 | 984.417312 |
| walker_stand | single | rain | smfa | 402002 | 947.518404 |
| walker_stand | single | rain | smfa | 402003 | 980.651624 |
| walker_stand | single | rain | smfa | 402004 | 952.318534 |
| walker_stand | single | fog | smfa | 402000 | 960.829175 |
| walker_stand | single | fog | smfa | 402001 | 972.158344 |
| walker_stand | single | fog | smfa | 402002 | 963.785422 |
| walker_stand | single | fog | smfa | 402003 | 980.434966 |
| walker_stand | single | fog | smfa | 402004 | 932.169301 |
| walker_stand | single | snow | smfa | 402000 | 933.593351 |
| walker_stand | single | snow | smfa | 402001 | 982.561904 |
| walker_stand | single | snow | smfa | 402002 | 984.024583 |
| walker_stand | single | snow | smfa | 402003 | 979.400139 |
| walker_stand | single | snow | smfa | 402004 | 973.592240 |
| walker_stand | single | motion_blur | smfa | 402000 | 980.971508 |
| walker_stand | single | motion_blur | smfa | 402001 | 972.897834 |
| walker_stand | single | motion_blur | smfa | 402002 | 981.985267 |
| walker_stand | single | motion_blur | smfa | 402003 | 921.737202 |
| walker_stand | single | motion_blur | smfa | 402004 | 883.644446 |
| walker_stand | single | gaussian_noise | smfa | 402000 | 975.446682 |
| walker_stand | single | gaussian_noise | smfa | 402001 | 984.202475 |
| walker_stand | single | gaussian_noise | smfa | 402002 | 967.296252 |
| walker_stand | single | gaussian_noise | smfa | 402003 | 980.507960 |
| walker_stand | single | gaussian_noise | smfa | 402004 | 953.185541 |
| walker_stand | single | low_light | smfa | 402000 | 984.385847 |
| walker_stand | single | low_light | smfa | 402001 | 984.156279 |
| walker_stand | single | low_light | smfa | 402002 | 982.292947 |
| walker_stand | single | low_light | smfa | 402003 | 980.996348 |
| walker_stand | single | low_light | smfa | 402004 | 952.023440 |
| walker_stand | single | jpeg | smfa | 402000 | 980.731412 |
| walker_stand | single | jpeg | smfa | 402001 | 954.198288 |
| walker_stand | single | jpeg | smfa | 402002 | 982.065191 |
| walker_stand | single | jpeg | smfa | 402003 | 980.634002 |
| walker_stand | single | jpeg | smfa | 402004 | 924.616277 |
| walker_stand | single | defocus_blur | smfa | 402000 | 939.013168 |
| walker_stand | single | defocus_blur | smfa | 402001 | 983.149965 |
| walker_stand | single | defocus_blur | smfa | 402002 | 962.614102 |
| walker_stand | single | defocus_blur | smfa | 402003 | 919.034561 |
| walker_stand | single | defocus_blur | smfa | 402004 | 963.216877 |
| walker_stand | single | frost | smfa | 402000 | 982.173698 |
| walker_stand | single | frost | smfa | 402001 | 981.260316 |
| walker_stand | single | frost | smfa | 402002 | 947.297561 |
| walker_stand | single | frost | smfa | 402003 | 980.273560 |
| walker_stand | single | frost | smfa | 402004 | 970.765025 |
| walker_stand | single | occlusion_patch | smfa | 402000 | 982.985023 |
| walker_stand | single | occlusion_patch | smfa | 402001 | 954.354948 |
| walker_stand | single | occlusion_patch | smfa | 402002 | 981.763287 |
| walker_stand | single | occlusion_patch | smfa | 402003 | 956.260009 |
| walker_stand | single | occlusion_patch | smfa | 402004 | 898.717784 |
| walker_stand | single | saturation | smfa | 402000 | 962.731387 |
| walker_stand | single | saturation | smfa | 402001 | 918.230684 |
| walker_stand | single | saturation | smfa | 402002 | 946.635016 |
| walker_stand | single | saturation | smfa | 402003 | 943.105950 |
| walker_stand | single | saturation | smfa | 402004 | 972.946315 |
| walker_stand | single | shadow | smfa | 402000 | 982.095726 |
| walker_stand | single | shadow | smfa | 402001 | 982.749476 |
| walker_stand | single | shadow | smfa | 402002 | 982.881557 |
| walker_stand | single | shadow | smfa | 402003 | 946.104248 |
| walker_stand | single | shadow | smfa | 402004 | 941.243118 |
| walker_stand | single | shot_noise | smfa | 402000 | 939.437816 |
| walker_stand | single | shot_noise | smfa | 402001 | 982.819654 |
| walker_stand | single | shot_noise | smfa | 402002 | 982.520377 |
| walker_stand | single | shot_noise | smfa | 402003 | 944.500701 |
| walker_stand | single | shot_noise | smfa | 402004 | 954.806235 |
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
| hopper_stand | markov | - | aco | 403000 | 439.766393 |
| hopper_stand | markov | - | aco | 403001 | 496.420526 |
| hopper_stand | markov | - | aco | 403002 | 308.531831 |
| hopper_stand | markov | - | aco | 403003 | 522.262153 |
| hopper_stand | markov | - | aco | 403004 | 0.000000 |
| hopper_stand | markov | - | aco | 403005 | 491.179366 |
| hopper_stand | markov | - | aco | 403006 | 491.875657 |
| hopper_stand | markov | - | aco | 403007 | 435.377862 |
| hopper_stand | markov | - | aco | 403008 | 609.966454 |
| hopper_stand | markov | - | aco | 403009 | 350.586969 |
| hopper_stand | single | rain | aco | 403000 | 894.615749 |
| hopper_stand | single | rain | aco | 403001 | 869.042258 |
| hopper_stand | single | rain | aco | 403002 | 896.822937 |
| hopper_stand | single | rain | aco | 403003 | 900.175973 |
| hopper_stand | single | rain | aco | 403004 | 0.000000 |
| hopper_stand | single | fog | aco | 403000 | 906.885341 |
| hopper_stand | single | fog | aco | 403001 | 839.280693 |
| hopper_stand | single | fog | aco | 403002 | 912.688475 |
| hopper_stand | single | fog | aco | 403003 | 861.955357 |
| hopper_stand | single | fog | aco | 403004 | 0.000000 |
| hopper_stand | single | snow | aco | 403000 | 893.287980 |
| hopper_stand | single | snow | aco | 403001 | 889.302437 |
| hopper_stand | single | snow | aco | 403002 | 900.721205 |
| hopper_stand | single | snow | aco | 403003 | 903.457768 |
| hopper_stand | single | snow | aco | 403004 | 0.000000 |
| hopper_stand | single | motion_blur | aco | 403000 | 264.803238 |
| hopper_stand | single | motion_blur | aco | 403001 | 457.984375 |
| hopper_stand | single | motion_blur | aco | 403002 | 247.557600 |
| hopper_stand | single | motion_blur | aco | 403003 | 282.037800 |
| hopper_stand | single | motion_blur | aco | 403004 | 0.000000 |
| hopper_stand | single | gaussian_noise | aco | 403000 | 0.000000 |
| hopper_stand | single | gaussian_noise | aco | 403001 | 77.310969 |
| hopper_stand | single | gaussian_noise | aco | 403002 | 80.530947 |
| hopper_stand | single | gaussian_noise | aco | 403003 | 12.531586 |
| hopper_stand | single | gaussian_noise | aco | 403004 | 0.000000 |
| hopper_stand | single | low_light | aco | 403000 | 0.000000 |
| hopper_stand | single | low_light | aco | 403001 | 10.488573 |
| hopper_stand | single | low_light | aco | 403002 | 0.000000 |
| hopper_stand | single | low_light | aco | 403003 | 0.000000 |
| hopper_stand | single | low_light | aco | 403004 | 0.000000 |
| hopper_stand | single | jpeg | aco | 403000 | 11.965407 |
| hopper_stand | single | jpeg | aco | 403001 | 26.129584 |
| hopper_stand | single | jpeg | aco | 403002 | 0.000000 |
| hopper_stand | single | jpeg | aco | 403003 | 0.000000 |
| hopper_stand | single | jpeg | aco | 403004 | 0.000000 |
| hopper_stand | single | defocus_blur | aco | 403000 | 316.834556 |
| hopper_stand | single | defocus_blur | aco | 403001 | 375.362558 |
| hopper_stand | single | defocus_blur | aco | 403002 | 234.335986 |
| hopper_stand | single | defocus_blur | aco | 403003 | 483.370382 |
| hopper_stand | single | defocus_blur | aco | 403004 | 0.000000 |
| hopper_stand | single | frost | aco | 403000 | 893.204271 |
| hopper_stand | single | frost | aco | 403001 | 719.193928 |
| hopper_stand | single | frost | aco | 403002 | 843.215691 |
| hopper_stand | single | frost | aco | 403003 | 892.948976 |
| hopper_stand | single | frost | aco | 403004 | 0.000000 |
| hopper_stand | single | occlusion_patch | aco | 403000 | 496.097586 |
| hopper_stand | single | occlusion_patch | aco | 403001 | 398.128889 |
| hopper_stand | single | occlusion_patch | aco | 403002 | 213.069022 |
| hopper_stand | single | occlusion_patch | aco | 403003 | 305.462039 |
| hopper_stand | single | occlusion_patch | aco | 403004 | 0.000000 |
| hopper_stand | single | saturation | aco | 403000 | 905.052136 |
| hopper_stand | single | saturation | aco | 403001 | 925.766172 |
| hopper_stand | single | saturation | aco | 403002 | 907.609127 |
| hopper_stand | single | saturation | aco | 403003 | 910.661361 |
| hopper_stand | single | saturation | aco | 403004 | 0.000000 |
| hopper_stand | single | shadow | aco | 403000 | 760.679747 |
| hopper_stand | single | shadow | aco | 403001 | 919.889626 |
| hopper_stand | single | shadow | aco | 403002 | 578.155845 |
| hopper_stand | single | shadow | aco | 403003 | 651.965880 |
| hopper_stand | single | shadow | aco | 403004 | 0.000000 |
| hopper_stand | single | shot_noise | aco | 403000 | 0.000000 |
| hopper_stand | single | shot_noise | aco | 403001 | 11.302547 |
| hopper_stand | single | shot_noise | aco | 403002 | 0.000000 |
| hopper_stand | single | shot_noise | aco | 403003 | 0.000000 |
| hopper_stand | single | shot_noise | aco | 403004 | 0.000000 |
| hopper_stand | markov | - | smfa | 403000 | 711.122670 |
| hopper_stand | markov | - | smfa | 403001 | 674.153287 |
| hopper_stand | markov | - | smfa | 403002 | 564.527961 |
| hopper_stand | markov | - | smfa | 403003 | 504.684588 |
| hopper_stand | markov | - | smfa | 403004 | 0.000000 |
| hopper_stand | markov | - | smfa | 403005 | 705.332223 |
| hopper_stand | markov | - | smfa | 403006 | 612.087071 |
| hopper_stand | markov | - | smfa | 403007 | 576.921719 |
| hopper_stand | markov | - | smfa | 403008 | 728.879611 |
| hopper_stand | markov | - | smfa | 403009 | 581.437167 |
| hopper_stand | single | rain | smfa | 403000 | 905.263868 |
| hopper_stand | single | rain | smfa | 403001 | 830.655472 |
| hopper_stand | single | rain | smfa | 403002 | 906.870207 |
| hopper_stand | single | rain | smfa | 403003 | 895.118944 |
| hopper_stand | single | rain | smfa | 403004 | 0.000000 |
| hopper_stand | single | fog | smfa | 403000 | 908.358792 |
| hopper_stand | single | fog | smfa | 403001 | 922.842675 |
| hopper_stand | single | fog | smfa | 403002 | 911.723548 |
| hopper_stand | single | fog | smfa | 403003 | 914.229223 |
| hopper_stand | single | fog | smfa | 403004 | 0.000000 |
| hopper_stand | single | snow | smfa | 403000 | 904.855340 |
| hopper_stand | single | snow | smfa | 403001 | 871.889814 |
| hopper_stand | single | snow | smfa | 403002 | 915.077125 |
| hopper_stand | single | snow | smfa | 403003 | 884.386886 |
| hopper_stand | single | snow | smfa | 403004 | 0.000000 |
| hopper_stand | single | motion_blur | smfa | 403000 | 202.989829 |
| hopper_stand | single | motion_blur | smfa | 403001 | 78.089617 |
| hopper_stand | single | motion_blur | smfa | 403002 | 296.120351 |
| hopper_stand | single | motion_blur | smfa | 403003 | 371.547439 |
| hopper_stand | single | motion_blur | smfa | 403004 | 0.000000 |
| hopper_stand | single | gaussian_noise | smfa | 403000 | 910.653170 |
| hopper_stand | single | gaussian_noise | smfa | 403001 | 916.522720 |
| hopper_stand | single | gaussian_noise | smfa | 403002 | 913.548459 |
| hopper_stand | single | gaussian_noise | smfa | 403003 | 903.676113 |
| hopper_stand | single | gaussian_noise | smfa | 403004 | 0.000000 |
| hopper_stand | single | low_light | smfa | 403000 | 893.365572 |
| hopper_stand | single | low_light | smfa | 403001 | 897.249475 |
| hopper_stand | single | low_light | smfa | 403002 | 900.598211 |
| hopper_stand | single | low_light | smfa | 403003 | 896.963348 |
| hopper_stand | single | low_light | smfa | 403004 | 0.000000 |
| hopper_stand | single | jpeg | smfa | 403000 | 693.762251 |
| hopper_stand | single | jpeg | smfa | 403001 | 487.646766 |
| hopper_stand | single | jpeg | smfa | 403002 | 758.676505 |
| hopper_stand | single | jpeg | smfa | 403003 | 639.095832 |
| hopper_stand | single | jpeg | smfa | 403004 | 0.000000 |
| hopper_stand | single | defocus_blur | smfa | 403000 | 249.282753 |
| hopper_stand | single | defocus_blur | smfa | 403001 | 151.669513 |
| hopper_stand | single | defocus_blur | smfa | 403002 | 191.089193 |
| hopper_stand | single | defocus_blur | smfa | 403003 | 78.310755 |
| hopper_stand | single | defocus_blur | smfa | 403004 | 0.000000 |
| hopper_stand | single | frost | smfa | 403000 | 909.315593 |
| hopper_stand | single | frost | smfa | 403001 | 925.579397 |
| hopper_stand | single | frost | smfa | 403002 | 907.720302 |
| hopper_stand | single | frost | smfa | 403003 | 910.556284 |
| hopper_stand | single | frost | smfa | 403004 | 0.000000 |
| hopper_stand | single | occlusion_patch | smfa | 403000 | 878.123156 |
| hopper_stand | single | occlusion_patch | smfa | 403001 | 937.727583 |
| hopper_stand | single | occlusion_patch | smfa | 403002 | 233.844886 |
| hopper_stand | single | occlusion_patch | smfa | 403003 | 4.718608 |
| hopper_stand | single | occlusion_patch | smfa | 403004 | 0.000000 |
| hopper_stand | single | saturation | smfa | 403000 | 908.733405 |
| hopper_stand | single | saturation | smfa | 403001 | 927.933865 |
| hopper_stand | single | saturation | smfa | 403002 | 913.832348 |
| hopper_stand | single | saturation | smfa | 403003 | 910.184911 |
| hopper_stand | single | saturation | smfa | 403004 | 0.000000 |
| hopper_stand | single | shadow | smfa | 403000 | 888.484761 |
| hopper_stand | single | shadow | smfa | 403001 | 827.928907 |
| hopper_stand | single | shadow | smfa | 403002 | 817.375334 |
| hopper_stand | single | shadow | smfa | 403003 | 914.361153 |
| hopper_stand | single | shadow | smfa | 403004 | 0.000000 |
| hopper_stand | single | shot_noise | smfa | 403000 | 892.052680 |
| hopper_stand | single | shot_noise | smfa | 403001 | 917.224961 |
| hopper_stand | single | shot_noise | smfa | 403002 | 902.031065 |
| hopper_stand | single | shot_noise | smfa | 403003 | 824.947692 |
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
| quadruped_run | markov | - | aco | 404000 | 429.266138 |
| quadruped_run | markov | - | aco | 404001 | 517.474020 |
| quadruped_run | markov | - | aco | 404002 | 476.246235 |
| quadruped_run | markov | - | aco | 404003 | 286.234873 |
| quadruped_run | markov | - | aco | 404004 | 555.067276 |
| quadruped_run | markov | - | aco | 404005 | 390.894970 |
| quadruped_run | markov | - | aco | 404006 | 324.585135 |
| quadruped_run | markov | - | aco | 404007 | 457.465178 |
| quadruped_run | markov | - | aco | 404008 | 515.992368 |
| quadruped_run | markov | - | aco | 404009 | 411.484755 |
| quadruped_run | single | rain | aco | 404000 | 427.708620 |
| quadruped_run | single | rain | aco | 404001 | 452.063806 |
| quadruped_run | single | rain | aco | 404002 | 526.731301 |
| quadruped_run | single | rain | aco | 404003 | 426.547229 |
| quadruped_run | single | rain | aco | 404004 | 546.746885 |
| quadruped_run | single | fog | aco | 404000 | 476.877487 |
| quadruped_run | single | fog | aco | 404001 | 235.816522 |
| quadruped_run | single | fog | aco | 404002 | 510.117349 |
| quadruped_run | single | fog | aco | 404003 | 424.319851 |
| quadruped_run | single | fog | aco | 404004 | 542.612757 |
| quadruped_run | single | snow | aco | 404000 | 427.285370 |
| quadruped_run | single | snow | aco | 404001 | 243.701397 |
| quadruped_run | single | snow | aco | 404002 | 526.149797 |
| quadruped_run | single | snow | aco | 404003 | 353.811262 |
| quadruped_run | single | snow | aco | 404004 | 544.897614 |
| quadruped_run | single | motion_blur | aco | 404000 | 428.563888 |
| quadruped_run | single | motion_blur | aco | 404001 | 274.359565 |
| quadruped_run | single | motion_blur | aco | 404002 | 258.488735 |
| quadruped_run | single | motion_blur | aco | 404003 | 237.739850 |
| quadruped_run | single | motion_blur | aco | 404004 | 204.619957 |
| quadruped_run | single | gaussian_noise | aco | 404000 | 373.108419 |
| quadruped_run | single | gaussian_noise | aco | 404001 | 237.276896 |
| quadruped_run | single | gaussian_noise | aco | 404002 | 134.195292 |
| quadruped_run | single | gaussian_noise | aco | 404003 | 256.434862 |
| quadruped_run | single | gaussian_noise | aco | 404004 | 301.297835 |
| quadruped_run | single | low_light | aco | 404000 | 258.237355 |
| quadruped_run | single | low_light | aco | 404001 | 23.177563 |
| quadruped_run | single | low_light | aco | 404002 | 267.853628 |
| quadruped_run | single | low_light | aco | 404003 | 295.076954 |
| quadruped_run | single | low_light | aco | 404004 | 291.641860 |
| quadruped_run | single | jpeg | aco | 404000 | 191.253814 |
| quadruped_run | single | jpeg | aco | 404001 | 243.964489 |
| quadruped_run | single | jpeg | aco | 404002 | 63.786854 |
| quadruped_run | single | jpeg | aco | 404003 | 431.459943 |
| quadruped_run | single | jpeg | aco | 404004 | 277.721190 |
| quadruped_run | single | defocus_blur | aco | 404000 | 309.863567 |
| quadruped_run | single | defocus_blur | aco | 404001 | 194.259194 |
| quadruped_run | single | defocus_blur | aco | 404002 | 271.336544 |
| quadruped_run | single | defocus_blur | aco | 404003 | 193.485799 |
| quadruped_run | single | defocus_blur | aco | 404004 | 219.138277 |
| quadruped_run | single | frost | aco | 404000 | 363.796629 |
| quadruped_run | single | frost | aco | 404001 | 359.124509 |
| quadruped_run | single | frost | aco | 404002 | 414.692193 |
| quadruped_run | single | frost | aco | 404003 | 465.405092 |
| quadruped_run | single | frost | aco | 404004 | 543.718968 |
| quadruped_run | single | occlusion_patch | aco | 404000 | 50.042253 |
| quadruped_run | single | occlusion_patch | aco | 404001 | 486.100900 |
| quadruped_run | single | occlusion_patch | aco | 404002 | 550.197603 |
| quadruped_run | single | occlusion_patch | aco | 404003 | 424.003631 |
| quadruped_run | single | occlusion_patch | aco | 404004 | 559.621884 |
| quadruped_run | single | saturation | aco | 404000 | 554.588534 |
| quadruped_run | single | saturation | aco | 404001 | 445.727441 |
| quadruped_run | single | saturation | aco | 404002 | 539.995777 |
| quadruped_run | single | saturation | aco | 404003 | 420.702889 |
| quadruped_run | single | saturation | aco | 404004 | 567.007678 |
| quadruped_run | single | shadow | aco | 404000 | 492.681818 |
| quadruped_run | single | shadow | aco | 404001 | 281.605655 |
| quadruped_run | single | shadow | aco | 404002 | 538.878328 |
| quadruped_run | single | shadow | aco | 404003 | 476.539959 |
| quadruped_run | single | shadow | aco | 404004 | 554.001249 |
| quadruped_run | single | shot_noise | aco | 404000 | 454.713568 |
| quadruped_run | single | shot_noise | aco | 404001 | 22.508119 |
| quadruped_run | single | shot_noise | aco | 404002 | 369.970871 |
| quadruped_run | single | shot_noise | aco | 404003 | 313.875366 |
| quadruped_run | single | shot_noise | aco | 404004 | 253.284405 |
| quadruped_run | markov | - | smfa | 404000 | 558.013540 |
| quadruped_run | markov | - | smfa | 404001 | 451.436321 |
| quadruped_run | markov | - | smfa | 404002 | 471.796725 |
| quadruped_run | markov | - | smfa | 404003 | 477.057070 |
| quadruped_run | markov | - | smfa | 404004 | 555.769028 |
| quadruped_run | markov | - | smfa | 404005 | 396.592119 |
| quadruped_run | markov | - | smfa | 404006 | 478.027297 |
| quadruped_run | markov | - | smfa | 404007 | 526.360275 |
| quadruped_run | markov | - | smfa | 404008 | 495.706449 |
| quadruped_run | markov | - | smfa | 404009 | 518.326105 |
| quadruped_run | single | rain | smfa | 404000 | 477.206201 |
| quadruped_run | single | rain | smfa | 404001 | 495.056221 |
| quadruped_run | single | rain | smfa | 404002 | 533.271312 |
| quadruped_run | single | rain | smfa | 404003 | 495.139575 |
| quadruped_run | single | rain | smfa | 404004 | 551.817473 |
| quadruped_run | single | fog | smfa | 404000 | 565.797576 |
| quadruped_run | single | fog | smfa | 404001 | 516.805802 |
| quadruped_run | single | fog | smfa | 404002 | 536.554615 |
| quadruped_run | single | fog | smfa | 404003 | 459.731581 |
| quadruped_run | single | fog | smfa | 404004 | 552.107010 |
| quadruped_run | single | snow | smfa | 404000 | 451.501828 |
| quadruped_run | single | snow | smfa | 404001 | 490.721555 |
| quadruped_run | single | snow | smfa | 404002 | 537.682197 |
| quadruped_run | single | snow | smfa | 404003 | 445.972373 |
| quadruped_run | single | snow | smfa | 404004 | 558.094602 |
| quadruped_run | single | motion_blur | smfa | 404000 | 564.187333 |
| quadruped_run | single | motion_blur | smfa | 404001 | 13.418338 |
| quadruped_run | single | motion_blur | smfa | 404002 | 534.412086 |
| quadruped_run | single | motion_blur | smfa | 404003 | 505.384440 |
| quadruped_run | single | motion_blur | smfa | 404004 | 563.652833 |
| quadruped_run | single | gaussian_noise | smfa | 404000 | 443.699087 |
| quadruped_run | single | gaussian_noise | smfa | 404001 | 489.382681 |
| quadruped_run | single | gaussian_noise | smfa | 404002 | 516.160206 |
| quadruped_run | single | gaussian_noise | smfa | 404003 | 479.833291 |
| quadruped_run | single | gaussian_noise | smfa | 404004 | 564.236550 |
| quadruped_run | single | low_light | smfa | 404000 | 543.404167 |
| quadruped_run | single | low_light | smfa | 404001 | 394.683744 |
| quadruped_run | single | low_light | smfa | 404002 | 538.248611 |
| quadruped_run | single | low_light | smfa | 404003 | 520.464480 |
| quadruped_run | single | low_light | smfa | 404004 | 558.597978 |
| quadruped_run | single | jpeg | smfa | 404000 | 559.967693 |
| quadruped_run | single | jpeg | smfa | 404001 | 532.365262 |
| quadruped_run | single | jpeg | smfa | 404002 | 539.002259 |
| quadruped_run | single | jpeg | smfa | 404003 | 508.778229 |
| quadruped_run | single | jpeg | smfa | 404004 | 563.415102 |
| quadruped_run | single | defocus_blur | smfa | 404000 | 556.197919 |
| quadruped_run | single | defocus_blur | smfa | 404001 | 497.914962 |
| quadruped_run | single | defocus_blur | smfa | 404002 | 531.043646 |
| quadruped_run | single | defocus_blur | smfa | 404003 | 468.680837 |
| quadruped_run | single | defocus_blur | smfa | 404004 | 551.764116 |
| quadruped_run | single | frost | smfa | 404000 | 503.972487 |
| quadruped_run | single | frost | smfa | 404001 | 520.267782 |
| quadruped_run | single | frost | smfa | 404002 | 536.588311 |
| quadruped_run | single | frost | smfa | 404003 | 456.051448 |
| quadruped_run | single | frost | smfa | 404004 | 511.007129 |
| quadruped_run | single | occlusion_patch | smfa | 404000 | 367.461103 |
| quadruped_run | single | occlusion_patch | smfa | 404001 | 470.787519 |
| quadruped_run | single | occlusion_patch | smfa | 404002 | 518.714427 |
| quadruped_run | single | occlusion_patch | smfa | 404003 | 471.930241 |
| quadruped_run | single | occlusion_patch | smfa | 404004 | 373.171683 |
| quadruped_run | single | saturation | smfa | 404000 | 568.542953 |
| quadruped_run | single | saturation | smfa | 404001 | 524.631308 |
| quadruped_run | single | saturation | smfa | 404002 | 531.122141 |
| quadruped_run | single | saturation | smfa | 404003 | 483.940961 |
| quadruped_run | single | saturation | smfa | 404004 | 563.382594 |
| quadruped_run | single | shadow | smfa | 404000 | 553.959369 |
| quadruped_run | single | shadow | smfa | 404001 | 520.121858 |
| quadruped_run | single | shadow | smfa | 404002 | 538.800588 |
| quadruped_run | single | shadow | smfa | 404003 | 418.409951 |
| quadruped_run | single | shadow | smfa | 404004 | 556.372052 |
| quadruped_run | single | shot_noise | smfa | 404000 | 553.567058 |
| quadruped_run | single | shot_noise | smfa | 404001 | 514.462692 |
| quadruped_run | single | shot_noise | smfa | 404002 | 541.853414 |
| quadruped_run | single | shot_noise | smfa | 404003 | 431.177185 |
| quadruped_run | single | shot_noise | smfa | 404004 | 557.216712 |
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
| finger_turn_hard | markov | - | aco | 405000 | 17.000000 |
| finger_turn_hard | markov | - | aco | 405001 | 912.000000 |
| finger_turn_hard | markov | - | aco | 405002 | 656.000000 |
| finger_turn_hard | markov | - | aco | 405003 | 4.000000 |
| finger_turn_hard | markov | - | aco | 405004 | 415.000000 |
| finger_turn_hard | markov | - | aco | 405005 | 838.000000 |
| finger_turn_hard | markov | - | aco | 405006 | 362.000000 |
| finger_turn_hard | markov | - | aco | 405007 | 13.000000 |
| finger_turn_hard | markov | - | aco | 405008 | 0.000000 |
| finger_turn_hard | markov | - | aco | 405009 | 647.000000 |
| finger_turn_hard | single | rain | aco | 405000 | 3.000000 |
| finger_turn_hard | single | rain | aco | 405001 | 914.000000 |
| finger_turn_hard | single | rain | aco | 405002 | 956.000000 |
| finger_turn_hard | single | rain | aco | 405003 | 872.000000 |
| finger_turn_hard | single | rain | aco | 405004 | 864.000000 |
| finger_turn_hard | single | fog | aco | 405000 | 635.000000 |
| finger_turn_hard | single | fog | aco | 405001 | 889.000000 |
| finger_turn_hard | single | fog | aco | 405002 | 954.000000 |
| finger_turn_hard | single | fog | aco | 405003 | 245.000000 |
| finger_turn_hard | single | fog | aco | 405004 | 925.000000 |
| finger_turn_hard | single | snow | aco | 405000 | 7.000000 |
| finger_turn_hard | single | snow | aco | 405001 | 0.000000 |
| finger_turn_hard | single | snow | aco | 405002 | 6.000000 |
| finger_turn_hard | single | snow | aco | 405003 | 0.000000 |
| finger_turn_hard | single | snow | aco | 405004 | 931.000000 |
| finger_turn_hard | single | motion_blur | aco | 405000 | 5.000000 |
| finger_turn_hard | single | motion_blur | aco | 405001 | 0.000000 |
| finger_turn_hard | single | motion_blur | aco | 405002 | 17.000000 |
| finger_turn_hard | single | motion_blur | aco | 405003 | 38.000000 |
| finger_turn_hard | single | motion_blur | aco | 405004 | 3.000000 |
| finger_turn_hard | single | gaussian_noise | aco | 405000 | 0.000000 |
| finger_turn_hard | single | gaussian_noise | aco | 405001 | 635.000000 |
| finger_turn_hard | single | gaussian_noise | aco | 405002 | 0.000000 |
| finger_turn_hard | single | gaussian_noise | aco | 405003 | 0.000000 |
| finger_turn_hard | single | gaussian_noise | aco | 405004 | 0.000000 |
| finger_turn_hard | single | low_light | aco | 405000 | 0.000000 |
| finger_turn_hard | single | low_light | aco | 405001 | 0.000000 |
| finger_turn_hard | single | low_light | aco | 405002 | 0.000000 |
| finger_turn_hard | single | low_light | aco | 405003 | 0.000000 |
| finger_turn_hard | single | low_light | aco | 405004 | 0.000000 |
| finger_turn_hard | single | jpeg | aco | 405000 | 388.000000 |
| finger_turn_hard | single | jpeg | aco | 405001 | 352.000000 |
| finger_turn_hard | single | jpeg | aco | 405002 | 0.000000 |
| finger_turn_hard | single | jpeg | aco | 405003 | 0.000000 |
| finger_turn_hard | single | jpeg | aco | 405004 | 0.000000 |
| finger_turn_hard | single | defocus_blur | aco | 405000 | 33.000000 |
| finger_turn_hard | single | defocus_blur | aco | 405001 | 236.000000 |
| finger_turn_hard | single | defocus_blur | aco | 405002 | 5.000000 |
| finger_turn_hard | single | defocus_blur | aco | 405003 | 0.000000 |
| finger_turn_hard | single | defocus_blur | aco | 405004 | 464.000000 |
| finger_turn_hard | single | frost | aco | 405000 | 669.000000 |
| finger_turn_hard | single | frost | aco | 405001 | 940.000000 |
| finger_turn_hard | single | frost | aco | 405002 | 957.000000 |
| finger_turn_hard | single | frost | aco | 405003 | 0.000000 |
| finger_turn_hard | single | frost | aco | 405004 | 932.000000 |
| finger_turn_hard | single | occlusion_patch | aco | 405000 | 892.000000 |
| finger_turn_hard | single | occlusion_patch | aco | 405001 | 2.000000 |
| finger_turn_hard | single | occlusion_patch | aco | 405002 | 32.000000 |
| finger_turn_hard | single | occlusion_patch | aco | 405003 | 13.000000 |
| finger_turn_hard | single | occlusion_patch | aco | 405004 | 935.000000 |
| finger_turn_hard | single | saturation | aco | 405000 | 0.000000 |
| finger_turn_hard | single | saturation | aco | 405001 | 0.000000 |
| finger_turn_hard | single | saturation | aco | 405002 | 932.000000 |
| finger_turn_hard | single | saturation | aco | 405003 | 921.000000 |
| finger_turn_hard | single | saturation | aco | 405004 | 822.000000 |
| finger_turn_hard | single | shadow | aco | 405000 | 23.000000 |
| finger_turn_hard | single | shadow | aco | 405001 | 878.000000 |
| finger_turn_hard | single | shadow | aco | 405002 | 15.000000 |
| finger_turn_hard | single | shadow | aco | 405003 | 14.000000 |
| finger_turn_hard | single | shadow | aco | 405004 | 870.000000 |
| finger_turn_hard | single | shot_noise | aco | 405000 | 0.000000 |
| finger_turn_hard | single | shot_noise | aco | 405001 | 0.000000 |
| finger_turn_hard | single | shot_noise | aco | 405002 | 0.000000 |
| finger_turn_hard | single | shot_noise | aco | 405003 | 0.000000 |
| finger_turn_hard | single | shot_noise | aco | 405004 | 0.000000 |
| finger_turn_hard | markov | - | smfa | 405000 | 3.000000 |
| finger_turn_hard | markov | - | smfa | 405001 | 0.000000 |
| finger_turn_hard | markov | - | smfa | 405002 | 930.000000 |
| finger_turn_hard | markov | - | smfa | 405003 | 15.000000 |
| finger_turn_hard | markov | - | smfa | 405004 | 898.000000 |
| finger_turn_hard | markov | - | smfa | 405005 | 943.000000 |
| finger_turn_hard | markov | - | smfa | 405006 | 936.000000 |
| finger_turn_hard | markov | - | smfa | 405007 | 669.000000 |
| finger_turn_hard | markov | - | smfa | 405008 | 927.000000 |
| finger_turn_hard | markov | - | smfa | 405009 | 899.000000 |
| finger_turn_hard | single | rain | smfa | 405000 | 0.000000 |
| finger_turn_hard | single | rain | smfa | 405001 | 913.000000 |
| finger_turn_hard | single | rain | smfa | 405002 | 957.000000 |
| finger_turn_hard | single | rain | smfa | 405003 | 0.000000 |
| finger_turn_hard | single | rain | smfa | 405004 | 933.000000 |
| finger_turn_hard | single | fog | smfa | 405000 | 0.000000 |
| finger_turn_hard | single | fog | smfa | 405001 | 928.000000 |
| finger_turn_hard | single | fog | smfa | 405002 | 954.000000 |
| finger_turn_hard | single | fog | smfa | 405003 | 0.000000 |
| finger_turn_hard | single | fog | smfa | 405004 | 934.000000 |
| finger_turn_hard | single | snow | smfa | 405000 | 974.000000 |
| finger_turn_hard | single | snow | smfa | 405001 | 931.000000 |
| finger_turn_hard | single | snow | smfa | 405002 | 947.000000 |
| finger_turn_hard | single | snow | smfa | 405003 | 0.000000 |
| finger_turn_hard | single | snow | smfa | 405004 | 939.000000 |
| finger_turn_hard | single | motion_blur | smfa | 405000 | 8.000000 |
| finger_turn_hard | single | motion_blur | smfa | 405001 | 330.000000 |
| finger_turn_hard | single | motion_blur | smfa | 405002 | 0.000000 |
| finger_turn_hard | single | motion_blur | smfa | 405003 | 32.000000 |
| finger_turn_hard | single | motion_blur | smfa | 405004 | 141.000000 |
| finger_turn_hard | single | gaussian_noise | smfa | 405000 | 0.000000 |
| finger_turn_hard | single | gaussian_noise | smfa | 405001 | 924.000000 |
| finger_turn_hard | single | gaussian_noise | smfa | 405002 | 958.000000 |
| finger_turn_hard | single | gaussian_noise | smfa | 405003 | 0.000000 |
| finger_turn_hard | single | gaussian_noise | smfa | 405004 | 922.000000 |
| finger_turn_hard | single | low_light | smfa | 405000 | 981.000000 |
| finger_turn_hard | single | low_light | smfa | 405001 | 923.000000 |
| finger_turn_hard | single | low_light | smfa | 405002 | 957.000000 |
| finger_turn_hard | single | low_light | smfa | 405003 | 0.000000 |
| finger_turn_hard | single | low_light | smfa | 405004 | 929.000000 |
| finger_turn_hard | single | jpeg | smfa | 405000 | 7.000000 |
| finger_turn_hard | single | jpeg | smfa | 405001 | 0.000000 |
| finger_turn_hard | single | jpeg | smfa | 405002 | 949.000000 |
| finger_turn_hard | single | jpeg | smfa | 405003 | 3.000000 |
| finger_turn_hard | single | jpeg | smfa | 405004 | 940.000000 |
| finger_turn_hard | single | defocus_blur | smfa | 405000 | 24.000000 |
| finger_turn_hard | single | defocus_blur | smfa | 405001 | 5.000000 |
| finger_turn_hard | single | defocus_blur | smfa | 405002 | 8.000000 |
| finger_turn_hard | single | defocus_blur | smfa | 405003 | 2.000000 |
| finger_turn_hard | single | defocus_blur | smfa | 405004 | 73.000000 |
| finger_turn_hard | single | frost | smfa | 405000 | 0.000000 |
| finger_turn_hard | single | frost | smfa | 405001 | 919.000000 |
| finger_turn_hard | single | frost | smfa | 405002 | 956.000000 |
| finger_turn_hard | single | frost | smfa | 405003 | 0.000000 |
| finger_turn_hard | single | frost | smfa | 405004 | 930.000000 |
| finger_turn_hard | single | occlusion_patch | smfa | 405000 | 982.000000 |
| finger_turn_hard | single | occlusion_patch | smfa | 405001 | 0.000000 |
| finger_turn_hard | single | occlusion_patch | smfa | 405002 | 899.000000 |
| finger_turn_hard | single | occlusion_patch | smfa | 405003 | 636.000000 |
| finger_turn_hard | single | occlusion_patch | smfa | 405004 | 928.000000 |
| finger_turn_hard | single | saturation | smfa | 405000 | 982.000000 |
| finger_turn_hard | single | saturation | smfa | 405001 | 926.000000 |
| finger_turn_hard | single | saturation | smfa | 405002 | 962.000000 |
| finger_turn_hard | single | saturation | smfa | 405003 | 0.000000 |
| finger_turn_hard | single | saturation | smfa | 405004 | 932.000000 |
| finger_turn_hard | single | shadow | smfa | 405000 | 974.000000 |
| finger_turn_hard | single | shadow | smfa | 405001 | 932.000000 |
| finger_turn_hard | single | shadow | smfa | 405002 | 959.000000 |
| finger_turn_hard | single | shadow | smfa | 405003 | 0.000000 |
| finger_turn_hard | single | shadow | smfa | 405004 | 939.000000 |
| finger_turn_hard | single | shot_noise | smfa | 405000 | 0.000000 |
| finger_turn_hard | single | shot_noise | smfa | 405001 | 929.000000 |
| finger_turn_hard | single | shot_noise | smfa | 405002 | 955.000000 |
| finger_turn_hard | single | shot_noise | smfa | 405003 | 0.000000 |
| finger_turn_hard | single | shot_noise | smfa | 405004 | 934.000000 |
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
| cartpole_swingup_sparse | markov | - | aco | 406000 | 8.000000 |
| cartpole_swingup_sparse | markov | - | aco | 406001 | 239.000000 |
| cartpole_swingup_sparse | markov | - | aco | 406002 | 23.000000 |
| cartpole_swingup_sparse | markov | - | aco | 406003 | 0.000000 |
| cartpole_swingup_sparse | markov | - | aco | 406004 | 21.000000 |
| cartpole_swingup_sparse | markov | - | aco | 406005 | 40.000000 |
| cartpole_swingup_sparse | markov | - | aco | 406006 | 36.000000 |
| cartpole_swingup_sparse | markov | - | aco | 406007 | 16.000000 |
| cartpole_swingup_sparse | markov | - | aco | 406008 | 79.000000 |
| cartpole_swingup_sparse | markov | - | aco | 406009 | 11.000000 |
| cartpole_swingup_sparse | single | rain | aco | 406000 | 820.000000 |
| cartpole_swingup_sparse | single | rain | aco | 406001 | 774.000000 |
| cartpole_swingup_sparse | single | rain | aco | 406002 | 838.000000 |
| cartpole_swingup_sparse | single | rain | aco | 406003 | 833.000000 |
| cartpole_swingup_sparse | single | rain | aco | 406004 | 833.000000 |
| cartpole_swingup_sparse | single | fog | aco | 406000 | 828.000000 |
| cartpole_swingup_sparse | single | fog | aco | 406001 | 826.000000 |
| cartpole_swingup_sparse | single | fog | aco | 406002 | 834.000000 |
| cartpole_swingup_sparse | single | fog | aco | 406003 | 836.000000 |
| cartpole_swingup_sparse | single | fog | aco | 406004 | 827.000000 |
| cartpole_swingup_sparse | single | snow | aco | 406000 | 833.000000 |
| cartpole_swingup_sparse | single | snow | aco | 406001 | 792.000000 |
| cartpole_swingup_sparse | single | snow | aco | 406002 | 782.000000 |
| cartpole_swingup_sparse | single | snow | aco | 406003 | 832.000000 |
| cartpole_swingup_sparse | single | snow | aco | 406004 | 830.000000 |
| cartpole_swingup_sparse | single | motion_blur | aco | 406000 | 21.000000 |
| cartpole_swingup_sparse | single | motion_blur | aco | 406001 | 30.000000 |
| cartpole_swingup_sparse | single | motion_blur | aco | 406002 | 4.000000 |
| cartpole_swingup_sparse | single | motion_blur | aco | 406003 | 9.000000 |
| cartpole_swingup_sparse | single | motion_blur | aco | 406004 | 21.000000 |
| cartpole_swingup_sparse | single | gaussian_noise | aco | 406000 | 0.000000 |
| cartpole_swingup_sparse | single | gaussian_noise | aco | 406001 | 0.000000 |
| cartpole_swingup_sparse | single | gaussian_noise | aco | 406002 | 0.000000 |
| cartpole_swingup_sparse | single | gaussian_noise | aco | 406003 | 0.000000 |
| cartpole_swingup_sparse | single | gaussian_noise | aco | 406004 | 0.000000 |
| cartpole_swingup_sparse | single | low_light | aco | 406000 | 0.000000 |
| cartpole_swingup_sparse | single | low_light | aco | 406001 | 0.000000 |
| cartpole_swingup_sparse | single | low_light | aco | 406002 | 0.000000 |
| cartpole_swingup_sparse | single | low_light | aco | 406003 | 0.000000 |
| cartpole_swingup_sparse | single | low_light | aco | 406004 | 0.000000 |
| cartpole_swingup_sparse | single | jpeg | aco | 406000 | 8.000000 |
| cartpole_swingup_sparse | single | jpeg | aco | 406001 | 5.000000 |
| cartpole_swingup_sparse | single | jpeg | aco | 406002 | 0.000000 |
| cartpole_swingup_sparse | single | jpeg | aco | 406003 | 0.000000 |
| cartpole_swingup_sparse | single | jpeg | aco | 406004 | 4.000000 |
| cartpole_swingup_sparse | single | defocus_blur | aco | 406000 | 15.000000 |
| cartpole_swingup_sparse | single | defocus_blur | aco | 406001 | 22.000000 |
| cartpole_swingup_sparse | single | defocus_blur | aco | 406002 | 24.000000 |
| cartpole_swingup_sparse | single | defocus_blur | aco | 406003 | 0.000000 |
| cartpole_swingup_sparse | single | defocus_blur | aco | 406004 | 34.000000 |
| cartpole_swingup_sparse | single | frost | aco | 406000 | 826.000000 |
| cartpole_swingup_sparse | single | frost | aco | 406001 | 829.000000 |
| cartpole_swingup_sparse | single | frost | aco | 406002 | 821.000000 |
| cartpole_swingup_sparse | single | frost | aco | 406003 | 833.000000 |
| cartpole_swingup_sparse | single | frost | aco | 406004 | 825.000000 |
| cartpole_swingup_sparse | single | occlusion_patch | aco | 406000 | 153.000000 |
| cartpole_swingup_sparse | single | occlusion_patch | aco | 406001 | 65.000000 |
| cartpole_swingup_sparse | single | occlusion_patch | aco | 406002 | 145.000000 |
| cartpole_swingup_sparse | single | occlusion_patch | aco | 406003 | 0.000000 |
| cartpole_swingup_sparse | single | occlusion_patch | aco | 406004 | 115.000000 |
| cartpole_swingup_sparse | single | saturation | aco | 406000 | 818.000000 |
| cartpole_swingup_sparse | single | saturation | aco | 406001 | 836.000000 |
| cartpole_swingup_sparse | single | saturation | aco | 406002 | 837.000000 |
| cartpole_swingup_sparse | single | saturation | aco | 406003 | 832.000000 |
| cartpole_swingup_sparse | single | saturation | aco | 406004 | 829.000000 |
| cartpole_swingup_sparse | single | shadow | aco | 406000 | 599.000000 |
| cartpole_swingup_sparse | single | shadow | aco | 406001 | 394.000000 |
| cartpole_swingup_sparse | single | shadow | aco | 406002 | 386.000000 |
| cartpole_swingup_sparse | single | shadow | aco | 406003 | 389.000000 |
| cartpole_swingup_sparse | single | shadow | aco | 406004 | 768.000000 |
| cartpole_swingup_sparse | single | shot_noise | aco | 406000 | 6.000000 |
| cartpole_swingup_sparse | single | shot_noise | aco | 406001 | 0.000000 |
| cartpole_swingup_sparse | single | shot_noise | aco | 406002 | 0.000000 |
| cartpole_swingup_sparse | single | shot_noise | aco | 406003 | 0.000000 |
| cartpole_swingup_sparse | single | shot_noise | aco | 406004 | 0.000000 |
| cartpole_swingup_sparse | markov | - | smfa | 406000 | 378.000000 |
| cartpole_swingup_sparse | markov | - | smfa | 406001 | 611.000000 |
| cartpole_swingup_sparse | markov | - | smfa | 406002 | 330.000000 |
| cartpole_swingup_sparse | markov | - | smfa | 406003 | 176.000000 |
| cartpole_swingup_sparse | markov | - | smfa | 406004 | 321.000000 |
| cartpole_swingup_sparse | markov | - | smfa | 406005 | 367.000000 |
| cartpole_swingup_sparse | markov | - | smfa | 406006 | 392.000000 |
| cartpole_swingup_sparse | markov | - | smfa | 406007 | 311.000000 |
| cartpole_swingup_sparse | markov | - | smfa | 406008 | 272.000000 |
| cartpole_swingup_sparse | markov | - | smfa | 406009 | 595.000000 |
| cartpole_swingup_sparse | single | rain | smfa | 406000 | 827.000000 |
| cartpole_swingup_sparse | single | rain | smfa | 406001 | 810.000000 |
| cartpole_swingup_sparse | single | rain | smfa | 406002 | 823.000000 |
| cartpole_swingup_sparse | single | rain | smfa | 406003 | 823.000000 |
| cartpole_swingup_sparse | single | rain | smfa | 406004 | 835.000000 |
| cartpole_swingup_sparse | single | fog | smfa | 406000 | 831.000000 |
| cartpole_swingup_sparse | single | fog | smfa | 406001 | 824.000000 |
| cartpole_swingup_sparse | single | fog | smfa | 406002 | 809.000000 |
| cartpole_swingup_sparse | single | fog | smfa | 406003 | 812.000000 |
| cartpole_swingup_sparse | single | fog | smfa | 406004 | 832.000000 |
| cartpole_swingup_sparse | single | snow | smfa | 406000 | 832.000000 |
| cartpole_swingup_sparse | single | snow | smfa | 406001 | 812.000000 |
| cartpole_swingup_sparse | single | snow | smfa | 406002 | 827.000000 |
| cartpole_swingup_sparse | single | snow | smfa | 406003 | 826.000000 |
| cartpole_swingup_sparse | single | snow | smfa | 406004 | 833.000000 |
| cartpole_swingup_sparse | single | motion_blur | smfa | 406000 | 5.000000 |
| cartpole_swingup_sparse | single | motion_blur | smfa | 406001 | 9.000000 |
| cartpole_swingup_sparse | single | motion_blur | smfa | 406002 | 8.000000 |
| cartpole_swingup_sparse | single | motion_blur | smfa | 406003 | 16.000000 |
| cartpole_swingup_sparse | single | motion_blur | smfa | 406004 | 27.000000 |
| cartpole_swingup_sparse | single | gaussian_noise | smfa | 406000 | 831.000000 |
| cartpole_swingup_sparse | single | gaussian_noise | smfa | 406001 | 827.000000 |
| cartpole_swingup_sparse | single | gaussian_noise | smfa | 406002 | 832.000000 |
| cartpole_swingup_sparse | single | gaussian_noise | smfa | 406003 | 836.000000 |
| cartpole_swingup_sparse | single | gaussian_noise | smfa | 406004 | 835.000000 |
| cartpole_swingup_sparse | single | low_light | smfa | 406000 | 809.000000 |
| cartpole_swingup_sparse | single | low_light | smfa | 406001 | 835.000000 |
| cartpole_swingup_sparse | single | low_light | smfa | 406002 | 287.000000 |
| cartpole_swingup_sparse | single | low_light | smfa | 406003 | 835.000000 |
| cartpole_swingup_sparse | single | low_light | smfa | 406004 | 822.000000 |
| cartpole_swingup_sparse | single | jpeg | smfa | 406000 | 91.000000 |
| cartpole_swingup_sparse | single | jpeg | smfa | 406001 | 152.000000 |
| cartpole_swingup_sparse | single | jpeg | smfa | 406002 | 63.000000 |
| cartpole_swingup_sparse | single | jpeg | smfa | 406003 | 171.000000 |
| cartpole_swingup_sparse | single | jpeg | smfa | 406004 | 164.000000 |
| cartpole_swingup_sparse | single | defocus_blur | smfa | 406000 | 28.000000 |
| cartpole_swingup_sparse | single | defocus_blur | smfa | 406001 | 10.000000 |
| cartpole_swingup_sparse | single | defocus_blur | smfa | 406002 | 0.000000 |
| cartpole_swingup_sparse | single | defocus_blur | smfa | 406003 | 17.000000 |
| cartpole_swingup_sparse | single | defocus_blur | smfa | 406004 | 0.000000 |
| cartpole_swingup_sparse | single | frost | smfa | 406000 | 834.000000 |
| cartpole_swingup_sparse | single | frost | smfa | 406001 | 830.000000 |
| cartpole_swingup_sparse | single | frost | smfa | 406002 | 831.000000 |
| cartpole_swingup_sparse | single | frost | smfa | 406003 | 822.000000 |
| cartpole_swingup_sparse | single | frost | smfa | 406004 | 832.000000 |
| cartpole_swingup_sparse | single | occlusion_patch | smfa | 406000 | 836.000000 |
| cartpole_swingup_sparse | single | occlusion_patch | smfa | 406001 | 1.000000 |
| cartpole_swingup_sparse | single | occlusion_patch | smfa | 406002 | 596.000000 |
| cartpole_swingup_sparse | single | occlusion_patch | smfa | 406003 | 509.000000 |
| cartpole_swingup_sparse | single | occlusion_patch | smfa | 406004 | 814.000000 |
| cartpole_swingup_sparse | single | saturation | smfa | 406000 | 831.000000 |
| cartpole_swingup_sparse | single | saturation | smfa | 406001 | 832.000000 |
| cartpole_swingup_sparse | single | saturation | smfa | 406002 | 834.000000 |
| cartpole_swingup_sparse | single | saturation | smfa | 406003 | 830.000000 |
| cartpole_swingup_sparse | single | saturation | smfa | 406004 | 832.000000 |
| cartpole_swingup_sparse | single | shadow | smfa | 406000 | 171.000000 |
| cartpole_swingup_sparse | single | shadow | smfa | 406001 | 399.000000 |
| cartpole_swingup_sparse | single | shadow | smfa | 406002 | 286.000000 |
| cartpole_swingup_sparse | single | shadow | smfa | 406003 | 291.000000 |
| cartpole_swingup_sparse | single | shadow | smfa | 406004 | 818.000000 |
| cartpole_swingup_sparse | single | shot_noise | smfa | 406000 | 834.000000 |
| cartpole_swingup_sparse | single | shot_noise | smfa | 406001 | 820.000000 |
| cartpole_swingup_sparse | single | shot_noise | smfa | 406002 | 838.000000 |
| cartpole_swingup_sparse | single | shot_noise | smfa | 406003 | 797.000000 |
| cartpole_swingup_sparse | single | shot_noise | smfa | 406004 | 830.000000 |
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
| cup_catch | markov | - | aco | 407000 | 921.000000 |
| cup_catch | markov | - | aco | 407001 | 683.000000 |
| cup_catch | markov | - | aco | 407002 | 988.000000 |
| cup_catch | markov | - | aco | 407003 | 442.000000 |
| cup_catch | markov | - | aco | 407004 | 958.000000 |
| cup_catch | markov | - | aco | 407005 | 845.000000 |
| cup_catch | markov | - | aco | 407006 | 780.000000 |
| cup_catch | markov | - | aco | 407007 | 726.000000 |
| cup_catch | markov | - | aco | 407008 | 880.000000 |
| cup_catch | markov | - | aco | 407009 | 971.000000 |
| cup_catch | single | rain | aco | 407000 | 972.000000 |
| cup_catch | single | rain | aco | 407001 | 963.000000 |
| cup_catch | single | rain | aco | 407002 | 990.000000 |
| cup_catch | single | rain | aco | 407003 | 988.000000 |
| cup_catch | single | rain | aco | 407004 | 973.000000 |
| cup_catch | single | fog | aco | 407000 | 972.000000 |
| cup_catch | single | fog | aco | 407001 | 964.000000 |
| cup_catch | single | fog | aco | 407002 | 991.000000 |
| cup_catch | single | fog | aco | 407003 | 988.000000 |
| cup_catch | single | fog | aco | 407004 | 972.000000 |
| cup_catch | single | snow | aco | 407000 | 971.000000 |
| cup_catch | single | snow | aco | 407001 | 963.000000 |
| cup_catch | single | snow | aco | 407002 | 991.000000 |
| cup_catch | single | snow | aco | 407003 | 988.000000 |
| cup_catch | single | snow | aco | 407004 | 971.000000 |
| cup_catch | single | motion_blur | aco | 407000 | 971.000000 |
| cup_catch | single | motion_blur | aco | 407001 | 964.000000 |
| cup_catch | single | motion_blur | aco | 407002 | 990.000000 |
| cup_catch | single | motion_blur | aco | 407003 | 983.000000 |
| cup_catch | single | motion_blur | aco | 407004 | 973.000000 |
| cup_catch | single | gaussian_noise | aco | 407000 | 931.000000 |
| cup_catch | single | gaussian_noise | aco | 407001 | 0.000000 |
| cup_catch | single | gaussian_noise | aco | 407002 | 11.000000 |
| cup_catch | single | gaussian_noise | aco | 407003 | 30.000000 |
| cup_catch | single | gaussian_noise | aco | 407004 | 0.000000 |
| cup_catch | single | low_light | aco | 407000 | 0.000000 |
| cup_catch | single | low_light | aco | 407001 | 0.000000 |
| cup_catch | single | low_light | aco | 407002 | 10.000000 |
| cup_catch | single | low_light | aco | 407003 | 5.000000 |
| cup_catch | single | low_light | aco | 407004 | 0.000000 |
| cup_catch | single | jpeg | aco | 407000 | 817.000000 |
| cup_catch | single | jpeg | aco | 407001 | 923.000000 |
| cup_catch | single | jpeg | aco | 407002 | 990.000000 |
| cup_catch | single | jpeg | aco | 407003 | 988.000000 |
| cup_catch | single | jpeg | aco | 407004 | 704.000000 |
| cup_catch | single | defocus_blur | aco | 407000 | 972.000000 |
| cup_catch | single | defocus_blur | aco | 407001 | 964.000000 |
| cup_catch | single | defocus_blur | aco | 407002 | 990.000000 |
| cup_catch | single | defocus_blur | aco | 407003 | 987.000000 |
| cup_catch | single | defocus_blur | aco | 407004 | 973.000000 |
| cup_catch | single | frost | aco | 407000 | 972.000000 |
| cup_catch | single | frost | aco | 407001 | 964.000000 |
| cup_catch | single | frost | aco | 407002 | 991.000000 |
| cup_catch | single | frost | aco | 407003 | 989.000000 |
| cup_catch | single | frost | aco | 407004 | 972.000000 |
| cup_catch | single | occlusion_patch | aco | 407000 | 16.000000 |
| cup_catch | single | occlusion_patch | aco | 407001 | 11.000000 |
| cup_catch | single | occlusion_patch | aco | 407002 | 830.000000 |
| cup_catch | single | occlusion_patch | aco | 407003 | 0.000000 |
| cup_catch | single | occlusion_patch | aco | 407004 | 924.000000 |
| cup_catch | single | saturation | aco | 407000 | 972.000000 |
| cup_catch | single | saturation | aco | 407001 | 962.000000 |
| cup_catch | single | saturation | aco | 407002 | 990.000000 |
| cup_catch | single | saturation | aco | 407003 | 988.000000 |
| cup_catch | single | saturation | aco | 407004 | 972.000000 |
| cup_catch | single | shadow | aco | 407000 | 969.000000 |
| cup_catch | single | shadow | aco | 407001 | 963.000000 |
| cup_catch | single | shadow | aco | 407002 | 944.000000 |
| cup_catch | single | shadow | aco | 407003 | 984.000000 |
| cup_catch | single | shadow | aco | 407004 | 966.000000 |
| cup_catch | single | shot_noise | aco | 407000 | 0.000000 |
| cup_catch | single | shot_noise | aco | 407001 | 0.000000 |
| cup_catch | single | shot_noise | aco | 407002 | 10.000000 |
| cup_catch | single | shot_noise | aco | 407003 | 12.000000 |
| cup_catch | single | shot_noise | aco | 407004 | 0.000000 |
| cup_catch | markov | - | smfa | 407000 | 962.000000 |
| cup_catch | markov | - | smfa | 407001 | 964.000000 |
| cup_catch | markov | - | smfa | 407002 | 985.000000 |
| cup_catch | markov | - | smfa | 407003 | 988.000000 |
| cup_catch | markov | - | smfa | 407004 | 972.000000 |
| cup_catch | markov | - | smfa | 407005 | 966.000000 |
| cup_catch | markov | - | smfa | 407006 | 965.000000 |
| cup_catch | markov | - | smfa | 407007 | 971.000000 |
| cup_catch | markov | - | smfa | 407008 | 973.000000 |
| cup_catch | markov | - | smfa | 407009 | 971.000000 |
| cup_catch | single | rain | smfa | 407000 | 972.000000 |
| cup_catch | single | rain | smfa | 407001 | 962.000000 |
| cup_catch | single | rain | smfa | 407002 | 991.000000 |
| cup_catch | single | rain | smfa | 407003 | 988.000000 |
| cup_catch | single | rain | smfa | 407004 | 972.000000 |
| cup_catch | single | fog | smfa | 407000 | 972.000000 |
| cup_catch | single | fog | smfa | 407001 | 964.000000 |
| cup_catch | single | fog | smfa | 407002 | 988.000000 |
| cup_catch | single | fog | smfa | 407003 | 988.000000 |
| cup_catch | single | fog | smfa | 407004 | 972.000000 |
| cup_catch | single | snow | smfa | 407000 | 972.000000 |
| cup_catch | single | snow | smfa | 407001 | 964.000000 |
| cup_catch | single | snow | smfa | 407002 | 990.000000 |
| cup_catch | single | snow | smfa | 407003 | 988.000000 |
| cup_catch | single | snow | smfa | 407004 | 973.000000 |
| cup_catch | single | motion_blur | smfa | 407000 | 970.000000 |
| cup_catch | single | motion_blur | smfa | 407001 | 0.000000 |
| cup_catch | single | motion_blur | smfa | 407002 | 987.000000 |
| cup_catch | single | motion_blur | smfa | 407003 | 982.000000 |
| cup_catch | single | motion_blur | smfa | 407004 | 963.000000 |
| cup_catch | single | gaussian_noise | smfa | 407000 | 972.000000 |
| cup_catch | single | gaussian_noise | smfa | 407001 | 964.000000 |
| cup_catch | single | gaussian_noise | smfa | 407002 | 991.000000 |
| cup_catch | single | gaussian_noise | smfa | 407003 | 989.000000 |
| cup_catch | single | gaussian_noise | smfa | 407004 | 972.000000 |
| cup_catch | single | low_light | smfa | 407000 | 972.000000 |
| cup_catch | single | low_light | smfa | 407001 | 964.000000 |
| cup_catch | single | low_light | smfa | 407002 | 990.000000 |
| cup_catch | single | low_light | smfa | 407003 | 988.000000 |
| cup_catch | single | low_light | smfa | 407004 | 972.000000 |
| cup_catch | single | jpeg | smfa | 407000 | 971.000000 |
| cup_catch | single | jpeg | smfa | 407001 | 963.000000 |
| cup_catch | single | jpeg | smfa | 407002 | 991.000000 |
| cup_catch | single | jpeg | smfa | 407003 | 984.000000 |
| cup_catch | single | jpeg | smfa | 407004 | 972.000000 |
| cup_catch | single | defocus_blur | smfa | 407000 | 0.000000 |
| cup_catch | single | defocus_blur | smfa | 407001 | 943.000000 |
| cup_catch | single | defocus_blur | smfa | 407002 | 990.000000 |
| cup_catch | single | defocus_blur | smfa | 407003 | 958.000000 |
| cup_catch | single | defocus_blur | smfa | 407004 | 0.000000 |
| cup_catch | single | frost | smfa | 407000 | 972.000000 |
| cup_catch | single | frost | smfa | 407001 | 964.000000 |
| cup_catch | single | frost | smfa | 407002 | 991.000000 |
| cup_catch | single | frost | smfa | 407003 | 988.000000 |
| cup_catch | single | frost | smfa | 407004 | 972.000000 |
| cup_catch | single | occlusion_patch | smfa | 407000 | 972.000000 |
| cup_catch | single | occlusion_patch | smfa | 407001 | 962.000000 |
| cup_catch | single | occlusion_patch | smfa | 407002 | 989.000000 |
| cup_catch | single | occlusion_patch | smfa | 407003 | 989.000000 |
| cup_catch | single | occlusion_patch | smfa | 407004 | 972.000000 |
| cup_catch | single | saturation | smfa | 407000 | 971.000000 |
| cup_catch | single | saturation | smfa | 407001 | 964.000000 |
| cup_catch | single | saturation | smfa | 407002 | 991.000000 |
| cup_catch | single | saturation | smfa | 407003 | 988.000000 |
| cup_catch | single | saturation | smfa | 407004 | 972.000000 |
| cup_catch | single | shadow | smfa | 407000 | 972.000000 |
| cup_catch | single | shadow | smfa | 407001 | 964.000000 |
| cup_catch | single | shadow | smfa | 407002 | 991.000000 |
| cup_catch | single | shadow | smfa | 407003 | 988.000000 |
| cup_catch | single | shadow | smfa | 407004 | 972.000000 |
| cup_catch | single | shot_noise | smfa | 407000 | 972.000000 |
| cup_catch | single | shot_noise | smfa | 407001 | 964.000000 |
| cup_catch | single | shot_noise | smfa | 407002 | 991.000000 |
| cup_catch | single | shot_noise | smfa | 407003 | 989.000000 |
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
| reacher_easy | markov | - | aco | 408000 | 861.000000 |
| reacher_easy | markov | - | aco | 408001 | 980.000000 |
| reacher_easy | markov | - | aco | 408002 | 971.000000 |
| reacher_easy | markov | - | aco | 408003 | 999.000000 |
| reacher_easy | markov | - | aco | 408004 | 993.000000 |
| reacher_easy | markov | - | aco | 408005 | 946.000000 |
| reacher_easy | markov | - | aco | 408006 | 966.000000 |
| reacher_easy | markov | - | aco | 408007 | 970.000000 |
| reacher_easy | markov | - | aco | 408008 | 619.000000 |
| reacher_easy | markov | - | aco | 408009 | 961.000000 |
| reacher_easy | single | rain | aco | 408000 | 960.000000 |
| reacher_easy | single | rain | aco | 408001 | 981.000000 |
| reacher_easy | single | rain | aco | 408002 | 976.000000 |
| reacher_easy | single | rain | aco | 408003 | 1000.000000 |
| reacher_easy | single | rain | aco | 408004 | 993.000000 |
| reacher_easy | single | fog | aco | 408000 | 962.000000 |
| reacher_easy | single | fog | aco | 408001 | 981.000000 |
| reacher_easy | single | fog | aco | 408002 | 976.000000 |
| reacher_easy | single | fog | aco | 408003 | 1000.000000 |
| reacher_easy | single | fog | aco | 408004 | 993.000000 |
| reacher_easy | single | snow | aco | 408000 | 961.000000 |
| reacher_easy | single | snow | aco | 408001 | 980.000000 |
| reacher_easy | single | snow | aco | 408002 | 976.000000 |
| reacher_easy | single | snow | aco | 408003 | 1000.000000 |
| reacher_easy | single | snow | aco | 408004 | 993.000000 |
| reacher_easy | single | motion_blur | aco | 408000 | 899.000000 |
| reacher_easy | single | motion_blur | aco | 408001 | 979.000000 |
| reacher_easy | single | motion_blur | aco | 408002 | 968.000000 |
| reacher_easy | single | motion_blur | aco | 408003 | 1000.000000 |
| reacher_easy | single | motion_blur | aco | 408004 | 993.000000 |
| reacher_easy | single | gaussian_noise | aco | 408000 | 196.000000 |
| reacher_easy | single | gaussian_noise | aco | 408001 | 975.000000 |
| reacher_easy | single | gaussian_noise | aco | 408002 | 974.000000 |
| reacher_easy | single | gaussian_noise | aco | 408003 | 993.000000 |
| reacher_easy | single | gaussian_noise | aco | 408004 | 544.000000 |
| reacher_easy | single | low_light | aco | 408000 | 0.000000 |
| reacher_easy | single | low_light | aco | 408001 | 375.000000 |
| reacher_easy | single | low_light | aco | 408002 | 668.000000 |
| reacher_easy | single | low_light | aco | 408003 | 641.000000 |
| reacher_easy | single | low_light | aco | 408004 | 51.000000 |
| reacher_easy | single | jpeg | aco | 408000 | 0.000000 |
| reacher_easy | single | jpeg | aco | 408001 | 0.000000 |
| reacher_easy | single | jpeg | aco | 408002 | 354.000000 |
| reacher_easy | single | jpeg | aco | 408003 | 9.000000 |
| reacher_easy | single | jpeg | aco | 408004 | 0.000000 |
| reacher_easy | single | defocus_blur | aco | 408000 | 939.000000 |
| reacher_easy | single | defocus_blur | aco | 408001 | 980.000000 |
| reacher_easy | single | defocus_blur | aco | 408002 | 971.000000 |
| reacher_easy | single | defocus_blur | aco | 408003 | 1000.000000 |
| reacher_easy | single | defocus_blur | aco | 408004 | 990.000000 |
| reacher_easy | single | frost | aco | 408000 | 958.000000 |
| reacher_easy | single | frost | aco | 408001 | 981.000000 |
| reacher_easy | single | frost | aco | 408002 | 976.000000 |
| reacher_easy | single | frost | aco | 408003 | 1000.000000 |
| reacher_easy | single | frost | aco | 408004 | 993.000000 |
| reacher_easy | single | occlusion_patch | aco | 408000 | 0.000000 |
| reacher_easy | single | occlusion_patch | aco | 408001 | 666.000000 |
| reacher_easy | single | occlusion_patch | aco | 408002 | 975.000000 |
| reacher_easy | single | occlusion_patch | aco | 408003 | 66.000000 |
| reacher_easy | single | occlusion_patch | aco | 408004 | 13.000000 |
| reacher_easy | single | saturation | aco | 408000 | 964.000000 |
| reacher_easy | single | saturation | aco | 408001 | 981.000000 |
| reacher_easy | single | saturation | aco | 408002 | 976.000000 |
| reacher_easy | single | saturation | aco | 408003 | 1000.000000 |
| reacher_easy | single | saturation | aco | 408004 | 993.000000 |
| reacher_easy | single | shadow | aco | 408000 | 956.000000 |
| reacher_easy | single | shadow | aco | 408001 | 7.000000 |
| reacher_easy | single | shadow | aco | 408002 | 975.000000 |
| reacher_easy | single | shadow | aco | 408003 | 1000.000000 |
| reacher_easy | single | shadow | aco | 408004 | 992.000000 |
| reacher_easy | single | shot_noise | aco | 408000 | 862.000000 |
| reacher_easy | single | shot_noise | aco | 408001 | 842.000000 |
| reacher_easy | single | shot_noise | aco | 408002 | 492.000000 |
| reacher_easy | single | shot_noise | aco | 408003 | 775.000000 |
| reacher_easy | single | shot_noise | aco | 408004 | 251.000000 |
| reacher_easy | markov | - | smfa | 408000 | 959.000000 |
| reacher_easy | markov | - | smfa | 408001 | 981.000000 |
| reacher_easy | markov | - | smfa | 408002 | 976.000000 |
| reacher_easy | markov | - | smfa | 408003 | 1000.000000 |
| reacher_easy | markov | - | smfa | 408004 | 993.000000 |
| reacher_easy | markov | - | smfa | 408005 | 944.000000 |
| reacher_easy | markov | - | smfa | 408006 | 966.000000 |
| reacher_easy | markov | - | smfa | 408007 | 970.000000 |
| reacher_easy | markov | - | smfa | 408008 | 967.000000 |
| reacher_easy | markov | - | smfa | 408009 | 965.000000 |
| reacher_easy | single | rain | smfa | 408000 | 962.000000 |
| reacher_easy | single | rain | smfa | 408001 | 981.000000 |
| reacher_easy | single | rain | smfa | 408002 | 976.000000 |
| reacher_easy | single | rain | smfa | 408003 | 1000.000000 |
| reacher_easy | single | rain | smfa | 408004 | 993.000000 |
| reacher_easy | single | fog | smfa | 408000 | 964.000000 |
| reacher_easy | single | fog | smfa | 408001 | 981.000000 |
| reacher_easy | single | fog | smfa | 408002 | 976.000000 |
| reacher_easy | single | fog | smfa | 408003 | 1000.000000 |
| reacher_easy | single | fog | smfa | 408004 | 993.000000 |
| reacher_easy | single | snow | smfa | 408000 | 958.000000 |
| reacher_easy | single | snow | smfa | 408001 | 981.000000 |
| reacher_easy | single | snow | smfa | 408002 | 976.000000 |
| reacher_easy | single | snow | smfa | 408003 | 1000.000000 |
| reacher_easy | single | snow | smfa | 408004 | 993.000000 |
| reacher_easy | single | motion_blur | smfa | 408000 | 0.000000 |
| reacher_easy | single | motion_blur | smfa | 408001 | 980.000000 |
| reacher_easy | single | motion_blur | smfa | 408002 | 969.000000 |
| reacher_easy | single | motion_blur | smfa | 408003 | 733.000000 |
| reacher_easy | single | motion_blur | smfa | 408004 | 984.000000 |
| reacher_easy | single | gaussian_noise | smfa | 408000 | 957.000000 |
| reacher_easy | single | gaussian_noise | smfa | 408001 | 981.000000 |
| reacher_easy | single | gaussian_noise | smfa | 408002 | 976.000000 |
| reacher_easy | single | gaussian_noise | smfa | 408003 | 1000.000000 |
| reacher_easy | single | gaussian_noise | smfa | 408004 | 993.000000 |
| reacher_easy | single | low_light | smfa | 408000 | 961.000000 |
| reacher_easy | single | low_light | smfa | 408001 | 981.000000 |
| reacher_easy | single | low_light | smfa | 408002 | 976.000000 |
| reacher_easy | single | low_light | smfa | 408003 | 1000.000000 |
| reacher_easy | single | low_light | smfa | 408004 | 992.000000 |
| reacher_easy | single | jpeg | smfa | 408000 | 958.000000 |
| reacher_easy | single | jpeg | smfa | 408001 | 981.000000 |
| reacher_easy | single | jpeg | smfa | 408002 | 975.000000 |
| reacher_easy | single | jpeg | smfa | 408003 | 1000.000000 |
| reacher_easy | single | jpeg | smfa | 408004 | 993.000000 |
| reacher_easy | single | defocus_blur | smfa | 408000 | 0.000000 |
| reacher_easy | single | defocus_blur | smfa | 408001 | 979.000000 |
| reacher_easy | single | defocus_blur | smfa | 408002 | 975.000000 |
| reacher_easy | single | defocus_blur | smfa | 408003 | 997.000000 |
| reacher_easy | single | defocus_blur | smfa | 408004 | 993.000000 |
| reacher_easy | single | frost | smfa | 408000 | 960.000000 |
| reacher_easy | single | frost | smfa | 408001 | 981.000000 |
| reacher_easy | single | frost | smfa | 408002 | 975.000000 |
| reacher_easy | single | frost | smfa | 408003 | 1000.000000 |
| reacher_easy | single | frost | smfa | 408004 | 993.000000 |
| reacher_easy | single | occlusion_patch | smfa | 408000 | 0.000000 |
| reacher_easy | single | occlusion_patch | smfa | 408001 | 433.000000 |
| reacher_easy | single | occlusion_patch | smfa | 408002 | 976.000000 |
| reacher_easy | single | occlusion_patch | smfa | 408003 | 9.000000 |
| reacher_easy | single | occlusion_patch | smfa | 408004 | 26.000000 |
| reacher_easy | single | saturation | smfa | 408000 | 961.000000 |
| reacher_easy | single | saturation | smfa | 408001 | 981.000000 |
| reacher_easy | single | saturation | smfa | 408002 | 976.000000 |
| reacher_easy | single | saturation | smfa | 408003 | 1000.000000 |
| reacher_easy | single | saturation | smfa | 408004 | 993.000000 |
| reacher_easy | single | shadow | smfa | 408000 | 958.000000 |
| reacher_easy | single | shadow | smfa | 408001 | 981.000000 |
| reacher_easy | single | shadow | smfa | 408002 | 976.000000 |
| reacher_easy | single | shadow | smfa | 408003 | 1000.000000 |
| reacher_easy | single | shadow | smfa | 408004 | 993.000000 |
| reacher_easy | single | shot_noise | smfa | 408000 | 961.000000 |
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
| reacher_hard | markov | - | aco | 409000 | 28.000000 |
| reacher_hard | markov | - | aco | 409001 | 0.000000 |
| reacher_hard | markov | - | aco | 409002 | 0.000000 |
| reacher_hard | markov | - | aco | 409003 | 0.000000 |
| reacher_hard | markov | - | aco | 409004 | 0.000000 |
| reacher_hard | markov | - | aco | 409005 | 2.000000 |
| reacher_hard | markov | - | aco | 409006 | 3.000000 |
| reacher_hard | markov | - | aco | 409007 | 0.000000 |
| reacher_hard | markov | - | aco | 409008 | 0.000000 |
| reacher_hard | markov | - | aco | 409009 | 81.000000 |
| reacher_hard | single | rain | aco | 409000 | 51.000000 |
| reacher_hard | single | rain | aco | 409001 | 0.000000 |
| reacher_hard | single | rain | aco | 409002 | 4.000000 |
| reacher_hard | single | rain | aco | 409003 | 0.000000 |
| reacher_hard | single | rain | aco | 409004 | 0.000000 |
| reacher_hard | single | fog | aco | 409000 | 44.000000 |
| reacher_hard | single | fog | aco | 409001 | 0.000000 |
| reacher_hard | single | fog | aco | 409002 | 0.000000 |
| reacher_hard | single | fog | aco | 409003 | 0.000000 |
| reacher_hard | single | fog | aco | 409004 | 0.000000 |
| reacher_hard | single | snow | aco | 409000 | 41.000000 |
| reacher_hard | single | snow | aco | 409001 | 0.000000 |
| reacher_hard | single | snow | aco | 409002 | 3.000000 |
| reacher_hard | single | snow | aco | 409003 | 0.000000 |
| reacher_hard | single | snow | aco | 409004 | 0.000000 |
| reacher_hard | single | motion_blur | aco | 409000 | 2.000000 |
| reacher_hard | single | motion_blur | aco | 409001 | 0.000000 |
| reacher_hard | single | motion_blur | aco | 409002 | 0.000000 |
| reacher_hard | single | motion_blur | aco | 409003 | 3.000000 |
| reacher_hard | single | motion_blur | aco | 409004 | 0.000000 |
| reacher_hard | single | gaussian_noise | aco | 409000 | 0.000000 |
| reacher_hard | single | gaussian_noise | aco | 409001 | 0.000000 |
| reacher_hard | single | gaussian_noise | aco | 409002 | 0.000000 |
| reacher_hard | single | gaussian_noise | aco | 409003 | 4.000000 |
| reacher_hard | single | gaussian_noise | aco | 409004 | 0.000000 |
| reacher_hard | single | low_light | aco | 409000 | 15.000000 |
| reacher_hard | single | low_light | aco | 409001 | 5.000000 |
| reacher_hard | single | low_light | aco | 409002 | 4.000000 |
| reacher_hard | single | low_light | aco | 409003 | 4.000000 |
| reacher_hard | single | low_light | aco | 409004 | 0.000000 |
| reacher_hard | single | jpeg | aco | 409000 | 0.000000 |
| reacher_hard | single | jpeg | aco | 409001 | 0.000000 |
| reacher_hard | single | jpeg | aco | 409002 | 2.000000 |
| reacher_hard | single | jpeg | aco | 409003 | 0.000000 |
| reacher_hard | single | jpeg | aco | 409004 | 7.000000 |
| reacher_hard | single | defocus_blur | aco | 409000 | 0.000000 |
| reacher_hard | single | defocus_blur | aco | 409001 | 0.000000 |
| reacher_hard | single | defocus_blur | aco | 409002 | 0.000000 |
| reacher_hard | single | defocus_blur | aco | 409003 | 3.000000 |
| reacher_hard | single | defocus_blur | aco | 409004 | 1.000000 |
| reacher_hard | single | frost | aco | 409000 | 36.000000 |
| reacher_hard | single | frost | aco | 409001 | 0.000000 |
| reacher_hard | single | frost | aco | 409002 | 3.000000 |
| reacher_hard | single | frost | aco | 409003 | 0.000000 |
| reacher_hard | single | frost | aco | 409004 | 0.000000 |
| reacher_hard | single | occlusion_patch | aco | 409000 | 6.000000 |
| reacher_hard | single | occlusion_patch | aco | 409001 | 0.000000 |
| reacher_hard | single | occlusion_patch | aco | 409002 | 0.000000 |
| reacher_hard | single | occlusion_patch | aco | 409003 | 23.000000 |
| reacher_hard | single | occlusion_patch | aco | 409004 | 8.000000 |
| reacher_hard | single | saturation | aco | 409000 | 51.000000 |
| reacher_hard | single | saturation | aco | 409001 | 0.000000 |
| reacher_hard | single | saturation | aco | 409002 | 0.000000 |
| reacher_hard | single | saturation | aco | 409003 | 0.000000 |
| reacher_hard | single | saturation | aco | 409004 | 0.000000 |
| reacher_hard | single | shadow | aco | 409000 | 11.000000 |
| reacher_hard | single | shadow | aco | 409001 | 0.000000 |
| reacher_hard | single | shadow | aco | 409002 | 1.000000 |
| reacher_hard | single | shadow | aco | 409003 | 453.000000 |
| reacher_hard | single | shadow | aco | 409004 | 0.000000 |
| reacher_hard | single | shot_noise | aco | 409000 | 0.000000 |
| reacher_hard | single | shot_noise | aco | 409001 | 0.000000 |
| reacher_hard | single | shot_noise | aco | 409002 | 0.000000 |
| reacher_hard | single | shot_noise | aco | 409003 | 4.000000 |
| reacher_hard | single | shot_noise | aco | 409004 | 0.000000 |
| reacher_hard | markov | - | smfa | 409000 | 35.000000 |
| reacher_hard | markov | - | smfa | 409001 | 0.000000 |
| reacher_hard | markov | - | smfa | 409002 | 4.000000 |
| reacher_hard | markov | - | smfa | 409003 | 0.000000 |
| reacher_hard | markov | - | smfa | 409004 | 0.000000 |
| reacher_hard | markov | - | smfa | 409005 | 10.000000 |
| reacher_hard | markov | - | smfa | 409006 | 13.000000 |
| reacher_hard | markov | - | smfa | 409007 | 2.000000 |
| reacher_hard | markov | - | smfa | 409008 | 0.000000 |
| reacher_hard | markov | - | smfa | 409009 | 0.000000 |
| reacher_hard | single | rain | smfa | 409000 | 40.000000 |
| reacher_hard | single | rain | smfa | 409001 | 0.000000 |
| reacher_hard | single | rain | smfa | 409002 | 0.000000 |
| reacher_hard | single | rain | smfa | 409003 | 0.000000 |
| reacher_hard | single | rain | smfa | 409004 | 4.000000 |
| reacher_hard | single | fog | smfa | 409000 | 39.000000 |
| reacher_hard | single | fog | smfa | 409001 | 0.000000 |
| reacher_hard | single | fog | smfa | 409002 | 2.000000 |
| reacher_hard | single | fog | smfa | 409003 | 0.000000 |
| reacher_hard | single | fog | smfa | 409004 | 4.000000 |
| reacher_hard | single | snow | smfa | 409000 | 39.000000 |
| reacher_hard | single | snow | smfa | 409001 | 0.000000 |
| reacher_hard | single | snow | smfa | 409002 | 2.000000 |
| reacher_hard | single | snow | smfa | 409003 | 0.000000 |
| reacher_hard | single | snow | smfa | 409004 | 4.000000 |
| reacher_hard | single | motion_blur | smfa | 409000 | 1.000000 |
| reacher_hard | single | motion_blur | smfa | 409001 | 0.000000 |
| reacher_hard | single | motion_blur | smfa | 409002 | 0.000000 |
| reacher_hard | single | motion_blur | smfa | 409003 | 2.000000 |
| reacher_hard | single | motion_blur | smfa | 409004 | 0.000000 |
| reacher_hard | single | gaussian_noise | smfa | 409000 | 41.000000 |
| reacher_hard | single | gaussian_noise | smfa | 409001 | 0.000000 |
| reacher_hard | single | gaussian_noise | smfa | 409002 | 0.000000 |
| reacher_hard | single | gaussian_noise | smfa | 409003 | 0.000000 |
| reacher_hard | single | gaussian_noise | smfa | 409004 | 4.000000 |
| reacher_hard | single | low_light | smfa | 409000 | 48.000000 |
| reacher_hard | single | low_light | smfa | 409001 | 0.000000 |
| reacher_hard | single | low_light | smfa | 409002 | 2.000000 |
| reacher_hard | single | low_light | smfa | 409003 | 0.000000 |
| reacher_hard | single | low_light | smfa | 409004 | 12.000000 |
| reacher_hard | single | jpeg | smfa | 409000 | 19.000000 |
| reacher_hard | single | jpeg | smfa | 409001 | 0.000000 |
| reacher_hard | single | jpeg | smfa | 409002 | 0.000000 |
| reacher_hard | single | jpeg | smfa | 409003 | 0.000000 |
| reacher_hard | single | jpeg | smfa | 409004 | 0.000000 |
| reacher_hard | single | defocus_blur | smfa | 409000 | 4.000000 |
| reacher_hard | single | defocus_blur | smfa | 409001 | 0.000000 |
| reacher_hard | single | defocus_blur | smfa | 409002 | 3.000000 |
| reacher_hard | single | defocus_blur | smfa | 409003 | 1.000000 |
| reacher_hard | single | defocus_blur | smfa | 409004 | 1.000000 |
| reacher_hard | single | frost | smfa | 409000 | 39.000000 |
| reacher_hard | single | frost | smfa | 409001 | 0.000000 |
| reacher_hard | single | frost | smfa | 409002 | 0.000000 |
| reacher_hard | single | frost | smfa | 409003 | 0.000000 |
| reacher_hard | single | frost | smfa | 409004 | 4.000000 |
| reacher_hard | single | occlusion_patch | smfa | 409000 | 28.000000 |
| reacher_hard | single | occlusion_patch | smfa | 409001 | 0.000000 |
| reacher_hard | single | occlusion_patch | smfa | 409002 | 0.000000 |
| reacher_hard | single | occlusion_patch | smfa | 409003 | 0.000000 |
| reacher_hard | single | occlusion_patch | smfa | 409004 | 0.000000 |
| reacher_hard | single | saturation | smfa | 409000 | 41.000000 |
| reacher_hard | single | saturation | smfa | 409001 | 0.000000 |
| reacher_hard | single | saturation | smfa | 409002 | 0.000000 |
| reacher_hard | single | saturation | smfa | 409003 | 0.000000 |
| reacher_hard | single | saturation | smfa | 409004 | 0.000000 |
| reacher_hard | single | shadow | smfa | 409000 | 44.000000 |
| reacher_hard | single | shadow | smfa | 409001 | 0.000000 |
| reacher_hard | single | shadow | smfa | 409002 | 0.000000 |
| reacher_hard | single | shadow | smfa | 409003 | 0.000000 |
| reacher_hard | single | shadow | smfa | 409004 | 4.000000 |
| reacher_hard | single | shot_noise | smfa | 409000 | 39.000000 |
| reacher_hard | single | shot_noise | smfa | 409001 | 0.000000 |
| reacher_hard | single | shot_noise | smfa | 409002 | 0.000000 |
| reacher_hard | single | shot_noise | smfa | 409003 | 0.000000 |
| reacher_hard | single | shot_noise | smfa | 409004 | 0.000000 |
