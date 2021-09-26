# -*- coding: utf-8 -*-

import os
import numpy as np
import nilearn.datasets as dataset
from nilearn.input_data import NiftiLabelsMasker, NiftiMapsMasker, NiftiSpheresMasker
from nilearn.datasets import load_mni152_template,load_mni152_brain_mask
brainmask = load_mni152_brain_mask()

def get_ts(data,atlas,t_r=1.5,masker_type='Labels'):
    
    """Extract time series from ROIs (Labels, Seed, Map)
    
    Parameters
    ----------
    data: Filenames of subjects
        e.g., dir contains 33 individual data
              data = sorted(glob(os.path.join(datadir,'*.gz')))
            {'/Volumes/Konglab/rfmri_sex/Huli/7ICA/ICA_clean/all_native/subj01.nii.gz'
            ...
              /Volumes/Konglab/rfmri_sex/Huli/7ICA/ICA_clean/all_native/subj39.nii.gz'}
             
             
    atlas: regions or coordinates to extract signals from.

    masker_type : 
                1)'Labels'
                2)'Spheres'
                3)'Maps'
    
        
    Returns
    ---------
    subject_ts : 2-D (n_subjects,n_regions) array-like time series
    """
    subjects_ts=[]
    
    if masker_type == 'Labels':
        masker = NiftiLabelsMasker(labels_img=atlas,
                                   mask_img=brainmask,
                                   standardize=False,detrend=False,
                                    t_r=t_r,
                                    resampling_target='data',
                                    verbose=0)
         
    elif masker_type== 'Spheres':
        masker = NiftiSpheresMasker(seeds=atlas, 
                                        radius=4 ,mask_img=brainmask,
                                        detrend=False, standardize=True, 
                                        t_r=t_r)
            
    elif masker_type == 'Maps':
        masker = NiftiMapsMasker(maps_img=atlas,
                                     mask_img=brainmask,
                                     standardize=True,
                                     detrend=False,t_r=t_r,
                                     resampling_target='data',
                                     verbose=0)
            
           
    for subj in data:
        time_series = masker.fit_transform(subj)
        subjects_ts.append(time_series)
            
    return subjects_ts