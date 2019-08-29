#!/usr/bin/env python3

"""
Usage: ./00-merge.py <ctab1> <ctab2>

"""
#file /Users/cmdb/qbb2019-answers/results/results/stringtie/SRR072893/t_data.ctab
#file /Users/cmdb/qbb2019-answers/results/results/stringtie/SRR072894/t_data.ctab

import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

name1= sys.argv[1].split(os.sep)[-2]
ctab1 = pd.read_csv(sys.argv[1], sep= "\t", index_col="t_name") 

name2= sys.argv[2].split(os.sep)[-2]
ctab2 = pd.read_csv(sys.argv[2], sep= "\t", index_col="t_name") 

#fpkm= {"1": [1,2,3], "sample2":[4,5,6]} #name of the col and values in the col
fpkm = {name1 : ctab1.loc[:,"FPKM"], name2 : ctab2.loc[:,"FPKM"]}
df= pd.DataFrame(fpkm)

srr1= df.loc[:,name1]
srr2= df.loc[:,name2]

log_srr1= np.log2(srr1 + 1)
log_srr2= np.log2(srr2 + 1)

fig, ax= plt.subplots()
ax.scatter(log_srr1, log_srr2, s=5, alpha= 0.15) 

coeff= np.polyfit(log_srr1, log_srr2, 1)
x= np.linspace(0, 12, 10)
y= coeff[0]*x + coeff[1]
ax.plot(x, y, label= "curve fit", color= "red")
ax.legend()

fig.suptitle("FPKMs of SRR0072893 vs SRR0072894")
ax.set_xlabel("SRR0072893")
ax.set_ylabel("SRR0072894")

fig.savefig("fpkm_comparisons.png")
plt.close(fig)