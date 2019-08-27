#!/usr/bin/env python3

import sys

#provide the file fly.txt 
f=open(sys.argv[1])
for i, line in enumerate(f):
    columns= line.split() ## split on whitespace
    for field in columns:
        if field.endswith("DROME"):
            if "FBgn" not in columns[-1]:
                continue
            print(columns[-1], columns[-2])
             ##prints last column & 2nd to last column
        


