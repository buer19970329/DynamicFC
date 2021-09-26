# %%
import os
import nilearn.connectome
import numpy as np
import scipy
from scipy import signal

# %%
def sl_1d(a,ws=24,ss=1):
    """creat n sliding window for EACH subj 
    
    Parameters
    ----------
    a:  1D array
    ws: window size
    ss: step size, unit = TR
    
    Returns
    ----------
    out : 2-D array (n_windows,ws)
          Vector with all sliding windows
    """ 
    valid = len(a) - ws
    
    nw = abs((valid) // ss)
    
    out = np.ndarray((nw,ws),dtype = a.dtype)
    
    for i in range(nw):
        # sliding window with $ws along the samples
        start = i * ss
        stop = start + ws
        out[i] = a[start : stop]
    
    return out

# %%
def wtype(window,ws=24,wtype='rect'):
    """ 处理每个窗的time series

    Q: which window type?
    A: Savva, A. D., Kassinopoulos, M., Smyrnis, N., Matsopoulos, G. K., & Mitsis, G. D. (2020). Effects of motion related outliers in dynamic functional connectivity using the sliding window method. Journal of neuroscience methods, 330, 108519.
    
    Parameters
    ----------
    window : 1d window
    ws: window size
    wtype: type of window ( default : rect )
    
    Returns
    -------
    out : 加窗后的时间序列
    
    """
    if wtype == 'tukey':
        wtype= scipy.signal.windows.tukey(ws,alpha=0.5,sym=True)
        
    if wtype == 'hanning':
        wtype= scipy.signal.windows.hann(ws, sym=True)
        
    if wtype == 'hamming':
        wtype= scipy.signal.windows.hamming(ws, sym=True)
        
    if wtype == 'gaussian':
        wtype= scipy.signal.windows.gaussian(ws, std=2, sym=True)
        
    if wtype == 'rect':
        wtype= scipy.signal.windows.boxcar(ws, sym=True)
##=============================================================================##
    ## First you must demean your data—otherwise, the window will shift energy from the mean into other frequencies. If you’re working in segments, you should demean (and detrend) each segment before you do anything further. (Savva et al., 2020)
    ## Removing the average value before tapering (to avoid spurious correlations at the beginning and end of the windows) (Savva et al., 2020)
##=============================================================================##
    window = window - np.mean(window)
    out=window*wtype
    
    return out


# %%
def sl(X,ws,ss=1,wt='rect'): 
    """Computing Sliding-window time-series per subject per region 
    i.e., Time_Series.shape = (n_subjects , n_volumes , n_ROIs)
        
    Parameters
    ----------
    X: 3D array-like time series (n_subjs, n_volumes, n_ROIs)
    ws : Window size 
    ss: window step size (default = 1 TR)
    wtpye: 
        1) rect
        2) tukey;
        3) hanning;
        4) hamming;
        5) gaussian (simga=2, parameter located at line 65 in <dynamicFC.py>);
    Returns
    -------
    slwin_ts : 4D Array-like (n_subjects,n_windows,ws,n_regions)
    """
    nsubj=X.shape[0] # number of subjects
    nvolm=X.shape[1] # number of volumes
    nfeat=X.shape[2] # number of brain regions   
    slwin_ts=np.ndarray((nsubj,np.int16(np.ceil((nvolm-ws)//ss)),ws,nfeat))
    for idx,s in enumerate(X):
        fulltimewin = np.arange(nvolm,dtype='int32')
        swins= sl_1d(a=fulltimewin,ws=ws,ss=ss)
        n_slwin = swins.shape[0] #number of sliding windows
        slwin_ts[idx]=np.empty((n_slwin,ws,nfeat)) #creat matrix shape
        for n, curwin in enumerate(swins):
            cur_ts = s[curwin,:]
            slwin_ts[idx][n]=np.ndarray((ws,nfeat))
            for i in range(nfeat):
                if wt == 'rect':
                    slwin_ts[idx][n][:,i]= wtype(cur_ts[:,i],ws,wtype='rect') 
                if wt == 'tukey':
                    slwin_ts[idx][n][:,i]= wtype(cur_ts[:,i],ws,wtype='tukey')
                if wt == 'hanning':
                    slwin_ts[idx][n][:,i]= wtype(cur_ts[:,i],ws,wtype='hanning')
                if wt == 'hamming':
                    slwin_ts[idx][n][:,i]= wtype(cur_ts[:,i],ws,wtype='hamming')
                if wt == 'gaussian':
                    slwin_ts[idx][n][:,i]= wtype(cur_ts[:,i],ws,wtype='gaussian')

    return slwin_ts,slwin_ts.shape[1]