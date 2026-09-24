# Full13 seed6 results

All 13 types are training-seen. Former OOD6 use fallback_v1; this is not a zero-shot OOD experiment.

One training seed per model. +/- denotes episode SD, not training-seed uncertainty. Pooled cross-task SD also contains task differences.

## Overall control

| Protocol | Raw | ACO | SMFA |
|---|---:|---:|---:|
| markov | 483.41 +/- 353.71 (n=100) | 358.80 +/- 328.02 (n=100) | 645.80 +/- 327.48 (n=100) |
| single/all | 460.57 +/- 396.01 (n=650) | 388.50 +/- 386.97 (n=650) | 651.63 +/- 378.03 (n=650) |

Clean: 734.21 +/- 334.50 (n=50)

## Image restoration

| Model / group | n | PSNR-Y | SSIM-Y | PSNR-RGB | SSIM-RGB |
|---|---:|---:|---:|---:|---:|
| aco/all | 130000 | 24.4800 | 0.754934 | 19.3917 | 0.595975 |
| aco/task/walker_walk | 13000 | 24.2282 | 0.774318 | 19.0375 | 0.606000 |
| aco/degradation/rain | 10000 | 22.1602 | 0.539328 | 20.1313 | 0.382329 |
| aco/walker_walk/rain | 1000 | 21.8979 | 0.602340 | 19.9309 | 0.430957 |
| aco/degradation/fog | 10000 | 27.4638 | 0.967346 | 17.4204 | 0.847196 |
| aco/walker_walk/fog | 1000 | 27.5228 | 0.964271 | 17.7937 | 0.845182 |
| aco/degradation/snow | 10000 | 19.3265 | 0.495498 | 17.8226 | 0.302724 |
| aco/walker_walk/snow | 1000 | 19.4108 | 0.571388 | 17.9046 | 0.363402 |
| aco/degradation/motion_blur | 10000 | 24.0530 | 0.824313 | 21.9084 | 0.784068 |
| aco/walker_walk/motion_blur | 1000 | 21.9246 | 0.796726 | 20.1862 | 0.752463 |
| aco/degradation/gaussian_noise | 10000 | 24.6329 | 0.546950 | 17.2431 | 0.218922 |
| aco/walker_walk/gaussian_noise | 1000 | 24.7976 | 0.603151 | 17.4666 | 0.266438 |
| aco/degradation/low_light | 10000 | 16.1994 | 0.539996 | 14.8287 | 0.266051 |
| aco/walker_walk/low_light | 1000 | 16.5137 | 0.554476 | 14.9426 | 0.238355 |
| aco/degradation/jpeg | 10000 | 26.4073 | 0.871321 | 19.9188 | 0.666406 |
| aco/walker_walk/jpeg | 1000 | 25.8647 | 0.866797 | 19.9154 | 0.634232 |
| aco/degradation/defocus_blur | 10000 | 24.3521 | 0.845165 | 22.2661 | 0.801883 |
| aco/walker_walk/defocus_blur | 1000 | 21.9592 | 0.820708 | 20.3038 | 0.772285 |
| aco/degradation/frost | 10000 | 29.7178 | 0.926858 | 19.3490 | 0.774488 |
| aco/walker_walk/frost | 1000 | 32.3638 | 0.950652 | 17.7015 | 0.814700 |
| aco/degradation/occlusion_patch | 10000 | 27.3131 | 0.882420 | 25.1816 | 0.872664 |
| aco/walker_walk/occlusion_patch | 1000 | 26.5632 | 0.886184 | 24.5029 | 0.869510 |
| aco/degradation/saturation | 10000 | 27.0142 | 0.954929 | 18.2352 | 0.762988 |
| aco/walker_walk/saturation | 1000 | 25.5179 | 0.944093 | 18.5562 | 0.759058 |
| aco/degradation/shadow | 10000 | 25.4979 | 0.944751 | 21.2887 | 0.892572 |
| aco/walker_walk/shadow | 1000 | 26.3075 | 0.956844 | 21.5761 | 0.906548 |
| aco/degradation/shot_noise | 10000 | 24.1017 | 0.475271 | 16.4985 | 0.175383 |
| aco/walker_walk/shot_noise | 1000 | 24.3228 | 0.548501 | 16.7072 | 0.224864 |
| aco/task/walker_run | 13000 | 24.2126 | 0.774357 | 19.0396 | 0.604756 |
| aco/walker_run/rain | 1000 | 21.9053 | 0.603925 | 19.9382 | 0.431442 |
| aco/walker_run/fog | 1000 | 27.4695 | 0.964424 | 17.8064 | 0.844710 |
| aco/walker_run/snow | 1000 | 19.4294 | 0.574518 | 17.9260 | 0.365267 |
| aco/walker_run/motion_blur | 1000 | 21.8239 | 0.790940 | 20.0790 | 0.745988 |
| aco/walker_run/gaussian_noise | 1000 | 24.8183 | 0.605932 | 17.4988 | 0.269580 |
| aco/walker_run/low_light | 1000 | 16.5909 | 0.556406 | 15.0231 | 0.237739 |
| aco/walker_run/jpeg | 1000 | 25.8165 | 0.864270 | 19.9262 | 0.626763 |
| aco/walker_run/defocus_blur | 1000 | 21.8847 | 0.818449 | 20.2253 | 0.768731 |
| aco/walker_run/frost | 1000 | 32.3933 | 0.950355 | 17.7387 | 0.813681 |
| aco/walker_run/occlusion_patch | 1000 | 26.4771 | 0.883458 | 24.4335 | 0.866888 |
| aco/walker_run/saturation | 1000 | 25.4547 | 0.942739 | 18.5569 | 0.755462 |
| aco/walker_run/shadow | 1000 | 26.3196 | 0.956796 | 21.6052 | 0.905934 |
| aco/walker_run/shot_noise | 1000 | 24.3799 | 0.554426 | 16.7570 | 0.229645 |
| aco/task/walker_stand | 13000 | 24.3409 | 0.779456 | 19.1942 | 0.603009 |
| aco/walker_stand/rain | 1000 | 22.1158 | 0.603705 | 20.1336 | 0.419799 |
| aco/walker_stand/fog | 1000 | 26.8753 | 0.962617 | 17.7021 | 0.839108 |
| aco/walker_stand/snow | 1000 | 19.6975 | 0.576757 | 18.1999 | 0.357667 |
| aco/walker_stand/motion_blur | 1000 | 21.9479 | 0.807777 | 20.2335 | 0.762351 |
| aco/walker_stand/gaussian_noise | 1000 | 25.1225 | 0.608681 | 17.7014 | 0.266155 |
| aco/walker_stand/low_light | 1000 | 16.9942 | 0.577762 | 15.4511 | 0.255257 |
| aco/walker_stand/jpeg | 1000 | 26.0035 | 0.866977 | 20.0610 | 0.615500 |
| aco/walker_stand/defocus_blur | 1000 | 21.9509 | 0.831638 | 20.3008 | 0.780898 |
| aco/walker_stand/frost | 1000 | 32.6568 | 0.948811 | 17.7799 | 0.801420 |
| aco/walker_stand/occlusion_patch | 1000 | 26.5484 | 0.883629 | 24.4654 | 0.862872 |
| aco/walker_stand/saturation | 1000 | 25.2905 | 0.942983 | 18.6510 | 0.743902 |
| aco/walker_stand/shadow | 1000 | 26.5127 | 0.957747 | 21.8135 | 0.903970 |
| aco/walker_stand/shot_noise | 1000 | 24.7161 | 0.563842 | 17.0319 | 0.230210 |
| aco/task/hopper_stand | 13000 | 24.3443 | 0.737911 | 19.5743 | 0.596385 |
| aco/hopper_stand/rain | 1000 | 21.1392 | 0.466899 | 19.2532 | 0.331760 |
| aco/hopper_stand/fog | 1000 | 26.3911 | 0.970811 | 17.2606 | 0.879366 |
| aco/hopper_stand/snow | 1000 | 18.6064 | 0.443299 | 17.1643 | 0.268554 |
| aco/hopper_stand/motion_blur | 1000 | 25.2996 | 0.858997 | 23.2157 | 0.820775 |
| aco/hopper_stand/gaussian_noise | 1000 | 24.9519 | 0.514737 | 17.3249 | 0.194708 |
| aco/hopper_stand/low_light | 1000 | 15.1016 | 0.522116 | 14.0513 | 0.288015 |
| aco/hopper_stand/jpeg | 1000 | 28.2145 | 0.870740 | 20.8954 | 0.690659 |
| aco/hopper_stand/defocus_blur | 1000 | 25.5704 | 0.870647 | 23.5635 | 0.827817 |
| aco/hopper_stand/frost | 1000 | 26.4510 | 0.875595 | 21.0327 | 0.739875 |
| aco/hopper_stand/occlusion_patch | 1000 | 27.8858 | 0.876939 | 25.7459 | 0.873780 |
| aco/hopper_stand/saturation | 1000 | 26.7070 | 0.957594 | 17.6080 | 0.796919 |
| aco/hopper_stand/shadow | 1000 | 26.1045 | 0.953013 | 21.0870 | 0.902359 |
| aco/hopper_stand/shot_noise | 1000 | 24.0526 | 0.411452 | 16.2641 | 0.138422 |
| aco/task/quadruped_run | 13000 | 24.8520 | 0.754705 | 19.4558 | 0.599158 |
| aco/quadruped_run/rain | 1000 | 21.9428 | 0.507740 | 20.0323 | 0.361964 |
| aco/quadruped_run/fog | 1000 | 27.6813 | 0.958235 | 17.8948 | 0.820997 |
| aco/quadruped_run/snow | 1000 | 19.2316 | 0.490719 | 17.7936 | 0.297412 |
| aco/quadruped_run/motion_blur | 1000 | 23.2846 | 0.754293 | 21.3243 | 0.703877 |
| aco/quadruped_run/gaussian_noise | 1000 | 25.2539 | 0.605897 | 17.6523 | 0.267583 |
| aco/quadruped_run/low_light | 1000 | 16.6886 | 0.564066 | 15.4298 | 0.332389 |
| aco/quadruped_run/jpeg | 1000 | 27.3022 | 0.872425 | 20.5642 | 0.683741 |
| aco/quadruped_run/defocus_blur | 1000 | 23.7176 | 0.776863 | 21.8321 | 0.722853 |
| aco/quadruped_run/frost | 1000 | 32.6016 | 0.954311 | 17.5603 | 0.821174 |
| aco/quadruped_run/occlusion_patch | 1000 | 27.0251 | 0.881246 | 24.8773 | 0.868184 |
| aco/quadruped_run/saturation | 1000 | 26.5847 | 0.944856 | 19.1254 | 0.789289 |
| aco/quadruped_run/shadow | 1000 | 27.1038 | 0.956809 | 21.9914 | 0.905903 |
| aco/quadruped_run/shot_noise | 1000 | 24.6584 | 0.543711 | 16.8470 | 0.213683 |
| aco/task/finger_turn_hard | 13000 | 24.3434 | 0.764183 | 19.1716 | 0.581736 |
| aco/finger_turn_hard/rain | 1000 | 21.9569 | 0.603043 | 20.0302 | 0.424530 |
| aco/finger_turn_hard/fog | 1000 | 26.5762 | 0.960804 | 17.4887 | 0.838139 |
| aco/finger_turn_hard/snow | 1000 | 19.6482 | 0.572722 | 18.1183 | 0.361675 |
| aco/finger_turn_hard/motion_blur | 1000 | 22.2478 | 0.769213 | 20.4509 | 0.721384 |
| aco/finger_turn_hard/gaussian_noise | 1000 | 25.1370 | 0.583254 | 17.3377 | 0.220518 |
| aco/finger_turn_hard/low_light | 1000 | 17.0771 | 0.528651 | 15.1946 | 0.196654 |
| aco/finger_turn_hard/jpeg | 1000 | 26.2900 | 0.855050 | 18.8657 | 0.581073 |
| aco/finger_turn_hard/defocus_blur | 1000 | 22.5531 | 0.802770 | 20.8278 | 0.751473 |
| aco/finger_turn_hard/frost | 1000 | 30.0443 | 0.931489 | 18.4097 | 0.759386 |
| aco/finger_turn_hard/occlusion_patch | 1000 | 26.9925 | 0.889243 | 24.8438 | 0.872169 |
| aco/finger_turn_hard/saturation | 1000 | 26.4552 | 0.949051 | 19.0017 | 0.743856 |
| aco/finger_turn_hard/shadow | 1000 | 26.8001 | 0.955215 | 21.8651 | 0.903577 |
| aco/finger_turn_hard/shot_noise | 1000 | 24.6852 | 0.533875 | 16.7971 | 0.188129 |
| aco/task/cartpole_swingup_sparse | 13000 | 24.2636 | 0.723710 | 19.4115 | 0.585684 |
| aco/cartpole_swingup_sparse/rain | 1000 | 21.1371 | 0.470009 | 19.3085 | 0.359206 |
| aco/cartpole_swingup_sparse/fog | 1000 | 26.4683 | 0.960227 | 17.1760 | 0.866284 |
| aco/cartpole_swingup_sparse/snow | 1000 | 18.4764 | 0.444124 | 17.0559 | 0.290356 |
| aco/cartpole_swingup_sparse/motion_blur | 1000 | 25.0215 | 0.780033 | 22.5879 | 0.739357 |
| aco/cartpole_swingup_sparse/gaussian_noise | 1000 | 24.8647 | 0.528225 | 17.0491 | 0.199968 |
| aco/cartpole_swingup_sparse/low_light | 1000 | 14.9981 | 0.502604 | 13.9653 | 0.291272 |
| aco/cartpole_swingup_sparse/jpeg | 1000 | 27.8184 | 0.864751 | 19.9216 | 0.687586 |
| aco/cartpole_swingup_sparse/defocus_blur | 1000 | 25.2191 | 0.788399 | 22.8508 | 0.747553 |
| aco/cartpole_swingup_sparse/frost | 1000 | 24.9842 | 0.840941 | 21.4858 | 0.708847 |
| aco/cartpole_swingup_sparse/occlusion_patch | 1000 | 28.1119 | 0.888994 | 25.9383 | 0.883967 |
| aco/cartpole_swingup_sparse/saturation | 1000 | 28.2619 | 0.956960 | 17.8912 | 0.791191 |
| aco/cartpole_swingup_sparse/shadow | 1000 | 26.0609 | 0.949038 | 21.0247 | 0.900501 |
| aco/cartpole_swingup_sparse/shot_noise | 1000 | 24.0041 | 0.433923 | 16.0943 | 0.147813 |
| aco/task/cup_catch | 13000 | 25.5869 | 0.752529 | 20.0194 | 0.582539 |
| aco/cup_catch/rain | 1000 | 21.7492 | 0.517128 | 20.0050 | 0.319305 |
| aco/cup_catch/fog | 1000 | 26.8153 | 0.962628 | 17.3675 | 0.828205 |
| aco/cup_catch/snow | 1000 | 19.4858 | 0.492966 | 18.1308 | 0.261919 |
| aco/cup_catch/motion_blur | 1000 | 26.7203 | 0.859052 | 24.4241 | 0.817740 |
| aco/cup_catch/gaussian_noise | 1000 | 25.5400 | 0.503606 | 17.7105 | 0.151363 |
| aco/cup_catch/low_light | 1000 | 17.1635 | 0.529755 | 16.0412 | 0.253461 |
| aco/cup_catch/jpeg | 1000 | 27.2960 | 0.856582 | 20.0641 | 0.664863 |
| aco/cup_catch/defocus_blur | 1000 | 26.9656 | 0.867342 | 24.7350 | 0.823659 |
| aco/cup_catch/frost | 1000 | 33.6792 | 0.948083 | 17.3761 | 0.795910 |
| aco/cup_catch/occlusion_patch | 1000 | 27.8522 | 0.880379 | 25.8028 | 0.863388 |
| aco/cup_catch/saturation | 1000 | 25.9353 | 0.949986 | 18.8536 | 0.763458 |
| aco/cup_catch/shadow | 1000 | 28.2178 | 0.963053 | 22.5669 | 0.906411 |
| aco/cup_catch/shot_noise | 1000 | 25.2097 | 0.452322 | 17.1752 | 0.123325 |
| aco/task/reacher_easy | 13000 | 24.2792 | 0.744733 | 19.4609 | 0.601191 |
| aco/reacher_easy/rain | 1000 | 23.8855 | 0.514680 | 21.3133 | 0.379763 |
| aco/reacher_easy/fog | 1000 | 29.2180 | 0.983392 | 16.8900 | 0.855445 |
| aco/reacher_easy/snow | 1000 | 19.6766 | 0.400815 | 17.9724 | 0.238371 |
| aco/reacher_easy/motion_blur | 1000 | 25.7671 | 0.908740 | 22.9857 | 0.883169 |
| aco/reacher_easy/gaussian_noise | 1000 | 22.9710 | 0.464439 | 16.3028 | 0.180022 |
| aco/reacher_easy/low_light | 1000 | 15.4742 | 0.534808 | 14.0724 | 0.288161 |
| aco/reacher_easy/jpeg | 1000 | 24.9009 | 0.890711 | 19.6966 | 0.739270 |
| aco/reacher_easy/defocus_blur | 1000 | 26.5500 | 0.932793 | 23.7739 | 0.906061 |
| aco/reacher_easy/frost | 1000 | 26.0177 | 0.934820 | 22.1407 | 0.746984 |
| aco/reacher_easy/occlusion_patch | 1000 | 27.7459 | 0.877113 | 25.4178 | 0.882201 |
| aco/reacher_easy/saturation | 1000 | 30.1290 | 0.979229 | 17.1641 | 0.739847 |
| aco/reacher_easy/shadow | 1000 | 20.7716 | 0.898776 | 19.6542 | 0.844958 |
| aco/reacher_easy/shot_noise | 1000 | 22.5222 | 0.361212 | 15.6084 | 0.131226 |
| aco/task/reacher_hard | 13000 | 24.3490 | 0.743441 | 19.5522 | 0.599292 |
| aco/reacher_hard/rain | 1000 | 23.8721 | 0.503816 | 21.3683 | 0.364561 |
| aco/reacher_hard/fog | 1000 | 29.6202 | 0.986047 | 16.8237 | 0.854520 |
| aco/reacher_hard/snow | 1000 | 19.6023 | 0.387670 | 17.9601 | 0.222613 |
| aco/reacher_hard/motion_blur | 1000 | 26.4927 | 0.917364 | 23.5966 | 0.893577 |
| aco/reacher_hard/gaussian_noise | 1000 | 22.8720 | 0.451576 | 16.3864 | 0.172887 |
| aco/reacher_hard/low_light | 1000 | 15.3919 | 0.529312 | 14.1156 | 0.279209 |
| aco/reacher_hard/jpeg | 1000 | 24.5663 | 0.904911 | 19.2783 | 0.740372 |
| aco/reacher_hard/defocus_blur | 1000 | 27.1506 | 0.942042 | 24.2477 | 0.917500 |
| aco/reacher_hard/frost | 1000 | 25.9866 | 0.933519 | 22.2649 | 0.742898 |
| aco/reacher_hard/occlusion_patch | 1000 | 27.9291 | 0.877020 | 25.7886 | 0.883681 |
| aco/reacher_hard/saturation | 1000 | 29.8063 | 0.981794 | 16.9438 | 0.746899 |
| aco/reacher_hard/shadow | 1000 | 20.7809 | 0.900221 | 19.7027 | 0.845564 |
| aco/reacher_hard/shot_noise | 1000 | 22.4663 | 0.349445 | 15.7026 | 0.126515 |
| aco/clean_input | 10000 | 28.4413 | 0.947924 | 22.6828 | 0.826738 |
| aco/original7 | 70000 | 22.8919 | 0.683536 | 18.4676 | 0.495385 |
| aco/added6 | 60000 | 26.3328 | 0.838232 | 20.4698 | 0.713330 |
| smfa/all | 130000 | 34.5949 | 0.928920 | 32.1625 | 0.903633 |
| smfa/task/walker_walk | 13000 | 33.4013 | 0.922238 | 31.2010 | 0.897963 |
| smfa/degradation/rain | 10000 | 35.8515 | 0.948587 | 34.2847 | 0.931326 |
| smfa/walker_walk/rain | 1000 | 34.2585 | 0.938975 | 32.8008 | 0.919903 |
| smfa/degradation/fog | 10000 | 40.7628 | 0.989819 | 38.5458 | 0.982565 |
| smfa/walker_walk/fog | 1000 | 40.2042 | 0.989477 | 38.1662 | 0.982566 |
| smfa/degradation/snow | 10000 | 34.1649 | 0.925931 | 32.5979 | 0.900130 |
| smfa/walker_walk/snow | 1000 | 32.3829 | 0.912076 | 30.9617 | 0.883258 |
| smfa/degradation/motion_blur | 10000 | 27.5603 | 0.812629 | 25.4955 | 0.792254 |
| smfa/walker_walk/motion_blur | 1000 | 25.3387 | 0.770983 | 23.5551 | 0.754516 |
| smfa/degradation/gaussian_noise | 10000 | 37.1776 | 0.945173 | 34.2988 | 0.912896 |
| smfa/walker_walk/gaussian_noise | 1000 | 36.4979 | 0.945566 | 33.7517 | 0.912465 |
| smfa/degradation/low_light | 10000 | 32.4498 | 0.899918 | 29.8565 | 0.844164 |
| smfa/walker_walk/low_light | 1000 | 31.9102 | 0.909816 | 29.4997 | 0.859111 |
| smfa/degradation/jpeg | 10000 | 34.2535 | 0.937188 | 30.6630 | 0.895409 |
| smfa/walker_walk/jpeg | 1000 | 33.1545 | 0.935609 | 29.8368 | 0.892532 |
| smfa/degradation/defocus_blur | 10000 | 28.2406 | 0.828109 | 26.2189 | 0.804799 |
| smfa/walker_walk/defocus_blur | 1000 | 26.4669 | 0.800297 | 24.7443 | 0.777904 |
| smfa/degradation/frost | 10000 | 36.7972 | 0.967336 | 34.9292 | 0.952526 |
| smfa/walker_walk/frost | 1000 | 35.6909 | 0.965586 | 33.9339 | 0.950148 |
| smfa/degradation/occlusion_patch | 10000 | 32.5234 | 0.932993 | 30.0018 | 0.916051 |
| smfa/walker_walk/occlusion_patch | 1000 | 29.9896 | 0.920889 | 27.9531 | 0.907558 |
| smfa/degradation/saturation | 10000 | 41.5375 | 0.993144 | 37.9767 | 0.982273 |
| smfa/walker_walk/saturation | 1000 | 40.8020 | 0.993323 | 37.6899 | 0.983880 |
| smfa/degradation/shadow | 10000 | 33.2783 | 0.973644 | 30.9330 | 0.956719 |
| smfa/walker_walk/shadow | 1000 | 33.3401 | 0.978718 | 31.2079 | 0.965349 |
| smfa/degradation/shot_noise | 10000 | 35.1360 | 0.921485 | 32.3114 | 0.876119 |
| smfa/walker_walk/shot_noise | 1000 | 34.1810 | 0.927775 | 31.5118 | 0.884333 |
| smfa/task/walker_run | 13000 | 33.2853 | 0.920791 | 31.0874 | 0.895946 |
| smfa/walker_run/rain | 1000 | 34.1224 | 0.937310 | 32.6611 | 0.917898 |
| smfa/walker_run/fog | 1000 | 40.2134 | 0.989632 | 38.1795 | 0.982778 |
| smfa/walker_run/snow | 1000 | 32.2597 | 0.910042 | 30.8410 | 0.880898 |
| smfa/walker_run/motion_blur | 1000 | 25.0750 | 0.763977 | 23.3233 | 0.746265 |
| smfa/walker_run/gaussian_noise | 1000 | 36.2142 | 0.944757 | 33.4759 | 0.910860 |
| smfa/walker_run/low_light | 1000 | 31.8346 | 0.909881 | 29.4440 | 0.859290 |
| smfa/walker_run/jpeg | 1000 | 32.9850 | 0.933808 | 29.6687 | 0.888961 |
| smfa/walker_run/defocus_blur | 1000 | 26.2607 | 0.795590 | 24.5594 | 0.771337 |
| smfa/walker_run/frost | 1000 | 35.3144 | 0.964888 | 33.5411 | 0.948728 |
| smfa/walker_run/occlusion_patch | 1000 | 29.7957 | 0.919884 | 27.7868 | 0.906562 |
| smfa/walker_run/saturation | 1000 | 40.8757 | 0.993303 | 37.7199 | 0.983718 |
| smfa/walker_run/shadow | 1000 | 33.7467 | 0.979596 | 31.5957 | 0.966398 |
| smfa/walker_run/shot_noise | 1000 | 34.0111 | 0.927613 | 31.3394 | 0.883607 |
| smfa/task/walker_stand | 13000 | 32.6265 | 0.921148 | 30.4506 | 0.893273 |
| smfa/walker_stand/rain | 1000 | 34.5962 | 0.937393 | 32.9844 | 0.914789 |
| smfa/walker_stand/fog | 1000 | 39.5670 | 0.988770 | 37.5817 | 0.981191 |
| smfa/walker_stand/snow | 1000 | 32.7343 | 0.911884 | 31.2611 | 0.880302 |
| smfa/walker_stand/motion_blur | 1000 | 24.9766 | 0.775136 | 23.1924 | 0.757634 |
| smfa/walker_stand/gaussian_noise | 1000 | 34.0230 | 0.936865 | 31.3379 | 0.896241 |
| smfa/walker_stand/low_light | 1000 | 31.8366 | 0.912137 | 29.4605 | 0.858276 |
| smfa/walker_stand/jpeg | 1000 | 31.8952 | 0.930539 | 28.8541 | 0.883191 |
| smfa/walker_stand/defocus_blur | 1000 | 26.1230 | 0.810487 | 24.3770 | 0.784986 |
| smfa/walker_stand/frost | 1000 | 33.0329 | 0.957539 | 31.1085 | 0.931934 |
| smfa/walker_stand/occlusion_patch | 1000 | 29.2544 | 0.920139 | 27.2425 | 0.904264 |
| smfa/walker_stand/saturation | 1000 | 39.9618 | 0.992266 | 37.1051 | 0.982198 |
| smfa/walker_stand/shadow | 1000 | 33.4375 | 0.978540 | 31.2850 | 0.963689 |
| smfa/walker_stand/shot_noise | 1000 | 32.7066 | 0.923235 | 30.0673 | 0.873848 |
| smfa/task/hopper_stand | 13000 | 34.7845 | 0.924814 | 32.5080 | 0.898181 |
| smfa/hopper_stand/rain | 1000 | 34.8152 | 0.937169 | 33.3936 | 0.918457 |
| smfa/hopper_stand/fog | 1000 | 40.7108 | 0.988212 | 38.5694 | 0.980441 |
| smfa/hopper_stand/snow | 1000 | 34.1758 | 0.918987 | 32.7747 | 0.891701 |
| smfa/hopper_stand/motion_blur | 1000 | 29.8095 | 0.846506 | 27.6565 | 0.830657 |
| smfa/hopper_stand/gaussian_noise | 1000 | 38.0270 | 0.931514 | 35.6212 | 0.898027 |
| smfa/hopper_stand/low_light | 1000 | 33.0714 | 0.878660 | 30.8409 | 0.819076 |
| smfa/hopper_stand/jpeg | 1000 | 35.3838 | 0.927669 | 32.1040 | 0.883109 |
| smfa/hopper_stand/defocus_blur | 1000 | 30.3891 | 0.854300 | 28.3058 | 0.837471 |
| smfa/hopper_stand/frost | 1000 | 36.6269 | 0.958348 | 34.5029 | 0.941733 |
| smfa/hopper_stand/occlusion_patch | 1000 | 33.7508 | 0.936078 | 31.2432 | 0.919397 |
| smfa/hopper_stand/saturation | 1000 | 43.3673 | 0.993996 | 40.1285 | 0.983689 |
| smfa/hopper_stand/shadow | 1000 | 26.2380 | 0.952120 | 24.1459 | 0.924412 |
| smfa/hopper_stand/shot_noise | 1000 | 35.8329 | 0.899024 | 33.3171 | 0.848185 |
| smfa/task/quadruped_run | 13000 | 33.4929 | 0.903626 | 31.2210 | 0.878830 |
| smfa/quadruped_run/rain | 1000 | 33.4376 | 0.908411 | 32.0404 | 0.889843 |
| smfa/quadruped_run/fog | 1000 | 40.2270 | 0.987817 | 38.0924 | 0.981542 |
| smfa/quadruped_run/snow | 1000 | 31.5953 | 0.869467 | 30.2476 | 0.844033 |
| smfa/quadruped_run/motion_blur | 1000 | 26.5745 | 0.737419 | 24.5025 | 0.706992 |
| smfa/quadruped_run/gaussian_noise | 1000 | 36.6152 | 0.939811 | 33.9075 | 0.911375 |
| smfa/quadruped_run/low_light | 1000 | 31.5488 | 0.887565 | 29.2095 | 0.840394 |
| smfa/quadruped_run/jpeg | 1000 | 33.1712 | 0.922569 | 29.4213 | 0.879964 |
| smfa/quadruped_run/defocus_blur | 1000 | 27.0643 | 0.735588 | 25.0118 | 0.704437 |
| smfa/quadruped_run/frost | 1000 | 35.5598 | 0.956533 | 33.9780 | 0.944259 |
| smfa/quadruped_run/occlusion_patch | 1000 | 31.1713 | 0.915132 | 29.0182 | 0.898491 |
| smfa/quadruped_run/saturation | 1000 | 40.0776 | 0.991731 | 37.0184 | 0.980578 |
| smfa/quadruped_run/shadow | 1000 | 33.5901 | 0.973828 | 31.3543 | 0.959232 |
| smfa/quadruped_run/shot_noise | 1000 | 34.7747 | 0.921267 | 32.0708 | 0.883656 |
| smfa/task/finger_turn_hard | 13000 | 34.9529 | 0.932363 | 32.0442 | 0.906236 |
| smfa/finger_turn_hard/rain | 1000 | 37.2264 | 0.966359 | 35.4183 | 0.949048 |
| smfa/finger_turn_hard/fog | 1000 | 40.5245 | 0.989790 | 38.1683 | 0.981520 |
| smfa/finger_turn_hard/snow | 1000 | 34.8333 | 0.945771 | 33.0409 | 0.917562 |
| smfa/finger_turn_hard/motion_blur | 1000 | 27.0877 | 0.787329 | 24.7309 | 0.759219 |
| smfa/finger_turn_hard/gaussian_noise | 1000 | 37.4774 | 0.949363 | 33.8952 | 0.916834 |
| smfa/finger_turn_hard/low_light | 1000 | 32.5779 | 0.910820 | 29.3440 | 0.858890 |
| smfa/finger_turn_hard/jpeg | 1000 | 34.2136 | 0.937121 | 29.7540 | 0.891465 |
| smfa/finger_turn_hard/defocus_blur | 1000 | 28.4726 | 0.826311 | 26.0246 | 0.794403 |
| smfa/finger_turn_hard/frost | 1000 | 38.1712 | 0.972380 | 35.9700 | 0.958234 |
| smfa/finger_turn_hard/occlusion_patch | 1000 | 30.9903 | 0.926844 | 28.4648 | 0.912522 |
| smfa/finger_turn_hard/saturation | 1000 | 41.8514 | 0.993649 | 36.7013 | 0.980142 |
| smfa/finger_turn_hard/shadow | 1000 | 35.7567 | 0.982605 | 33.1480 | 0.968985 |
| smfa/finger_turn_hard/shot_noise | 1000 | 35.2050 | 0.932376 | 31.9145 | 0.892251 |
| smfa/task/cartpole_swingup_sparse | 13000 | 34.8306 | 0.913596 | 32.4244 | 0.889341 |
| smfa/cartpole_swingup_sparse/rain | 1000 | 35.0285 | 0.941771 | 33.6429 | 0.927656 |
| smfa/cartpole_swingup_sparse/fog | 1000 | 41.1088 | 0.990354 | 39.0747 | 0.984629 |
| smfa/cartpole_swingup_sparse/snow | 1000 | 34.3696 | 0.921978 | 33.0042 | 0.901999 |
| smfa/cartpole_swingup_sparse/motion_blur | 1000 | 29.7878 | 0.769190 | 27.5268 | 0.739933 |
| smfa/cartpole_swingup_sparse/gaussian_noise | 1000 | 37.5492 | 0.935149 | 34.6749 | 0.906729 |
| smfa/cartpole_swingup_sparse/low_light | 1000 | 32.5743 | 0.873903 | 30.1170 | 0.823160 |
| smfa/cartpole_swingup_sparse/jpeg | 1000 | 35.4986 | 0.933787 | 32.0225 | 0.897658 |
| smfa/cartpole_swingup_sparse/defocus_blur | 1000 | 30.0529 | 0.765870 | 27.8301 | 0.736913 |
| smfa/cartpole_swingup_sparse/frost | 1000 | 36.6469 | 0.966460 | 34.9638 | 0.955325 |
| smfa/cartpole_swingup_sparse/occlusion_patch | 1000 | 33.8586 | 0.925699 | 31.3472 | 0.908522 |
| smfa/cartpole_swingup_sparse/saturation | 1000 | 43.9787 | 0.994591 | 39.9882 | 0.985955 |
| smfa/cartpole_swingup_sparse/shadow | 1000 | 26.5713 | 0.951080 | 24.4572 | 0.928364 |
| smfa/cartpole_swingup_sparse/shot_noise | 1000 | 35.7722 | 0.906909 | 32.8676 | 0.864590 |
| smfa/task/cup_catch | 13000 | 37.1958 | 0.937888 | 34.6297 | 0.913095 |
| smfa/cup_catch/rain | 1000 | 38.1418 | 0.955143 | 36.5278 | 0.935440 |
| smfa/cup_catch/fog | 1000 | 43.0596 | 0.988239 | 40.7306 | 0.980373 |
| smfa/cup_catch/snow | 1000 | 35.9761 | 0.934788 | 34.3653 | 0.907841 |
| smfa/cup_catch/motion_blur | 1000 | 31.9648 | 0.868939 | 29.4635 | 0.849593 |
| smfa/cup_catch/gaussian_noise | 1000 | 38.8129 | 0.939154 | 35.7486 | 0.903991 |
| smfa/cup_catch/low_light | 1000 | 34.0480 | 0.899133 | 31.0600 | 0.843630 |
| smfa/cup_catch/jpeg | 1000 | 35.8996 | 0.932731 | 32.4191 | 0.895688 |
| smfa/cup_catch/defocus_blur | 1000 | 31.8176 | 0.863937 | 29.3828 | 0.845927 |
| smfa/cup_catch/frost | 1000 | 38.2170 | 0.964612 | 36.4325 | 0.948802 |
| smfa/cup_catch/occlusion_patch | 1000 | 36.9455 | 0.951285 | 34.0958 | 0.933430 |
| smfa/cup_catch/saturation | 1000 | 43.1627 | 0.991689 | 40.1151 | 0.981050 |
| smfa/cup_catch/shadow | 1000 | 38.0784 | 0.980385 | 35.4921 | 0.966019 |
| smfa/cup_catch/shot_noise | 1000 | 37.4213 | 0.922509 | 34.3527 | 0.878443 |
| smfa/task/reacher_easy | 13000 | 35.4442 | 0.956651 | 32.7208 | 0.930950 |
| smfa/reacher_easy/rain | 1000 | 38.1389 | 0.980511 | 36.4156 | 0.968897 |
| smfa/reacher_easy/fog | 1000 | 40.8657 | 0.992433 | 38.0642 | 0.984625 |
| smfa/reacher_easy/snow | 1000 | 36.1682 | 0.965153 | 34.3212 | 0.944433 |
| smfa/reacher_easy/motion_blur | 1000 | 27.5253 | 0.906839 | 25.4372 | 0.887267 |
| smfa/reacher_easy/gaussian_noise | 1000 | 38.1367 | 0.964414 | 35.0661 | 0.935357 |
| smfa/reacher_easy/low_light | 1000 | 32.5406 | 0.909174 | 29.4904 | 0.839035 |
| smfa/reacher_easy/jpeg | 1000 | 35.2684 | 0.962206 | 31.3308 | 0.924456 |
| smfa/reacher_easy/defocus_blur | 1000 | 27.9386 | 0.920462 | 26.0029 | 0.897449 |
| smfa/reacher_easy/frost | 1000 | 39.1141 | 0.982965 | 37.1978 | 0.972586 |
| smfa/reacher_easy/occlusion_patch | 1000 | 33.9914 | 0.953915 | 30.6518 | 0.931555 |
| smfa/reacher_easy/saturation | 1000 | 39.9355 | 0.992846 | 36.0359 | 0.980426 |
| smfa/reacher_easy/shadow | 1000 | 35.6375 | 0.979338 | 32.7934 | 0.961392 |
| smfa/reacher_easy/shot_noise | 1000 | 35.5143 | 0.926212 | 32.5635 | 0.874872 |
| smfa/task/reacher_hard | 13000 | 35.9347 | 0.956082 | 33.3385 | 0.932517 |
| smfa/reacher_hard/rain | 1000 | 38.7494 | 0.982831 | 36.9624 | 0.971331 |
| smfa/reacher_hard/fog | 1000 | 41.1468 | 0.993463 | 38.8308 | 0.985989 |
| smfa/reacher_hard/snow | 1000 | 37.1541 | 0.969163 | 35.1613 | 0.949270 |
| smfa/reacher_hard/motion_blur | 1000 | 27.4634 | 0.899973 | 25.5664 | 0.890464 |
| smfa/reacher_hard/gaussian_noise | 1000 | 38.4224 | 0.965139 | 35.5090 | 0.937077 |
| smfa/reacher_hard/low_light | 1000 | 32.5561 | 0.908093 | 30.0987 | 0.840782 |
| smfa/reacher_hard/jpeg | 1000 | 35.0646 | 0.955840 | 31.2188 | 0.917069 |
| smfa/reacher_hard/defocus_blur | 1000 | 27.8202 | 0.908252 | 25.9501 | 0.897165 |
| smfa/reacher_hard/frost | 1000 | 39.5982 | 0.984047 | 37.6636 | 0.973516 |
| smfa/reacher_hard/occlusion_patch | 1000 | 35.4862 | 0.960069 | 32.2147 | 0.938210 |
| smfa/reacher_hard/saturation | 1000 | 41.3618 | 0.994041 | 37.2644 | 0.981097 |
| smfa/reacher_hard/shadow | 1000 | 36.3864 | 0.980236 | 33.8508 | 0.963347 |
| smfa/reacher_hard/shot_noise | 1000 | 35.9413 | 0.927926 | 33.1089 | 0.877405 |
| smfa/clean_input | 10000 | 43.2863 | 0.995250 | 40.4855 | 0.989728 |
| smfa/original7 | 70000 | 34.6029 | 0.922749 | 32.2489 | 0.894106 |
| smfa/added6 | 60000 | 34.5855 | 0.936119 | 32.0618 | 0.914748 |

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
| markov/aco | 358.80 +/- 328.02 (n=100) |
| single/all/aco | 388.50 +/- 386.97 (n=650) |
| single/original7/aco | 368.65 +/- 382.12 (n=350) |
| single/added6/aco | 411.65 +/- 391.92 (n=300) |
| single/rain/aco | 653.67 +/- 368.26 (n=50) |
| single/fog/aco | 171.68 +/- 293.78 (n=50) |
| single/snow/aco | 570.41 +/- 373.32 (n=50) |
| single/motion_blur/aco | 540.23 +/- 376.15 (n=50) |
| single/gaussian_noise/aco | 72.54 +/- 122.86 (n=50) |
| single/low_light/aco | 380.85 +/- 320.96 (n=50) |
| single/jpeg/aco | 191.19 +/- 321.40 (n=50) |
| single/defocus_blur/aco | 581.53 +/- 376.42 (n=50) |
| single/frost/aco | 317.14 +/- 357.47 (n=50) |
| single/occlusion_patch/aco | 516.39 +/- 383.91 (n=50) |
| single/saturation/aco | 457.26 +/- 419.80 (n=50) |
| single/shadow/aco | 528.21 +/- 378.70 (n=50) |
| single/shot_noise/aco | 69.34 +/- 124.30 (n=50) |
| task/walker_walk/single_mean/aco | 451.83 +/- 379.72 (n=65) |
| task/walker_walk/markov/aco | 195.67 +/- 89.57 (n=10) |
| task/walker_walk/rain/aco | 889.48 +/- 49.49 (n=5) |
| task/walker_walk/fog/aco | 31.19 +/- 7.42 (n=5) |
| task/walker_walk/snow/aco | 802.04 +/- 108.36 (n=5) |
| task/walker_walk/motion_blur/aco | 795.16 +/- 125.43 (n=5) |
| task/walker_walk/gaussian_noise/aco | 30.34 +/- 8.56 (n=5) |
| task/walker_walk/low_light/aco | 239.30 +/- 81.27 (n=5) |
| task/walker_walk/jpeg/aco | 102.43 +/- 53.56 (n=5) |
| task/walker_walk/defocus_blur/aco | 786.94 +/- 85.89 (n=5) |
| task/walker_walk/frost/aco | 40.54 +/- 25.20 (n=5) |
| task/walker_walk/occlusion_patch/aco | 844.48 +/- 118.58 (n=5) |
| task/walker_walk/saturation/aco | 685.80 +/- 369.05 (n=5) |
| task/walker_walk/shadow/aco | 589.16 +/- 254.92 (n=5) |
| task/walker_walk/shot_noise/aco | 37.00 +/- 13.97 (n=5) |
| task/walker_run/single_mean/aco | 170.18 +/- 138.42 (n=65) |
| task/walker_run/markov/aco | 116.72 +/- 40.15 (n=10) |
| task/walker_run/rain/aco | 347.92 +/- 36.88 (n=5) |
| task/walker_run/fog/aco | 35.58 +/- 5.99 (n=5) |
| task/walker_run/snow/aco | 290.12 +/- 48.58 (n=5) |
| task/walker_run/motion_blur/aco | 313.98 +/- 19.85 (n=5) |
| task/walker_run/gaussian_noise/aco | 30.62 +/- 10.13 (n=5) |
| task/walker_run/low_light/aco | 118.03 +/- 22.12 (n=5) |
| task/walker_run/jpeg/aco | 44.67 +/- 11.04 (n=5) |
| task/walker_run/defocus_blur/aco | 315.57 +/- 58.13 (n=5) |
| task/walker_run/frost/aco | 27.81 +/- 14.88 (n=5) |
| task/walker_run/occlusion_patch/aco | 299.89 +/- 60.28 (n=5) |
| task/walker_run/saturation/aco | 87.97 +/- 139.95 (n=5) |
| task/walker_run/shadow/aco | 270.40 +/- 54.58 (n=5) |
| task/walker_run/shot_noise/aco | 29.77 +/- 8.47 (n=5) |
| task/walker_stand/single_mean/aco | 689.08 +/- 330.71 (n=65) |
| task/walker_stand/markov/aco | 681.03 +/- 135.58 (n=10) |
| task/walker_stand/rain/aco | 970.37 +/- 16.14 (n=5) |
| task/walker_stand/fog/aco | 262.55 +/- 86.76 (n=5) |
| task/walker_stand/snow/aco | 969.99 +/- 13.31 (n=5) |
| task/walker_stand/motion_blur/aco | 950.38 +/- 31.32 (n=5) |
| task/walker_stand/gaussian_noise/aco | 244.27 +/- 71.46 (n=5) |
| task/walker_stand/low_light/aco | 695.00 +/- 97.46 (n=5) |
| task/walker_stand/jpeg/aco | 876.68 +/- 97.47 (n=5) |
| task/walker_stand/defocus_blur/aco | 956.99 +/- 24.02 (n=5) |
| task/walker_stand/frost/aco | 202.20 +/- 70.03 (n=5) |
| task/walker_stand/occlusion_patch/aco | 889.14 +/- 175.40 (n=5) |
| task/walker_stand/saturation/aco | 749.09 +/- 314.46 (n=5) |
| task/walker_stand/shadow/aco | 943.91 +/- 33.02 (n=5) |
| task/walker_stand/shot_noise/aco | 247.44 +/- 115.82 (n=5) |
| task/hopper_stand/single_mean/aco | 374.84 +/- 381.48 (n=65) |
| task/hopper_stand/markov/aco | 314.05 +/- 131.02 (n=10) |
| task/hopper_stand/rain/aco | 720.03 +/- 402.52 (n=5) |
| task/hopper_stand/fog/aco | 2.76 +/- 6.18 (n=5) |
| task/hopper_stand/snow/aco | 666.69 +/- 378.04 (n=5) |
| task/hopper_stand/motion_blur/aco | 333.87 +/- 247.30 (n=5) |
| task/hopper_stand/gaussian_noise/aco | 2.09 +/- 4.67 (n=5) |
| task/hopper_stand/low_light/aco | 650.17 +/- 366.05 (n=5) |
| task/hopper_stand/jpeg/aco | 4.68 +/- 10.47 (n=5) |
| task/hopper_stand/defocus_blur/aco | 574.56 +/- 321.73 (n=5) |
| task/hopper_stand/frost/aco | 460.48 +/- 374.51 (n=5) |
| task/hopper_stand/occlusion_patch/aco | 462.05 +/- 372.84 (n=5) |
| task/hopper_stand/saturation/aco | 483.94 +/- 443.18 (n=5) |
| task/hopper_stand/shadow/aco | 509.49 +/- 314.43 (n=5) |
| task/hopper_stand/shot_noise/aco | 2.07 +/- 4.63 (n=5) |
| task/quadruped_run/single_mean/aco | 364.31 +/- 162.12 (n=65) |
| task/quadruped_run/markov/aco | 429.44 +/- 154.08 (n=10) |
| task/quadruped_run/rain/aco | 289.14 +/- 254.08 (n=5) |
| task/quadruped_run/fog/aco | 357.89 +/- 100.36 (n=5) |
| task/quadruped_run/snow/aco | 495.43 +/- 51.74 (n=5) |
| task/quadruped_run/motion_blur/aco | 513.12 +/- 33.74 (n=5) |
| task/quadruped_run/gaussian_noise/aco | 319.70 +/- 146.96 (n=5) |
| task/quadruped_run/low_light/aco | 300.62 +/- 108.54 (n=5) |
| task/quadruped_run/jpeg/aco | 240.66 +/- 31.85 (n=5) |
| task/quadruped_run/defocus_blur/aco | 438.20 +/- 134.21 (n=5) |
| task/quadruped_run/frost/aco | 315.41 +/- 165.65 (n=5) |
| task/quadruped_run/occlusion_patch/aco | 418.39 +/- 186.67 (n=5) |
| task/quadruped_run/saturation/aco | 392.78 +/- 214.26 (n=5) |
| task/quadruped_run/shadow/aco | 395.16 +/- 144.96 (n=5) |
| task/quadruped_run/shot_noise/aco | 259.53 +/- 219.34 (n=5) |
| task/finger_turn_hard/single_mean/aco | 211.71 +/- 344.06 (n=65) |
| task/finger_turn_hard/markov/aco | 170.60 +/- 290.48 (n=10) |
| task/finger_turn_hard/rain/aco | 690.60 +/- 389.37 (n=5) |
| task/finger_turn_hard/fog/aco | 68.80 +/- 153.84 (n=5) |
| task/finger_turn_hard/snow/aco | 95.60 +/- 191.67 (n=5) |
| task/finger_turn_hard/motion_blur/aco | 148.00 +/- 248.34 (n=5) |
| task/finger_turn_hard/gaussian_noise/aco | 0.00 +/- 0.00 (n=5) |
| task/finger_turn_hard/low_light/aco | 117.00 +/- 184.15 (n=5) |
| task/finger_turn_hard/jpeg/aco | 0.00 +/- 0.00 (n=5) |
| task/finger_turn_hard/defocus_blur/aco | 448.60 +/- 465.77 (n=5) |
| task/finger_turn_hard/frost/aco | 190.80 +/- 329.72 (n=5) |
| task/finger_turn_hard/occlusion_patch/aco | 589.40 +/- 390.75 (n=5) |
| task/finger_turn_hard/saturation/aco | 3.00 +/- 6.71 (n=5) |
| task/finger_turn_hard/shadow/aco | 400.40 +/- 496.69 (n=5) |
| task/finger_turn_hard/shot_noise/aco | 0.00 +/- 0.00 (n=5) |
| task/cartpole_swingup_sparse/single_mean/aco | 315.48 +/- 314.97 (n=65) |
| task/cartpole_swingup_sparse/markov/aco | 90.30 +/- 118.04 (n=10) |
| task/cartpole_swingup_sparse/rain/aco | 663.00 +/- 67.33 (n=5) |
| task/cartpole_swingup_sparse/fog/aco | 3.40 +/- 7.60 (n=5) |
| task/cartpole_swingup_sparse/snow/aco | 422.40 +/- 98.61 (n=5) |
| task/cartpole_swingup_sparse/motion_blur/aco | 387.60 +/- 361.43 (n=5) |
| task/cartpole_swingup_sparse/gaussian_noise/aco | 0.00 +/- 0.00 (n=5) |
| task/cartpole_swingup_sparse/low_light/aco | 365.40 +/- 77.45 (n=5) |
| task/cartpole_swingup_sparse/jpeg/aco | 0.00 +/- 0.00 (n=5) |
| task/cartpole_swingup_sparse/defocus_blur/aco | 336.00 +/- 370.47 (n=5) |
| task/cartpole_swingup_sparse/frost/aco | 676.60 +/- 157.47 (n=5) |
| task/cartpole_swingup_sparse/occlusion_patch/aco | 450.20 +/- 406.75 (n=5) |
| task/cartpole_swingup_sparse/saturation/aco | 594.60 +/- 368.43 (n=5) |
| task/cartpole_swingup_sparse/shadow/aco | 202.00 +/- 59.63 (n=5) |
| task/cartpole_swingup_sparse/shot_noise/aco | 0.00 +/- 0.00 (n=5) |
| task/cup_catch/single_mean/aco | 614.97 +/- 457.39 (n=65) |
| task/cup_catch/markov/aco | 689.60 +/- 340.53 (n=10) |
| task/cup_catch/rain/aco | 977.00 +/- 11.85 (n=5) |
| task/cup_catch/fog/aco | 4.60 +/- 6.31 (n=5) |
| task/cup_catch/snow/aco | 971.40 +/- 15.76 (n=5) |
| task/cup_catch/motion_blur/aco | 976.80 +/- 11.90 (n=5) |
| task/cup_catch/gaussian_noise/aco | 3.00 +/- 4.24 (n=5) |
| task/cup_catch/low_light/aco | 683.80 +/- 307.22 (n=5) |
| task/cup_catch/jpeg/aco | 199.40 +/- 428.11 (n=5) |
| task/cup_catch/defocus_blur/aco | 976.80 +/- 12.28 (n=5) |
| task/cup_catch/frost/aco | 269.20 +/- 396.94 (n=5) |
| task/cup_catch/occlusion_patch/aco | 977.00 +/- 11.14 (n=5) |
| task/cup_catch/saturation/aco | 975.40 +/- 12.97 (n=5) |
| task/cup_catch/shadow/aco | 976.20 +/- 10.11 (n=5) |
| task/cup_catch/shot_noise/aco | 4.00 +/- 5.52 (n=5) |
| task/reacher_easy/single_mean/aco | 685.17 +/- 419.38 (n=65) |
| task/reacher_easy/markov/aco | 878.90 +/- 108.50 (n=10) |
| task/reacher_easy/rain/aco | 982.40 +/- 14.54 (n=5) |
| task/reacher_easy/fog/aco | 948.40 +/- 69.45 (n=5) |
| task/reacher_easy/snow/aco | 982.00 +/- 15.22 (n=5) |
| task/reacher_easy/motion_blur/aco | 975.60 +/- 25.44 (n=5) |
| task/reacher_easy/gaussian_noise/aco | 89.00 +/- 94.48 (n=5) |
| task/reacher_easy/low_light/aco | 629.20 +/- 424.86 (n=5) |
| task/reacher_easy/jpeg/aco | 442.40 +/- 427.05 (n=5) |
| task/reacher_easy/defocus_blur/aco | 977.20 +/- 24.47 (n=5) |
| task/reacher_easy/frost/aco | 982.20 +/- 14.87 (n=5) |
| task/reacher_easy/occlusion_patch/aco | 220.20 +/- 422.40 (n=5) |
| task/reacher_easy/saturation/aco | 591.80 +/- 534.38 (n=5) |
| task/reacher_easy/shadow/aco | 981.00 +/- 15.73 (n=5) |
| task/reacher_easy/shot_noise/aco | 105.80 +/- 98.95 (n=5) |
| task/reacher_hard/single_mean/aco | 7.40 +/- 12.61 (n=65) |
| task/reacher_hard/markov/aco | 21.70 +/- 54.01 (n=10) |
| task/reacher_hard/rain/aco | 6.80 +/- 12.60 (n=5) |
| task/reacher_hard/fog/aco | 1.60 +/- 3.58 (n=5) |
| task/reacher_hard/snow/aco | 8.40 +/- 16.07 (n=5) |
| task/reacher_hard/motion_blur/aco | 7.80 +/- 11.50 (n=5) |
| task/reacher_hard/gaussian_noise/aco | 6.40 +/- 14.31 (n=5) |
| task/reacher_hard/low_light/aco | 10.00 +/- 15.86 (n=5) |
| task/reacher_hard/jpeg/aco | 1.00 +/- 2.24 (n=5) |
| task/reacher_hard/defocus_blur/aco | 4.40 +/- 6.27 (n=5) |
| task/reacher_hard/frost/aco | 6.20 +/- 9.12 (n=5) |
| task/reacher_hard/occlusion_patch/aco | 13.20 +/- 21.38 (n=5) |
| task/reacher_hard/saturation/aco | 8.20 +/- 14.74 (n=5) |
| task/reacher_hard/shadow/aco | 14.40 +/- 20.18 (n=5) |
| task/reacher_hard/shot_noise/aco | 7.80 +/- 9.63 (n=5) |
| markov/smfa | 645.80 +/- 327.48 (n=100) |
| single/all/smfa | 651.63 +/- 378.03 (n=650) |
| single/original7/smfa | 669.63 +/- 370.59 (n=350) |
| single/added6/smfa | 630.62 +/- 386.09 (n=300) |
| single/rain/smfa | 723.25 +/- 348.20 (n=50) |
| single/fog/smfa | 743.21 +/- 334.06 (n=50) |
| single/snow/smfa | 748.64 +/- 333.59 (n=50) |
| single/motion_blur/smfa | 414.24 +/- 389.55 (n=50) |
| single/gaussian_noise/smfa | 726.04 +/- 348.29 (n=50) |
| single/low_light/smfa | 693.60 +/- 363.73 (n=50) |
| single/jpeg/smfa | 638.47 +/- 377.47 (n=50) |
| single/defocus_blur/smfa | 407.08 +/- 404.56 (n=50) |
| single/frost/smfa | 736.19 +/- 349.64 (n=50) |
| single/occlusion_patch/smfa | 469.02 +/- 396.00 (n=50) |
| single/saturation/smfa | 746.74 +/- 330.40 (n=50) |
| single/shadow/smfa | 703.97 +/- 346.05 (n=50) |
| single/shot_noise/smfa | 720.71 +/- 348.46 (n=50) |
| task/walker_walk/single_mean/smfa | 888.85 +/- 182.32 (n=65) |
| task/walker_walk/markov/smfa | 850.82 +/- 207.99 (n=10) |
| task/walker_walk/rain/smfa | 963.36 +/- 7.95 (n=5) |
| task/walker_walk/fog/smfa | 961.29 +/- 13.12 (n=5) |
| task/walker_walk/snow/smfa | 960.62 +/- 11.18 (n=5) |
| task/walker_walk/motion_blur/smfa | 648.11 +/- 118.82 (n=5) |
| task/walker_walk/gaussian_noise/smfa | 954.85 +/- 10.43 (n=5) |
| task/walker_walk/low_light/smfa | 954.00 +/- 20.68 (n=5) |
| task/walker_walk/jpeg/smfa | 960.08 +/- 11.00 (n=5) |
| task/walker_walk/defocus_blur/smfa | 923.64 +/- 39.70 (n=5) |
| task/walker_walk/frost/smfa | 961.84 +/- 10.27 (n=5) |
| task/walker_walk/occlusion_patch/smfa | 421.37 +/- 329.32 (n=5) |
| task/walker_walk/saturation/smfa | 943.10 +/- 30.98 (n=5) |
| task/walker_walk/shadow/smfa | 944.94 +/- 33.99 (n=5) |
| task/walker_walk/shot_noise/smfa | 957.90 +/- 7.16 (n=5) |
| task/walker_run/single_mean/smfa | 643.65 +/- 174.75 (n=65) |
| task/walker_run/markov/smfa | 580.23 +/- 40.86 (n=10) |
| task/walker_run/rain/smfa | 726.17 +/- 37.41 (n=5) |
| task/walker_run/fog/smfa | 714.90 +/- 34.22 (n=5) |
| task/walker_run/snow/smfa | 734.12 +/- 25.56 (n=5) |
| task/walker_run/motion_blur/smfa | 309.87 +/- 75.08 (n=5) |
| task/walker_run/gaussian_noise/smfa | 750.71 +/- 10.86 (n=5) |
| task/walker_run/low_light/smfa | 707.50 +/- 42.49 (n=5) |
| task/walker_run/jpeg/smfa | 720.76 +/- 13.08 (n=5) |
| task/walker_run/defocus_blur/smfa | 496.03 +/- 124.01 (n=5) |
| task/walker_run/frost/smfa | 742.19 +/- 23.92 (n=5) |
| task/walker_run/occlusion_patch/smfa | 252.62 +/- 65.04 (n=5) |
| task/walker_run/saturation/smfa | 747.49 +/- 22.69 (n=5) |
| task/walker_run/shadow/smfa | 722.17 +/- 39.02 (n=5) |
| task/walker_run/shot_noise/smfa | 742.96 +/- 13.75 (n=5) |
| task/walker_stand/single_mean/smfa | 963.57 +/- 34.35 (n=65) |
| task/walker_stand/markov/smfa | 960.45 +/- 29.81 (n=10) |
| task/walker_stand/rain/smfa | 978.65 +/- 9.38 (n=5) |
| task/walker_stand/fog/smfa | 964.11 +/- 22.77 (n=5) |
| task/walker_stand/snow/smfa | 980.67 +/- 4.55 (n=5) |
| task/walker_stand/motion_blur/smfa | 930.49 +/- 67.90 (n=5) |
| task/walker_stand/gaussian_noise/smfa | 972.51 +/- 10.18 (n=5) |
| task/walker_stand/low_light/smfa | 969.97 +/- 19.93 (n=5) |
| task/walker_stand/jpeg/smfa | 970.84 +/- 19.35 (n=5) |
| task/walker_stand/defocus_blur/smfa | 956.97 +/- 34.97 (n=5) |
| task/walker_stand/frost/smfa | 976.13 +/- 12.05 (n=5) |
| task/walker_stand/occlusion_patch/smfa | 922.29 +/- 75.96 (n=5) |
| task/walker_stand/saturation/smfa | 966.92 +/- 13.61 (n=5) |
| task/walker_stand/shadow/smfa | 970.23 +/- 16.06 (n=5) |
| task/walker_stand/shot_noise/smfa | 966.59 +/- 22.01 (n=5) |
| task/hopper_stand/single_mean/smfa | 597.30 +/- 397.18 (n=65) |
| task/hopper_stand/markov/smfa | 473.88 +/- 201.65 (n=10) |
| task/hopper_stand/rain/smfa | 708.50 +/- 396.92 (n=5) |
| task/hopper_stand/fog/smfa | 720.04 +/- 402.99 (n=5) |
| task/hopper_stand/snow/smfa | 733.14 +/- 409.85 (n=5) |
| task/hopper_stand/motion_blur/smfa | 146.92 +/- 92.94 (n=5) |
| task/hopper_stand/gaussian_noise/smfa | 732.43 +/- 409.49 (n=5) |
| task/hopper_stand/low_light/smfa | 706.13 +/- 397.19 (n=5) |
| task/hopper_stand/jpeg/smfa | 531.22 +/- 327.67 (n=5) |
| task/hopper_stand/defocus_blur/smfa | 140.18 +/- 103.34 (n=5) |
| task/hopper_stand/frost/smfa | 730.46 +/- 408.34 (n=5) |
| task/hopper_stand/occlusion_patch/smfa | 448.82 +/- 450.75 (n=5) |
| task/hopper_stand/saturation/smfa | 726.67 +/- 406.25 (n=5) |
| task/hopper_stand/shadow/smfa | 714.74 +/- 400.82 (n=5) |
| task/hopper_stand/shot_noise/smfa | 725.71 +/- 405.77 (n=5) |
| task/quadruped_run/single_mean/smfa | 486.54 +/- 116.57 (n=65) |
| task/quadruped_run/markov/smfa | 506.30 +/- 42.37 (n=10) |
| task/quadruped_run/rain/smfa | 505.98 +/- 56.97 (n=5) |
| task/quadruped_run/fog/smfa | 509.16 +/- 92.69 (n=5) |
| task/quadruped_run/snow/smfa | 528.09 +/- 23.87 (n=5) |
| task/quadruped_run/motion_blur/smfa | 409.36 +/- 224.79 (n=5) |
| task/quadruped_run/gaussian_noise/smfa | 507.67 +/- 67.02 (n=5) |
| task/quadruped_run/low_light/smfa | 454.99 +/- 99.94 (n=5) |
| task/quadruped_run/jpeg/smfa | 516.62 +/- 66.42 (n=5) |
| task/quadruped_run/defocus_blur/smfa | 491.80 +/- 77.49 (n=5) |
| task/quadruped_run/frost/smfa | 392.64 +/- 214.85 (n=5) |
| task/quadruped_run/occlusion_patch/smfa | 437.50 +/- 215.80 (n=5) |
| task/quadruped_run/saturation/smfa | 530.60 +/- 26.74 (n=5) |
| task/quadruped_run/shadow/smfa | 522.05 +/- 29.05 (n=5) |
| task/quadruped_run/shot_noise/smfa | 518.56 +/- 47.99 (n=5) |
| task/finger_turn_hard/single_mean/smfa | 568.25 +/- 450.57 (n=65) |
| task/finger_turn_hard/markov/smfa | 708.60 +/- 348.53 (n=10) |
| task/finger_turn_hard/rain/smfa | 561.80 +/- 512.11 (n=5) |
| task/finger_turn_hard/fog/smfa | 758.40 +/- 424.35 (n=5) |
| task/finger_turn_hard/snow/smfa | 760.80 +/- 425.57 (n=5) |
| task/finger_turn_hard/motion_blur/smfa | 142.20 +/- 231.08 (n=5) |
| task/finger_turn_hard/gaussian_noise/smfa | 552.20 +/- 504.19 (n=5) |
| task/finger_turn_hard/low_light/smfa | 376.80 +/- 516.08 (n=5) |
| task/finger_turn_hard/jpeg/smfa | 549.20 +/- 502.43 (n=5) |
| task/finger_turn_hard/defocus_blur/smfa | 267.40 +/- 365.65 (n=5) |
| task/finger_turn_hard/frost/smfa | 755.00 +/- 422.52 (n=5) |
| task/finger_turn_hard/occlusion_patch/smfa | 586.20 +/- 501.13 (n=5) |
| task/finger_turn_hard/saturation/smfa | 759.20 +/- 424.97 (n=5) |
| task/finger_turn_hard/shadow/smfa | 754.20 +/- 422.35 (n=5) |
| task/finger_turn_hard/shot_noise/smfa | 563.80 +/- 514.77 (n=5) |
| task/cartpole_swingup_sparse/single_mean/smfa | 579.42 +/- 340.89 (n=65) |
| task/cartpole_swingup_sparse/markov/smfa | 442.50 +/- 148.88 (n=10) |
| task/cartpole_swingup_sparse/rain/smfa | 819.60 +/- 14.64 (n=5) |
| task/cartpole_swingup_sparse/fog/smfa | 834.20 +/- 5.26 (n=5) |
| task/cartpole_swingup_sparse/snow/smfa | 821.20 +/- 10.21 (n=5) |
| task/cartpole_swingup_sparse/motion_blur/smfa | 4.40 +/- 9.84 (n=5) |
| task/cartpole_swingup_sparse/gaussian_noise/smfa | 823.00 +/- 17.90 (n=5) |
| task/cartpole_swingup_sparse/low_light/smfa | 797.40 +/- 48.83 (n=5) |
| task/cartpole_swingup_sparse/jpeg/smfa | 174.60 +/- 50.91 (n=5) |
| task/cartpole_swingup_sparse/defocus_blur/smfa | 4.80 +/- 0.84 (n=5) |
| task/cartpole_swingup_sparse/frost/smfa | 834.20 +/- 2.17 (n=5) |
| task/cartpole_swingup_sparse/occlusion_patch/smfa | 389.20 +/- 366.01 (n=5) |
| task/cartpole_swingup_sparse/saturation/smfa | 823.60 +/- 13.79 (n=5) |
| task/cartpole_swingup_sparse/shadow/smfa | 442.80 +/- 198.32 (n=5) |
| task/cartpole_swingup_sparse/shot_noise/smfa | 763.40 +/- 150.70 (n=5) |
| task/cup_catch/single_mean/smfa | 886.25 +/- 285.06 (n=65) |
| task/cup_catch/markov/smfa | 956.60 +/- 30.38 (n=10) |
| task/cup_catch/rain/smfa | 977.60 +/- 11.80 (n=5) |
| task/cup_catch/fog/smfa | 977.60 +/- 11.80 (n=5) |
| task/cup_catch/snow/smfa | 977.60 +/- 11.41 (n=5) |
| task/cup_catch/motion_blur/smfa | 773.00 +/- 432.74 (n=5) |
| task/cup_catch/gaussian_noise/smfa | 977.60 +/- 11.80 (n=5) |
| task/cup_catch/low_light/smfa | 977.20 +/- 11.65 (n=5) |
| task/cup_catch/jpeg/smfa | 974.20 +/- 13.31 (n=5) |
| task/cup_catch/defocus_blur/smfa | 0.00 +/- 0.00 (n=5) |
| task/cup_catch/frost/smfa | 977.40 +/- 11.52 (n=5) |
| task/cup_catch/occlusion_patch/smfa | 976.80 +/- 10.76 (n=5) |
| task/cup_catch/saturation/smfa | 977.40 +/- 11.93 (n=5) |
| task/cup_catch/shadow/smfa | 977.40 +/- 11.52 (n=5) |
| task/cup_catch/shot_noise/smfa | 977.40 +/- 11.76 (n=5) |
| task/reacher_easy/single_mean/smfa | 895.26 +/- 274.08 (n=65) |
| task/reacher_easy/markov/smfa | 972.30 +/- 16.19 (n=10) |
| task/reacher_easy/rain/smfa | 982.00 +/- 15.22 (n=5) |
| task/reacher_easy/fog/smfa | 982.40 +/- 14.84 (n=5) |
| task/reacher_easy/snow/smfa | 982.60 +/- 14.50 (n=5) |
| task/reacher_easy/motion_blur/smfa | 777.00 +/- 434.59 (n=5) |
| task/reacher_easy/gaussian_noise/smfa | 982.20 +/- 15.19 (n=5) |
| task/reacher_easy/low_light/smfa | 982.60 +/- 14.50 (n=5) |
| task/reacher_easy/jpeg/smfa | 982.00 +/- 15.54 (n=5) |
| task/reacher_easy/defocus_blur/smfa | 789.00 +/- 441.20 (n=5) |
| task/reacher_easy/frost/smfa | 982.60 +/- 14.29 (n=5) |
| task/reacher_easy/occlusion_patch/smfa | 250.80 +/- 413.45 (n=5) |
| task/reacher_easy/saturation/smfa | 981.80 +/- 15.64 (n=5) |
| task/reacher_easy/shadow/smfa | 981.60 +/- 16.26 (n=5) |
| task/reacher_easy/shot_noise/smfa | 981.80 +/- 15.32 (n=5) |
| task/reacher_hard/single_mean/smfa | 7.18 +/- 14.63 (n=65) |
| task/reacher_hard/markov/smfa | 6.30 +/- 10.91 (n=10) |
| task/reacher_hard/rain/smfa | 8.80 +/- 19.68 (n=5) |
| task/reacher_hard/fog/smfa | 10.00 +/- 17.32 (n=5) |
| task/reacher_hard/snow/smfa | 7.60 +/- 16.99 (n=5) |
| task/reacher_hard/motion_blur/smfa | 1.00 +/- 2.24 (n=5) |
| task/reacher_hard/gaussian_noise/smfa | 7.20 +/- 16.10 (n=5) |
| task/reacher_hard/low_light/smfa | 9.40 +/- 18.35 (n=5) |
| task/reacher_hard/jpeg/smfa | 5.20 +/- 9.09 (n=5) |
| task/reacher_hard/defocus_blur/smfa | 1.00 +/- 2.24 (n=5) |
| task/reacher_hard/frost/smfa | 9.40 +/- 18.86 (n=5) |
| task/reacher_hard/occlusion_patch/smfa | 4.60 +/- 10.29 (n=5) |
| task/reacher_hard/saturation/smfa | 10.60 +/- 21.54 (n=5) |
| task/reacher_hard/shadow/smfa | 9.60 +/- 19.31 (n=5) |
| task/reacher_hard/shot_noise/smfa | 9.00 +/- 17.41 (n=5) |
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
| walker_walk | markov | - | aco | 400000 | 352.060374 |
| walker_walk | markov | - | aco | 400001 | 200.625664 |
| walker_walk | markov | - | aco | 400002 | 169.185795 |
| walker_walk | markov | - | aco | 400003 | 93.733758 |
| walker_walk | markov | - | aco | 400004 | 157.744200 |
| walker_walk | markov | - | aco | 400005 | 169.660107 |
| walker_walk | markov | - | aco | 400006 | 192.341874 |
| walker_walk | markov | - | aco | 400007 | 357.267360 |
| walker_walk | markov | - | aco | 400008 | 144.080603 |
| walker_walk | markov | - | aco | 400009 | 120.000960 |
| walker_walk | single | rain | aco | 400000 | 907.351046 |
| walker_walk | single | rain | aco | 400001 | 801.083670 |
| walker_walk | single | rain | aco | 400002 | 913.496963 |
| walker_walk | single | rain | aco | 400003 | 914.200639 |
| walker_walk | single | rain | aco | 400004 | 911.279670 |
| walker_walk | single | fog | aco | 400000 | 39.590866 |
| walker_walk | single | fog | aco | 400001 | 35.486618 |
| walker_walk | single | fog | aco | 400002 | 29.630973 |
| walker_walk | single | fog | aco | 400003 | 31.387746 |
| walker_walk | single | fog | aco | 400004 | 19.837298 |
| walker_walk | single | snow | aco | 400000 | 821.300085 |
| walker_walk | single | snow | aco | 400001 | 850.494277 |
| walker_walk | single | snow | aco | 400002 | 839.425628 |
| walker_walk | single | snow | aco | 400003 | 886.084398 |
| walker_walk | single | snow | aco | 400004 | 612.873232 |
| walker_walk | single | motion_blur | aco | 400000 | 900.519369 |
| walker_walk | single | motion_blur | aco | 400001 | 580.889086 |
| walker_walk | single | motion_blur | aco | 400002 | 843.762520 |
| walker_walk | single | motion_blur | aco | 400003 | 854.802563 |
| walker_walk | single | motion_blur | aco | 400004 | 795.820765 |
| walker_walk | single | gaussian_noise | aco | 400000 | 43.558124 |
| walker_walk | single | gaussian_noise | aco | 400001 | 24.090228 |
| walker_walk | single | gaussian_noise | aco | 400002 | 32.478296 |
| walker_walk | single | gaussian_noise | aco | 400003 | 29.896561 |
| walker_walk | single | gaussian_noise | aco | 400004 | 21.689833 |
| walker_walk | single | low_light | aco | 400000 | 280.324976 |
| walker_walk | single | low_light | aco | 400001 | 119.112689 |
| walker_walk | single | low_light | aco | 400002 | 259.256559 |
| walker_walk | single | low_light | aco | 400003 | 205.093925 |
| walker_walk | single | low_light | aco | 400004 | 332.701884 |
| walker_walk | single | jpeg | aco | 400000 | 51.706568 |
| walker_walk | single | jpeg | aco | 400001 | 140.650943 |
| walker_walk | single | jpeg | aco | 400002 | 155.701906 |
| walker_walk | single | jpeg | aco | 400003 | 125.463879 |
| walker_walk | single | jpeg | aco | 400004 | 38.613566 |
| walker_walk | single | defocus_blur | aco | 400000 | 644.521460 |
| walker_walk | single | defocus_blur | aco | 400001 | 874.780114 |
| walker_walk | single | defocus_blur | aco | 400002 | 788.718188 |
| walker_walk | single | defocus_blur | aco | 400003 | 820.754303 |
| walker_walk | single | defocus_blur | aco | 400004 | 805.935203 |
| walker_walk | single | frost | aco | 400000 | 84.159532 |
| walker_walk | single | frost | aco | 400001 | 26.768632 |
| walker_walk | single | frost | aco | 400002 | 36.692228 |
| walker_walk | single | frost | aco | 400003 | 34.484337 |
| walker_walk | single | frost | aco | 400004 | 20.611189 |
| walker_walk | single | occlusion_patch | aco | 400000 | 795.794927 |
| walker_walk | single | occlusion_patch | aco | 400001 | 963.422677 |
| walker_walk | single | occlusion_patch | aco | 400002 | 922.595257 |
| walker_walk | single | occlusion_patch | aco | 400003 | 876.613402 |
| walker_walk | single | occlusion_patch | aco | 400004 | 663.950513 |
| walker_walk | single | saturation | aco | 400000 | 863.064096 |
| walker_walk | single | saturation | aco | 400001 | 819.608081 |
| walker_walk | single | saturation | aco | 400002 | 26.771598 |
| walker_walk | single | saturation | aco | 400003 | 877.367487 |
| walker_walk | single | saturation | aco | 400004 | 842.182720 |
| walker_walk | single | shadow | aco | 400000 | 518.741685 |
| walker_walk | single | shadow | aco | 400001 | 206.978501 |
| walker_walk | single | shadow | aco | 400002 | 891.846359 |
| walker_walk | single | shadow | aco | 400003 | 719.160342 |
| walker_walk | single | shadow | aco | 400004 | 609.088244 |
| walker_walk | single | shot_noise | aco | 400000 | 57.262268 |
| walker_walk | single | shot_noise | aco | 400001 | 21.695408 |
| walker_walk | single | shot_noise | aco | 400002 | 29.915172 |
| walker_walk | single | shot_noise | aco | 400003 | 31.594416 |
| walker_walk | single | shot_noise | aco | 400004 | 44.519124 |
| walker_walk | markov | - | smfa | 400000 | 946.513385 |
| walker_walk | markov | - | smfa | 400001 | 853.956774 |
| walker_walk | markov | - | smfa | 400002 | 271.919832 |
| walker_walk | markov | - | smfa | 400003 | 956.276184 |
| walker_walk | markov | - | smfa | 400004 | 829.924875 |
| walker_walk | markov | - | smfa | 400005 | 892.023467 |
| walker_walk | markov | - | smfa | 400006 | 926.555408 |
| walker_walk | markov | - | smfa | 400007 | 933.239359 |
| walker_walk | markov | - | smfa | 400008 | 949.096620 |
| walker_walk | markov | - | smfa | 400009 | 948.743766 |
| walker_walk | single | rain | smfa | 400000 | 973.892989 |
| walker_walk | single | rain | smfa | 400001 | 954.088336 |
| walker_walk | single | rain | smfa | 400002 | 960.532786 |
| walker_walk | single | rain | smfa | 400003 | 968.969403 |
| walker_walk | single | rain | smfa | 400004 | 959.333985 |
| walker_walk | single | fog | smfa | 400000 | 966.613979 |
| walker_walk | single | fog | smfa | 400001 | 966.612251 |
| walker_walk | single | fog | smfa | 400002 | 937.866590 |
| walker_walk | single | fog | smfa | 400003 | 968.577727 |
| walker_walk | single | fog | smfa | 400004 | 966.765275 |
| walker_walk | single | snow | smfa | 400000 | 968.067919 |
| walker_walk | single | snow | smfa | 400001 | 942.596067 |
| walker_walk | single | snow | smfa | 400002 | 963.196890 |
| walker_walk | single | snow | smfa | 400003 | 970.976504 |
| walker_walk | single | snow | smfa | 400004 | 958.261795 |
| walker_walk | single | motion_blur | smfa | 400000 | 741.145207 |
| walker_walk | single | motion_blur | smfa | 400001 | 681.266199 |
| walker_walk | single | motion_blur | smfa | 400002 | 595.966366 |
| walker_walk | single | motion_blur | smfa | 400003 | 754.704067 |
| walker_walk | single | motion_blur | smfa | 400004 | 467.461482 |
| walker_walk | single | gaussian_noise | smfa | 400000 | 955.029171 |
| walker_walk | single | gaussian_noise | smfa | 400001 | 954.585782 |
| walker_walk | single | gaussian_noise | smfa | 400002 | 940.763593 |
| walker_walk | single | gaussian_noise | smfa | 400003 | 970.198214 |
| walker_walk | single | gaussian_noise | smfa | 400004 | 953.676256 |
| walker_walk | single | low_light | smfa | 400000 | 968.561758 |
| walker_walk | single | low_light | smfa | 400001 | 947.381718 |
| walker_walk | single | low_light | smfa | 400002 | 920.640362 |
| walker_walk | single | low_light | smfa | 400003 | 969.752647 |
| walker_walk | single | low_light | smfa | 400004 | 963.670325 |
| walker_walk | single | jpeg | smfa | 400000 | 970.571952 |
| walker_walk | single | jpeg | smfa | 400001 | 942.157364 |
| walker_walk | single | jpeg | smfa | 400002 | 962.022391 |
| walker_walk | single | jpeg | smfa | 400003 | 966.945741 |
| walker_walk | single | jpeg | smfa | 400004 | 958.685745 |
| walker_walk | single | defocus_blur | smfa | 400000 | 970.243480 |
| walker_walk | single | defocus_blur | smfa | 400001 | 863.424851 |
| walker_walk | single | defocus_blur | smfa | 400002 | 930.214260 |
| walker_walk | single | defocus_blur | smfa | 400003 | 912.330895 |
| walker_walk | single | defocus_blur | smfa | 400004 | 941.971804 |
| walker_walk | single | frost | smfa | 400000 | 968.544106 |
| walker_walk | single | frost | smfa | 400001 | 964.525174 |
| walker_walk | single | frost | smfa | 400002 | 944.443480 |
| walker_walk | single | frost | smfa | 400003 | 970.049348 |
| walker_walk | single | frost | smfa | 400004 | 961.643578 |
| walker_walk | single | occlusion_patch | smfa | 400000 | 203.682155 |
| walker_walk | single | occlusion_patch | smfa | 400001 | 589.473983 |
| walker_walk | single | occlusion_patch | smfa | 400002 | 925.126993 |
| walker_walk | single | occlusion_patch | smfa | 400003 | 219.266166 |
| walker_walk | single | occlusion_patch | smfa | 400004 | 169.284740 |
| walker_walk | single | saturation | smfa | 400000 | 961.748741 |
| walker_walk | single | saturation | smfa | 400001 | 948.935755 |
| walker_walk | single | saturation | smfa | 400002 | 961.551665 |
| walker_walk | single | saturation | smfa | 400003 | 888.508613 |
| walker_walk | single | saturation | smfa | 400004 | 954.777684 |
| walker_walk | single | shadow | smfa | 400000 | 887.416471 |
| walker_walk | single | shadow | smfa | 400001 | 962.257579 |
| walker_walk | single | shadow | smfa | 400002 | 941.038101 |
| walker_walk | single | shadow | smfa | 400003 | 970.439665 |
| walker_walk | single | shadow | smfa | 400004 | 963.568556 |
| walker_walk | single | shot_noise | smfa | 400000 | 948.859021 |
| walker_walk | single | shot_noise | smfa | 400001 | 954.783016 |
| walker_walk | single | shot_noise | smfa | 400002 | 959.679983 |
| walker_walk | single | shot_noise | smfa | 400003 | 968.400631 |
| walker_walk | single | shot_noise | smfa | 400004 | 957.786502 |
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
| walker_run | markov | - | aco | 401000 | 151.534510 |
| walker_run | markov | - | aco | 401001 | 76.509068 |
| walker_run | markov | - | aco | 401002 | 101.954749 |
| walker_run | markov | - | aco | 401003 | 214.709132 |
| walker_run | markov | - | aco | 401004 | 96.970770 |
| walker_run | markov | - | aco | 401005 | 95.473228 |
| walker_run | markov | - | aco | 401006 | 127.813700 |
| walker_run | markov | - | aco | 401007 | 91.527057 |
| walker_run | markov | - | aco | 401008 | 103.836720 |
| walker_run | markov | - | aco | 401009 | 106.837146 |
| walker_run | single | rain | aco | 401000 | 357.385499 |
| walker_run | single | rain | aco | 401001 | 311.477787 |
| walker_run | single | rain | aco | 401002 | 307.316512 |
| walker_run | single | rain | aco | 401003 | 374.999417 |
| walker_run | single | rain | aco | 401004 | 388.433574 |
| walker_run | single | fog | aco | 401000 | 44.876766 |
| walker_run | single | fog | aco | 401001 | 30.634388 |
| walker_run | single | fog | aco | 401002 | 30.048901 |
| walker_run | single | fog | aco | 401003 | 35.275657 |
| walker_run | single | fog | aco | 401004 | 37.041216 |
| walker_run | single | snow | aco | 401000 | 285.990485 |
| walker_run | single | snow | aco | 401001 | 351.085146 |
| walker_run | single | snow | aco | 401002 | 260.456387 |
| walker_run | single | snow | aco | 401003 | 323.730573 |
| walker_run | single | snow | aco | 401004 | 229.325120 |
| walker_run | single | motion_blur | aco | 401000 | 301.927102 |
| walker_run | single | motion_blur | aco | 401001 | 292.990499 |
| walker_run | single | motion_blur | aco | 401002 | 308.318614 |
| walker_run | single | motion_blur | aco | 401003 | 343.566225 |
| walker_run | single | motion_blur | aco | 401004 | 323.117115 |
| walker_run | single | gaussian_noise | aco | 401000 | 17.242600 |
| walker_run | single | gaussian_noise | aco | 401001 | 26.008828 |
| walker_run | single | gaussian_noise | aco | 401002 | 37.862336 |
| walker_run | single | gaussian_noise | aco | 401003 | 43.071147 |
| walker_run | single | gaussian_noise | aco | 401004 | 28.939427 |
| walker_run | single | low_light | aco | 401000 | 141.204001 |
| walker_run | single | low_light | aco | 401001 | 106.725084 |
| walker_run | single | low_light | aco | 401002 | 115.350295 |
| walker_run | single | low_light | aco | 401003 | 88.509437 |
| walker_run | single | low_light | aco | 401004 | 138.383885 |
| walker_run | single | jpeg | aco | 401000 | 32.424585 |
| walker_run | single | jpeg | aco | 401001 | 49.415481 |
| walker_run | single | jpeg | aco | 401002 | 61.220911 |
| walker_run | single | jpeg | aco | 401003 | 40.030027 |
| walker_run | single | jpeg | aco | 401004 | 40.254267 |
| walker_run | single | defocus_blur | aco | 401000 | 291.015641 |
| walker_run | single | defocus_blur | aco | 401001 | 325.308148 |
| walker_run | single | defocus_blur | aco | 401002 | 234.161120 |
| walker_run | single | defocus_blur | aco | 401003 | 391.622679 |
| walker_run | single | defocus_blur | aco | 401004 | 335.739404 |
| walker_run | single | frost | aco | 401000 | 14.159146 |
| walker_run | single | frost | aco | 401001 | 40.971550 |
| walker_run | single | frost | aco | 401002 | 16.200963 |
| walker_run | single | frost | aco | 401003 | 46.456327 |
| walker_run | single | frost | aco | 401004 | 21.239620 |
| walker_run | single | occlusion_patch | aco | 401000 | 312.015506 |
| walker_run | single | occlusion_patch | aco | 401001 | 302.845493 |
| walker_run | single | occlusion_patch | aco | 401002 | 243.939985 |
| walker_run | single | occlusion_patch | aco | 401003 | 392.481838 |
| walker_run | single | occlusion_patch | aco | 401004 | 248.185230 |
| walker_run | single | saturation | aco | 401000 | 25.490572 |
| walker_run | single | saturation | aco | 401001 | 337.874049 |
| walker_run | single | saturation | aco | 401002 | 11.846916 |
| walker_run | single | saturation | aco | 401003 | 33.987886 |
| walker_run | single | saturation | aco | 401004 | 30.674393 |
| walker_run | single | shadow | aco | 401000 | 318.869008 |
| walker_run | single | shadow | aco | 401001 | 208.013155 |
| walker_run | single | shadow | aco | 401002 | 331.934935 |
| walker_run | single | shadow | aco | 401003 | 265.973062 |
| walker_run | single | shadow | aco | 401004 | 227.197240 |
| walker_run | single | shot_noise | aco | 401000 | 24.907043 |
| walker_run | single | shot_noise | aco | 401001 | 39.991094 |
| walker_run | single | shot_noise | aco | 401002 | 18.160997 |
| walker_run | single | shot_noise | aco | 401003 | 31.367895 |
| walker_run | single | shot_noise | aco | 401004 | 34.445561 |
| walker_run | markov | - | smfa | 401000 | 601.440477 |
| walker_run | markov | - | smfa | 401001 | 577.786829 |
| walker_run | markov | - | smfa | 401002 | 582.781479 |
| walker_run | markov | - | smfa | 401003 | 592.174329 |
| walker_run | markov | - | smfa | 401004 | 555.270396 |
| walker_run | markov | - | smfa | 401005 | 545.174354 |
| walker_run | markov | - | smfa | 401006 | 555.067697 |
| walker_run | markov | - | smfa | 401007 | 520.934292 |
| walker_run | markov | - | smfa | 401008 | 669.265060 |
| walker_run | markov | - | smfa | 401009 | 602.374243 |
| walker_run | single | rain | smfa | 401000 | 679.586169 |
| walker_run | single | rain | smfa | 401001 | 744.933648 |
| walker_run | single | rain | smfa | 401002 | 737.324346 |
| walker_run | single | rain | smfa | 401003 | 772.008401 |
| walker_run | single | rain | smfa | 401004 | 697.021041 |
| walker_run | single | fog | smfa | 401000 | 711.466665 |
| walker_run | single | fog | smfa | 401001 | 708.488914 |
| walker_run | single | fog | smfa | 401002 | 666.125732 |
| walker_run | single | fog | smfa | 401003 | 760.559989 |
| walker_run | single | fog | smfa | 401004 | 727.863030 |
| walker_run | single | snow | smfa | 401000 | 715.677604 |
| walker_run | single | snow | smfa | 401001 | 763.214842 |
| walker_run | single | snow | smfa | 401002 | 701.302049 |
| walker_run | single | snow | smfa | 401003 | 752.411288 |
| walker_run | single | snow | smfa | 401004 | 737.977857 |
| walker_run | single | motion_blur | smfa | 401000 | 275.405566 |
| walker_run | single | motion_blur | smfa | 401001 | 382.329807 |
| walker_run | single | motion_blur | smfa | 401002 | 394.873588 |
| walker_run | single | motion_blur | smfa | 401003 | 274.076287 |
| walker_run | single | motion_blur | smfa | 401004 | 222.662503 |
| walker_run | single | gaussian_noise | smfa | 401000 | 746.023205 |
| walker_run | single | gaussian_noise | smfa | 401001 | 765.427263 |
| walker_run | single | gaussian_noise | smfa | 401002 | 744.219790 |
| walker_run | single | gaussian_noise | smfa | 401003 | 758.540359 |
| walker_run | single | gaussian_noise | smfa | 401004 | 739.336559 |
| walker_run | single | low_light | smfa | 401000 | 718.720184 |
| walker_run | single | low_light | smfa | 401001 | 748.586536 |
| walker_run | single | low_light | smfa | 401002 | 683.986489 |
| walker_run | single | low_light | smfa | 401003 | 740.218149 |
| walker_run | single | low_light | smfa | 401004 | 645.975205 |
| walker_run | single | jpeg | smfa | 401000 | 722.224439 |
| walker_run | single | jpeg | smfa | 401001 | 716.653022 |
| walker_run | single | jpeg | smfa | 401002 | 701.715547 |
| walker_run | single | jpeg | smfa | 401003 | 737.420312 |
| walker_run | single | jpeg | smfa | 401004 | 725.808404 |
| walker_run | single | defocus_blur | smfa | 401000 | 562.171550 |
| walker_run | single | defocus_blur | smfa | 401001 | 403.387059 |
| walker_run | single | defocus_blur | smfa | 401002 | 632.101957 |
| walker_run | single | defocus_blur | smfa | 401003 | 550.894286 |
| walker_run | single | defocus_blur | smfa | 401004 | 331.612672 |
| walker_run | single | frost | smfa | 401000 | 718.139157 |
| walker_run | single | frost | smfa | 401001 | 770.638947 |
| walker_run | single | frost | smfa | 401002 | 723.951320 |
| walker_run | single | frost | smfa | 401003 | 764.465262 |
| walker_run | single | frost | smfa | 401004 | 733.731909 |
| walker_run | single | occlusion_patch | smfa | 401000 | 188.399284 |
| walker_run | single | occlusion_patch | smfa | 401001 | 331.959414 |
| walker_run | single | occlusion_patch | smfa | 401002 | 199.237519 |
| walker_run | single | occlusion_patch | smfa | 401003 | 233.551861 |
| walker_run | single | occlusion_patch | smfa | 401004 | 309.961870 |
| walker_run | single | saturation | smfa | 401000 | 750.967008 |
| walker_run | single | saturation | smfa | 401001 | 756.927822 |
| walker_run | single | saturation | smfa | 401002 | 714.000997 |
| walker_run | single | saturation | smfa | 401003 | 775.443544 |
| walker_run | single | saturation | smfa | 401004 | 740.091042 |
| walker_run | single | shadow | smfa | 401000 | 734.367082 |
| walker_run | single | shadow | smfa | 401001 | 741.068859 |
| walker_run | single | shadow | smfa | 401002 | 725.692131 |
| walker_run | single | shadow | smfa | 401003 | 754.729082 |
| walker_run | single | shadow | smfa | 401004 | 654.997292 |
| walker_run | single | shot_noise | smfa | 401000 | 740.750160 |
| walker_run | single | shot_noise | smfa | 401001 | 758.363065 |
| walker_run | single | shot_noise | smfa | 401002 | 722.300058 |
| walker_run | single | shot_noise | smfa | 401003 | 752.150442 |
| walker_run | single | shot_noise | smfa | 401004 | 741.243134 |
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
| walker_stand | markov | - | aco | 402000 | 734.962475 |
| walker_stand | markov | - | aco | 402001 | 683.553497 |
| walker_stand | markov | - | aco | 402002 | 665.069343 |
| walker_stand | markov | - | aco | 402003 | 626.783251 |
| walker_stand | markov | - | aco | 402004 | 549.907755 |
| walker_stand | markov | - | aco | 402005 | 705.705345 |
| walker_stand | markov | - | aco | 402006 | 511.357121 |
| walker_stand | markov | - | aco | 402007 | 905.377900 |
| walker_stand | markov | - | aco | 402008 | 540.182382 |
| walker_stand | markov | - | aco | 402009 | 887.361011 |
| walker_stand | single | rain | aco | 402000 | 982.170134 |
| walker_stand | single | rain | aco | 402001 | 948.118958 |
| walker_stand | single | rain | aco | 402002 | 981.771591 |
| walker_stand | single | rain | aco | 402003 | 981.674813 |
| walker_stand | single | rain | aco | 402004 | 958.118227 |
| walker_stand | single | fog | aco | 402000 | 190.614936 |
| walker_stand | single | fog | aco | 402001 | 186.742479 |
| walker_stand | single | fog | aco | 402002 | 381.004266 |
| walker_stand | single | fog | aco | 402003 | 228.555260 |
| walker_stand | single | fog | aco | 402004 | 325.821842 |
| walker_stand | single | snow | aco | 402000 | 956.619280 |
| walker_stand | single | snow | aco | 402001 | 980.821885 |
| walker_stand | single | snow | aco | 402002 | 983.349955 |
| walker_stand | single | snow | aco | 402003 | 973.964493 |
| walker_stand | single | snow | aco | 402004 | 955.199789 |
| walker_stand | single | motion_blur | aco | 402000 | 905.275990 |
| walker_stand | single | motion_blur | aco | 402001 | 931.906125 |
| walker_stand | single | motion_blur | aco | 402002 | 980.837317 |
| walker_stand | single | motion_blur | aco | 402003 | 960.946663 |
| walker_stand | single | motion_blur | aco | 402004 | 972.929160 |
| walker_stand | single | gaussian_noise | aco | 402000 | 176.336392 |
| walker_stand | single | gaussian_noise | aco | 402001 | 160.568416 |
| walker_stand | single | gaussian_noise | aco | 402002 | 322.327512 |
| walker_stand | single | gaussian_noise | aco | 402003 | 282.753781 |
| walker_stand | single | gaussian_noise | aco | 402004 | 279.384274 |
| walker_stand | single | low_light | aco | 402000 | 617.514641 |
| walker_stand | single | low_light | aco | 402001 | 641.878455 |
| walker_stand | single | low_light | aco | 402002 | 665.720096 |
| walker_stand | single | low_light | aco | 402003 | 863.059920 |
| walker_stand | single | low_light | aco | 402004 | 686.841013 |
| walker_stand | single | jpeg | aco | 402000 | 978.594501 |
| walker_stand | single | jpeg | aco | 402001 | 790.894887 |
| walker_stand | single | jpeg | aco | 402002 | 756.379377 |
| walker_stand | single | jpeg | aco | 402003 | 942.229848 |
| walker_stand | single | jpeg | aco | 402004 | 915.283053 |
| walker_stand | single | defocus_blur | aco | 402000 | 934.924487 |
| walker_stand | single | defocus_blur | aco | 402001 | 980.061917 |
| walker_stand | single | defocus_blur | aco | 402002 | 983.384073 |
| walker_stand | single | defocus_blur | aco | 402003 | 932.879269 |
| walker_stand | single | defocus_blur | aco | 402004 | 953.689069 |
| walker_stand | single | frost | aco | 402000 | 236.102922 |
| walker_stand | single | frost | aco | 402001 | 116.947990 |
| walker_stand | single | frost | aco | 402002 | 294.593461 |
| walker_stand | single | frost | aco | 402003 | 151.497148 |
| walker_stand | single | frost | aco | 402004 | 211.870282 |
| walker_stand | single | occlusion_patch | aco | 402000 | 983.987446 |
| walker_stand | single | occlusion_patch | aco | 402001 | 975.501475 |
| walker_stand | single | occlusion_patch | aco | 402002 | 963.393814 |
| walker_stand | single | occlusion_patch | aco | 402003 | 946.406091 |
| walker_stand | single | occlusion_patch | aco | 402004 | 576.394134 |
| walker_stand | single | saturation | aco | 402000 | 967.122612 |
| walker_stand | single | saturation | aco | 402001 | 958.885136 |
| walker_stand | single | saturation | aco | 402002 | 962.396151 |
| walker_stand | single | saturation | aco | 402003 | 265.809081 |
| walker_stand | single | saturation | aco | 402004 | 591.240651 |
| walker_stand | single | shadow | aco | 402000 | 951.492340 |
| walker_stand | single | shadow | aco | 402001 | 981.047578 |
| walker_stand | single | shadow | aco | 402002 | 957.530437 |
| walker_stand | single | shadow | aco | 402003 | 937.505705 |
| walker_stand | single | shadow | aco | 402004 | 891.974242 |
| walker_stand | single | shot_noise | aco | 402000 | 399.592029 |
| walker_stand | single | shot_noise | aco | 402001 | 162.169525 |
| walker_stand | single | shot_noise | aco | 402002 | 184.113894 |
| walker_stand | single | shot_noise | aco | 402003 | 343.688232 |
| walker_stand | single | shot_noise | aco | 402004 | 147.613352 |
| walker_stand | markov | - | smfa | 402000 | 941.364168 |
| walker_stand | markov | - | smfa | 402001 | 914.490591 |
| walker_stand | markov | - | smfa | 402002 | 928.645481 |
| walker_stand | markov | - | smfa | 402003 | 980.097092 |
| walker_stand | markov | - | smfa | 402004 | 970.593556 |
| walker_stand | markov | - | smfa | 402005 | 927.179817 |
| walker_stand | markov | - | smfa | 402006 | 997.476790 |
| walker_stand | markov | - | smfa | 402007 | 970.765992 |
| walker_stand | markov | - | smfa | 402008 | 982.935142 |
| walker_stand | markov | - | smfa | 402009 | 990.961681 |
| walker_stand | single | rain | smfa | 402000 | 982.963842 |
| walker_stand | single | rain | smfa | 402001 | 984.397111 |
| walker_stand | single | rain | smfa | 402002 | 982.216751 |
| walker_stand | single | rain | smfa | 402003 | 981.692248 |
| walker_stand | single | rain | smfa | 402004 | 961.956630 |
| walker_stand | single | fog | smfa | 402000 | 943.838683 |
| walker_stand | single | fog | smfa | 402001 | 978.600795 |
| walker_stand | single | fog | smfa | 402002 | 982.929935 |
| walker_stand | single | fog | smfa | 402003 | 980.094491 |
| walker_stand | single | fog | smfa | 402004 | 935.079261 |
| walker_stand | single | snow | smfa | 402000 | 983.827873 |
| walker_stand | single | snow | smfa | 402001 | 983.403994 |
| walker_stand | single | snow | smfa | 402002 | 982.990452 |
| walker_stand | single | snow | smfa | 402003 | 980.197844 |
| walker_stand | single | snow | smfa | 402004 | 972.933058 |
| walker_stand | single | motion_blur | smfa | 402000 | 967.222098 |
| walker_stand | single | motion_blur | smfa | 402001 | 975.008265 |
| walker_stand | single | motion_blur | smfa | 402002 | 928.930689 |
| walker_stand | single | motion_blur | smfa | 402003 | 813.406155 |
| walker_stand | single | motion_blur | smfa | 402004 | 967.868875 |
| walker_stand | single | gaussian_noise | smfa | 402000 | 976.957482 |
| walker_stand | single | gaussian_noise | smfa | 402001 | 960.928086 |
| walker_stand | single | gaussian_noise | smfa | 402002 | 980.659847 |
| walker_stand | single | gaussian_noise | smfa | 402003 | 981.836527 |
| walker_stand | single | gaussian_noise | smfa | 402004 | 962.151117 |
| walker_stand | single | low_light | smfa | 402000 | 977.623758 |
| walker_stand | single | low_light | smfa | 402001 | 972.164315 |
| walker_stand | single | low_light | smfa | 402002 | 985.045372 |
| walker_stand | single | low_light | smfa | 402003 | 979.743959 |
| walker_stand | single | low_light | smfa | 402004 | 935.285760 |
| walker_stand | single | jpeg | smfa | 402000 | 972.747948 |
| walker_stand | single | jpeg | smfa | 402001 | 980.556378 |
| walker_stand | single | jpeg | smfa | 402002 | 983.139999 |
| walker_stand | single | jpeg | smfa | 402003 | 980.814545 |
| walker_stand | single | jpeg | smfa | 402004 | 936.954985 |
| walker_stand | single | defocus_blur | smfa | 402000 | 957.958482 |
| walker_stand | single | defocus_blur | smfa | 402001 | 983.713960 |
| walker_stand | single | defocus_blur | smfa | 402002 | 978.418892 |
| walker_stand | single | defocus_blur | smfa | 402003 | 896.990814 |
| walker_stand | single | defocus_blur | smfa | 402004 | 967.764277 |
| walker_stand | single | frost | smfa | 402000 | 979.805143 |
| walker_stand | single | frost | smfa | 402001 | 982.431462 |
| walker_stand | single | frost | smfa | 402002 | 984.144201 |
| walker_stand | single | frost | smfa | 402003 | 979.411613 |
| walker_stand | single | frost | smfa | 402004 | 954.855172 |
| walker_stand | single | occlusion_patch | smfa | 402000 | 980.924290 |
| walker_stand | single | occlusion_patch | smfa | 402001 | 983.670199 |
| walker_stand | single | occlusion_patch | smfa | 402002 | 959.998687 |
| walker_stand | single | occlusion_patch | smfa | 402003 | 811.672609 |
| walker_stand | single | occlusion_patch | smfa | 402004 | 875.184008 |
| walker_stand | single | saturation | smfa | 402000 | 959.525292 |
| walker_stand | single | saturation | smfa | 402001 | 958.154983 |
| walker_stand | single | saturation | smfa | 402002 | 982.966017 |
| walker_stand | single | saturation | smfa | 402003 | 980.228262 |
| walker_stand | single | saturation | smfa | 402004 | 953.706102 |
| walker_stand | single | shadow | smfa | 402000 | 962.226695 |
| walker_stand | single | shadow | smfa | 402001 | 982.657067 |
| walker_stand | single | shadow | smfa | 402002 | 981.873600 |
| walker_stand | single | shadow | smfa | 402003 | 978.748920 |
| walker_stand | single | shadow | smfa | 402004 | 945.627672 |
| walker_stand | single | shot_noise | smfa | 402000 | 984.084277 |
| walker_stand | single | shot_noise | smfa | 402001 | 952.088947 |
| walker_stand | single | shot_noise | smfa | 402002 | 981.447544 |
| walker_stand | single | shot_noise | smfa | 402003 | 980.471307 |
| walker_stand | single | shot_noise | smfa | 402004 | 934.848154 |
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
| hopper_stand | markov | - | aco | 403000 | 241.495586 |
| hopper_stand | markov | - | aco | 403001 | 370.506188 |
| hopper_stand | markov | - | aco | 403002 | 462.725873 |
| hopper_stand | markov | - | aco | 403003 | 324.864291 |
| hopper_stand | markov | - | aco | 403004 | 0.000000 |
| hopper_stand | markov | - | aco | 403005 | 315.088324 |
| hopper_stand | markov | - | aco | 403006 | 406.629214 |
| hopper_stand | markov | - | aco | 403007 | 436.307487 |
| hopper_stand | markov | - | aco | 403008 | 273.282936 |
| hopper_stand | markov | - | aco | 403009 | 309.620305 |
| hopper_stand | single | rain | aco | 403000 | 903.463319 |
| hopper_stand | single | rain | aco | 403001 | 900.608122 |
| hopper_stand | single | rain | aco | 403002 | 899.606002 |
| hopper_stand | single | rain | aco | 403003 | 896.496423 |
| hopper_stand | single | rain | aco | 403004 | 0.000000 |
| hopper_stand | single | fog | aco | 403000 | 0.000000 |
| hopper_stand | single | fog | aco | 403001 | 13.810711 |
| hopper_stand | single | fog | aco | 403002 | 0.000000 |
| hopper_stand | single | fog | aco | 403003 | 0.000000 |
| hopper_stand | single | fog | aco | 403004 | 0.000000 |
| hopper_stand | single | snow | aco | 403000 | 891.307337 |
| hopper_stand | single | snow | aco | 403001 | 740.696486 |
| hopper_stand | single | snow | aco | 403002 | 892.679859 |
| hopper_stand | single | snow | aco | 403003 | 808.790292 |
| hopper_stand | single | snow | aco | 403004 | 0.000000 |
| hopper_stand | single | motion_blur | aco | 403000 | 295.295338 |
| hopper_stand | single | motion_blur | aco | 403001 | 342.369227 |
| hopper_stand | single | motion_blur | aco | 403002 | 696.643099 |
| hopper_stand | single | motion_blur | aco | 403003 | 335.029976 |
| hopper_stand | single | motion_blur | aco | 403004 | 0.000000 |
| hopper_stand | single | gaussian_noise | aco | 403000 | 0.000000 |
| hopper_stand | single | gaussian_noise | aco | 403001 | 10.451768 |
| hopper_stand | single | gaussian_noise | aco | 403002 | 0.000000 |
| hopper_stand | single | gaussian_noise | aco | 403003 | 0.000000 |
| hopper_stand | single | gaussian_noise | aco | 403004 | 0.000000 |
| hopper_stand | single | low_light | aco | 403000 | 818.962028 |
| hopper_stand | single | low_light | aco | 403001 | 747.416409 |
| hopper_stand | single | low_light | aco | 403002 | 814.541617 |
| hopper_stand | single | low_light | aco | 403003 | 869.920583 |
| hopper_stand | single | low_light | aco | 403004 | 0.000000 |
| hopper_stand | single | jpeg | aco | 403000 | 0.000000 |
| hopper_stand | single | jpeg | aco | 403001 | 23.402767 |
| hopper_stand | single | jpeg | aco | 403002 | 0.000000 |
| hopper_stand | single | jpeg | aco | 403003 | 0.000000 |
| hopper_stand | single | jpeg | aco | 403004 | 0.000000 |
| hopper_stand | single | defocus_blur | aco | 403000 | 727.603319 |
| hopper_stand | single | defocus_blur | aco | 403001 | 742.449145 |
| hopper_stand | single | defocus_blur | aco | 403002 | 692.520000 |
| hopper_stand | single | defocus_blur | aco | 403003 | 710.209572 |
| hopper_stand | single | defocus_blur | aco | 403004 | 0.000000 |
| hopper_stand | single | frost | aco | 403000 | 810.157169 |
| hopper_stand | single | frost | aco | 403001 | 446.335890 |
| hopper_stand | single | frost | aco | 403002 | 853.645202 |
| hopper_stand | single | frost | aco | 403003 | 192.255641 |
| hopper_stand | single | frost | aco | 403004 | 0.000000 |
| hopper_stand | single | occlusion_patch | aco | 403000 | 869.647328 |
| hopper_stand | single | occlusion_patch | aco | 403001 | 818.982423 |
| hopper_stand | single | occlusion_patch | aco | 403002 | 270.389214 |
| hopper_stand | single | occlusion_patch | aco | 403003 | 351.214520 |
| hopper_stand | single | occlusion_patch | aco | 403004 | 0.000000 |
| hopper_stand | single | saturation | aco | 403000 | 0.000000 |
| hopper_stand | single | saturation | aco | 403001 | 749.553338 |
| hopper_stand | single | saturation | aco | 403002 | 843.013673 |
| hopper_stand | single | saturation | aco | 403003 | 827.117992 |
| hopper_stand | single | saturation | aco | 403004 | 0.000000 |
| hopper_stand | single | shadow | aco | 403000 | 590.182248 |
| hopper_stand | single | shadow | aco | 403001 | 791.698279 |
| hopper_stand | single | shadow | aco | 403002 | 722.395003 |
| hopper_stand | single | shadow | aco | 403003 | 443.176004 |
| hopper_stand | single | shadow | aco | 403004 | 0.000000 |
| hopper_stand | single | shot_noise | aco | 403000 | 0.000000 |
| hopper_stand | single | shot_noise | aco | 403001 | 10.348625 |
| hopper_stand | single | shot_noise | aco | 403002 | 0.000000 |
| hopper_stand | single | shot_noise | aco | 403003 | 0.000000 |
| hopper_stand | single | shot_noise | aco | 403004 | 0.000000 |
| hopper_stand | markov | - | smfa | 403000 | 652.964676 |
| hopper_stand | markov | - | smfa | 403001 | 504.501305 |
| hopper_stand | markov | - | smfa | 403002 | 295.515418 |
| hopper_stand | markov | - | smfa | 403003 | 477.973320 |
| hopper_stand | markov | - | smfa | 403004 | 0.000000 |
| hopper_stand | markov | - | smfa | 403005 | 587.421116 |
| hopper_stand | markov | - | smfa | 403006 | 546.330648 |
| hopper_stand | markov | - | smfa | 403007 | 507.284650 |
| hopper_stand | markov | - | smfa | 403008 | 712.457824 |
| hopper_stand | markov | - | smfa | 403009 | 454.363404 |
| hopper_stand | single | rain | smfa | 403000 | 910.170573 |
| hopper_stand | single | rain | smfa | 403001 | 844.907272 |
| hopper_stand | single | rain | smfa | 403002 | 906.142495 |
| hopper_stand | single | rain | smfa | 403003 | 881.296332 |
| hopper_stand | single | rain | smfa | 403004 | 0.000000 |
| hopper_stand | single | fog | smfa | 403000 | 909.502795 |
| hopper_stand | single | fog | smfa | 403001 | 866.069401 |
| hopper_stand | single | fog | smfa | 403002 | 911.228596 |
| hopper_stand | single | fog | smfa | 403003 | 913.389648 |
| hopper_stand | single | fog | smfa | 403004 | 0.000000 |
| hopper_stand | single | snow | smfa | 403000 | 912.622364 |
| hopper_stand | single | snow | smfa | 403001 | 922.276229 |
| hopper_stand | single | snow | smfa | 403002 | 915.467774 |
| hopper_stand | single | snow | smfa | 403003 | 915.323007 |
| hopper_stand | single | snow | smfa | 403004 | 0.000000 |
| hopper_stand | single | motion_blur | smfa | 403000 | 225.763075 |
| hopper_stand | single | motion_blur | smfa | 403001 | 125.602808 |
| hopper_stand | single | motion_blur | smfa | 403002 | 157.735964 |
| hopper_stand | single | motion_blur | smfa | 403003 | 225.516327 |
| hopper_stand | single | motion_blur | smfa | 403004 | 0.000000 |
| hopper_stand | single | gaussian_noise | smfa | 403000 | 908.756605 |
| hopper_stand | single | gaussian_noise | smfa | 403001 | 925.633576 |
| hopper_stand | single | gaussian_noise | smfa | 403002 | 913.402581 |
| hopper_stand | single | gaussian_noise | smfa | 403003 | 914.346389 |
| hopper_stand | single | gaussian_noise | smfa | 403004 | 0.000000 |
| hopper_stand | single | low_light | smfa | 403000 | 904.682696 |
| hopper_stand | single | low_light | smfa | 403001 | 916.816825 |
| hopper_stand | single | low_light | smfa | 403002 | 806.936417 |
| hopper_stand | single | low_light | smfa | 403003 | 902.228643 |
| hopper_stand | single | low_light | smfa | 403004 | 0.000000 |
| hopper_stand | single | jpeg | smfa | 403000 | 489.876912 |
| hopper_stand | single | jpeg | smfa | 403001 | 699.795936 |
| hopper_stand | single | jpeg | smfa | 403002 | 866.550508 |
| hopper_stand | single | jpeg | smfa | 403003 | 599.859286 |
| hopper_stand | single | jpeg | smfa | 403004 | 0.000000 |
| hopper_stand | single | defocus_blur | smfa | 403000 | 209.152190 |
| hopper_stand | single | defocus_blur | smfa | 403001 | 101.178487 |
| hopper_stand | single | defocus_blur | smfa | 403002 | 268.484339 |
| hopper_stand | single | defocus_blur | smfa | 403003 | 122.067310 |
| hopper_stand | single | defocus_blur | smfa | 403004 | 0.000000 |
| hopper_stand | single | frost | smfa | 403000 | 910.090459 |
| hopper_stand | single | frost | smfa | 403001 | 916.562562 |
| hopper_stand | single | frost | smfa | 403002 | 914.107562 |
| hopper_stand | single | frost | smfa | 403003 | 911.515431 |
| hopper_stand | single | frost | smfa | 403004 | 0.000000 |
| hopper_stand | single | occlusion_patch | smfa | 403000 | 911.618950 |
| hopper_stand | single | occlusion_patch | smfa | 403001 | 921.155910 |
| hopper_stand | single | occlusion_patch | smfa | 403002 | 372.573226 |
| hopper_stand | single | occlusion_patch | smfa | 403003 | 38.741962 |
| hopper_stand | single | occlusion_patch | smfa | 403004 | 0.000000 |
| hopper_stand | single | saturation | smfa | 403000 | 912.034847 |
| hopper_stand | single | saturation | smfa | 403001 | 907.478620 |
| hopper_stand | single | saturation | smfa | 403002 | 900.869508 |
| hopper_stand | single | saturation | smfa | 403003 | 912.975313 |
| hopper_stand | single | saturation | smfa | 403004 | 0.000000 |
| hopper_stand | single | shadow | smfa | 403000 | 894.542562 |
| hopper_stand | single | shadow | smfa | 403001 | 923.917502 |
| hopper_stand | single | shadow | smfa | 403002 | 841.487147 |
| hopper_stand | single | shadow | smfa | 403003 | 913.775030 |
| hopper_stand | single | shadow | smfa | 403004 | 0.000000 |
| hopper_stand | single | shot_noise | smfa | 403000 | 908.257936 |
| hopper_stand | single | shot_noise | smfa | 403001 | 919.426351 |
| hopper_stand | single | shot_noise | smfa | 403002 | 896.586910 |
| hopper_stand | single | shot_noise | smfa | 403003 | 904.289142 |
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
| quadruped_run | markov | - | aco | 404000 | 547.898668 |
| quadruped_run | markov | - | aco | 404001 | 438.291576 |
| quadruped_run | markov | - | aco | 404002 | 530.786287 |
| quadruped_run | markov | - | aco | 404003 | 543.314480 |
| quadruped_run | markov | - | aco | 404004 | 563.919843 |
| quadruped_run | markov | - | aco | 404005 | 251.222577 |
| quadruped_run | markov | - | aco | 404006 | 427.140008 |
| quadruped_run | markov | - | aco | 404007 | 460.554574 |
| quadruped_run | markov | - | aco | 404008 | 76.139043 |
| quadruped_run | markov | - | aco | 404009 | 455.182433 |
| quadruped_run | single | rain | aco | 404000 | 36.973368 |
| quadruped_run | single | rain | aco | 404001 | 522.007295 |
| quadruped_run | single | rain | aco | 404002 | 30.205678 |
| quadruped_run | single | rain | aco | 404003 | 296.631436 |
| quadruped_run | single | rain | aco | 404004 | 559.876531 |
| quadruped_run | single | fog | aco | 404000 | 426.719703 |
| quadruped_run | single | fog | aco | 404001 | 195.761605 |
| quadruped_run | single | fog | aco | 404002 | 332.880565 |
| quadruped_run | single | fog | aco | 404003 | 388.390009 |
| quadruped_run | single | fog | aco | 404004 | 445.693526 |
| quadruped_run | single | snow | aco | 404000 | 418.216477 |
| quadruped_run | single | snow | aco | 404001 | 525.357209 |
| quadruped_run | single | snow | aco | 404002 | 521.661880 |
| quadruped_run | single | snow | aco | 404003 | 467.604806 |
| quadruped_run | single | snow | aco | 404004 | 544.317349 |
| quadruped_run | single | motion_blur | aco | 404000 | 490.210167 |
| quadruped_run | single | motion_blur | aco | 404001 | 511.821859 |
| quadruped_run | single | motion_blur | aco | 404002 | 533.552968 |
| quadruped_run | single | motion_blur | aco | 404003 | 472.569938 |
| quadruped_run | single | motion_blur | aco | 404004 | 557.436764 |
| quadruped_run | single | gaussian_noise | aco | 404000 | 66.292745 |
| quadruped_run | single | gaussian_noise | aco | 404001 | 413.409206 |
| quadruped_run | single | gaussian_noise | aco | 404002 | 427.047048 |
| quadruped_run | single | gaussian_noise | aco | 404003 | 361.699572 |
| quadruped_run | single | gaussian_noise | aco | 404004 | 330.069257 |
| quadruped_run | single | low_light | aco | 404000 | 228.145436 |
| quadruped_run | single | low_light | aco | 404001 | 400.702047 |
| quadruped_run | single | low_light | aco | 404002 | 226.203584 |
| quadruped_run | single | low_light | aco | 404003 | 211.713049 |
| quadruped_run | single | low_light | aco | 404004 | 436.325278 |
| quadruped_run | single | jpeg | aco | 404000 | 225.713404 |
| quadruped_run | single | jpeg | aco | 404001 | 251.458140 |
| quadruped_run | single | jpeg | aco | 404002 | 242.154724 |
| quadruped_run | single | jpeg | aco | 404003 | 198.898837 |
| quadruped_run | single | jpeg | aco | 404004 | 285.062129 |
| quadruped_run | single | defocus_blur | aco | 404000 | 541.066540 |
| quadruped_run | single | defocus_blur | aco | 404001 | 442.292503 |
| quadruped_run | single | defocus_blur | aco | 404002 | 541.055262 |
| quadruped_run | single | defocus_blur | aco | 404003 | 213.167981 |
| quadruped_run | single | defocus_blur | aco | 404004 | 453.413341 |
| quadruped_run | single | frost | aco | 404000 | 348.919740 |
| quadruped_run | single | frost | aco | 404001 | 23.545628 |
| quadruped_run | single | frost | aco | 404002 | 427.223393 |
| quadruped_run | single | frost | aco | 404003 | 378.373328 |
| quadruped_run | single | frost | aco | 404004 | 398.996256 |
| quadruped_run | single | occlusion_patch | aco | 404000 | 561.987523 |
| quadruped_run | single | occlusion_patch | aco | 404001 | 193.298283 |
| quadruped_run | single | occlusion_patch | aco | 404002 | 535.713015 |
| quadruped_run | single | occlusion_patch | aco | 404003 | 236.618929 |
| quadruped_run | single | occlusion_patch | aco | 404004 | 564.328754 |
| quadruped_run | single | saturation | aco | 404000 | 520.012242 |
| quadruped_run | single | saturation | aco | 404001 | 449.405628 |
| quadruped_run | single | saturation | aco | 404002 | 433.625018 |
| quadruped_run | single | saturation | aco | 404003 | 18.401913 |
| quadruped_run | single | saturation | aco | 404004 | 542.456864 |
| quadruped_run | single | shadow | aco | 404000 | 456.107967 |
| quadruped_run | single | shadow | aco | 404001 | 181.777731 |
| quadruped_run | single | shadow | aco | 404002 | 525.970107 |
| quadruped_run | single | shadow | aco | 404003 | 499.417897 |
| quadruped_run | single | shadow | aco | 404004 | 312.510445 |
| quadruped_run | single | shot_noise | aco | 404000 | 30.957693 |
| quadruped_run | single | shot_noise | aco | 404001 | 17.686599 |
| quadruped_run | single | shot_noise | aco | 404002 | 449.000434 |
| quadruped_run | single | shot_noise | aco | 404003 | 343.711877 |
| quadruped_run | single | shot_noise | aco | 404004 | 456.300904 |
| quadruped_run | markov | - | smfa | 404000 | 552.407647 |
| quadruped_run | markov | - | smfa | 404001 | 503.826602 |
| quadruped_run | markov | - | smfa | 404002 | 531.293159 |
| quadruped_run | markov | - | smfa | 404003 | 474.929882 |
| quadruped_run | markov | - | smfa | 404004 | 559.060416 |
| quadruped_run | markov | - | smfa | 404005 | 411.226367 |
| quadruped_run | markov | - | smfa | 404006 | 496.421670 |
| quadruped_run | markov | - | smfa | 404007 | 514.493148 |
| quadruped_run | markov | - | smfa | 404008 | 523.907855 |
| quadruped_run | markov | - | smfa | 404009 | 495.451348 |
| quadruped_run | single | rain | smfa | 404000 | 548.057319 |
| quadruped_run | single | rain | smfa | 404001 | 420.952582 |
| quadruped_run | single | rain | smfa | 404002 | 527.736168 |
| quadruped_run | single | rain | smfa | 404003 | 476.060774 |
| quadruped_run | single | rain | smfa | 404004 | 557.084461 |
| quadruped_run | single | fog | smfa | 404000 | 565.917593 |
| quadruped_run | single | fog | smfa | 404001 | 533.792505 |
| quadruped_run | single | fog | smfa | 404002 | 537.291746 |
| quadruped_run | single | fog | smfa | 404003 | 345.433524 |
| quadruped_run | single | fog | smfa | 404004 | 563.350683 |
| quadruped_run | single | snow | smfa | 404000 | 532.450235 |
| quadruped_run | single | snow | smfa | 404001 | 528.969332 |
| quadruped_run | single | snow | smfa | 404002 | 535.048342 |
| quadruped_run | single | snow | smfa | 404003 | 489.305331 |
| quadruped_run | single | snow | smfa | 404004 | 554.671136 |
| quadruped_run | single | motion_blur | smfa | 404000 | 502.008515 |
| quadruped_run | single | motion_blur | smfa | 404001 | 14.770596 |
| quadruped_run | single | motion_blur | smfa | 404002 | 533.642661 |
| quadruped_run | single | motion_blur | smfa | 404003 | 440.714278 |
| quadruped_run | single | motion_blur | smfa | 404004 | 555.669400 |
| quadruped_run | single | gaussian_noise | smfa | 404000 | 563.545697 |
| quadruped_run | single | gaussian_noise | smfa | 404001 | 478.983133 |
| quadruped_run | single | gaussian_noise | smfa | 404002 | 536.062775 |
| quadruped_run | single | gaussian_noise | smfa | 404003 | 403.503611 |
| quadruped_run | single | gaussian_noise | smfa | 404004 | 556.276955 |
| quadruped_run | single | low_light | smfa | 404000 | 312.094834 |
| quadruped_run | single | low_light | smfa | 404001 | 395.160461 |
| quadruped_run | single | low_light | smfa | 404002 | 514.547515 |
| quadruped_run | single | low_light | smfa | 404003 | 493.708910 |
| quadruped_run | single | low_light | smfa | 404004 | 559.436740 |
| quadruped_run | single | jpeg | smfa | 404000 | 563.187034 |
| quadruped_run | single | jpeg | smfa | 404001 | 513.899081 |
| quadruped_run | single | jpeg | smfa | 404002 | 540.300411 |
| quadruped_run | single | jpeg | smfa | 404003 | 403.388656 |
| quadruped_run | single | jpeg | smfa | 404004 | 562.311626 |
| quadruped_run | single | defocus_blur | smfa | 404000 | 551.693926 |
| quadruped_run | single | defocus_blur | smfa | 404001 | 452.685295 |
| quadruped_run | single | defocus_blur | smfa | 404002 | 512.250632 |
| quadruped_run | single | defocus_blur | smfa | 404003 | 377.288831 |
| quadruped_run | single | defocus_blur | smfa | 404004 | 565.101434 |
| quadruped_run | single | frost | smfa | 404000 | 64.091996 |
| quadruped_run | single | frost | smfa | 404001 | 512.785017 |
| quadruped_run | single | frost | smfa | 404002 | 534.959653 |
| quadruped_run | single | frost | smfa | 404003 | 284.574090 |
| quadruped_run | single | frost | smfa | 404004 | 566.795484 |
| quadruped_run | single | occlusion_patch | smfa | 404000 | 559.442419 |
| quadruped_run | single | occlusion_patch | smfa | 404001 | 510.601033 |
| quadruped_run | single | occlusion_patch | smfa | 404002 | 497.945978 |
| quadruped_run | single | occlusion_patch | smfa | 404003 | 55.023128 |
| quadruped_run | single | occlusion_patch | smfa | 404004 | 564.468943 |
| quadruped_run | single | saturation | smfa | 404000 | 557.535925 |
| quadruped_run | single | saturation | smfa | 404001 | 529.015035 |
| quadruped_run | single | saturation | smfa | 404002 | 527.055557 |
| quadruped_run | single | saturation | smfa | 404003 | 489.012873 |
| quadruped_run | single | saturation | smfa | 404004 | 550.364831 |
| quadruped_run | single | shadow | smfa | 404000 | 532.992096 |
| quadruped_run | single | shadow | smfa | 404001 | 499.878391 |
| quadruped_run | single | shadow | smfa | 404002 | 538.854026 |
| quadruped_run | single | shadow | smfa | 404003 | 484.150042 |
| quadruped_run | single | shadow | smfa | 404004 | 554.377103 |
| quadruped_run | single | shot_noise | smfa | 404000 | 566.720478 |
| quadruped_run | single | shot_noise | smfa | 404001 | 465.188201 |
| quadruped_run | single | shot_noise | smfa | 404002 | 510.734667 |
| quadruped_run | single | shot_noise | smfa | 404003 | 480.920555 |
| quadruped_run | single | shot_noise | smfa | 404004 | 569.231274 |
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
| finger_turn_hard | markov | - | aco | 405001 | 0.000000 |
| finger_turn_hard | markov | - | aco | 405002 | 5.000000 |
| finger_turn_hard | markov | - | aco | 405003 | 106.000000 |
| finger_turn_hard | markov | - | aco | 405004 | 396.000000 |
| finger_turn_hard | markov | - | aco | 405005 | 9.000000 |
| finger_turn_hard | markov | - | aco | 405006 | 919.000000 |
| finger_turn_hard | markov | - | aco | 405007 | 71.000000 |
| finger_turn_hard | markov | - | aco | 405008 | 180.000000 |
| finger_turn_hard | markov | - | aco | 405009 | 3.000000 |
| finger_turn_hard | single | rain | aco | 405000 | 807.000000 |
| finger_turn_hard | single | rain | aco | 405001 | 0.000000 |
| finger_turn_hard | single | rain | aco | 405002 | 928.000000 |
| finger_turn_hard | single | rain | aco | 405003 | 897.000000 |
| finger_turn_hard | single | rain | aco | 405004 | 821.000000 |
| finger_turn_hard | single | fog | aco | 405000 | 344.000000 |
| finger_turn_hard | single | fog | aco | 405001 | 0.000000 |
| finger_turn_hard | single | fog | aco | 405002 | 0.000000 |
| finger_turn_hard | single | fog | aco | 405003 | 0.000000 |
| finger_turn_hard | single | fog | aco | 405004 | 0.000000 |
| finger_turn_hard | single | snow | aco | 405000 | 0.000000 |
| finger_turn_hard | single | snow | aco | 405001 | 0.000000 |
| finger_turn_hard | single | snow | aco | 405002 | 41.000000 |
| finger_turn_hard | single | snow | aco | 405003 | 437.000000 |
| finger_turn_hard | single | snow | aco | 405004 | 0.000000 |
| finger_turn_hard | single | motion_blur | aco | 405000 | 0.000000 |
| finger_turn_hard | single | motion_blur | aco | 405001 | 0.000000 |
| finger_turn_hard | single | motion_blur | aco | 405002 | 167.000000 |
| finger_turn_hard | single | motion_blur | aco | 405003 | 0.000000 |
| finger_turn_hard | single | motion_blur | aco | 405004 | 573.000000 |
| finger_turn_hard | single | gaussian_noise | aco | 405000 | 0.000000 |
| finger_turn_hard | single | gaussian_noise | aco | 405001 | 0.000000 |
| finger_turn_hard | single | gaussian_noise | aco | 405002 | 0.000000 |
| finger_turn_hard | single | gaussian_noise | aco | 405003 | 0.000000 |
| finger_turn_hard | single | gaussian_noise | aco | 405004 | 0.000000 |
| finger_turn_hard | single | low_light | aco | 405000 | 0.000000 |
| finger_turn_hard | single | low_light | aco | 405001 | 0.000000 |
| finger_turn_hard | single | low_light | aco | 405002 | 153.000000 |
| finger_turn_hard | single | low_light | aco | 405003 | 7.000000 |
| finger_turn_hard | single | low_light | aco | 405004 | 425.000000 |
| finger_turn_hard | single | jpeg | aco | 405000 | 0.000000 |
| finger_turn_hard | single | jpeg | aco | 405001 | 0.000000 |
| finger_turn_hard | single | jpeg | aco | 405002 | 0.000000 |
| finger_turn_hard | single | jpeg | aco | 405003 | 0.000000 |
| finger_turn_hard | single | jpeg | aco | 405004 | 0.000000 |
| finger_turn_hard | single | defocus_blur | aco | 405000 | 30.000000 |
| finger_turn_hard | single | defocus_blur | aco | 405001 | 915.000000 |
| finger_turn_hard | single | defocus_blur | aco | 405002 | 960.000000 |
| finger_turn_hard | single | defocus_blur | aco | 405003 | 0.000000 |
| finger_turn_hard | single | defocus_blur | aco | 405004 | 338.000000 |
| finger_turn_hard | single | frost | aco | 405000 | 0.000000 |
| finger_turn_hard | single | frost | aco | 405001 | 0.000000 |
| finger_turn_hard | single | frost | aco | 405002 | 129.000000 |
| finger_turn_hard | single | frost | aco | 405003 | 773.000000 |
| finger_turn_hard | single | frost | aco | 405004 | 52.000000 |
| finger_turn_hard | single | occlusion_patch | aco | 405000 | 564.000000 |
| finger_turn_hard | single | occlusion_patch | aco | 405001 | 0.000000 |
| finger_turn_hard | single | occlusion_patch | aco | 405002 | 961.000000 |
| finger_turn_hard | single | occlusion_patch | aco | 405003 | 493.000000 |
| finger_turn_hard | single | occlusion_patch | aco | 405004 | 929.000000 |
| finger_turn_hard | single | saturation | aco | 405000 | 0.000000 |
| finger_turn_hard | single | saturation | aco | 405001 | 0.000000 |
| finger_turn_hard | single | saturation | aco | 405002 | 0.000000 |
| finger_turn_hard | single | saturation | aco | 405003 | 15.000000 |
| finger_turn_hard | single | saturation | aco | 405004 | 0.000000 |
| finger_turn_hard | single | shadow | aco | 405000 | 980.000000 |
| finger_turn_hard | single | shadow | aco | 405001 | 903.000000 |
| finger_turn_hard | single | shadow | aco | 405002 | 7.000000 |
| finger_turn_hard | single | shadow | aco | 405003 | 0.000000 |
| finger_turn_hard | single | shadow | aco | 405004 | 112.000000 |
| finger_turn_hard | single | shot_noise | aco | 405000 | 0.000000 |
| finger_turn_hard | single | shot_noise | aco | 405001 | 0.000000 |
| finger_turn_hard | single | shot_noise | aco | 405002 | 0.000000 |
| finger_turn_hard | single | shot_noise | aco | 405003 | 0.000000 |
| finger_turn_hard | single | shot_noise | aco | 405004 | 0.000000 |
| finger_turn_hard | markov | - | smfa | 405000 | 103.000000 |
| finger_turn_hard | markov | - | smfa | 405001 | 888.000000 |
| finger_turn_hard | markov | - | smfa | 405002 | 920.000000 |
| finger_turn_hard | markov | - | smfa | 405003 | 16.000000 |
| finger_turn_hard | markov | - | smfa | 405004 | 842.000000 |
| finger_turn_hard | markov | - | smfa | 405005 | 944.000000 |
| finger_turn_hard | markov | - | smfa | 405006 | 925.000000 |
| finger_turn_hard | markov | - | smfa | 405007 | 724.000000 |
| finger_turn_hard | markov | - | smfa | 405008 | 826.000000 |
| finger_turn_hard | markov | - | smfa | 405009 | 898.000000 |
| finger_turn_hard | single | rain | smfa | 405000 | 2.000000 |
| finger_turn_hard | single | rain | smfa | 405001 | 919.000000 |
| finger_turn_hard | single | rain | smfa | 405002 | 956.000000 |
| finger_turn_hard | single | rain | smfa | 405003 | 0.000000 |
| finger_turn_hard | single | rain | smfa | 405004 | 932.000000 |
| finger_turn_hard | single | fog | smfa | 405000 | 974.000000 |
| finger_turn_hard | single | fog | smfa | 405001 | 934.000000 |
| finger_turn_hard | single | fog | smfa | 405002 | 956.000000 |
| finger_turn_hard | single | fog | smfa | 405003 | 0.000000 |
| finger_turn_hard | single | fog | smfa | 405004 | 928.000000 |
| finger_turn_hard | single | snow | smfa | 405000 | 973.000000 |
| finger_turn_hard | single | snow | smfa | 405001 | 934.000000 |
| finger_turn_hard | single | snow | smfa | 405002 | 957.000000 |
| finger_turn_hard | single | snow | smfa | 405003 | 0.000000 |
| finger_turn_hard | single | snow | smfa | 405004 | 940.000000 |
| finger_turn_hard | single | motion_blur | smfa | 405000 | 42.000000 |
| finger_turn_hard | single | motion_blur | smfa | 405001 | 553.000000 |
| finger_turn_hard | single | motion_blur | smfa | 405002 | 0.000000 |
| finger_turn_hard | single | motion_blur | smfa | 405003 | 44.000000 |
| finger_turn_hard | single | motion_blur | smfa | 405004 | 72.000000 |
| finger_turn_hard | single | gaussian_noise | smfa | 405000 | 0.000000 |
| finger_turn_hard | single | gaussian_noise | smfa | 405001 | 932.000000 |
| finger_turn_hard | single | gaussian_noise | smfa | 405002 | 925.000000 |
| finger_turn_hard | single | gaussian_noise | smfa | 405003 | 0.000000 |
| finger_turn_hard | single | gaussian_noise | smfa | 405004 | 904.000000 |
| finger_turn_hard | single | low_light | smfa | 405000 | 0.000000 |
| finger_turn_hard | single | low_light | smfa | 405001 | 0.000000 |
| finger_turn_hard | single | low_light | smfa | 405002 | 958.000000 |
| finger_turn_hard | single | low_light | smfa | 405003 | 0.000000 |
| finger_turn_hard | single | low_light | smfa | 405004 | 926.000000 |
| finger_turn_hard | single | jpeg | smfa | 405000 | 867.000000 |
| finger_turn_hard | single | jpeg | smfa | 405001 | 0.000000 |
| finger_turn_hard | single | jpeg | smfa | 405002 | 960.000000 |
| finger_turn_hard | single | jpeg | smfa | 405003 | 0.000000 |
| finger_turn_hard | single | jpeg | smfa | 405004 | 919.000000 |
| finger_turn_hard | single | defocus_blur | smfa | 405000 | 7.000000 |
| finger_turn_hard | single | defocus_blur | smfa | 405001 | 791.000000 |
| finger_turn_hard | single | defocus_blur | smfa | 405002 | 17.000000 |
| finger_turn_hard | single | defocus_blur | smfa | 405003 | 6.000000 |
| finger_turn_hard | single | defocus_blur | smfa | 405004 | 516.000000 |
| finger_turn_hard | single | frost | smfa | 405000 | 972.000000 |
| finger_turn_hard | single | frost | smfa | 405001 | 932.000000 |
| finger_turn_hard | single | frost | smfa | 405002 | 951.000000 |
| finger_turn_hard | single | frost | smfa | 405003 | 0.000000 |
| finger_turn_hard | single | frost | smfa | 405004 | 920.000000 |
| finger_turn_hard | single | occlusion_patch | smfa | 405000 | 981.000000 |
| finger_turn_hard | single | occlusion_patch | smfa | 405001 | 0.000000 |
| finger_turn_hard | single | occlusion_patch | smfa | 405002 | 949.000000 |
| finger_turn_hard | single | occlusion_patch | smfa | 405003 | 77.000000 |
| finger_turn_hard | single | occlusion_patch | smfa | 405004 | 924.000000 |
| finger_turn_hard | single | saturation | smfa | 405000 | 980.000000 |
| finger_turn_hard | single | saturation | smfa | 405001 | 931.000000 |
| finger_turn_hard | single | saturation | smfa | 405002 | 959.000000 |
| finger_turn_hard | single | saturation | smfa | 405003 | 0.000000 |
| finger_turn_hard | single | saturation | smfa | 405004 | 926.000000 |
| finger_turn_hard | single | shadow | smfa | 405000 | 974.000000 |
| finger_turn_hard | single | shadow | smfa | 405001 | 923.000000 |
| finger_turn_hard | single | shadow | smfa | 405002 | 960.000000 |
| finger_turn_hard | single | shadow | smfa | 405003 | 0.000000 |
| finger_turn_hard | single | shadow | smfa | 405004 | 914.000000 |
| finger_turn_hard | single | shot_noise | smfa | 405000 | 0.000000 |
| finger_turn_hard | single | shot_noise | smfa | 405001 | 937.000000 |
| finger_turn_hard | single | shot_noise | smfa | 405002 | 955.000000 |
| finger_turn_hard | single | shot_noise | smfa | 405003 | 0.000000 |
| finger_turn_hard | single | shot_noise | smfa | 405004 | 927.000000 |
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
| cartpole_swingup_sparse | markov | - | aco | 406000 | 12.000000 |
| cartpole_swingup_sparse | markov | - | aco | 406001 | 385.000000 |
| cartpole_swingup_sparse | markov | - | aco | 406002 | 180.000000 |
| cartpole_swingup_sparse | markov | - | aco | 406003 | 29.000000 |
| cartpole_swingup_sparse | markov | - | aco | 406004 | 116.000000 |
| cartpole_swingup_sparse | markov | - | aco | 406005 | 92.000000 |
| cartpole_swingup_sparse | markov | - | aco | 406006 | 26.000000 |
| cartpole_swingup_sparse | markov | - | aco | 406007 | 0.000000 |
| cartpole_swingup_sparse | markov | - | aco | 406008 | 12.000000 |
| cartpole_swingup_sparse | markov | - | aco | 406009 | 51.000000 |
| cartpole_swingup_sparse | single | rain | aco | 406000 | 625.000000 |
| cartpole_swingup_sparse | single | rain | aco | 406001 | 630.000000 |
| cartpole_swingup_sparse | single | rain | aco | 406002 | 639.000000 |
| cartpole_swingup_sparse | single | rain | aco | 406003 | 783.000000 |
| cartpole_swingup_sparse | single | rain | aco | 406004 | 638.000000 |
| cartpole_swingup_sparse | single | fog | aco | 406000 | 0.000000 |
| cartpole_swingup_sparse | single | fog | aco | 406001 | 0.000000 |
| cartpole_swingup_sparse | single | fog | aco | 406002 | 0.000000 |
| cartpole_swingup_sparse | single | fog | aco | 406003 | 17.000000 |
| cartpole_swingup_sparse | single | fog | aco | 406004 | 0.000000 |
| cartpole_swingup_sparse | single | snow | aco | 406000 | 477.000000 |
| cartpole_swingup_sparse | single | snow | aco | 406001 | 253.000000 |
| cartpole_swingup_sparse | single | snow | aco | 406002 | 475.000000 |
| cartpole_swingup_sparse | single | snow | aco | 406003 | 418.000000 |
| cartpole_swingup_sparse | single | snow | aco | 406004 | 489.000000 |
| cartpole_swingup_sparse | single | motion_blur | aco | 406000 | 716.000000 |
| cartpole_swingup_sparse | single | motion_blur | aco | 406001 | 50.000000 |
| cartpole_swingup_sparse | single | motion_blur | aco | 406002 | 47.000000 |
| cartpole_swingup_sparse | single | motion_blur | aco | 406003 | 811.000000 |
| cartpole_swingup_sparse | single | motion_blur | aco | 406004 | 314.000000 |
| cartpole_swingup_sparse | single | gaussian_noise | aco | 406000 | 0.000000 |
| cartpole_swingup_sparse | single | gaussian_noise | aco | 406001 | 0.000000 |
| cartpole_swingup_sparse | single | gaussian_noise | aco | 406002 | 0.000000 |
| cartpole_swingup_sparse | single | gaussian_noise | aco | 406003 | 0.000000 |
| cartpole_swingup_sparse | single | gaussian_noise | aco | 406004 | 0.000000 |
| cartpole_swingup_sparse | single | low_light | aco | 406000 | 384.000000 |
| cartpole_swingup_sparse | single | low_light | aco | 406001 | 461.000000 |
| cartpole_swingup_sparse | single | low_light | aco | 406002 | 320.000000 |
| cartpole_swingup_sparse | single | low_light | aco | 406003 | 402.000000 |
| cartpole_swingup_sparse | single | low_light | aco | 406004 | 260.000000 |
| cartpole_swingup_sparse | single | jpeg | aco | 406000 | 0.000000 |
| cartpole_swingup_sparse | single | jpeg | aco | 406001 | 0.000000 |
| cartpole_swingup_sparse | single | jpeg | aco | 406002 | 0.000000 |
| cartpole_swingup_sparse | single | jpeg | aco | 406003 | 0.000000 |
| cartpole_swingup_sparse | single | jpeg | aco | 406004 | 0.000000 |
| cartpole_swingup_sparse | single | defocus_blur | aco | 406000 | 746.000000 |
| cartpole_swingup_sparse | single | defocus_blur | aco | 406001 | 737.000000 |
| cartpole_swingup_sparse | single | defocus_blur | aco | 406002 | 46.000000 |
| cartpole_swingup_sparse | single | defocus_blur | aco | 406003 | 87.000000 |
| cartpole_swingup_sparse | single | defocus_blur | aco | 406004 | 64.000000 |
| cartpole_swingup_sparse | single | frost | aco | 406000 | 469.000000 |
| cartpole_swingup_sparse | single | frost | aco | 406001 | 580.000000 |
| cartpole_swingup_sparse | single | frost | aco | 406002 | 675.000000 |
| cartpole_swingup_sparse | single | frost | aco | 406003 | 831.000000 |
| cartpole_swingup_sparse | single | frost | aco | 406004 | 828.000000 |
| cartpole_swingup_sparse | single | occlusion_patch | aco | 406000 | 829.000000 |
| cartpole_swingup_sparse | single | occlusion_patch | aco | 406001 | 19.000000 |
| cartpole_swingup_sparse | single | occlusion_patch | aco | 406002 | 617.000000 |
| cartpole_swingup_sparse | single | occlusion_patch | aco | 406003 | 779.000000 |
| cartpole_swingup_sparse | single | occlusion_patch | aco | 406004 | 7.000000 |
| cartpole_swingup_sparse | single | saturation | aco | 406000 | 837.000000 |
| cartpole_swingup_sparse | single | saturation | aco | 406001 | 468.000000 |
| cartpole_swingup_sparse | single | saturation | aco | 406002 | 835.000000 |
| cartpole_swingup_sparse | single | saturation | aco | 406003 | 833.000000 |
| cartpole_swingup_sparse | single | saturation | aco | 406004 | 0.000000 |
| cartpole_swingup_sparse | single | shadow | aco | 406000 | 153.000000 |
| cartpole_swingup_sparse | single | shadow | aco | 406001 | 205.000000 |
| cartpole_swingup_sparse | single | shadow | aco | 406002 | 144.000000 |
| cartpole_swingup_sparse | single | shadow | aco | 406003 | 293.000000 |
| cartpole_swingup_sparse | single | shadow | aco | 406004 | 215.000000 |
| cartpole_swingup_sparse | single | shot_noise | aco | 406000 | 0.000000 |
| cartpole_swingup_sparse | single | shot_noise | aco | 406001 | 0.000000 |
| cartpole_swingup_sparse | single | shot_noise | aco | 406002 | 0.000000 |
| cartpole_swingup_sparse | single | shot_noise | aco | 406003 | 0.000000 |
| cartpole_swingup_sparse | single | shot_noise | aco | 406004 | 0.000000 |
| cartpole_swingup_sparse | markov | - | smfa | 406000 | 332.000000 |
| cartpole_swingup_sparse | markov | - | smfa | 406001 | 670.000000 |
| cartpole_swingup_sparse | markov | - | smfa | 406002 | 593.000000 |
| cartpole_swingup_sparse | markov | - | smfa | 406003 | 330.000000 |
| cartpole_swingup_sparse | markov | - | smfa | 406004 | 586.000000 |
| cartpole_swingup_sparse | markov | - | smfa | 406005 | 211.000000 |
| cartpole_swingup_sparse | markov | - | smfa | 406006 | 505.000000 |
| cartpole_swingup_sparse | markov | - | smfa | 406007 | 504.000000 |
| cartpole_swingup_sparse | markov | - | smfa | 406008 | 354.000000 |
| cartpole_swingup_sparse | markov | - | smfa | 406009 | 340.000000 |
| cartpole_swingup_sparse | single | rain | smfa | 406000 | 818.000000 |
| cartpole_swingup_sparse | single | rain | smfa | 406001 | 835.000000 |
| cartpole_swingup_sparse | single | rain | smfa | 406002 | 796.000000 |
| cartpole_swingup_sparse | single | rain | smfa | 406003 | 822.000000 |
| cartpole_swingup_sparse | single | rain | smfa | 406004 | 827.000000 |
| cartpole_swingup_sparse | single | fog | smfa | 406000 | 825.000000 |
| cartpole_swingup_sparse | single | fog | smfa | 406001 | 836.000000 |
| cartpole_swingup_sparse | single | fog | smfa | 406002 | 838.000000 |
| cartpole_swingup_sparse | single | fog | smfa | 406003 | 837.000000 |
| cartpole_swingup_sparse | single | fog | smfa | 406004 | 835.000000 |
| cartpole_swingup_sparse | single | snow | smfa | 406000 | 819.000000 |
| cartpole_swingup_sparse | single | snow | smfa | 406001 | 818.000000 |
| cartpole_swingup_sparse | single | snow | smfa | 406002 | 807.000000 |
| cartpole_swingup_sparse | single | snow | smfa | 406003 | 829.000000 |
| cartpole_swingup_sparse | single | snow | smfa | 406004 | 833.000000 |
| cartpole_swingup_sparse | single | motion_blur | smfa | 406000 | 0.000000 |
| cartpole_swingup_sparse | single | motion_blur | smfa | 406001 | 0.000000 |
| cartpole_swingup_sparse | single | motion_blur | smfa | 406002 | 22.000000 |
| cartpole_swingup_sparse | single | motion_blur | smfa | 406003 | 0.000000 |
| cartpole_swingup_sparse | single | motion_blur | smfa | 406004 | 0.000000 |
| cartpole_swingup_sparse | single | gaussian_noise | smfa | 406000 | 836.000000 |
| cartpole_swingup_sparse | single | gaussian_noise | smfa | 406001 | 834.000000 |
| cartpole_swingup_sparse | single | gaussian_noise | smfa | 406002 | 795.000000 |
| cartpole_swingup_sparse | single | gaussian_noise | smfa | 406003 | 815.000000 |
| cartpole_swingup_sparse | single | gaussian_noise | smfa | 406004 | 835.000000 |
| cartpole_swingup_sparse | single | low_light | smfa | 406000 | 774.000000 |
| cartpole_swingup_sparse | single | low_light | smfa | 406001 | 825.000000 |
| cartpole_swingup_sparse | single | low_light | smfa | 406002 | 722.000000 |
| cartpole_swingup_sparse | single | low_light | smfa | 406003 | 835.000000 |
| cartpole_swingup_sparse | single | low_light | smfa | 406004 | 831.000000 |
| cartpole_swingup_sparse | single | jpeg | smfa | 406000 | 98.000000 |
| cartpole_swingup_sparse | single | jpeg | smfa | 406001 | 177.000000 |
| cartpole_swingup_sparse | single | jpeg | smfa | 406002 | 206.000000 |
| cartpole_swingup_sparse | single | jpeg | smfa | 406003 | 232.000000 |
| cartpole_swingup_sparse | single | jpeg | smfa | 406004 | 160.000000 |
| cartpole_swingup_sparse | single | defocus_blur | smfa | 406000 | 4.000000 |
| cartpole_swingup_sparse | single | defocus_blur | smfa | 406001 | 5.000000 |
| cartpole_swingup_sparse | single | defocus_blur | smfa | 406002 | 4.000000 |
| cartpole_swingup_sparse | single | defocus_blur | smfa | 406003 | 6.000000 |
| cartpole_swingup_sparse | single | defocus_blur | smfa | 406004 | 5.000000 |
| cartpole_swingup_sparse | single | frost | smfa | 406000 | 836.000000 |
| cartpole_swingup_sparse | single | frost | smfa | 406001 | 831.000000 |
| cartpole_swingup_sparse | single | frost | smfa | 406002 | 836.000000 |
| cartpole_swingup_sparse | single | frost | smfa | 406003 | 835.000000 |
| cartpole_swingup_sparse | single | frost | smfa | 406004 | 833.000000 |
| cartpole_swingup_sparse | single | occlusion_patch | smfa | 406000 | 833.000000 |
| cartpole_swingup_sparse | single | occlusion_patch | smfa | 406001 | 29.000000 |
| cartpole_swingup_sparse | single | occlusion_patch | smfa | 406002 | 157.000000 |
| cartpole_swingup_sparse | single | occlusion_patch | smfa | 406003 | 195.000000 |
| cartpole_swingup_sparse | single | occlusion_patch | smfa | 406004 | 732.000000 |
| cartpole_swingup_sparse | single | saturation | smfa | 406000 | 833.000000 |
| cartpole_swingup_sparse | single | saturation | smfa | 406001 | 801.000000 |
| cartpole_swingup_sparse | single | saturation | smfa | 406002 | 822.000000 |
| cartpole_swingup_sparse | single | saturation | smfa | 406003 | 826.000000 |
| cartpole_swingup_sparse | single | saturation | smfa | 406004 | 836.000000 |
| cartpole_swingup_sparse | single | shadow | smfa | 406000 | 323.000000 |
| cartpole_swingup_sparse | single | shadow | smfa | 406001 | 401.000000 |
| cartpole_swingup_sparse | single | shadow | smfa | 406002 | 378.000000 |
| cartpole_swingup_sparse | single | shadow | smfa | 406003 | 320.000000 |
| cartpole_swingup_sparse | single | shadow | smfa | 406004 | 792.000000 |
| cartpole_swingup_sparse | single | shot_noise | smfa | 406000 | 835.000000 |
| cartpole_swingup_sparse | single | shot_noise | smfa | 406001 | 828.000000 |
| cartpole_swingup_sparse | single | shot_noise | smfa | 406002 | 494.000000 |
| cartpole_swingup_sparse | single | shot_noise | smfa | 406003 | 837.000000 |
| cartpole_swingup_sparse | single | shot_noise | smfa | 406004 | 823.000000 |
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
| cup_catch | markov | - | aco | 407000 | 775.000000 |
| cup_catch | markov | - | aco | 407001 | 0.000000 |
| cup_catch | markov | - | aco | 407002 | 986.000000 |
| cup_catch | markov | - | aco | 407003 | 360.000000 |
| cup_catch | markov | - | aco | 407004 | 348.000000 |
| cup_catch | markov | - | aco | 407005 | 740.000000 |
| cup_catch | markov | - | aco | 407006 | 773.000000 |
| cup_catch | markov | - | aco | 407007 | 971.000000 |
| cup_catch | markov | - | aco | 407008 | 972.000000 |
| cup_catch | markov | - | aco | 407009 | 971.000000 |
| cup_catch | single | rain | aco | 407000 | 972.000000 |
| cup_catch | single | rain | aco | 407001 | 962.000000 |
| cup_catch | single | rain | aco | 407002 | 991.000000 |
| cup_catch | single | rain | aco | 407003 | 987.000000 |
| cup_catch | single | rain | aco | 407004 | 973.000000 |
| cup_catch | single | fog | aco | 407000 | 0.000000 |
| cup_catch | single | fog | aco | 407001 | 0.000000 |
| cup_catch | single | fog | aco | 407002 | 11.000000 |
| cup_catch | single | fog | aco | 407003 | 12.000000 |
| cup_catch | single | fog | aco | 407004 | 0.000000 |
| cup_catch | single | snow | aco | 407000 | 954.000000 |
| cup_catch | single | snow | aco | 407001 | 957.000000 |
| cup_catch | single | snow | aco | 407002 | 990.000000 |
| cup_catch | single | snow | aco | 407003 | 983.000000 |
| cup_catch | single | snow | aco | 407004 | 973.000000 |
| cup_catch | single | motion_blur | aco | 407000 | 971.000000 |
| cup_catch | single | motion_blur | aco | 407001 | 964.000000 |
| cup_catch | single | motion_blur | aco | 407002 | 989.000000 |
| cup_catch | single | motion_blur | aco | 407003 | 990.000000 |
| cup_catch | single | motion_blur | aco | 407004 | 970.000000 |
| cup_catch | single | gaussian_noise | aco | 407000 | 0.000000 |
| cup_catch | single | gaussian_noise | aco | 407001 | 0.000000 |
| cup_catch | single | gaussian_noise | aco | 407002 | 9.000000 |
| cup_catch | single | gaussian_noise | aco | 407003 | 6.000000 |
| cup_catch | single | gaussian_noise | aco | 407004 | 0.000000 |
| cup_catch | single | low_light | aco | 407000 | 972.000000 |
| cup_catch | single | low_light | aco | 407001 | 963.000000 |
| cup_catch | single | low_light | aco | 407002 | 272.000000 |
| cup_catch | single | low_light | aco | 407003 | 738.000000 |
| cup_catch | single | low_light | aco | 407004 | 474.000000 |
| cup_catch | single | jpeg | aco | 407000 | 0.000000 |
| cup_catch | single | jpeg | aco | 407001 | 965.000000 |
| cup_catch | single | jpeg | aco | 407002 | 7.000000 |
| cup_catch | single | jpeg | aco | 407003 | 25.000000 |
| cup_catch | single | jpeg | aco | 407004 | 0.000000 |
| cup_catch | single | defocus_blur | aco | 407000 | 971.000000 |
| cup_catch | single | defocus_blur | aco | 407001 | 962.000000 |
| cup_catch | single | defocus_blur | aco | 407002 | 991.000000 |
| cup_catch | single | defocus_blur | aco | 407003 | 988.000000 |
| cup_catch | single | defocus_blur | aco | 407004 | 972.000000 |
| cup_catch | single | frost | aco | 407000 | 0.000000 |
| cup_catch | single | frost | aco | 407001 | 908.000000 |
| cup_catch | single | frost | aco | 407002 | 409.000000 |
| cup_catch | single | frost | aco | 407003 | 29.000000 |
| cup_catch | single | frost | aco | 407004 | 0.000000 |
| cup_catch | single | occlusion_patch | aco | 407000 | 972.000000 |
| cup_catch | single | occlusion_patch | aco | 407001 | 964.000000 |
| cup_catch | single | occlusion_patch | aco | 407002 | 991.000000 |
| cup_catch | single | occlusion_patch | aco | 407003 | 986.000000 |
| cup_catch | single | occlusion_patch | aco | 407004 | 972.000000 |
| cup_catch | single | saturation | aco | 407000 | 963.000000 |
| cup_catch | single | saturation | aco | 407001 | 964.000000 |
| cup_catch | single | saturation | aco | 407002 | 991.000000 |
| cup_catch | single | saturation | aco | 407003 | 987.000000 |
| cup_catch | single | saturation | aco | 407004 | 972.000000 |
| cup_catch | single | shadow | aco | 407000 | 972.000000 |
| cup_catch | single | shadow | aco | 407001 | 964.000000 |
| cup_catch | single | shadow | aco | 407002 | 989.000000 |
| cup_catch | single | shadow | aco | 407003 | 984.000000 |
| cup_catch | single | shadow | aco | 407004 | 972.000000 |
| cup_catch | single | shot_noise | aco | 407000 | 0.000000 |
| cup_catch | single | shot_noise | aco | 407001 | 0.000000 |
| cup_catch | single | shot_noise | aco | 407002 | 11.000000 |
| cup_catch | single | shot_noise | aco | 407003 | 9.000000 |
| cup_catch | single | shot_noise | aco | 407004 | 0.000000 |
| cup_catch | markov | - | smfa | 407000 | 954.000000 |
| cup_catch | markov | - | smfa | 407001 | 964.000000 |
| cup_catch | markov | - | smfa | 407002 | 921.000000 |
| cup_catch | markov | - | smfa | 407003 | 988.000000 |
| cup_catch | markov | - | smfa | 407004 | 973.000000 |
| cup_catch | markov | - | smfa | 407005 | 967.000000 |
| cup_catch | markov | - | smfa | 407006 | 886.000000 |
| cup_catch | markov | - | smfa | 407007 | 969.000000 |
| cup_catch | markov | - | smfa | 407008 | 973.000000 |
| cup_catch | markov | - | smfa | 407009 | 971.000000 |
| cup_catch | single | rain | smfa | 407000 | 972.000000 |
| cup_catch | single | rain | smfa | 407001 | 964.000000 |
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
| cup_catch | single | snow | smfa | 407003 | 989.000000 |
| cup_catch | single | snow | smfa | 407004 | 973.000000 |
| cup_catch | single | motion_blur | smfa | 407000 | 0.000000 |
| cup_catch | single | motion_blur | smfa | 407001 | 928.000000 |
| cup_catch | single | motion_blur | smfa | 407002 | 987.000000 |
| cup_catch | single | motion_blur | smfa | 407003 | 982.000000 |
| cup_catch | single | motion_blur | smfa | 407004 | 968.000000 |
| cup_catch | single | gaussian_noise | smfa | 407000 | 972.000000 |
| cup_catch | single | gaussian_noise | smfa | 407001 | 964.000000 |
| cup_catch | single | gaussian_noise | smfa | 407002 | 991.000000 |
| cup_catch | single | gaussian_noise | smfa | 407003 | 989.000000 |
| cup_catch | single | gaussian_noise | smfa | 407004 | 972.000000 |
| cup_catch | single | low_light | smfa | 407000 | 972.000000 |
| cup_catch | single | low_light | smfa | 407001 | 964.000000 |
| cup_catch | single | low_light | smfa | 407002 | 990.000000 |
| cup_catch | single | low_light | smfa | 407003 | 989.000000 |
| cup_catch | single | low_light | smfa | 407004 | 971.000000 |
| cup_catch | single | jpeg | smfa | 407000 | 961.000000 |
| cup_catch | single | jpeg | smfa | 407001 | 963.000000 |
| cup_catch | single | jpeg | smfa | 407002 | 991.000000 |
| cup_catch | single | jpeg | smfa | 407003 | 985.000000 |
| cup_catch | single | jpeg | smfa | 407004 | 971.000000 |
| cup_catch | single | defocus_blur | smfa | 407000 | 0.000000 |
| cup_catch | single | defocus_blur | smfa | 407001 | 0.000000 |
| cup_catch | single | defocus_blur | smfa | 407002 | 0.000000 |
| cup_catch | single | defocus_blur | smfa | 407003 | 0.000000 |
| cup_catch | single | defocus_blur | smfa | 407004 | 0.000000 |
| cup_catch | single | frost | smfa | 407000 | 972.000000 |
| cup_catch | single | frost | smfa | 407001 | 964.000000 |
| cup_catch | single | frost | smfa | 407002 | 990.000000 |
| cup_catch | single | frost | smfa | 407003 | 989.000000 |
| cup_catch | single | frost | smfa | 407004 | 972.000000 |
| cup_catch | single | occlusion_patch | smfa | 407000 | 972.000000 |
| cup_catch | single | occlusion_patch | smfa | 407001 | 964.000000 |
| cup_catch | single | occlusion_patch | smfa | 407002 | 989.000000 |
| cup_catch | single | occlusion_patch | smfa | 407003 | 987.000000 |
| cup_catch | single | occlusion_patch | smfa | 407004 | 972.000000 |
| cup_catch | single | saturation | smfa | 407000 | 971.000000 |
| cup_catch | single | saturation | smfa | 407001 | 964.000000 |
| cup_catch | single | saturation | smfa | 407002 | 991.000000 |
| cup_catch | single | saturation | smfa | 407003 | 989.000000 |
| cup_catch | single | saturation | smfa | 407004 | 972.000000 |
| cup_catch | single | shadow | smfa | 407000 | 972.000000 |
| cup_catch | single | shadow | smfa | 407001 | 964.000000 |
| cup_catch | single | shadow | smfa | 407002 | 990.000000 |
| cup_catch | single | shadow | smfa | 407003 | 989.000000 |
| cup_catch | single | shadow | smfa | 407004 | 972.000000 |
| cup_catch | single | shot_noise | smfa | 407000 | 972.000000 |
| cup_catch | single | shot_noise | smfa | 407001 | 963.000000 |
| cup_catch | single | shot_noise | smfa | 407002 | 991.000000 |
| cup_catch | single | shot_noise | smfa | 407003 | 988.000000 |
| cup_catch | single | shot_noise | smfa | 407004 | 973.000000 |
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
| reacher_easy | markov | - | aco | 408000 | 634.000000 |
| reacher_easy | markov | - | aco | 408001 | 980.000000 |
| reacher_easy | markov | - | aco | 408002 | 924.000000 |
| reacher_easy | markov | - | aco | 408003 | 766.000000 |
| reacher_easy | markov | - | aco | 408004 | 984.000000 |
| reacher_easy | markov | - | aco | 408005 | 908.000000 |
| reacher_easy | markov | - | aco | 408006 | 930.000000 |
| reacher_easy | markov | - | aco | 408007 | 859.000000 |
| reacher_easy | markov | - | aco | 408008 | 852.000000 |
| reacher_easy | markov | - | aco | 408009 | 952.000000 |
| reacher_easy | single | rain | aco | 408000 | 963.000000 |
| reacher_easy | single | rain | aco | 408001 | 980.000000 |
| reacher_easy | single | rain | aco | 408002 | 976.000000 |
| reacher_easy | single | rain | aco | 408003 | 1000.000000 |
| reacher_easy | single | rain | aco | 408004 | 993.000000 |
| reacher_easy | single | fog | aco | 408000 | 827.000000 |
| reacher_easy | single | fog | aco | 408001 | 959.000000 |
| reacher_easy | single | fog | aco | 408002 | 970.000000 |
| reacher_easy | single | fog | aco | 408003 | 993.000000 |
| reacher_easy | single | fog | aco | 408004 | 993.000000 |
| reacher_easy | single | snow | aco | 408000 | 961.000000 |
| reacher_easy | single | snow | aco | 408001 | 980.000000 |
| reacher_easy | single | snow | aco | 408002 | 976.000000 |
| reacher_easy | single | snow | aco | 408003 | 1000.000000 |
| reacher_easy | single | snow | aco | 408004 | 993.000000 |
| reacher_easy | single | motion_blur | aco | 408000 | 934.000000 |
| reacher_easy | single | motion_blur | aco | 408001 | 980.000000 |
| reacher_easy | single | motion_blur | aco | 408002 | 973.000000 |
| reacher_easy | single | motion_blur | aco | 408003 | 1000.000000 |
| reacher_easy | single | motion_blur | aco | 408004 | 991.000000 |
| reacher_easy | single | gaussian_noise | aco | 408000 | 239.000000 |
| reacher_easy | single | gaussian_noise | aco | 408001 | 13.000000 |
| reacher_easy | single | gaussian_noise | aco | 408002 | 4.000000 |
| reacher_easy | single | gaussian_noise | aco | 408003 | 86.000000 |
| reacher_easy | single | gaussian_noise | aco | 408004 | 103.000000 |
| reacher_easy | single | low_light | aco | 408000 | 809.000000 |
| reacher_easy | single | low_light | aco | 408001 | 326.000000 |
| reacher_easy | single | low_light | aco | 408002 | 969.000000 |
| reacher_easy | single | low_light | aco | 408003 | 1000.000000 |
| reacher_easy | single | low_light | aco | 408004 | 42.000000 |
| reacher_easy | single | jpeg | aco | 408000 | 48.000000 |
| reacher_easy | single | jpeg | aco | 408001 | 924.000000 |
| reacher_easy | single | jpeg | aco | 408002 | 883.000000 |
| reacher_easy | single | jpeg | aco | 408003 | 244.000000 |
| reacher_easy | single | jpeg | aco | 408004 | 113.000000 |
| reacher_easy | single | defocus_blur | aco | 408000 | 937.000000 |
| reacher_easy | single | defocus_blur | aco | 408001 | 980.000000 |
| reacher_easy | single | defocus_blur | aco | 408002 | 976.000000 |
| reacher_easy | single | defocus_blur | aco | 408003 | 1000.000000 |
| reacher_easy | single | defocus_blur | aco | 408004 | 993.000000 |
| reacher_easy | single | frost | aco | 408000 | 962.000000 |
| reacher_easy | single | frost | aco | 408001 | 980.000000 |
| reacher_easy | single | frost | aco | 408002 | 976.000000 |
| reacher_easy | single | frost | aco | 408003 | 1000.000000 |
| reacher_easy | single | frost | aco | 408004 | 993.000000 |
| reacher_easy | single | occlusion_patch | aco | 408000 | 0.000000 |
| reacher_easy | single | occlusion_patch | aco | 408001 | 105.000000 |
| reacher_easy | single | occlusion_patch | aco | 408002 | 972.000000 |
| reacher_easy | single | occlusion_patch | aco | 408003 | 8.000000 |
| reacher_easy | single | occlusion_patch | aco | 408004 | 16.000000 |
| reacher_easy | single | saturation | aco | 408000 | 0.000000 |
| reacher_easy | single | saturation | aco | 408001 | 981.000000 |
| reacher_easy | single | saturation | aco | 408002 | 972.000000 |
| reacher_easy | single | saturation | aco | 408003 | 13.000000 |
| reacher_easy | single | saturation | aco | 408004 | 993.000000 |
| reacher_easy | single | shadow | aco | 408000 | 961.000000 |
| reacher_easy | single | shadow | aco | 408001 | 979.000000 |
| reacher_easy | single | shadow | aco | 408002 | 972.000000 |
| reacher_easy | single | shadow | aco | 408003 | 1000.000000 |
| reacher_easy | single | shadow | aco | 408004 | 993.000000 |
| reacher_easy | single | shot_noise | aco | 408000 | 221.000000 |
| reacher_easy | single | shot_noise | aco | 408001 | 20.000000 |
| reacher_easy | single | shot_noise | aco | 408002 | 0.000000 |
| reacher_easy | single | shot_noise | aco | 408003 | 97.000000 |
| reacher_easy | single | shot_noise | aco | 408004 | 191.000000 |
| reacher_easy | markov | - | smfa | 408000 | 960.000000 |
| reacher_easy | markov | - | smfa | 408001 | 981.000000 |
| reacher_easy | markov | - | smfa | 408002 | 976.000000 |
| reacher_easy | markov | - | smfa | 408003 | 1000.000000 |
| reacher_easy | markov | - | smfa | 408004 | 993.000000 |
| reacher_easy | markov | - | smfa | 408005 | 944.000000 |
| reacher_easy | markov | - | smfa | 408006 | 966.000000 |
| reacher_easy | markov | - | smfa | 408007 | 971.000000 |
| reacher_easy | markov | - | smfa | 408008 | 967.000000 |
| reacher_easy | markov | - | smfa | 408009 | 965.000000 |
| reacher_easy | single | rain | smfa | 408000 | 961.000000 |
| reacher_easy | single | rain | smfa | 408001 | 980.000000 |
| reacher_easy | single | rain | smfa | 408002 | 976.000000 |
| reacher_easy | single | rain | smfa | 408003 | 1000.000000 |
| reacher_easy | single | rain | smfa | 408004 | 993.000000 |
| reacher_easy | single | fog | smfa | 408000 | 962.000000 |
| reacher_easy | single | fog | smfa | 408001 | 981.000000 |
| reacher_easy | single | fog | smfa | 408002 | 976.000000 |
| reacher_easy | single | fog | smfa | 408003 | 1000.000000 |
| reacher_easy | single | fog | smfa | 408004 | 993.000000 |
| reacher_easy | single | snow | smfa | 408000 | 963.000000 |
| reacher_easy | single | snow | smfa | 408001 | 981.000000 |
| reacher_easy | single | snow | smfa | 408002 | 976.000000 |
| reacher_easy | single | snow | smfa | 408003 | 1000.000000 |
| reacher_easy | single | snow | smfa | 408004 | 993.000000 |
| reacher_easy | single | motion_blur | smfa | 408000 | 0.000000 |
| reacher_easy | single | motion_blur | smfa | 408001 | 979.000000 |
| reacher_easy | single | motion_blur | smfa | 408002 | 972.000000 |
| reacher_easy | single | motion_blur | smfa | 408003 | 948.000000 |
| reacher_easy | single | motion_blur | smfa | 408004 | 986.000000 |
| reacher_easy | single | gaussian_noise | smfa | 408000 | 961.000000 |
| reacher_easy | single | gaussian_noise | smfa | 408001 | 981.000000 |
| reacher_easy | single | gaussian_noise | smfa | 408002 | 976.000000 |
| reacher_easy | single | gaussian_noise | smfa | 408003 | 1000.000000 |
| reacher_easy | single | gaussian_noise | smfa | 408004 | 993.000000 |
| reacher_easy | single | low_light | smfa | 408000 | 963.000000 |
| reacher_easy | single | low_light | smfa | 408001 | 981.000000 |
| reacher_easy | single | low_light | smfa | 408002 | 976.000000 |
| reacher_easy | single | low_light | smfa | 408003 | 1000.000000 |
| reacher_easy | single | low_light | smfa | 408004 | 993.000000 |
| reacher_easy | single | jpeg | smfa | 408000 | 960.000000 |
| reacher_easy | single | jpeg | smfa | 408001 | 981.000000 |
| reacher_easy | single | jpeg | smfa | 408002 | 976.000000 |
| reacher_easy | single | jpeg | smfa | 408003 | 1000.000000 |
| reacher_easy | single | jpeg | smfa | 408004 | 993.000000 |
| reacher_easy | single | defocus_blur | smfa | 408000 | 0.000000 |
| reacher_easy | single | defocus_blur | smfa | 408001 | 979.000000 |
| reacher_easy | single | defocus_blur | smfa | 408002 | 973.000000 |
| reacher_easy | single | defocus_blur | smfa | 408003 | 1000.000000 |
| reacher_easy | single | defocus_blur | smfa | 408004 | 993.000000 |
| reacher_easy | single | frost | smfa | 408000 | 964.000000 |
| reacher_easy | single | frost | smfa | 408001 | 981.000000 |
| reacher_easy | single | frost | smfa | 408002 | 975.000000 |
| reacher_easy | single | frost | smfa | 408003 | 1000.000000 |
| reacher_easy | single | frost | smfa | 408004 | 993.000000 |
| reacher_easy | single | occlusion_patch | smfa | 408000 | 0.000000 |
| reacher_easy | single | occlusion_patch | smfa | 408001 | 211.000000 |
| reacher_easy | single | occlusion_patch | smfa | 408002 | 975.000000 |
| reacher_easy | single | occlusion_patch | smfa | 408003 | 54.000000 |
| reacher_easy | single | occlusion_patch | smfa | 408004 | 14.000000 |
| reacher_easy | single | saturation | smfa | 408000 | 960.000000 |
| reacher_easy | single | saturation | smfa | 408001 | 981.000000 |
| reacher_easy | single | saturation | smfa | 408002 | 975.000000 |
| reacher_easy | single | saturation | smfa | 408003 | 1000.000000 |
| reacher_easy | single | saturation | smfa | 408004 | 993.000000 |
| reacher_easy | single | shadow | smfa | 408000 | 958.000000 |
| reacher_easy | single | shadow | smfa | 408001 | 981.000000 |
| reacher_easy | single | shadow | smfa | 408002 | 976.000000 |
| reacher_easy | single | shadow | smfa | 408003 | 1000.000000 |
| reacher_easy | single | shadow | smfa | 408004 | 993.000000 |
| reacher_easy | single | shot_noise | smfa | 408000 | 961.000000 |
| reacher_easy | single | shot_noise | smfa | 408001 | 980.000000 |
| reacher_easy | single | shot_noise | smfa | 408002 | 975.000000 |
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
| reacher_hard | markov | - | aco | 409000 | 9.000000 |
| reacher_hard | markov | - | aco | 409001 | 0.000000 |
| reacher_hard | markov | - | aco | 409002 | 9.000000 |
| reacher_hard | markov | - | aco | 409003 | 0.000000 |
| reacher_hard | markov | - | aco | 409004 | 10.000000 |
| reacher_hard | markov | - | aco | 409005 | 3.000000 |
| reacher_hard | markov | - | aco | 409006 | 4.000000 |
| reacher_hard | markov | - | aco | 409007 | 0.000000 |
| reacher_hard | markov | - | aco | 409008 | 7.000000 |
| reacher_hard | markov | - | aco | 409009 | 175.000000 |
| reacher_hard | single | rain | aco | 409000 | 29.000000 |
| reacher_hard | single | rain | aco | 409001 | 0.000000 |
| reacher_hard | single | rain | aco | 409002 | 5.000000 |
| reacher_hard | single | rain | aco | 409003 | 0.000000 |
| reacher_hard | single | rain | aco | 409004 | 0.000000 |
| reacher_hard | single | fog | aco | 409000 | 0.000000 |
| reacher_hard | single | fog | aco | 409001 | 0.000000 |
| reacher_hard | single | fog | aco | 409002 | 0.000000 |
| reacher_hard | single | fog | aco | 409003 | 8.000000 |
| reacher_hard | single | fog | aco | 409004 | 0.000000 |
| reacher_hard | single | snow | aco | 409000 | 37.000000 |
| reacher_hard | single | snow | aco | 409001 | 0.000000 |
| reacher_hard | single | snow | aco | 409002 | 4.000000 |
| reacher_hard | single | snow | aco | 409003 | 0.000000 |
| reacher_hard | single | snow | aco | 409004 | 1.000000 |
| reacher_hard | single | motion_blur | aco | 409000 | 10.000000 |
| reacher_hard | single | motion_blur | aco | 409001 | 0.000000 |
| reacher_hard | single | motion_blur | aco | 409002 | 2.000000 |
| reacher_hard | single | motion_blur | aco | 409003 | 0.000000 |
| reacher_hard | single | motion_blur | aco | 409004 | 27.000000 |
| reacher_hard | single | gaussian_noise | aco | 409000 | 0.000000 |
| reacher_hard | single | gaussian_noise | aco | 409001 | 0.000000 |
| reacher_hard | single | gaussian_noise | aco | 409002 | 0.000000 |
| reacher_hard | single | gaussian_noise | aco | 409003 | 32.000000 |
| reacher_hard | single | gaussian_noise | aco | 409004 | 0.000000 |
| reacher_hard | single | low_light | aco | 409000 | 3.000000 |
| reacher_hard | single | low_light | aco | 409001 | 0.000000 |
| reacher_hard | single | low_light | aco | 409002 | 38.000000 |
| reacher_hard | single | low_light | aco | 409003 | 7.000000 |
| reacher_hard | single | low_light | aco | 409004 | 2.000000 |
| reacher_hard | single | jpeg | aco | 409000 | 0.000000 |
| reacher_hard | single | jpeg | aco | 409001 | 0.000000 |
| reacher_hard | single | jpeg | aco | 409002 | 5.000000 |
| reacher_hard | single | jpeg | aco | 409003 | 0.000000 |
| reacher_hard | single | jpeg | aco | 409004 | 0.000000 |
| reacher_hard | single | defocus_blur | aco | 409000 | 2.000000 |
| reacher_hard | single | defocus_blur | aco | 409001 | 0.000000 |
| reacher_hard | single | defocus_blur | aco | 409002 | 5.000000 |
| reacher_hard | single | defocus_blur | aco | 409003 | 0.000000 |
| reacher_hard | single | defocus_blur | aco | 409004 | 15.000000 |
| reacher_hard | single | frost | aco | 409000 | 22.000000 |
| reacher_hard | single | frost | aco | 409001 | 0.000000 |
| reacher_hard | single | frost | aco | 409002 | 5.000000 |
| reacher_hard | single | frost | aco | 409003 | 0.000000 |
| reacher_hard | single | frost | aco | 409004 | 4.000000 |
| reacher_hard | single | occlusion_patch | aco | 409000 | 14.000000 |
| reacher_hard | single | occlusion_patch | aco | 409001 | 0.000000 |
| reacher_hard | single | occlusion_patch | aco | 409002 | 2.000000 |
| reacher_hard | single | occlusion_patch | aco | 409003 | 50.000000 |
| reacher_hard | single | occlusion_patch | aco | 409004 | 0.000000 |
| reacher_hard | single | saturation | aco | 409000 | 34.000000 |
| reacher_hard | single | saturation | aco | 409001 | 0.000000 |
| reacher_hard | single | saturation | aco | 409002 | 0.000000 |
| reacher_hard | single | saturation | aco | 409003 | 0.000000 |
| reacher_hard | single | saturation | aco | 409004 | 7.000000 |
| reacher_hard | single | shadow | aco | 409000 | 11.000000 |
| reacher_hard | single | shadow | aco | 409001 | 0.000000 |
| reacher_hard | single | shadow | aco | 409002 | 49.000000 |
| reacher_hard | single | shadow | aco | 409003 | 0.000000 |
| reacher_hard | single | shadow | aco | 409004 | 12.000000 |
| reacher_hard | single | shot_noise | aco | 409000 | 0.000000 |
| reacher_hard | single | shot_noise | aco | 409001 | 23.000000 |
| reacher_hard | single | shot_noise | aco | 409002 | 11.000000 |
| reacher_hard | single | shot_noise | aco | 409003 | 5.000000 |
| reacher_hard | single | shot_noise | aco | 409004 | 0.000000 |
| reacher_hard | markov | - | smfa | 409000 | 33.000000 |
| reacher_hard | markov | - | smfa | 409001 | 0.000000 |
| reacher_hard | markov | - | smfa | 409002 | 4.000000 |
| reacher_hard | markov | - | smfa | 409003 | 0.000000 |
| reacher_hard | markov | - | smfa | 409004 | 0.000000 |
| reacher_hard | markov | - | smfa | 409005 | 6.000000 |
| reacher_hard | markov | - | smfa | 409006 | 18.000000 |
| reacher_hard | markov | - | smfa | 409007 | 2.000000 |
| reacher_hard | markov | - | smfa | 409008 | 0.000000 |
| reacher_hard | markov | - | smfa | 409009 | 0.000000 |
| reacher_hard | single | rain | smfa | 409000 | 44.000000 |
| reacher_hard | single | rain | smfa | 409001 | 0.000000 |
| reacher_hard | single | rain | smfa | 409002 | 0.000000 |
| reacher_hard | single | rain | smfa | 409003 | 0.000000 |
| reacher_hard | single | rain | smfa | 409004 | 0.000000 |
| reacher_hard | single | fog | smfa | 409000 | 40.000000 |
| reacher_hard | single | fog | smfa | 409001 | 0.000000 |
| reacher_hard | single | fog | smfa | 409002 | 10.000000 |
| reacher_hard | single | fog | smfa | 409003 | 0.000000 |
| reacher_hard | single | fog | smfa | 409004 | 0.000000 |
| reacher_hard | single | snow | smfa | 409000 | 38.000000 |
| reacher_hard | single | snow | smfa | 409001 | 0.000000 |
| reacher_hard | single | snow | smfa | 409002 | 0.000000 |
| reacher_hard | single | snow | smfa | 409003 | 0.000000 |
| reacher_hard | single | snow | smfa | 409004 | 0.000000 |
| reacher_hard | single | motion_blur | smfa | 409000 | 5.000000 |
| reacher_hard | single | motion_blur | smfa | 409001 | 0.000000 |
| reacher_hard | single | motion_blur | smfa | 409002 | 0.000000 |
| reacher_hard | single | motion_blur | smfa | 409003 | 0.000000 |
| reacher_hard | single | motion_blur | smfa | 409004 | 0.000000 |
| reacher_hard | single | gaussian_noise | smfa | 409000 | 36.000000 |
| reacher_hard | single | gaussian_noise | smfa | 409001 | 0.000000 |
| reacher_hard | single | gaussian_noise | smfa | 409002 | 0.000000 |
| reacher_hard | single | gaussian_noise | smfa | 409003 | 0.000000 |
| reacher_hard | single | gaussian_noise | smfa | 409004 | 0.000000 |
| reacher_hard | single | low_light | smfa | 409000 | 42.000000 |
| reacher_hard | single | low_light | smfa | 409001 | 0.000000 |
| reacher_hard | single | low_light | smfa | 409002 | 0.000000 |
| reacher_hard | single | low_light | smfa | 409003 | 0.000000 |
| reacher_hard | single | low_light | smfa | 409004 | 5.000000 |
| reacher_hard | single | jpeg | smfa | 409000 | 21.000000 |
| reacher_hard | single | jpeg | smfa | 409001 | 0.000000 |
| reacher_hard | single | jpeg | smfa | 409002 | 0.000000 |
| reacher_hard | single | jpeg | smfa | 409003 | 0.000000 |
| reacher_hard | single | jpeg | smfa | 409004 | 5.000000 |
| reacher_hard | single | defocus_blur | smfa | 409000 | 5.000000 |
| reacher_hard | single | defocus_blur | smfa | 409001 | 0.000000 |
| reacher_hard | single | defocus_blur | smfa | 409002 | 0.000000 |
| reacher_hard | single | defocus_blur | smfa | 409003 | 0.000000 |
| reacher_hard | single | defocus_blur | smfa | 409004 | 0.000000 |
| reacher_hard | single | frost | smfa | 409000 | 43.000000 |
| reacher_hard | single | frost | smfa | 409001 | 0.000000 |
| reacher_hard | single | frost | smfa | 409002 | 0.000000 |
| reacher_hard | single | frost | smfa | 409003 | 0.000000 |
| reacher_hard | single | frost | smfa | 409004 | 4.000000 |
| reacher_hard | single | occlusion_patch | smfa | 409000 | 23.000000 |
| reacher_hard | single | occlusion_patch | smfa | 409001 | 0.000000 |
| reacher_hard | single | occlusion_patch | smfa | 409002 | 0.000000 |
| reacher_hard | single | occlusion_patch | smfa | 409003 | 0.000000 |
| reacher_hard | single | occlusion_patch | smfa | 409004 | 0.000000 |
| reacher_hard | single | saturation | smfa | 409000 | 49.000000 |
| reacher_hard | single | saturation | smfa | 409001 | 0.000000 |
| reacher_hard | single | saturation | smfa | 409002 | 0.000000 |
| reacher_hard | single | saturation | smfa | 409003 | 0.000000 |
| reacher_hard | single | saturation | smfa | 409004 | 4.000000 |
| reacher_hard | single | shadow | smfa | 409000 | 44.000000 |
| reacher_hard | single | shadow | smfa | 409001 | 0.000000 |
| reacher_hard | single | shadow | smfa | 409002 | 0.000000 |
| reacher_hard | single | shadow | smfa | 409003 | 0.000000 |
| reacher_hard | single | shadow | smfa | 409004 | 4.000000 |
| reacher_hard | single | shot_noise | smfa | 409000 | 40.000000 |
| reacher_hard | single | shot_noise | smfa | 409001 | 0.000000 |
| reacher_hard | single | shot_noise | smfa | 409002 | 1.000000 |
| reacher_hard | single | shot_noise | smfa | 409003 | 0.000000 |
| reacher_hard | single | shot_noise | smfa | 409004 | 4.000000 |
