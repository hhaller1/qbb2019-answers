#!/usr/bin/env python3

#kinetics simulation lab: single molecule folding reaction probability density function analysis (PDF)

from __future__ import division
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
matplotlib.rcParams.update({"axes.formatter.limits": (-3,3)})
plotStyles={"markersize":10,"markeredgewidth":2.0,"linewidth":2.0}
stepStyles={"markersize":12,"markeredgewidth":3.0,"linewidth":3.0,"where":"post"}

import numpy.random as rnd
import scipy.optimize as optimize

k1=0.15
k2=0.07
ts=[0.0]   # a list of the times when a state change has occurred
states=[0] # state 0 is unfolded, state 1 is folded
tf=10000.0   # the final time of the simulation

fold=[]
unfold=[]

while (ts[-1]<tf):
    
    # If we are in the unfolded state, figure out when the molecule transitions to the folded state.
    if states[-1] == 0:
        ts.append(ts[-1]+rnd.exponential(1/k1))
        states.append(1)
    
    # If we are in the folded state, figure out when the molecule transitions to the unfolded state.
    else:
        ts.append(ts[-1]+rnd.exponential(1/k2))
        states.append(0)

##this makes the FRET looking plot for a single molecule
# matplotlib.rcParams.update({'font.size': 15, "figure.figsize": (15,5)})
# step(ts,states, **stepStyles)
# xlabel('t'); ylim([-0.1,1.1]); ylabel('State');
# #plt.show()


res = [y-x for x, y in zip(ts, ts[1:])]
#print(res)
fold = [res[0:len(res):2]]
unfold = [res[1:len(res):2]]
#print(unfold)
#print(fold)

hist1, bin_edges1 = np.histogram(fold, bins = 20)
bin_width1 = bin_edges1[1] - bin_edges1[0]

fold_PDF=[]
for value in hist1:
    fold_PDF.append(value/(bin_width1 * sum(hist1)))


hist2, bin_edges2 = np.histogram(unfold, bins = 20)
bin_width2 = bin_edges2[1] - bin_edges2[0]

unfold_PDF=[]
for value in hist2:
    unfold_PDF.append(value/(bin_width2 * sum(hist2)))

#print(unfold_PDF)

unfold_center = np.mean(np.vstack([bin_edges2[0:-1], bin_edges2[1:]]), axis = 0)
fold_center = np.mean(np.vstack([bin_edges1[0:-1], bin_edges1[1:]]), axis = 0)

#the PDF for an exponential distribution

# f_exp_PDF= k2 * np.exp(-k2*fold_center)
# u_exp_PDF= k1 * np.exp(-k1*unfold_center)
def func(k, t):
    return k * np.exp(-k*t)

bin_center1 = np.array(fold_center, dtype = float)
avg_count1 = np.array(fold_PDF, dtype = float)
popt1, pcov = optimize.curve_fit(func, bin_center1, avg_count1)

bin_center2 = np.array(unfold_center, dtype = float)
avg_count2 = np.array(unfold_PDF, dtype = float)
popt2, pcov2 = optimize.curve_fit(func, bin_center2, avg_count2)

'''popt1 and popt2 give you the predicted k values popt1 -> k2 & popt2 -> k1'''

f_bestfit= popt1 * np.exp(-popt1*unfold_center)
u_bestfit= popt2 * np.exp(-popt2*unfold_center)

fig,(ax1,ax2)=plt.subplots(nrows=2)

ax1.bar(fold_center, fold_PDF, color = "blue", alpha=0.4, label = "Folded -> Unfolded")
ax2.bar(unfold_center, unfold_PDF, color = "red",alpha=0.4, label = "Unfolded -> Folded")

ax1.bar(fold_center, f_bestfit, color="green",alpha=0.4, label = "best fit")
ax2.bar(unfold_center, u_bestfit, color="yellow",alpha=0.5, label = "best fit")


ax2.set_xlabel("wait times (s)")
ax1.set_ylabel("PDF")
ax2.set_ylabel("PDF")
ax1.legend(loc="upper right")
ax2.legend(loc="upper right")
ax1.set_title("Probability Density Function for Folding Transitions (t=10000s)")

fig.savefig("PDF2_t10000.png")
plt.close(fig)
plt.show()

rel_error= popt1-k2/k2
rel_error2= popt2-k1/k1
print("k1 error=", rel_error2, "k2 error=", rel_error)





