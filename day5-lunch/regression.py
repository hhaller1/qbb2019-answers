#!/usr/bin/env python3

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import scipy

df= pd.read_csv(sys.argv[1], sep="\t", index_col="t_name") #Users/cmdb/qbb2019-answers/results/results/stringtie/SRR072893/t_data.ctab 
df2=pd.read_csv(sys.argv[2], sep="\t", index_col=0, header= None) #H3K4me3.tab
df3=pd.read_csv(sys.argv[3], sep="\t", index_col=0, header= None) #H3K4me1.tab
df4=pd.read_csv(sys.argv[4], sep="\t", index_col=0, header= None) #H3K9me3.tab

histone_dict = {"FPKM" : df.loc[:,"FPKM"],
               "H3K4me1": df2.iloc[:,-1],  ##i to specify column
               "H3K4me3": df3.iloc[:,-1],
               "H3K9me3": df4.iloc[:,-1]}

histone_df = pd.DataFrame(histone_dict)
#print(histone_df)
model = sm.formula.ols(formula = "FPKM ~ H3K4me1 + H3K4me3 + H3K9me3", data = histone_df)
ols_result = model.fit()
print(ols_result.summary())

#iloc finds by position (index value) and loc finds by label

# col_names= df.columns.values.tolist()
#
# goi= pd.DataFrame(df.loc[sys.argv[2]].iloc[1:]) #FBtr0302347
# goi.columns= ["FPKM"]
#
# goi["FPKM"]= pd.to_numeric(goi["FPKM"])
#
# goi["sex"], goi["stage"]= goi.index.str.split("_", 1).str
# #break the index column into two new col by splitting at the _
#
#
# #FPKM is response variable and sex is predictor variable( can be more than one variabe eq. sex + stage)
# ols_results= model.fit()
# #this does least squares fitting
#
# print (ols_results.summary())