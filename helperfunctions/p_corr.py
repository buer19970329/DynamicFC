# %%

def p_corr(parray,method = 'bonferroni'): 
    """
method:
    - `bonferroni` : one-step correction
    - `sidak` : one-step correction
    - `holm-sidak` : step down method using Sidak adjustments
    - `holm` : step-down method using Bonferroni adjustments
    - `simes-hochberg` : step-up method  (independent)
    - `hommel` : closed method based on Simes tests (non-negative)
    - `fdr_bh` : Benjamini/Hochberg  (non-negative)
    - `fdr_by` : Benjamini/Yekutieli (negative)
    - `fdr_tsbh` : two stage fdr correction (non-negative)
    - `fdr_tsbky` : two stage fdr correction (non-negative)
    """
    from statsmodels.stats import multitest as mt

    _,p_corrected,_,_ = mt.multipletests(parray,method=method)
    l = len(parray)
    for i in range(l):
        if p_corrected[i] < 0.05:
            if len(parray) == len(p_data_sd):
                print("Congrats! \033[1;35m %s \033[0m survived \033[1;31m %s \033[0m correction,p.%s=\033[1;31m %.3f \033[0m😁" % (corr_labels_sd[i], method, method, p_corrected[i]))
            if len(parray) == len(p_data_str):
                print("Congrats! \033[1;35m %s \033[0m survived \033[1;31m %s \033[0m correction,p.%s=\033[1;31m %.3f \033[0m😁" % (corr_labels_str[i], method, method, p_corrected[i]))
    return p_corrected
#仅适用于本样本,报错修改<line 23>
