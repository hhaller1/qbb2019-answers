#!/usr/bin/env python3
import sys

f= open(sys.argv[1])
counter=0
for lines in f:
    fields= lines.split("\t")
    if fields[2] != "*":
        counter += 1
    else:
        continue
print(counter)
    