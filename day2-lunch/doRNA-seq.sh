#!/bin/bash

GENOME=../genomes/genomes/BDGP6.fa
ANNOTATION=BDGP6.Ensembl.81.gtf
THREADS= 4

for SAMPLE in SRR072893 SRR072903 SRR072905 SRR072915
do
  echo "*** Processing $SAMPLE"
  cp ../rawdata/$SAMPLE.fastq .
  fastqc $SAMPLE.fastq
  hisat2 -p 4 -x BDGP6 -U $SAMPLE.fastq -S $SAMPLE.sam
  samtools sort -@ 4 $SAMPLE.sam -o $SAMPLE.bam
  samtools index -b -@ 4 $SAMPLE.bam $SAMPLE.bai
  stringtie $SAMPLE.bam -G BDGP6.Ensembl.81.gtf -o $SAMPLE.gtf -p 4 -e -B
done