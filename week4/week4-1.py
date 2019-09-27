#!/usr/bin/env python3

"""PLINK to preform PCA: plink --vcf BYxRM_segs_saccer3.bam.simplified.vcf 
--pca 2 --allow-extra-chr --allow-no-sex --mind
used plink.eigenvec file for this plot"""

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

eigenvec= open(sys.argv[1]) #plink.eigenvec file

comp1= []
comp2= []

for line in eigenvec:
    col = line.split(" ")
    third= float(col[2])
    fourth= float(col[3])
    comp1.append(third)
    comp2.append(fourth)
#print(comp1)

fig, ax = plt.subplots()
ax.scatter(comp1, comp2)
fig.suptitle("PCA")
ax.set_xlabel("PC1")
ax.set_ylabel("PC2")

fig.savefig("pca.png")
plt.close()

    
    
