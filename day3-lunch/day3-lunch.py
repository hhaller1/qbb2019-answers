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
        position_list.append((name, int(columns[3]), int(columns[4])))


lo= 0
hi= int(len(position_list))-1
mid = 0
number_of_interations= 0
search_pos= int(sys.argv[2]) #21378950

#def distance_fxn(m):
    

while lo <= hi:
    mid = int(((int(hi) + int(lo))/2))
    number_of_interations += 1
    if mid == hi or mid == lo:
    #if hi-lo == 1:
        if (abs(position_list[lo][2]-search_pos)) > (abs(position_list[hi][1]-search_pos)):
            mid = hi
            print (abs(position_list[hi][1]-search_pos))
        elif (abs(position_list[lo][2]-search_pos)) < (abs(position_list[hi][1]-search_pos)):
            mid = lo
            print (abs(position_list[lo][1]-search_pos))
        break
    if search_pos < int(position_list[mid][2]):
        hi = mid
    elif search_pos > int(position_list[mid][2]):
        lo = mid
    else:
        break
                
print(number_of_interations)
print(position_list[mid])     