import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import Normalizer, OrdinalEncoder
from sklearn.metrics import plot_confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.metrics import classification_report

# reading data
print('Running tool---')
# get the data
#genes = list(pd.read_csv('top_500_genes_brca.csv')['GENES'])
brca = pd.read_csv('Cancers/BRCA_Dropped.csv.csv')#, usecols=[*genes, 'SUBTYPE'])
subtype_brca = pd.DataFrame(columns=['SUBTYPE'])
subtypes = brca['SUBTYPE']
print(subtypes.unique())
subtype_brca['SUBTYPE'] = subtypes

brca.drop(['SAMPLE_BARCODE', 'DISEASE', 'PIK3CA_snv', 'log10_mut', 'SUBTYPE'], axis=1, inplace=True)


print('Transforming data...')
# Encoding y matrix
enc = OrdinalEncoder()
y_encoded = enc.fit_transform(subtype_brca)
y_encoded = y_encoded.ravel()

print('Y data transformed')

# transforming x matrix
transformer = Normalizer()
x_encoded = transformer.fit_transform(brca)
# print update
print('X data transformed')

x_train, x_test, y_train, y_test = train_test_split(x_encoded, y_encoded, test_size=0.2, random_state=10)
y_test_df = pd.DataFrame

# print update
print('Training model...')

# training model
model = LogisticRegression(solver='sag')
model.fit(x_train, y_train)
print('Model trained')

y_hat = model.predict(x_test)

print(accuracy_score(y_test, y_hat))
labels = ['Luminal A', 'HER2', 'Luminal B', 'Triple-Negative']
print(classification_report(y_test, y_hat, target_names=labels))

#np.random.seed(0)
#X, y = load_iris(return_X_y=True)
#indices = np.arange(y.shape[0])
#np.random.shuffle(indices)
#X, y = X[indices], y[indices]

#train_scores, valid_scores = validation_curve(Ridge(), X, y, param_name="alpha", param_range=np.logspace(-7, 3, 3), cv=5)
#print(train_scores)
#print(valid_scores)

#cm = confusion_matrix(y_test, y_hat)
#print(cm)
#matrix = plot_confusion_matrix(model, x_test, y_test, cmap=plt.cm.Reds, normalize=None)
#matrix.ax_.set_title('Confusion Matrix', color='black')
#plt.xlabel('Predicted Subtype', color='black')
#plt.ylabel('Actual Subtype', color='black')
#plt.gcf().axes[0].tick_params(colors='black')
#plt.gcf().axes[1].tick_params(colors='black')
#plt.gcf().set_size_inches(10, 6)
#plt.rcParams['font.size'] = '30'
#plt.show()


