"""Frozen fallback protocol, not a claim of exact ACO F.7 reproduction.

Only defocus kernel implementation is reused from ACO. All base strengths and
remaining five operators are explicitly supplementary, as authorized by user.
One strength draw and spatial pattern per episode; shot noise changes per frame.
"""
import cv2
import numpy as np
from corruptions import get_degradation


class OOD:
    def __init__(self,kind,seed,c):
        self.kind,self.c=kind,c
        self.rng=np.random.RandomState(seed)
        self.u=self.rng.uniform(1-c['jitter'],1+c['jitter'])
        self.pattern=None
        self.defocus=get_degradation('defocus_blur',intensity=c['defocus_intensity']*self.u,seed=seed) if kind=='defocus_blur' else None

    def __call__(self,image):
        im=image.astype(np.float32); h,w=im.shape[:2]; c=self.c
        if self.defocus is not None: return self.defocus(image)
        if self.kind=='frost':
            if self.pattern is None:
                coarse=self.rng.rand(8,8).astype(np.float32)
                field=cv2.resize(coarse,(w,h),interpolation=cv2.INTER_CUBIC)
                streak=np.zeros((h,w),np.float32)
                for _ in range(45):
                    x,y=self.rng.randint(w),self.rng.randint(h)
                    cv2.line(streak,(x,y),(int(np.clip(x+self.rng.randint(-12,13),0,w-1)),int(np.clip(y+self.rng.randint(-12,13),0,h-1))),1.,1)
                self.pattern=np.clip(.5+.35*field+.3*cv2.GaussianBlur(streak,(3,3),.6),0,1)[...,None]
            alpha=c['frost_alpha']*self.u*self.pattern
            out=im*(1-alpha)+np.array([220,235,255],np.float32)*alpha
        elif self.kind=='occlusion_patch':
            if self.pattern is None:
                side=max(1,min(h,w,int(round(np.sqrt(c['occlusion_area']*self.u*h*w)))))
                self.pattern=(self.rng.randint(h-side+1),self.rng.randint(w-side+1),side)
            y,x,s=self.pattern; out=im.copy(); out[y:y+s,x:x+s]=0
        elif self.kind=='saturation':
            hsv=cv2.cvtColor(im/255.,cv2.COLOR_RGB2HSV)
            hsv[...,1]*=max(0,1-c['saturation_reduction']*self.u)
            out=cv2.cvtColor(hsv,cv2.COLOR_HSV2RGB)*255.
        elif self.kind=='shadow':
            if self.pattern is None:
                angle=self.rng.uniform(0,2*np.pi); offset=self.rng.uniform(-.1,.1)*min(h,w)
                y,x=np.mgrid[:h,:w]
                signed=(x-(w-1)/2)*np.cos(angle)+(y-(h-1)/2)*np.sin(angle)-offset
                self.pattern=(1/(1+np.exp(-signed/2.)))[...,None]
            out=im*(1-c['shadow_reduction']*self.u*self.pattern)
        elif self.kind=='shot_noise':
            levels=c['shot_levels']/self.u
            out=self.rng.poisson(im/255.*levels)/levels*255.
        else: raise ValueError(self.kind)
        return np.clip(np.rint(out),0,255).astype(np.uint8)
