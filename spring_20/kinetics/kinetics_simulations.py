#!/usr/bin/env python3

#kinetics simulation lab: single molecule folding reaction

from __future__ import division
import matplotlib
import numpy as np
from pylab import *
matplotlib.rcParams.update({"axes.formatter.limits": (-3,3)})
plotStyles={"markersize":10,"markeredgewidth":2.0,"linewidth":2.0}
stepStyles={"markersize":12,"markeredgewidth":3.0,"linewidth":3.0,"where":"post"}

import numpy.random as rnd

k1=0.15
k2=0.07
ts=[0.0]   # a list of the times when a state change has occurred
states=[0] # state 0 is unfolded, state 1 is folded
tf=1000.0   # the final time of the simulation

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

fig,(ax1,ax2)=plt.subplots(nrows=2)
ax1.hist(fold, bins= 20, color = "blue", label = "Folded -> Unfolded")
ax2.hist(unfold, bins= 20, color = "green", label = "Unfolded -> Folded")
ax2.set_xlabel("Wait times (s)")
ax1.set_ylabel("# of transitions")
ax2.set_ylabel("# of transitions")
ax1.legend(loc="center right")
ax2.legend(loc="center right")
ax1.set_title("Wait times in the Folded and Unfolded State")

fig.savefig("Histograms.png")
plt.close(fig)
#plt.show()