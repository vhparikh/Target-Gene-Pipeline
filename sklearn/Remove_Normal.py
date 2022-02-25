import pandas as pd

# reading data
print('Running tool---')
# get the data
brca = pd.read_csv('Cancers/BRCA.csv')
genes = brca.columns
print(len(genes))
count = 0
print(brca.shape)
print(len(brca[brca['SUBTYPE']=='LumA']))
brca_dropped = brca[brca.SUBTYPE != 'Normal']
print(brca_dropped.shape)
print(len(brca_dropped[brca_dropped['SUBTYPE']=='LumA']))

#for row in iter(brca['SUBTYPE']):
    #if row == 'Normal':
        #print(count)
        #brca = brca.drop(brca.index[count])
    #count += 1
brca_dropped.to_csv('Cancers/BRCA_Dropped.csv', index=False)