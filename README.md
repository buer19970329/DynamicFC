# DynamicFC


A very simply function for computing dynamic functional connectivity (dfc), based on python.


-----

This repository contains:

# 1. Function
```
Docstring:
Computing Sliding-window time-series per subject per region 
i.e., Time_Series.shape = (n_subjects , n_volumes , n_ROIs)

Signature: 
sl(X, ws, ss=1, wt='rect')       # X = timeseries; ws = window size; ss = step size; wt = window type

Window tpyes(wt): 
    1) rect
    2) tukey; 
    3) hanning;
    4) hamming;
    5) gaussian (simga=2, parameter located at line 65 in <dynamicFC.py>);
```
* Python scripts : [dynamicFC.py](/dynamicFC.py)
* Here is a rough pipeline showing how to use it: [dfc_pipeline.ipynb](/dfc_pipeline.ipynb)


# 2. HelperFunctions
1) get time series: [get_ts.py](helpfunctions/get_ts.py)
2) p value corrected after computing dfc: [p_corred.py](helpfunctions/p_corred.py)
-------
**Do not hesitate contact me if you have any further questions**

**Have fun :)**
