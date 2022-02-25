import matplotlib
import pandas as pd
import numpy as np
from matplotlib.patches import Patch
matplotlib.use('tkagg')
import matplotlib.pyplot as plt

import seaborn as sns

print('Start')
data = []
genes = []

first = True

basal = pd.read_csv('Basal_top_20.csv')['GENE']
her2 = pd.read_csv('Her2_top_20.csv')['GENE']
luma = pd.read_csv('LumA_top_20.csv')['GENE']
lumb = pd.read_csv('LumB_top_20.csv')['GENE']

basal_x_matrix = pd.read_csv('Basal_x_matrix.csv')
her2_x_matrix = pd.read_csv('Her2_x_matrix.csv')
luma_x_matrix = pd.read_csv('LumA_x_matrix.csv')
lumb_x_matrix = pd.read_csv('LumB_top_20.csv')

all_subtypes = pd.concat([basal, her2, luma, lumb])
unique_genes = all_subtypes.unique()
unique_genes = list(unique_genes)
all_genes = basal_x_matrix.columns
#print(len(unique_genes))

dataframe = pd.read_csv('brca_top_200_x_matrix.csv', usecols=[*unique_genes, 'SUBTYPE'])
dataframe = dataframe[dataframe.SUBTYPE != 'Normal']
print(len(unique_genes))
print('loaded')
subtype = dataframe['SUBTYPE']
print(subtype.unique())

# reformatting data
for index, row in dataframe.iterrows():
    if first:
        sample_names = row[1:]
        first = False

    else:
        genes.append(row[0])
        data.append(row[1:])

# creating dataframe
data = pd.DataFrame(data)

subtype_list = list(subtype)
#print(subtype_list.index('Normal'))
print(subtype_list.index('LumB'))
print(subtype_list.index('LumA'))
print(subtype_list.index('Her2'))
print(subtype_list.index('Basal'))

# getting gene columns
columns = data.columns
numerical_cols = list(columns)[:-1]

lut = dict(zip(subtype.unique(), ['Salmon', 'MediumAquamarine', 'Green', 'DeepSkyBlue']))
row_colors = subtype.map(lut)

# creating heatmap
print('creating heatmap')
sns.set_context("paper", font_scale=1.3)
sns_plot = sns.clustermap(data[numerical_cols], xticklabels=unique_genes, yticklabels=False, row_colors=row_colors, row_cluster=False,
                          figsize=(15, 10))
sns_plot.savefig("heatmap.pdf")

print('creating legend')
#creating legend
handles = [Patch(facecolor=lut[name]) for name in lut]
plt.legend(handles, lut, title='Subtypes',
           bbox_to_anchor=(0, 0), bbox_transform=plt.gcf().transFigure, loc='lower left', handleheight=1, handlelength=7,
           fontsize=7, title_fontsize='xx-large')

plt.show()
