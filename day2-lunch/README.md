Question 1

make day2-lunch/SRR072893.10k.fastq
	head -n 40000 SRR072893.fastq > SRR072893.10k.fastq
confirm 40000 lines (10k reads)
	wc -l SRR072893.10k.fastq 

fastqc SRR0772893.10k.fastq

$ hisat2 -p 4 -x BDGP6 -U SRR072893.10k.fastq -S stdout.sam

.sam to .bam
	$ samtools sort -@ 4 stdout.sam -o SRR072893.bam
.bam to .bai
	$ samtools index -b -@ 4 SRR072893.bam SRR072893.10k.bai
	
StringTie on .bam
	stringtie SRR072893.bam -G BDGP6.Ensembl.81.gtf -o SRR072893.10k.gtf -p 4 -e -B
	
Question 3
sort SRR072893.10k.gtf | cut -f 1 | uniq -c > SRR072893.10k.txt

Questions 4
a) samtools view SRR072893.sam | awk '{print NF}' | sort SRR072893.10k.gtf | cut -f 1 | uniq -c > SRR072893.columns
b) the lines with 20+ columns contain alignment scores and other information about the alignment and the lines that have fewer columns might not align to anything aka contain less information.