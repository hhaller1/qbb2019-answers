#!/usr/bin/env python3
"""
Usage: ./homework-timecourse.py <t_name> samples.csv FPKMs
subset using loolean filters
"""
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#specify transcript of interest FBtr0331261
t_name= sys.argv[1]
#load metadata
samples= pd.read_csv(sys.argv[2]) #/Users/cmdb/qbb2019/data/samples.csv

def sex_fxn(sex):   
    soi= samples.loc[:,"sex"] == sex
    srr_ids= samples.loc[soi,"sample"]

    fpkms= pd.read_csv(sys.argv[3], index_col="t_name")
    #/Users/cmdb/qbb2019-answers/day4-afternoon/all.csv
    
    my_data= []
    for srr_id in srr_ids:
        my_data.append(fpkms.loc[t_name,srr_id])
    return my_data
    
f_vals= sex_fxn("female")
m_vals= sex_fxn("male")


fig, ax= plt.subplots()
ax.plot(f_vals, color="red", label="female")
ax.plot(m_vals, color="blue", label="male")
plt.legend(loc="upper center", bbox_to_anchor=(1.2,0.5))

fig.suptitle("Sxl")
ax.set_xlabel("Developmental Stage")
ax.set_ylabel("mRNA abundance(RPKM)")
ax.set_xticklabels(["0", "10", "11", "12", "13", "14A", "14B", "14C", "14D"])
plt.tight_layout()
plt.subplots_adjust(top=0.9)

fig.savefig("hwtimecourse.png")
plt.close(fig)
    