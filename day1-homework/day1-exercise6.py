#!/usr/bin/env python3
import sys

f= open(sys.argv[1])

count= 0

for lines in f:
    fields= lines.split("\t")
    if "2L" in fields[2] and int(fields[3])<= 20000 and int(fields[3])>= 10000:
        count += 1
print(count)
    