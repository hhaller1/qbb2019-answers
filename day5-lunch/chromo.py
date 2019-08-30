#!/usr/bin/env python3

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.decomposition import PCA

ctab_file= open(sys.argv[1])

df= pd.read_csv(ctab_file, sep="\t")
#print (df)

genes= df.loc[:,("t_name", "start", "end", "chr", "strand")]

for i, t in genes.iterrows():
    c= t.loc["chr"]
    t_name = t.loc["t_name"]

    if t.loc["strand"] == "+":
        promoter_start1= int(t.loc["start"]) -500
        promoter_end1= int(t.loc["start"]) + 500
        if promoter_start1 > 0:
            print(c, promoter_start1, promoter_end1, t_name, sep= "\t")
        else:
            print(c, 1, promoter_end1, t_name, sep= "\t")

    elif t.loc["strand"] == "-":
        promoter_start2= int(t.loc["end"]) -500
        promoter_end2= int(t.loc["end"]) +500
        if promoter_start2 > 0:
            print(c, promoter_start2, promoter_end2, t_name, sep= "\t")
        else:
            print(c, 1, promoter_end2, t_name, sep= "\t")
