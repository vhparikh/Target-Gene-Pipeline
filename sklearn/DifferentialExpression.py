import pandas as pd
import numpy as np
from scipy.stats import ttest_ind
import pickle

# reading in data
x_matrix = pd.read_csv("BRCA_Subtypes/brca_top_200_x_matrix.csv")

# getting subtypes and genes
subtypes = x_matrix['SUBTYPE'].unique()
genes = list(x_matrix.columns)[:-1]

# setting variables
df_dict = {}
base_subtype = 'Normal'

# splitting dataframe by subtype
for subtype in subtypes:
    # df = pd.DataFrame()
    df = x_matrix.loc[x_matrix['SUBTYPE'] == subtype]
    df = df.drop(['SUBTYPE'], axis=1)
    filepath = 'BRCA_Subtypes/' + str(subtype) + '_x_matrix.csv'
    df.to_csv(filepath, index=False)
    df_dict[subtype] = df



# calculating fold value and p value for each gene for each subtype
#impact_factor = {}
for subtype in subtypes:
    # setting comparison
    base_gene_samples = df_dict[base_subtype]
    subtype_impact_factor = pd.DataFrame(columns=['GENE', 'FACTOR', 'PVALUE'])
    subtype_gene_samples = df_dict[subtype]
    if subtype == base_subtype:
        continue
    else:
        for gene in genes:
            total_base = 0.0
            total_subtype = 0.0
            base_avg = 0.0
            subtype_avg = 0.0
            factor = 0.0

            gene_p_value = ttest_ind(base_gene_samples[gene], subtype_gene_samples[gene])
            # gets base subtype gene expression sum
            for sample in list(base_gene_samples[gene]):
                total_base = total_base + float(sample)

            # gets subtype gene expression sum
            for sample in list(subtype_gene_samples[gene]):
                total_subtype = total_subtype + float(sample)

            # compares base subtype and subtype gene expressions
            if total_base != float(0) or total_subtype != float(0):
                base_avg = total_base / len(base_gene_samples.index)
                subtype_avg = total_subtype / len(subtype_gene_samples.index)
                factor = base_avg / subtype_avg
                subtype_impact_factor.loc[len(subtype_impact_factor)] = [gene, factor, gene_p_value[1]]
        subtype_impact_factor = subtype_impact_factor.sort_values(by=['PVALUE'], ascending=True)
        top_20_subtype_genes = subtype_impact_factor.head(20)['GENE']
        filepath_genes = 'BRCA_Subtypes/' + str(subtype) + '_top_20.csv'
        filepath_full = 'BRCA_Subtypes/' + str(subtype) + '.csv'
        subtype_impact_factor.to_csv(filepath_full, index=False)
        top_20_subtype_genes.to_csv(filepath_genes, index=False)
#impact_factor_sorted = {}
#for key, value in impact_factor.items():
#    impact_factor_sorted[key] = value.sort_values(by=['PVALUE'], ascending=True)

