#!/usr/bin/env python3

"""Plotting four figures in one for Variant Detection 
input file: filterdecall.vsf (a vcf file miss label when created)"""

import sys
import matplotlib.pyplot as plt

vcf=open(sys.argv[1])

dp_list = []
qual_value = []
allele_list = []
predicted_dict = {}

#Plotting for Depth Info
for line in vcf: 
    if line.startswith("#"):
        continue
    column = line.rstrip("\n").split("\t")
    fields = column[7].rstrip("\n").split(";")
    dp = fields[7].rstrip("\n").split("=")
    dp_list.append(dp[1])
    
#Genotype Quality Distribution 
    qual_dist = float(column[5])
    qual_value.append(float(qual_dist))


#Allele frequency spectrum
    allele_freq = fields[3].rstrip("\n").split("=")
    allele_list.append(allele_freq[1])

#Predicted Effect 
    col=fields[41].rstrip("\n").split("|")
    ai=col[1]
    if ai in predicted_dict:
        predicted_dict[ai] += 1
    else:
        predicted_dict[ai] = 1
    
  
#Graphing the values 
fig,ax = plt.subplots(4)

ax[0].hist(dp_list, bins = 100)
ax[0].set_title("Depth", size = 5)
ax[1].hist(qual_value, bins = 1000, range= [0, 5000])
ax[1].set_title("Quality", size = 5)
ax[2].hist(allele_list, bins = 50)
ax[2].set_title("Allele Frequency", size = 5)
plt.bar(range(len(predicted_dict)), list(predicted_dict.values()), align = 'center')
plt.xticks(range(len(predicted_dict)), list(predicted_dict.keys()), rotation = 'vertical', size = 5)
ax[3].set_title("Predicted Effects", size = 5)
ax[3].set_ylabel("Frequency", size = 5)


plt.tight_layout()
fig.savefig("plots.png")
plt.close(fig)
