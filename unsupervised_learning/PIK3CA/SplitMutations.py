import pandas as pd
print('Reading Data')

x_matrix_cancer = pd.DataFrame
x_matrix_cancer = pd.read_csv("x_matrix_cancer.csv")

diseases = ['GBM', 'OV', 'LUAD', 'LUSC', 'PRAD', 'UCEC', 'BLCA', 'ESCA', 'LIHC', 'SARC', 'BRCA', 'COAD', 'STAD', 'SKCM', 'KIRC', 'CESC', 'HNSC', 'READ', 'LGG', 'UCS']

print(x_matrix_cancer.xs('GBM'))

#mutated = pd.DataFrame
#non_mutated = pd.DataFrame

#for disease in diseases:
    #df = x_matrix_cancer.xs(disease)
    #print(df.head())

#print('Data Read, Splitting Data')
#mutated = x_matrix_cancer.loc[x_matrix_cancer['PIK3CA_snv'] == 1]
#non_mutated = x_matrix_cancer.loc[x_matrix_cancer['PIK3CA_snv'] == 0]

#mutated = mutated.drop(columns=['log10_mut', 'PIK3CA_snv'])
#non_mutated = non_mutated.drop(columns=['log10_mut', 'PIK3CA_snv'])
#print(mutated.head())

#print('Writing Data')
#mutated.to_csv('mutated.csv', index=False)
#non_mutated.to_csv('non_mutated.csv', index=False)
