import pandas as pd

basal = pd.read_excel('(Basal) enrichment.xlsx', usecols = ['term description', 'strength', 'false discovery rate', 'matching proteins in your network (labels)'])
her2 = pd.read_excel('(HER2) enrichment.xlsx', usecols = ['term description', 'strength', 'false discovery rate', 'matching proteins in your network (labels)'])
luma = pd.read_excel('(LumA) enrichment.xlsx', usecols = ['term description', 'strength', 'false discovery rate', 'matching proteins in your network (labels)'])
lumb = pd.read_excel('(LumB) enrichment.xlsx', usecols = ['term description', 'strength', 'false discovery rate', 'matching proteins in your network (labels)'])

pathways_df = pd.read_csv('uniquepathways_colored.csv')

basal_pathways = basal['term description']
her2_pathways = her2['term description']
luma_pathways = luma['term description']
lumb_pathways = lumb['term description']

pathways = pathways_df['PATHWAY']
pathways_df['BASALGENES'] = ''
pathways_df['HER2GENES'] = ''
pathways_df['LUMAGENES'] = ''
pathways_df['LUMBGENES'] = ''
print(pathways)
for pathway in pathways:
    pathway_index = list(pathways).index(pathway)
    if pathway in list(basal_pathways):
        basal_index = list(basal_pathways).index(pathway)
        pathways_df.at[pathway_index, 'BASALGENES'] = basal['matching proteins in your network (labels)'][basal_index]
    if pathway in list(her2_pathways):
        her2_index = list(her2_pathways).index(pathway)
        pathways_df.at[pathway_index, 'HER2GENES'] = her2['matching proteins in your network (labels)'][her2_index]
    if pathway in list(luma_pathways):
        luma_index = list(luma_pathways).index(pathway)
        pathways_df.at[pathway_index,'LUMAGENES'] = luma['matching proteins in your network (labels)'][luma_index]
    if pathway in list(lumb_pathways):
        lumb_index = list(lumb_pathways).index(pathway)
        pathways_df.at[pathway_index, 'LUMBGENES'] = lumb['matching proteins in your network (labels)'][lumb_index]
pathways_df.to_csv('pathways_genes.csv', index=False)
print(pathways_df.head())