# GUI Tool for Computing DynamicFC


A very simply function for computing dynamic functional connectivity (dfc), based on python.


-----

This repository contains:

# 1. GUI tool
```
For people who don't enjoy coding. ˃͜˂
```

**Step:**
1) [Python environment](https://www.python.org/)
2) install [PyQt5](https://pypi.org/project/PyQt5/) & [nilearn](https://nilearn.github.io/)
* you can just type the following command in your terminal or cmd
```
pip install PyQt5
pip install nilearn
```
* or, python our script [setup.py](Tool-for-Computing-DynamicFC/setup.py):
```
python setup.py
```
3) run GUI
```
python3.9 run_gui.py
```
4) GUI manual
* This tool is divided into three parts by two horizontal lines
```
Part 1: 

Usage:creating 3D matrix (nsubj, nvolm, nroi)
* input: 
        a. full path of a folder which contains timeseries (i.e., individual_ts.txt, nvolme * nroi) of all subjects (e.g., test_data)
* output: 
        a. 3D timeseries matrix
```
```
Part 2: 

Usage: computing timeseries along windows, given window type, window size, step size
* input: 
        a. ts:full path of all_ts.npz (i.e., ~/all_ts.npz);
        b. wtype: window type
        c. ws: window size (highly recommend: number of image volumes divides ws would be an integer)
        d. ss: step size
        e. output: full dir path
* output:
        a. 4D matrix (nsubj, nwindows, ws, nrois)
```
```
Part 3 (optional): 

Usage: computing dynamic functional connectivity between ROIs
* input:
        a. Connectivity Measures: correlation or covariance, based on nilearn.connectome.ConnectivityMeasure
        b. Vectorize: lower triangular of not?
* output: 
        a. 4D matrix (nsubj, nwindows, nrois, nrois) 
        b. or, 3D matrix (nsubj, nwindows, nrois * nrois), depending on Vectorize
```
**Note**: Try to compute [test_data](Tool-for-Computing-DynamicFC/test_data) before computing your real data

# 2. Python Function
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
* Python scripts : [dynamicFC.py](/helperfunctions/dynamicFC.py)
* Here is a rough pipeline showing how to execute it in Python Command: [python_pipeline.ipynb](/helperfunctions/python_pipeline.ipynb)


# 3. HelperFunctions
1) get time series: [get_ts.py](helperfunctions/get_ts.py)
2) p value corrected after computing dfc: [p_corr.py](helperfunctions/p_corr.py)
3) ~~convert .npz output to csv~~
* use python to check your dfc output (very easy & convenient, just type: `np.load('path_to_your_output/output.npz')`)

# Reference:
1. Zhuang, X., Yang, Z., Mishra, V., Sreenivasan, K., Bernick, C., & Cordes, D. (2020). Single-scale time-dependent window-sizes in sliding-window dynamic functional connectivity analysis: a validation study. Neuroimage, 220, 117111.
2. Mokhtari, F., Akhlaghi, M. I., Simpson, S. L., Wu, G., & Laurienti, P. J. (2019). Sliding window correlation analysis: Modulating window shape for dynamic brain connectivity in resting state. Neuroimage, 189, 655-666.

-------

**Do not hesitate to contact me if you have any further questions**

**Have fun :)**
