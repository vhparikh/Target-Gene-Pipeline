import pandas as pd
import numpy as np
import random as rd
from sklearn.decomposition import PCA
from sklearn import preprocessing
import matplotlib.pyplot as plt  # NOTE: This was tested with matplotlib v. 2.1.0

#########################
#
# Data Generation Code
#
#########################
## In this example, the data is in a data frame called data.
## Columns are individual samples (i.e. cells)
## Rows are measurements taken for all the samples (i.e. genes)
## Just for the sake of the example, we'll use made up data...
x_matrix = pd.read_csv('BRCA_Dropped.csv')
samples = x_matrix['SAMPLE_BARCODE']
subtypes = x_matrix['SUBTYPE']
x_matrix['SUBTYPE'] = subtypes

unique_subtypes = x_matrix['SUBTYPE'].unique()
subtypes_encoded = []
for subtype in subtypes:
    subtypes_encoded.append(list(unique_subtypes).index(subtype))
print(unique_subtypes)
print(subtypes_encoded)
colormap = np.array(['#7f5e00', 'b', 'g', 'r', 'c', 'm', 'y', 'w', 'k', 'aquamarine', 'mediumseagreen', '#ff81c0',
                     '#ae7181', '#7a9703', '#89fe05', '#ceb301', '#5a86ad', '#ffb07c', '#650021', '#6f828a'])


#poke_data = pd.read_csv('pandas-master/pokemon_data.csv')
combined = x_matrix.drop(columns=['SAMPLE_BARCODE', 'log10_mut', 'SUBTYPE', 'DISEASE'])
# print(blca_data.head())
a = combined.columns
genes = a.to_list()
print(genes)

#########################
#
# Perform PCA on the data
#
#########################
# First center and scale the data
scaled_data = preprocessing.scale(combined)

pca = PCA()  # create a PCA object
pca.fit(scaled_data)  # do the math
pca_data = pca.transform(scaled_data)  # get PCA coordinates for scaled_data

#########################
#
# Draw a scree plot and a PCA plot
#
#########################

# The following code constructs the Scree plot
per_var = np.round(pca.explained_variance_ratio_ * 100, decimals=1)
labels = ['PC' + str(x) for x in range(1, len(per_var) + 1)]

plt.bar(x=range(1, len(per_var) + 1), height=per_var, tick_label=labels)
plt.ylabel('Percentage of Explained Variance')
plt.xlabel('Principal Component')
plt.title('Scree Plot')
plt.show()

# the following code makes a fancy looking plot using PC1 and PC2
pca_df = pd.DataFrame(pca_data, index=[*subtypes], columns=labels)

plt.scatter(pca_df.PC1, pca_df.PC2, c=colormap[subtypes_encoded])
plt.title('My PCA Graph')
plt.xlabel('PC1 - {0}%'.format(per_var[0]))
plt.ylabel('PC2 - {0}%'.format(per_var[1]))

# for sample in pca_df.index:
# plt.annotate(sample, (pca_df.PC1.loc[sample], pca_df.PC2.loc[sample]))

plt.show()

#########################
#
# Determine which genes had the biggest influence on PC1
#
#########################

## get the name of the top 10 measurements (genes) that contribute
## most to pc1.
## first, get the loading scores
loading_scores = pd.Series(pca.components_[0], index=subtypes)
## now sort the loading scores based on their magnitude
sorted_loading_scores = loading_scores.abs().sort_values(ascending=False)

# get the names of the top 10 genes
top_10_genes = sorted_loading_scores[0:10].index.values

## print the gene names and their scores (and +/- sign)
print(loading_scores[top_10_genes])
