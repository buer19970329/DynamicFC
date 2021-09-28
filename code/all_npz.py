# %%
import pandas as pd
import numpy as np
import os


def txt2npz(dir):
    files = os.listdir(os.path.join(dir))
    for i in files:
        if not i.startswith('.'):
            a = pd.DataFrame(np.loadtxt(os.path.join(dir,i)))
            np.savez(os.path.join(dir,i),a)

def allts(dir):
    all_ts = []
    files = os.listdir(os.path.join(dir))
    for ts in files:
        if ts.endswith(".txt.npz"):
            all_ts.append(np.load(os.path.join(dir,ts))['arr_0'])

    all_ts = np.stack(all_ts)
    np.savez_compressed(os.path.join(dir,'all_ts.npz'),all_ts=all_ts)
