#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt
import numpy as np
import scipy as sc
import math

#np.random.binomial(num of trials, prob of each trial, output size)

def wrightfisher(n, p, trials):
    pops= n
    gen_list=[]

    for gen in range(trials):
        a_freq= p
        gen_counter= 0
    
        while True:
            numoffspring= np.random.binomial(n=(pops*2), p= a_freq)
            a_freq= (numoffspring/(2*pops))
            gen_counter += 1
            #print(a_freq)
            if (a_freq == 0) or (a_freq==1):
                break
        gen_list.append(gen_counter) 
    return gen_list
    
#print(gen_list)
"""first plot info"""
# fig, ax=plt.subplots(tight_layout=True)
# ax.set_xlabel("# of Generations")
# plt.hist(gen_list)
# fig.savefig("num_of_gens.png")
# #plt.show()
# plt.close(fig)

"""2nd plot info"""
# sizes= [100, 1000, 10000, 100000, 1000000]
# fixa=[]
#
# sizes_log=[]
#
# for number in sizes:
#     fixa.append(wrightfisher(number, 0.5, 1000))
#
# for values in sizes:
#     sizes_log.append(math.log(values,10))
#
# """make 2nd plot"""
# fig, ax=plt.subplots(tight_layout=True)
# ax.set_xlabel("log population size")
# ax.set_ylabel("time to fixation")
# plt.scatter(x=sizes_log, y=fixa)
# fig.savefig("change_pop_size.png")
# #plt.show()
# plt.close(fig)

"""3rd plot info"""
a_freq= [0.1, 0.3, 0.5, 0.7, 0.9]
fixa={}

for value in a_freq:
    a= wrightfisher(100, value, 100)
    fixa[value]= a

# print(fixa)

for key in a_freq:
    for j in fixa[key]:
        # print(key, j)
        plt.scatter(x=key, y=j, alpha= 0.3)

plt.show()


