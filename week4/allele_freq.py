#!/usr/bin/env python3

"""PLINK to determine allele freq:  plink --vcf 
BYxRM_segs_saccer3.bam.simplified.vcf --freq counts --allow-extra-chr
used plink.frq file for this plot"""

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

freq= open(sys.argv[1]) #plink.frq file

minor_allele_freq= []

for line in freq:
    if "CHR" in line:
        continue
    else:
        col = line.split()
        values= float(col[4])
        minor_allele_freq.append(values)
  
#print(minor_allele_freq)

fig, ax = plt.subplots()
ax.hist(minor_allele_freq, bins= 50)
fig.suptitle("allele frequencies")
ax.set_xlabel("allele")
ax.set_ylabel("frequency")

fig.savefig("freq.png")
plt.close()
