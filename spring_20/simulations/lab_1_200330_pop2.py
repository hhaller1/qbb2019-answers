#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt
import numpy as np
import scipy as sc
import math


def StatW_Fold(deltaH, Tm, deltaCp):
    R_const= 0.01987
    Temp= [] 
    for value in range(223,374):
        Temp.append(value)
    #print(Temp)
    weights=[]
    prob_fold=[]
    
    for number in Temp:
        sw= np.exp(-(deltaH * (1 - (number/Tm)) + deltaCp * (number * (1 - np.log(number/Tm)) - Tm))/(R_const * number))
        weights.append(sw)
  
    for weight in weights:
        p= 1 / (1 + weight) 
        prob_fold.append(p)   
        
    return prob_fold 

def StatW_UnFold(deltaH, Tm, deltaCp):
    R_const= 0.01987
    Temp= [] 
    for value in range(223,374):
        Temp.append(value)
    #print(Temp)
    weights=[]
    prob_unfold=[]
    
    for number in Temp:
        sw= np.exp(-(deltaH * (1 - (number/Tm)) + deltaCp * (number * (1 - np.log(number/Tm)) - Tm))/(R_const * number))
        weights.append(sw)
  
    for weight in weights:
        p= weight / (1 + weight) 
        prob_unfold.append(p)   
        
    return prob_unfold 
    
Temp= [] 
for value in range(223,374):
    Temp.append(value)
    #print(Temp)
    
unfold_list1=StatW_UnFold(100,323,0)
fold_list1=StatW_Fold(100,323,0)

fold_list2=StatW_Fold(100,323,1.5)
unfold_list2=StatW_UnFold(100,323,1.5)

fold_list3=StatW_Fold(100,323,3)
unfold_list3=StatW_UnFold(100,323,3)

#Plotting the Folding and Unfolding Curves
# fig, (ax1,ax2,ax3)=plt.subplots(nrows=3)
# ax1.plot(Temp, fold_list1 , color = "red", label = "Folded")
# ax1.plot(Temp, unfold_list1 , color = "blue", label = "Unfolded")
# ax2.plot(Temp, fold_list2 , color = "red", label = "Folded")
# ax2.plot(Temp, unfold_list2 , color = "blue", label = "Unfolded")
# ax3.plot(Temp, fold_list3 , color = "red", label = "Folded")
# ax3.plot(Temp, unfold_list3 , color = "blue", label = "Unfolded")
#
# plt.legend(loc="center right")
# ax1.set_title("Probability of Folded & Unfolded State")
#
# ax3.set_xlabel("Temperature (K)")
# ax1.set_ylabel("Probability")
# ax2.set_ylabel("Probability")
# ax3.set_ylabel("Probability")
# # fig.savefig("Folding curves_Cp.png")
# # plt.close(fig)
# plt.show()

#Ploting only the Folded States for the 3 cases
fig, ax = plt.subplots()
ax.plot(Temp, unfold_list1 , color = "red", label = "Case1")
ax.plot(Temp, unfold_list2 , color = "darkgreen", label = "Case2")
ax.plot(Temp, unfold_list3 , color = "blue", label = "Case3")

plt.legend(loc="center right")
ax.set_title("Probability of Folded vs Temp")
ax.set_xlabel("Temperature (K)")
ax.set_ylabel("Probability")

# fig.savefig("PvsT_Cp.png")
# plt.close(fig)
plt.show()