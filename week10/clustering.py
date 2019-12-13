#!/usr/bin/env python3

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, leaves_list
from sklearn.cluster import KMeans
import scipy.stats as sp

hema = open(sys.argv[1]) #hema_data.txt

df = pd.read_csv(hema, sep = "\t", index_col = 0)

linky=linkage(df, method='average', metric='euclidean')
leafy=leaves_list(linky)

trans_df=df.transpose()
linky2=linkage(trans_df, method='average', metric='euclidean')
leafy2=leaves_list(linky2)

df2= df.iloc[leafy,:]
df3=df2.iloc[:, leafy2]

'''HEATMAP CODE'''
#fig, ax=plt.subplots()
#plt.pcolor(df2)

#plt.xticks(np.arange(0.5, len(df3.columns), 1), df3.columns)
#ax.set_ylabel("Genes")
#ax.set_xlabel("Cell Type")


'''DENDROGRAM CODE'''
#fig, ax=plt.subplots()
#ax= dendrogram(linky2, truncate_mode="lastp", labels=trans_df.index, leaf_rotation=90)


'''K MEANS CODE'''
cfu=df["CFU"].values
poly=df["poly"].values
the_data={'x' : cfu, 'y' : poly}
kmeans_df=pd.DataFrame(the_data, columns=['x','y'])

kmeans=KMeans(n_clusters=5).fit(kmeans_df)
centroids= kmeans.cluster_centers_

#fig, ax=plt.subplots()
#plt.scatter(kmeans_df['x'], kmeans_df['y'], c= kmeans.labels_.astype(float), s=50, alpha=0.5)
#plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
#ax.set_ylabel("CFU")
#ax.set_xlabel("poly")

#fig.tight_layout()
#fig.savefig("heatmap_sorted.png")
#fig.savefig("hema_dendrogram.png")
#fig.savefig("kmeans_cfu_vs_poly.png")
#plt.close(fig)
#plt.show()


# diff_exp_high = ((df['mys'] + df['unk'])/2)/((df['poly'] + df['int'])/2) >= 2
# diff_exp_low = ((df['mys'] + df['unk'])/2)/((df['poly'] + df['int'])/2) <= 0.5
#
# diff_exp_genes = df[diff_exp_high | diff_exp_low]
# #print(diff_exp_genes)
# for gene_name, row in diff_exp_genes.iterrows():
#     sample1 = [row['mys'], row['unk']]
#     sample2 = [row['poly'], row['int']]
#
#     if sp.ttest_rel(sample1, sample2).pvalue <= 0.05:
#         print(gene_name,sp.ttest_rel(sample1, sample2).pvalue)

labels = list(kmeans.labels_)
genes = list(df.index.values)

#Pisd-ps3= the differentially expressed gene
goi_index = genes.index(sys.argv[2])
goi_cluster = labels[goi_index]

related_genes = []
for i, gene in enumerate(genes):
    if labels[i] == goi_cluster:
        related_genes.append(gene)
        
for gene in related_genes:
    print(gene)