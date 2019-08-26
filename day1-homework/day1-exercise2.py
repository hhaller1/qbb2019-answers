#!/usr/bin/env python3
import sys

f= open(sys.argv[1])
counter=0
for lines in f:
    fields= lines.split("\t")
    if "NM:i:0" in fields:
        counter+=1

print(counter)