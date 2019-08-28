#!/usr/bin/env python3

"""match all kmers in a FASTA file"""

from fasta import FASTAReader
#import the fasta file to parse FASTA files- imports only the FASTAReader

import sys
target = FASTAReader(open(sys.argv[1]))
query = FASTAReader(open(sys.argv[2]))
k = int(sys.argv[3])

kmers_from_target = {}

for ident, sequence in target:
    sequence = sequence.upper()
    for i in range(0, len(sequence)- k + 1):  ## i is position ident is identity
        kmertarget = sequence[i:i+k]
        if kmertarget not in kmers_from_target:
            kmers_from_target[kmertarget]= [(ident, i)]
        else:
            kmers_from_target[kmertarget].append((ident, i))
         
    
for ident1, sequence1 in query:
    sequence1 = sequence1.upper()
    for i1 in range(0, len(sequence1)- k + 1):
        kmerquery = sequence1[i1:i1+k]
        if kmerquery not in kmers_from_target:
            continue
        else:
            print (kmers_from_target[kmerquery], str(i1), kmerquery)
    
    