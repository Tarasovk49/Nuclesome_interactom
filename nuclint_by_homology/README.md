# Nuclesome_interactom
**Part of a project dedicated to establishment of interactions of human histones and non-nucleosome human proteins.**

Propose interactions of human histones with non-nucleosome human proteins based on homology of these proteins to those derived from emdb and pdb for other species. Human homologues to non-human protein complexes from emdb and pdb pose as potential human interactors to be investigated in future.

## Files
1. *pdb_list.csv* - list of pdb structures containing histones obtained during previous work.
2. *pdb_chain_uniprot.csv* - from [SIFTS](https://www.ebi.ac.uk/pdbe/docs/sifts/quick.html).
3. *human.protein.faa\** - from refseq database of NCBI(ftp://ftp.ncbi.nlm.nih.gov/refseq/H_sapiens/mRNA_Prot/). 4 files to be merged together into *human.protein.faa*.
4. *emdbdumps.xml* - downloaded from [EMDB](https://www.ebi.ac.uk/pdbe/emdb/searchForm.html/) by query 'histone'.
5. *histone_genes.csv* - list of all known human histone genes obtained during previous work.

## Description
### interactions.py
1. For EMDB database download file with structures containing histones and derive pdb identifiers that those structures were adjusted to.
2. Find Uniprot identifiers of proteins listed in pdb structures. We can't use FASTA sequencies from pdb entries directly because they are often incomplete. 
3. Create database based on *human.protein.faa* with all known human genes that is needed for ncbi-blast-2.9.0+.
4. Download FASTA sequences matching Uniprot identifiers.
5. Perform BLAST alignment of FASTA sequences with human genes database and keep accession numbers of best hits.
6. Obtain HGNC gene names by accession numbers using Entrez.
7. Write a table with human genes for each pdb structure.
### wordcloud.py
1. Sort genes from obtained tables according to *histone_genes.csv* on histone and non-histone proteins.
2. Generate two text files with histone and non-histone genes to be used by https://www.wordclouds.com/. Gene letter size is proportional to frequency of according protein being represented in pdb files.

## Dependencies
1. python 3.*
2. [ncbi-blast-2.9.0+](https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/).
3. [Entrez](https://github.com/jordibc/entrez) and [MDAnalysis](https://github.com/MDAnalysis/mdanalysis) libraries. Both are available within the package [Biopython](https://biopython.org/).
