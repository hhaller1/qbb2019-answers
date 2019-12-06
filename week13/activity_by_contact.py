#!/usr/bin/env python2

import sys
import hifive
import numpy



activity= open(sys.argv[1]) #chr10_activity_binned.bed
rna= open(sys.argv[2]) #chr10_rna_binned.bed

# rnal= {}
rnal= [0] * 7000
# activityl= {}
activityl= [0] * 7000

for i, line in enumerate(rna):
    if i == 0:
        continue
    col = line.rstrip("\n").split("\t")
    if int(col[1]) >= 5000000 and int(col[2])<=40000000:
        index = (int(col[2])-5000000)/5000
        rnal[index] = float(col[4])

for i, line in enumerate(activity):
    if i == 0:
        continue
    col = line.rstrip("\n").split("\t")
    if int(col[1]) >= 5000000 and int(col[2])<=40000000:
        index = (int(col[2])-5000000)/5000
        activityl[index] = float(col[4])

rnaa= numpy.array(rnal)
activitya=numpy.array(activityl)
         
hic = hifive.HiC('PROJECT', 'r')
data = hic.cis_heatmap(chrom='chr10', start=5000000, stop=40000000, binsize=5000, datatype='fend', arraytype='full')
where = numpy.where(data[:, :, 1] > 0)
data[where[0], where[1], 0] /= data[where[0], where[1], 1]
data = numpy.log(data[:, :, 0] + 0.1)
data -= numpy.amin(data)


data_subset=data[numpy.where(rnaa > 0), :]
sum_data_subset= numpy.sum(data_subset, axis=1)
R= numpy.corrcoef(sum_data_subset, rnaa)[0, 1]
print(R)