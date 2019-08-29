#!/usr/bin/env python3
"""match extender"""

from fasta import FASTAReader
import sys

target = FASTAReader(open(sys.argv[1])) #subset.fa
query = FASTAReader(open(sys.argv[2])) #droYak2_seq.fa
k = int(sys.argv[3])

kmers_from_target = {}
target_sequence= {}

for ident, sequence in target:
  sequence = sequence.upper()
  target_sequence[ident]= sequence
  for i in range(0, len(sequence) - k +1):
      kmer = sequence[i:i+k]
      if kmer in kmers_from_target:
          kmers_from_target[kmer].append((ident,i))
      else:
          kmers_from_target[kmer]=[(ident,i)]

elongated_seq= []

for ident, sequence1 in query:
  sequence1 = sequence1.upper()
  for i in range(0, len(sequence) - k +1):
      kmer = sequence1[i:i+k]
      if kmer in kmers_from_target:
          for ident, j in kmers_from_target[kmer]:
              tsequence= target_sequence[ident]
              end = j + k - 1
              end1= i + k - 1
              newtsequence= kmer
              while True:
                  if len(tsequence) - 1 == end:
                      break
                  newtseq = tsequence[end + 1]
                  newseq = sequence[end1 + 1]
                  if newtseq == newseq:
                      end += 1
                      end1 += 1
                      newtsequence += tsequence[end]
                  else:
                      elongated_seq.append(newtsequence)
                      break
for item in sorted(elongated_seq, key= len, reverse= True):
    print (item)

                      
    


               
                
                
            
            
#print (kmers_from_target[kmerquery], str(i1), kmerquery)

    