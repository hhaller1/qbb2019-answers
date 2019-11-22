#!/usr/bin/env python3

import sys

file1 = open(sys.argv[1]) #SRR1035452_1_bismark_bt2_pe.bedGraph
file2 = open(sys.argv[2]) #SRR1035454_1_bismark_bt2_pe.bedGraph

input1 = []
overlap = []

file1uniq = []
file2uniq = []

for i, line in enumerate(file1):
    if i == 0:
        continue
    input1.append(line)

for i, line in enumerate(file2):
    if i == 0:
        continue
    if line not in input1:
        file2uniq.append(line)
    else:
        overlap.append(line)

for item in input1:
    if item not in overlap:
        file1uniq.append(item)

print (file1uniq)
print (file2uniq)