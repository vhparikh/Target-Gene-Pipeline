# import statements
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import Normalizer, OrdinalEncoder

# reading data
print('Running tool---')
# get the data
brca = pd.read_csv('Cancers/BRCA.csv')
blca = pd.read_csv('Cancers/BLCA.csv')

# setting subtypes
subtype_brca = brca['SUBTYPE']
subtype_blca = blca['SUBTYPE']
#print(subtype_brca)

# combining diseases
y_matrix = pd.DataFrame()
combined = pd.DataFrame()
combined = pd.concat([blca, brca])

# encoding disease
ones = [1 for i in range(len(blca['DISEASE']))]
twos = [2 for i in range(len(brca['DISEASE']))]

disease = [*ones, *twos]

# Setting y_matrix
y_matrix['DISEASE'] = disease

# dropping columns to form x_matrix
#brca.drop(['SAMPLE_BARCODE', 'log10_mut', 'PIK3CA_snv', 'DISEASE', 'SUBTYPE'], axis=1, inplace=True)
combined.drop(['SAMPLE_BARCODE', 'log10_mut', 'PIK3CA_snv', 'DISEASE', 'SUBTYPE'], axis=1, inplace=True)

print('Transforming data...')
# Encoding y matrix
enc = OrdinalEncoder()
y_encoded = enc.fit_transform(y_matrix)[0:]
y_encoded = y_encoded.ravel()

print('Y data transformed')

# transforming x matrix
transformer = Normalizer()
x_encoded = transformer.fit_transform(combined)
# print update
print('X data transformed')

# splitting data
x_train, x_test, y_train, y_test = train_test_split(x_encoded, y_encoded, test_size=0.3, random_state=10)

# print update
print('Training model...')

# training model
model = LogisticRegression(solver='sag')
model.fit(x_train, y_train)
print('Model trained')

# creating coefficients dataframe
coefficients = pd.DataFrame(columns=['GENE', 'COEFFICIENTS', 'DISEASE'])
coefficients['GENE'] = combined.columns
values = model.coef_

#np.random.seed(0)
#X, y = load_iris(return_X_y=True)
#indices = np.arange(y.shape[0])
#np.random.shuffle(indices)
#X, y = X[indices], y[indices]

#train_scores, valid_scores = validation_curve(Ridge(), X, y, param_name="alpha", param_range=np.logspace(-7, 3, 3), cv=5)
#print(train_scores)
#print(valid_scores)

#training = sns.load_dataset(train_scores)
#sns_plot = sns.lineplot(x="score", y="test", data=train_scores)
#plt.show(sns_plot)

''''
coefficients['COEFFICIENTS'] = list(values[0])

for i in range(8000):
    if coefficients['COEFFICIENTS'][i] > 0:
        coefficients['DISEASE'][i] = 'BREAST'
    else:
        coefficients['DISEASE'][i] = 'BLADDER'
    coefficients['COEFFICIENTS'][i] = abs(coefficients['COEFFICIENTS'][i])

# split coefficients by disease
brca_coefficients = coefficients.loc[coefficients['DISEASE'] == 'BREAST']
blca_coefficients = coefficients.loc[coefficients['DISEASE'] == 'BLADDER']

# sorts coefficients highest to lowest
brca_coefficients = brca_coefficients.sort_values(by=['COEFFICIENTS'], ascending=False)
blca_coefficients = blca_coefficients.sort_values(by=['COEFFICIENTS'], ascending=False)

# isolating top 200 genes
brca_top_200_genes = brca_coefficients.head(200)['GENE']
blca_top_200_genes = blca_coefficients.head(200)['GENE']

#sending gene names to file
brca_top_200_genes.to_csv('top_genes\\brca_top_200_genes.csv', index=False)
blca_top_200_genes.to_csv('top_genes\\blca_top_200_genes.csv', index=False)

# pulling top 200 genes for x matrix
brca_top_200_x_matrix = brca[brca_top_200_genes]
blca_top_200_x_matrix = blca[blca_top_200_genes]

# adding subtype column
brca_top_200_x_matrix['SUBTYPE'] = subtype_brca
blca_top_200_x_matrix['SUBTYPE'] = subtype_blca

#sorting by subtype
brca_top_200_x_matrix = brca_top_200_x_matrix.sort_values(by=['SUBTYPE'], ascending=False)
blca_top_200_x_matrix = blca_top_200_x_matrix.sort_values(by=['SUBTYPE'], ascending=False)

#brca_top_200_x_matrix.drop(['SUBTYPE'], axis=1, inplace=True)
#blca_top_200_x_matrix.drop(['SUBTYPE'], axis=1, inplace=True)

#writing to
brca_top_200_x_matrix.to_csv('top_genes/brca_top_200_x_matrix.csv', index=False)
blca_top_200_x_matrix.to_csv('top_genes/blca_top_200_x_matrix.csv', index=False)
'''''