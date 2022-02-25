import pandas as pd
from scipy.stats import ttest_ind

mutated = pd.read_csv("mutated.csv")
non_mutated = pd.read_csv("non_mutated.csv")

mutated = mutated.drop(columns=['SAMPLE_BARCODE', 'LGG', 'READ', 'UCS'])
non_mutated = non_mutated.drop(columns=['SAMPLE_BARCODE', 'LGG', 'READ', 'UCS'])

#len non mutated 3384
#mutated 1121

#print(len(mutated.index))
impact_factor = {}

genes = mutated.columns

for gene in genes:
    #print(gene)
    total_mutated = 0.0
    total_nonmutated = 0.0
    mutated_avg = 0.0
    nonmutated_avg = 0.0
    factor = 0.0

    mutated_gene_samples = mutated[gene]
    nonmutated_gene_samples = non_mutated[gene]

    p_value = ttest_ind(mutated_gene_samples, nonmutated_gene_samples)

    for sample in mutated_gene_samples:
        total_mutated = total_mutated + float(sample)

    for sample in nonmutated_gene_samples:
        total_nonmutated = total_nonmutated + float(sample)

    if total_mutated != float(0) or total_nonmutated != float(0):
        mutated_avg = total_mutated/1121
        nonmutated_avg = total_nonmutated/3384
        factor = mutated_avg/nonmutated_avg
        impact_factor[gene] = (factor, p_value[1])

p_threshold = 0.01

print('test')

significant_genes = {}

for gene, stats in impact_factor.items():
    p_value = float(stats[1])
    p_value = "{:.64f}".format(p_value)
    fold = float(stats[0])
    if float(p_value) <= p_threshold and (fold > 2 or fold < 0.5):
        significant_genes[gene] = (stats[0], float(p_value))

print(significant_genes)
print(len(significant_genes))