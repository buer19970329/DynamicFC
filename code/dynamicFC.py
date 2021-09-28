# %%
import os
import nilearn.connectome
import numpy as np
import scipy
from scipy import signal
import warnings

# %%
def sl_1d(ts_1d,ws=24,ss=1):
    """
    creat n sliding window for EACH subj

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
    
    nw = np.int16(np.ceil((abs((len(ts_1d) - ws) // ss))))
    out = np.ndarray((nw,ws),dtype = ts_1d.dtype)
    for i in range(nw):
        start = i * ss
        stop = start + ws
        out[i] = ts_1d[start : stop]
    return out

# %%
def wtype(window,ws=24,wtype='rect'):
    """ computing time series with window function

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
    warnings.simplefilter(action='ignore', category=FutureWarning)
    if wtype == 'rect':
        wf_par = scipy.signal.windows.boxcar(ws, sym=True)
    if wtype == 'hanning':
        wf_par = scipy.signal.windows.hann(ws, sym=True)
    if wtype == 'hamming':
        wf_par = scipy.signal.windows.hamming(ws, sym=True)
    if wtype == 'gaussian':
        wf_par = scipy.signal.windows.gaussian(ws, std=2, sym=True)
    if wtype == 'tukey':
        wf_par = scipy.signal.windows.tukey(ws, alpha=0.5, sym=True)

    ##=============================================================================##
    ## First you must demean your data—otherwise, the window will shift energy from the mean into other frequencies. If you’re working in segments, you should demean (and detrend) each segment before you do anything further. (Savva et al., 2020)
    ## Removing the average value before tapering (to avoid spurious correlations at the beginning and end of the windows) (Savva et al., 2020)
    ##=============================================================================##
    window = window - np.mean(window)
    filtered_window = window * wf_par
    
    return filtered_window

# %%
def sl_run(ts_3d,ws,ss=1,wt='rect'):
    """Computing Sliding-window time-series per subject per region 
    i.e., Time_Series.shape = (n_subjects , n_volumes , n_ROIs)
        
    Parameters
    ----------
    ts_3d: 3D array-like time series (n_subjs, n_volumes, n_ROIs)
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
    # 提取subject, volume, roi numbers
    nsubj,nvolm,nroi =ts_3d.shape[0],ts_3d.shape[1],ts_3d.shape[2]
    nslw = np.int16(np.ceil(nvolm-ws)//ss)
    # creating a blank matrix
    all_slw_ts = np.ndarray((nsubj,nslw,ws,nroi))
    ############ loop along windows ############
    for i, s in enumerate(ts_3d):
        sim_ts = np.arange(nvolm,dtype='int32') # simulation to get the number of sl windows
        n_slw = sl_1d(sim_ts,ws,ss).shape[0]    # get the number of sliding windows
        all_slw_ts[i]=np.empty((n_slw,ws,nroi))   # creat matrix shape
        ############ loop along (slwin, ws, nroi) ############
        for n, curwin in enumerate(sl_1d(sim_ts,ws,ss)):
            cur_ts = s[curwin,:]    # get nsl_windows * (ws, roi)
            all_slw_ts[i][n]=np.ndarray((ws,nroi))    # get sliding ts for each subject
            # post-processing time series using window function
            for roi in range(nroi):
                all_slw_ts[i][n][:, roi] = wtype(cur_ts[:, roi], ws, wt)

    return all_slw_ts