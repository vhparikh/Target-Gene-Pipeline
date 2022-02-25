import numpy as np
import matplotlib

import pandas as pd
from matplotlib.patches import Patch
matplotlib.use('tkagg')
import matplotlib.pyplot as plt

import seaborn as sns

print('Start')
data = []
genes = []

first = True

# brca = pd.read_csv('top-genes/brca_top_200_x_matrix.csv')
# brca = brca.drop(columns=['SUBTYPE'])
dataframe = pd.read_csv('BRCA_Subtypes/brca_top_200_x_matrix.csv')
print('loaded')

dataframe = dataframe[dataframe.SUBTYPE != 'Normal']

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
sns_plot = sns.clustermap(data[numerical_cols], xticklabels=False, yticklabels=False, row_colors=row_colors, row_cluster=False,
                          figsize=(15, 10))
sns_plot.savefig("heatmap.pdf")


print('creating legend')
#creating legend
handles = [Patch(facecolor=lut[name]) for name in lut]
plt.legend(handles, lut, title='Subtypes',
           bbox_to_anchor=(0, 0), bbox_transform=plt.gcf().transFigure, loc='lower left', handleheight=2, handlelength=7,
           fontsize=7, title_fontsize='xx-large')

plt.show()