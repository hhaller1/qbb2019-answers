#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt
import numpy as np
import scipy as sc
import math


def two_state(deltaH, Tm, deltaCp):
    
    Temp= [] 
    for value in range(273,374):
        Temp.append(value)
    #print(Temp)
    
    deltaG=[]
    for number in Temp:
        dG= deltaH * (1 - (number/Tm)) + deltaCp * (number * (1 - np.log(number/Tm)) - Tm)
        deltaG.append(dG)
        #print(deltaG)
    return deltaG

Temp= [] 
for value in range(273,374):
    Temp.append(value)
    #print(Temp)
    

glist_1=two_state(100,323,0)
glist_2=two_state(100,323,1.5)
glist_3=two_state(100,323,3)

fig, ax = plt.subplots()
ax.plot(Temp, glist_1 , color = "red", label = "Case1")
ax.plot(Temp, glist_2 , color = "darkgreen", label = "Case2")
ax.plot(Temp, glist_3 , color = "blue", label = "Case3")
plt.legend(loc="upper right")
ax.set_title("Number3")
ax.set_xlabel("Temperature (K)")
ax.set_ylabel("Delta G (kcal/mol K)")
fig.savefig("Number3.png")
plt.close(fig)
# plt.show()