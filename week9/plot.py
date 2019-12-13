#!/usr/bin/env python3

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

fimo=open(sys.argv[1]) #memechip_out/fimo_out_1/fimo.tsv

starts= []

for i, line in enumerate(fimo):
    col=line.rstrip("\n").split("\t")
    if i==0:
        continue
    if i > 140:
        continue
    start=col[3]
    score = round(float(col[6]))
    for j in range(score):
        starts.append(int(start)) 
        
starts.sort()

chr19=[0]*61431566

for i in starts:
    for j in range(20):
        chr19[i+j] += 1
        
position=[]
for i in range(len(chr19)):
    if chr19[i]!=0:
        for j in range(chr19[i]):
            position.append(i)
      
fig, ax=plt.subplots(tight_layout=True)
sns.distplot(position, hist=True)
ax.set_xlabel("Position")
ax.set_ylabel("Frequency")
fig.savefig("distribution.png")
plt.close(fig)
#plt.show()
