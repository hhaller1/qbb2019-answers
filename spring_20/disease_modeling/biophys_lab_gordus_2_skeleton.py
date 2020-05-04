#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Andrew Gordus
May, 2020
Quantitative Biology and Biophysics (AS.020.674/250.644)	Spring 2020
Gordus Lab #2

"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp


#---------------#
# Set Variables #
#---------------#

S0 = 1 # Actual NYC population: 8*np.power(10,6)
I0 = 30 / (8*np.power(10,6))

R0 = 2.2
gamma = 0.44
beta = R0*gamma/S0


#-------------------#
# Current NYC Stats #
#-------------------#

# Current NYC Stats
# Shelter in Place occurred t = 12 days
# Confirmed cases was ~17644 at this point

Conf = 167000 #52 days from t0
Dead = 13000 #52 days from t0
Rec = 40000 #52 days from t0


f = Dead/Conf


#-------------#
# PHASE PLANE #
#-------------#

# Null Clines

Sn = gamma/beta
In = 0


Sspan = np.linspace(0,S0,10)
Ispan = np.linspace(0,S0,10)

# Grid of x & y values
S, I = np.meshgrid(Sspan, Ispan)

# Empty matrices to fill in with velocity data
dS = np.zeros(np.shape(S))
dI = np.zeros(np.shape(I))

#Fill velocities into grid.
for m in range(S.shape[0]):
    for n in range(I.shape[0]):
        dS[m,n] = -beta * S[m][n] * I[m][n]
        dI[m,n] = beta * S[m][n] * I[m][n] - gamma * I[m][n]


#----------------------#
# NUMERICAL SIMULATION #
#----------------------#


# ODE

y0 = np.array([1 - 23/(8*np.power(10,6)), 23/(8*np.power(10,6)), 0,0])


def SIR(t,y):
    dSdt = -1 * beta * y[0] * y[1]
    dIdt = beta * y[0] * y[1] - gamma * y[1]
    dRdt = (1-f) * gamma * y[1]
    dDdt = f * gamma * y[1]
    
    return np.array([dSdt, dIdt, dRdt, dDdt])
    


# Integrators
    
# Runge-Kutta
def runge_kutta(y0, t, h):
    timesteps = int(t/h)
    yn=y0
    
    for i in range(1, timesteps): 
            k1 = SIR(i, yn)
            k2 = SIR(i, yn + 0.5 * h * k1)
            k3 = SIR(i, yn + 0.5 * h * k2)
            k4 = SIR(i, yn + h * k3)
            yn += (h/6) * (k1 + 2 * k2 + 2 * k3 +k4)
    
    return yn
        

# Scipy integrator

sol1 = solve_ivp(SIR, [0,12],[S0,I0,0,0],max_step = 1)
sol2 = solve_ivp(SIR, [0,50],[S0,I0,0,0],max_step = 1)
sol3 = solve_ivp(SIR, [0,100],[S0,I0,0,0],max_step = 1)
irdsol1=(sol1.y[1]+ sol1.y[2]+ sol1.y[3]) #sum of I R and D for part 1d
irdsol2=(sol2.y[1]+ sol2.y[2]+ sol2.y[3])
irdsol3=(sol3.y[1]+ sol3.y[2]+ sol3.y[3])
#print(sumsol1)

sol38=solve_ivp(SIR, [12,38],[S0,I0,0,0],max_step = 1)
irdsol38=(sol38.y[1]+ sol38.y[2]+ sol38.y[3])
sol88=solve_ivp(SIR, [12,88],[S0,I0,0,0],max_step = 1)
irdsol88=(sol88.y[1]+ sol88.y[2]+ sol88.y[3])

# NOTE:
# sol.t = time vector
# sol.y = matrix of output. Rows are S, I, R, D; Columns are time
#print(sol.y[0])


# Set up the matplotlib figure 

#----------------------#
#        Part 1        #
#----------------------#

X = np.arange(-10, 10, 1)
Y = np.arange(-10, 10, 1)
U, V = np.meshgrid(X, Y)

fig, ax = plt.subplots(2,2)
plt.tight_layout()
q = ax[0,0].quiver(S , I , dS, dI)
ax[0,0].quiverkey(q, X=0.3, Y=1.1, U=1,label='Quiver key, length = 1', labelpos='E')
ax[0,0].plot([Sn, Sn], [0,S0])
ax[0,0].set_xlabel('S')
ax[0,0].set_ylabel('I')

ax[0,1].plot(sol1.t, sol1.y[0], color="blue", label="S")
ax[0,1].plot(sol1.t, sol1.y[1], color="red", label="I")
ax[0,1].plot(sol1.t, sol1.y[2], color="green", label="R")
ax[0,1].plot(sol1.t, sol1.y[3], color="black", label="D")
ax[0,1].plot(sol1.t, irdsol1, color="orange", label="I+R+D")
ax[0,1].set_title("12")

ax[1,0].plot(sol2.t, sol2.y[0], color="blue", label="S")
ax[1,0].plot(sol2.t, sol2.y[1], color="red", label="I")
ax[1,0].plot(sol2.t, sol2.y[2], color="green", label="R")
ax[1,0].plot(sol2.t, sol2.y[3], color="black", label="D")
ax[1,0].plot(sol2.t, irdsol2, color="orange", label="I+R+D")
ax[1,0].set_title("50")

ax[1,1].plot(sol3.t, sol3.y[0], color="blue", label="S")
ax[1,1].plot(sol3.t, sol3.y[1], color="red", label="I")
ax[1,1].plot(sol3.t, sol3.y[2], color="green", label="R")
ax[1,1].plot(sol3.t, sol3.y[3], color="black", label="D")
ax[1,1].plot(sol3.t, irdsol3, color="orange", label="I+R+D")
ax[1,1].set_title("100")

ax[0,1].legend()

#plt.show()
fig.savefig("Part1.png")
plt.close(fig)

#----------------------#
#        Part 2        #
#----------------------#

# fig, ax = plt.subplots(2,2)
# plt.tight_layout()
#
# ax[0,0].plot(sol1.t, sol1.y[0], color="blue", label="S")
# ax[0,0].plot(sol1.t, sol1.y[1], color="red", label="I")
# ax[0,0].plot(sol1.t, sol1.y[2], color="green", label="R")
# ax[0,0].plot(sol1.t, sol1.y[3], color="black", label="D")
# ax[0,0].plot(sol1.t, irdsol1, color="orange", label="I+R+D")
# ax[0,0].set_title("12")
#
# ax[1,0].plot(sol38.t, sol38.y[0], color="blue", label="S")
# ax[1,0].plot(sol38.t, sol38.y[1], color="red", label="I")
# ax[1,0].plot(sol38.t, sol38.y[2], color="green", label="R")
# ax[1,0].plot(sol38.t, sol38.y[3], color="black", label="D")
# ax[1,0].plot(sol38.t, irdsol38, color="orange", label="I+R+D")
# ax[1,0].set_title("38")
#
# ax[1,1].plot(sol88.t, sol88.y[0], color="blue", label="S")
# ax[1,1].plot(sol88.t, sol88.y[1], color="red", label="I")
# ax[1,1].plot(sol88.t, sol88.y[2], color="green", label="R")
# ax[1,1].plot(sol88.t, sol88.y[3], color="black", label="D")
# ax[1,1].plot(sol88.t, irdsol88, color="orange", label="I+R+D")
# ax[1,1].set_title("88")
#
# ax[0,0].legend()
#
# #plt.show()
# fig.savefig("Part2.png")
# plt.close(fig)



