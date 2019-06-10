# Nuclesome_interactom
**Part of a project dedicated to establishment of proteins interacting with nucleosomes.**

Establish interactions of human histones with human not-nucleosome proteins based on homology of these proteins to those derived from emdb and pdb for other species. In other words human homologues to non-human protein complexes from emdb and pdb pose as potential human interactors to be investigated in future research.

## Files
1. *pdb_list.csv* - list of pdb structures containing histones generated during previous work.
2. *pdb_chain_uniprot.csv* - from [SIFTS](https://www.ebi.ac.uk/pdbe/docs/sifts/quick.html).
3. *human.protein.faa* - from refseq database of [NCBI](ftp://ftp.ncbi.nlm.nih.gov/refseq/H_sapiens/mRNA_Prot/). All 7 files merged together.
4. *emdbdumps.xml* - downloaded from [EMDB](https://www.ebi.ac.uk/pdbe/emdb/searchForm.html/) by query 'histone'.

## Description 
1. For EMDB database download file with structures containing histones and derive pdb identifiers that those structures were adjusted to.
2. Find Uniprot identifiers of proteins listed in pdb structures. We can't use FASTA sequencies from pdb entries directly because they are often incomplete. 
3. Create database based on *human.protein.faa* with all known human genes that is needed for ncbi-blast-2.9.0+.
4. Download FASTA sequences matching Uniprot identifiers.
5. Perform BLAST alignment of FASTA sequences with human genes database and keep accession numbers of best hits.
6. Derive HGNC gene names by accession numbers.
7. Write a table with human genes for each pdb structure.

## Dependencies
1. python 3.*
2. [ncbi-blast-2.9.0+](https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/).
3. [Entrez](https://github.com/jordibc/entrez) and [MDAnalysis](https://github.com/MDAnalysis/mdanalysis) libraries. Both are available within the package [Biopython](https://biopython.org/).
