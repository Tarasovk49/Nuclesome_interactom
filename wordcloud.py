# Generate input file for generating word cloud with https://www.wordclouds.com/
# Gene letter size is proportional to frequency of according protein being represented in pdb files

# Select database
database = 'pdb'
#database = 'emdb'

import pandas as pd
with open(database+'_table.csv') as f:
    pdb = pd.read_csv(f, dtype=str)
    
def word_count(input):
    counts = dict()
    words = input
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

with open('histone_genes.csv', 'r') as input:
    histone_genes = pd.read_csv(input, dtype=str, skiprows=1)
histone = pd.DataFrame()
other = pdb

for gene in histone_genes.iloc[:,2]:
    histone = histone.append(pdb.loc[pdb['HGNC'] == gene])
    other = other.loc[other['HGNC'] != gene]

with open('histone_list_' + database + '.txt', 'w') as f:
    if database=='pdb':
        a = word_count(histone.iloc[:,2])
    elif database=='emdb':
        a = word_count(histone.iloc[:,3])
    for key, field in a.items():
        f.write(str(field)+' '+key+'\n')

with open('other_list_' + database + '.txt', 'w') as f:
    if database=='pdb':
        a = word_count(other.iloc[:,2])
    elif database=='emdb':
        a = word_count(other.iloc[:,3])
    for key, field in a.items():
        f.write(str(field)+' '+key+'\n')
