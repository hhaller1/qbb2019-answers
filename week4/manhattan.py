#!/usr/bin/env python3

"""makes a manhanttan plot"""
import sys 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

x = open(sys.argv[1])

p = []

for i, line in enumerate(x): 
    if i == 0:
        continue 
    if "NA" in line:
        continue
    cols = line.rstrip("\n").split()
    p.append(cols[8])

logp=[]
counter = 0
pos = []
for pvalue in p:
    if pvalue == "NA":
        continue 
    elif pvalue == 0:
        continue
    else:
        logp.append(-(np.log10(float(pvalue))))
        counter += 1
        pos.append(counter)

fig, ax = plt.subplots()
for i in range(len(pos)):
    if logp[i] > 5:
        ax.scatter(x = pos[i], y=logp[i], alpha = 0.3, color = "red")
    else: 
        ax.scatter(x=pos[i], y=logp[i], alpha = 0.3, color = "blue")
fig.savefig(sys.argv[1] + ".png")
plt.close(fig)
