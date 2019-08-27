#!/usr/bin/env python3

import sys

gene_dict= {} ##create a dictionary from the data in in the file we made in #1
              ##which includes gene IDs and Uniprot ID only
#arg 1 is the file used to make the dictionary              
for i, line in enumerate(open(sys.argv[1])):
    column= line.rstrip("\n").split()
    gene_name= column[0]
    uniprot= column[1]
    if gene_name in gene_dict:
        continue
    else:
        gene_dict[gene_name]= uniprot ##adds the info to the dictionary

#second argument is the .ctab file
for i, line in enumerate(open(sys.argv[2])):
    column= line.split("\t")
    gene_ID= column[8] ##columnn containing GeneID
    
    if gene_ID in gene_dict:
        print (line, gene_dict[gene_ID]) ##prints line from teh .ctab file + Uniprot
    elif gene_ID not in gene_dict and sys.argv[3] == "nothing":
        continue
    elif gene_ID not in gene_dict and sys.argv[3] == "default":
        print("N/A")

#include a third argument of default(if you want to print N/A) or nothing(if you want to skip them) 
        
        
        