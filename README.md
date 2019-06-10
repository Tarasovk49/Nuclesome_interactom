# Nuclesome_interactom
**Part of a project dedicated to establishment of proteins interacting with nucleosomes.**

Establish interactions of human histones with human not-nucleosome proteins based on homology of these proteins to those derived from emdb and pdb for other species. In other words human homologues to non-human protein complexes from emdb and pdb pose as potential human interactors to be investigated in future research.

## Files
1. *pdb_list.csv* - list of pdb structures containing histones generated during previous work
2. *pdb_chain_uniprot.csv* - from [SIFTS](https://www.ebi.ac.uk/pdbe/docs/sifts/quick.html)
3. *human.protein.faa* - from refseq database of [NCBI](ftp://ftp.ncbi.nlm.nih.gov/refseq/H_sapiens/mRNA_Prot/)

## Dependencies
1. python 3.*
2. [ncbi-blast-2.9.0+](https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/).
3. [Entrez](https://github.com/jordibc/entrez) and [MDAnalysis](https://github.com/MDAnalysis/mdanalysis) libraries. Both are available within the package [Biopython](https://biopython.org/).
