#!/usr/bin/env python3

"""
Usage: ./01-hist.py <ctab>
plot FMPK
"""
import sys
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats #import distributions

#file /Users/cmdb/qbb2019-answers/results/results/stringtie/SRR072893/t_data.ctab

fpkms= []

for i, line in enumerate(open(sys.argv[1])):
    if i == 0:
        continue
    fields= line.rstrip("\n").split("\t")
    if float(fields[11]) > 0:
        fpkms.append(float(fields[11]))

print(len(fpkms))    

my_data= np.log2(fpkms)
a= float(sys.argv[2])
mu= float(sys.argv[3])
sigma= float(sys.argv[4])

x= np.linspace(-15, 15, 100)
y= stats.skewnorm.pdf(x, a, mu, sigma) 

mu1= 0
sigma1= 1
x1= np.linspace(-15, 15, 100)
y1= stats.norm.pdf(x1, mu1, sigma1)

fig, ax= plt.subplots() #fig corresponds to the image ax is the the number of subplots
ax.hist(my_data, bins=100, density=True)
ax.plot(x, y, label= "Skew Distribution")
ax.plot(x1, y1, label= "Normal Distribution")
ax.legend()

fig.suptitle("FPKMs in SRR072893 data")
plt.text(-15, 0.15,"a= %0.1f mu=%0.1f sigma=%0.1f" %(a,mu,sigma))
ax.set_xlabel("log2(number of fpkms)")
ax.set_ylabel("probability")
fig.savefig("fpkms.png")
plt.close(fig)