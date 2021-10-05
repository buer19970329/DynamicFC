# %%
import numpy as np
import scipy.io as io
import os
import sys

def npz2mat(data='full_path'):
    """
    Usage
    ----------
    convert .npz data file to .mat data file

    Parameters
    ----------
    data: full path of data
    
    Example:
    ----------
    import npz2mat
    npz2mat('/Users/linxiaomin/Desktop/LINIP/Python/GUI/Tool-for-Computing-DynamicFC-main/test_data/dfc_dfc_output.npz')
    
    
    """
    # extract data path
    data_path = data.split('/')
    data_name = data_path[-1].split('.')[0] +'.mat'
    data_path.pop(-1)
    data_path = '/'.join(data_path)
    # convert npz to mat
    npz = np.load(data)
    io.savemat(os.path.join(data_path,data_name),{'data':npz})
    
if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2])
