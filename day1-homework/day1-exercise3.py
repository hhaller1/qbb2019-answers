#!/usr/bin/env python3
import sys

f= open(sys.argv[1])
counter=0
for lines in f:
    fields= lines.rstrip("\n").split("\t")
    if "NH:i:1" in fields:
        counter+=1

print(counter)