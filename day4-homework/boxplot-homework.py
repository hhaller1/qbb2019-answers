#!/usr/bin/env python3

"""
Usage: ./00-metadata.py <metadata.csv> <ctab_dir>

box plot all transcripts for male and female
"""

import sys
import os
import pandas as pd
import matplotlib.pyplot as plt

gene_name= sys.argv[1] #Sxl
fpkm_file= sys.argv[2] #w_col_names.csv


df= pd.read_csv(fpkm_file, index_col= "t_name")

goi=df.loc[:,"gene_name"]==gene_name  
fpkms= df.drop(columns="gene_name")

col_names=fpkms.columns
col_names2=[]
col_names3=[]
for i in col_names:
   if "female" in i:
       col_names2.append(True)
   else:
       col_names2.append(False)
       
for i in col_names2:
   if i== True:
       col_names3.append(False)
   else:
       col_names3.append(True)

fig,(ax1, ax2)=plt.subplots(nrows=2)
ax1.boxplot(fpkms.loc[goi,col_names2].T) #.T to transpose the matrix
ax2.boxplot(fpkms.loc[goi,col_names3].T)
fig.suptitle("FPKM values for Sxl gene in females and males")
ax1.set_ylabel("fpkm values")
ax2.set_ylabel("fpkm values")
ax2.set_xlabel("developmental stages")
ax1.set_xticklabels(["10", "11", "12", "13", "14A", "14B", "14C", "14D"])
ax2.set_xticklabels(["10", "11", "12", "13", "14A", "14B", "14C", "14D"])
ax1.set_title("Females")
ax2.set_title("Males")graphbo
plt.subplots_adjust(hspace=0.6)
fig.savefig("homework_boxplot.png")

plt.close(fig)
