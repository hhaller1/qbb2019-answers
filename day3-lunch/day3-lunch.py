#!/usr/bin/env python3

import sys

f=open(sys.argv[1])
position_list=[]
for i, line in enumerate(f):
    if "#" in line:
        continue
    
    columns= line.rstrip("\n").split()
    if "protein_coding" in line and "3R" in columns[0]:
        counter= 8
        for i in columns[8:]:
            counter += 1
            if i == "gene_name":
                name= columns[counter]
                break
        position_list.append((name, columns[3], columns[4]))


lo= 0
hi= int(len(position_list))-1
mid = 0
number_of_interations= 0
search_pos= 21378950

#def distance_fxn(m):
    

while lo <= hi:
    mid = int(((int(hi) + int(lo))/2))
    number_of_interations += 1
    if mid == hi or mid == lo:
        print(number_of_interations)
        print(position_list[mid][0])
        print ("Sure thing")
        break
    if search_pos < int(position_list[mid][1]):
        hi = mid
    elif search_pos > int(position_list[mid][2]):
        lo = mid
    else:
        print(number_of_interations)
        print(position_list[mid][0])
        break
                
#didn't have time to calculate the distance