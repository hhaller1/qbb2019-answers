#!/usr/bin/env python3
"""
Usage: ./02-timecourse.py <t_name> <samples.csv> <FPKMs.csv>
Create a timecourse of a given transcript for females
"""
import sys
import pandas as pd
import matplotlib.pyplot as plt
import os
#specify transcript of interest
t_name= sys.argv[1]
#load metadata
samples= pd.read_csv(sys.argv[2])
replicates=pd.read_csv(sys.argv[3])
ctab_dir = sys.argv[4]
def sexfinder(sex,rep):
    soi= rep.loc[:,"sex"] == sex # Identify which sample rows match target sex
    srr_ids = rep.loc[soi, "sample"] # Find the samples, corresponding to rows in soi
    my_data = []
   
    for srr_id in srr_ids:
        ctab_path = os.path.join (ctab_dir, srr_id, "t_data.ctab") # Find path to ctab file
        df = pd.read_csv (ctab_path, sep="\t",index_col="t_name") # Load ctab file
        my_data.append(df.loc[t_name,"FPKM"]) # Grab the FPKM value for our transcript, and append to my_data
       # fpkms = pd.read_csv(sys.argv[3], index_col="t_name")
       # my_data.append(fpkms.loc[t_name,srr_id])
    return my_data
       
female_fpkms = sexfinder('female', samples)
female_fpkms2 = sexfinder('female', replicates)
male_fpkms = sexfinder('male', samples)
male_fpkms2 = sexfinder('male', replicates)
fig, (ax) =plt.subplots()
ax.plot(female_fpkms, color="red", label='female')
ax.plot(range(4,8),female_fpkms2,"x", color="red", label='female')
ax.plot(male_fpkms, color="blue", label='male')
ax.plot(range(4,8),male_fpkms2,"x", color="blue", label='male')
ax.legend(loc='lower right', bbox_to_anchor=(1.3, .5))
ax.set_xticklabels(["0", "10", "11", "12", "13", "14A", "14B", "14C", "14D"])
ax.set_ylabel("mRNA abundance(RPKM)")
ax.set_xlabel("development stage")
fig.suptitle("Sxl", style="italic")
plt.tight_layout()
plt.subplots_adjust(top=0.9)

fig.savefig("timecourse.png")
plt.close(fig)

   