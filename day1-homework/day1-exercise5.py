#!/usr/bin/env python3
import sys

f= open(sys.argv[1])

map_list=[]
for line in f:
    fields= line.split("\t")
    value= int(fields[4])
    map_list.append(value)
    
length=len(map_list)
total_map = sum(map_list)
ave= total_map/length
print (ave)