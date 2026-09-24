import torch


def restoration_loss(pred,target,weight=.05):
    # FFT in float32 even under AMP; rfft2 defaults to norm='backward', like SMFANet.
    p,t=pred.float(),target.float()
    pixel=(p-t).abs().mean()
    pf,tf=torch.fft.rfft2(p),torch.fft.rfft2(t)
    fft=(torch.view_as_real(pf)-torch.view_as_real(tf)).abs().mean()
    return pixel+weight*fft,pixel,fft
