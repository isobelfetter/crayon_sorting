#!/usr/bin/env python3

import scanpy as sc
import anndata as ad

sc.settings.set_figure_params(dpi=250, facecolor="white")

with open("colors_rgb.txt") as your_data:
    adata = ad.read_csv(your_data, delimiter='\t')

adata.layers["counts"] = adata.X.copy()

#print(sc.datasets.pbmc68k_reduced())

#sc.pp.normalize_total(adata)

sc.tl.pca(adata)

sc.pp.neighbors(adata)

sc.tl.umap(adata) 

sc.tl.leiden(adata, flavor="igraph", n_iterations=2)

sc.pl.umap(adata)

sc.tl.dendrogram(adata)
#sc.pl.dendrogram(adata, groupby='obs_names') figure out adding labels to observations

