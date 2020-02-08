#!/usr/bin/env python3
import sys
import matplotlib.pyplot as plt
import numpy as np
import scipy as sc

def wrightfisher_sel(n,p,trials,s):
    pops= n
    trials= 1000
    gen_list=[]
    
    for gen in range(trials):
        a_freq= p
        gen_counter= 0
        while True:
            numoffspring = np.random.binomial(n=(pops*2), p= a_freq)
            a_freq = (numoffspring * (1 + s)) / (( 2 * pops) - numoffspring + numoffspring * ( 1 + s ))
            gen_counter += 1
            #print(a_freq)
            if (a_freq == 0) or (a_freq==1):
                break
        gen_list.append(gen_counter)
    return(gen_counter)

"""4th plot info"""
sel = []
for i in range(200):
    sel.append(0.002 * i - 0.2)
gen = []
for j in sel:
    k = wrightfisher_sel(200, 0.5, 1, j)
    gen.append(k)
fig, ax = plt.subplots()
ax.scatter(sel, gen, s= 4)
ax.set_xlabel("Selection coefficient")
ax.set_ylabel("Number of generations")
fig.savefig("selection.png")
#plt.show()
plt.close(fig)





