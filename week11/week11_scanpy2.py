#!/usr/bin/env python3

import scanpy as sc
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#Read 10x dataset
adata = sc.read_10x_h5("neuron_10k_v3_filtered_feature_bc_matrix.h5")
#Make variable names (in this case the genes) unique
adata.var_names_make_unique()
sc.pp.filter_genes(adata, min_counts = 1) #only consider genes with more than 1 count
sc.pp.normalize_per_cell(adata, key_n_counts = 'n_counts_all') #normalize with total UMI count per cell
filter_result = sc.pp.filter_genes_dispersion(adata.X, flavor = 'cell_ranger', n_top_genes=1000, log = False)
adata = adata[:, filter_result.gene_subset] #filter genes
sc.pp.normalize_per_cell(adata)  # need to redo normalization after filtering
sc.pp.log1p(adata)
sc.pp.scale(adata)
sc.tl.pca(adata,n_comps=50)
sc.pl.pca(adata)

