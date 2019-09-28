#!/bin/bash

#loop to go through all the plink files to make the manhattan plots
#Use directory Users/cmdb/qbb2019-answers/week4/plinks/*

echo "enter the directory path:"
read directory
for file in $directory; do
    ./manhattan.py $file
done