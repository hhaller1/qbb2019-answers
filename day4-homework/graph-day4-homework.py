#!/usr/bin/env python3

"""
Usage: ./graph-day4-homework.py <metadata.csv> <ctab_dir>
~/qbb2019/data/samples.csv 
/Users/cmdb/qbb2019-answers/results/results/stringtie
"""

import sys
import os
import pandas as pd

metadata= sys.argv[1]
ctab_dir= sys.argv[2]

fpkms= {}

for i, line in enumerate(open(metadata)):
    if i==0:
        continue
    fields= line.rstrip("\n").split(",")
    srr_id= fields[0]
    sex= fields[1]
    stage= fields[2]
    sex_stage= sex + "_" + stage
    ctab_path= os.path.join(ctab_dir, srr_id, "t_data.ctab")
    
    #print(ctab_path)
    df= pd.read_csv(ctab_path, sep="\t", index_col="t_name")
    if i== 1:
        fpkms["gene_name"]= df.loc[:,"gene_name"]
    fpkms[(sex_stage)]= df.loc[:,"FPKM"]

df_fpkms = pd.DataFrame(fpkms)
print(df_fpkms.describe())
pd.DataFrame.to_csv(df_fpkms, "w_col_names.csv")