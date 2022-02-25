import pandas as pd

basal = pd.read_excel('(Basal) enrichment.xlsx', usecols = ['term description', 'strength', 'false discovery rate'])
her2 = pd.read_excel('(HER2) enrichment.xlsx', usecols = ['term description', 'strength', 'false discovery rate'])
luma = pd.read_excel('(LumA) enrichment.xlsx', usecols = ['term description', 'strength', 'false discovery rate'])
lumb = pd.read_excel('(LumB) enrichment.xlsx', usecols = ['term description', 'strength', 'false discovery rate'])

basal_pathways = basal['term description']
her2_pathways = her2['term description']
luma_pathways = luma['term description']
lumb_pathways = lumb['term description']

print(basal_pathways)

#basal.set_index('term description')
#her2.set_index('term description')
#luma.set_index('term description')
#lumb.set_index('term description')

all_pathways = pd.concat([basal_pathways, her2_pathways, luma_pathways, lumb_pathways])
unique_pathways = list(all_pathways.unique())

combined_df = pd.DataFrame(columns=['PATHWAY','BASALSTRENGTH', 'BASALFDR', 'HER2STRENGTH', 'HER2FDR', 'LUMASTRENGTH', 'LUMAFDR', 'LUMBSTRENGTH', 'LUMBFDR'])
combined_df['PATHWAY'] = unique_pathways
#combined_df.set_index('PATHWAY')

print(basal.head())

print(basal['strength'][20])

for pathway in unique_pathways:
    pathway_index = list(unique_pathways).index(pathway)
    if pathway in list(basal_pathways):
        basal_index = list(basal_pathways).index(pathway)
        combined_df.at[pathway_index, 'BASALSTRENGTH'] = basal['strength'][basal_index]
        combined_df.at[pathway_index, 'BASALFDR'] = basal['false discovery rate'][basal_index]
    if pathway in list(her2_pathways):
        her2_index = list(her2_pathways).index(pathway)
        combined_df.at[pathway_index, 'HER2STRENGTH'] = her2['strength'][her2_index]
        combined_df.at[pathway_index, 'HER2FDR'] = her2['false discovery rate'][her2_index]
    if pathway in list(luma_pathways):
        luma_index = list(luma_pathways).index(pathway)
        combined_df.at[pathway_index,'LUMASTRENGTH'] = luma['strength'][luma_index]
        combined_df.at[pathway_index, 'LUMAFDR'] = luma['false discovery rate'][luma_index]
    if pathway in list(lumb_pathways):
        lumb_index = list(lumb_pathways).index(pathway)
        combined_df.at[pathway_index, 'LUMBSTRENGTH'] = lumb['strength'][lumb_index]
        combined_df.at[pathway_index, 'LUMBFDR'] = lumb['false discovery rate'][lumb_index]

#combined_df.to_csv('uniquepathways.csv')
print(combined_df.head())
