#!/usr/bin/env python3
"""match extender"""

from fasta import FASTAReader
import sys

target = FASTAReader(open(sys.argv[1])) #subset.fa
query = FASTAReader(open(sys.argv[2])) #droYak2_seq.fa
k = int(sys.argv[3])

kmers_from_target = {}

for ident, sequence in target:
  sequence = sequence.upper()
  for i in range(0, len(sequence) - k +1):
      kmer = sequence[i:i+k]
      if kmer in kmers_from_target:
          kmers_from_target[kmer].append((ident,i))
      else:
          kmers_from_target[kmer]=[(ident,i)]

for ident, sequence in query:
  sequence = sequence.upper()
  for i in range(0, len(sequence) - k +1):
      kmer = sequence[i:i+k]
      if kmer in kmers_from_target:
          for ident, j in kmers_from_target[kmer]:
              print(ident, j, i, kmer)