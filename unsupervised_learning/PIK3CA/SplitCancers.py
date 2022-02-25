import pandas as pd
import numpy as np

x_matrix = pd.read_csv("PIK3CA_X_matrix.tsv", delimiter='\t')
y_matrix = pd.read_csv("PIK3CA_y_matrix.tsv", delimiter='\t', usecols=['SAMPLE_BARCODE', 'DISEASE', 'PIK3CA_snv', 'SUBTYPE'])



mutations = y_matrix['PIK3CA_snv'].to_list()
x_matrix['PIK3CA_snv'] = mutations

diseases = y_matrix['DISEASE']
x_matrix['DISEASE'] = diseases

subtypes = y_matrix['SUBTYPE']
x_matrix['SUBTYPE'] = subtypes

disease_names = ['GBM', 'OV', 'LUAD', 'LUSC', 'PRAD', 'UCEC', 'BLCA', 'ESCA', 'LIHC', 'SARC', 'BRCA', 'COAD', 'STAD', 'SKCM', 'KIRC', 'CESC', 'HNSC', 'READ', 'LGG', 'UCS']

#print(x_matrix.loc[x_matrix['DISEASE'] == 'GBM'].head())

for disease in disease_names:
    df = x_matrix.loc[x_matrix['DISEASE'] == disease]
    filepath = 'Cancers/' + disease + '.csv'
    df.to_csv(filepath, index=False)
