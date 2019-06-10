import pandas as pd
with open('pdblist.csv') as f:
    pdblist = f.read().splitlines()
with open('pdb_chain_uniprot.csv') as f:
    pdb_uniprot = pd.read_csv(f, dtype=str, skiprows=1)

uniprotdict = {}
chaindict = {}
for key in pdblist:
    uniprotdict[key] = pdb_uniprot.loc[pdb_uniprot['PDB'] == key.lower()]['SP_PRIMARY'].tolist()
    chaindict[key] = pdb_uniprot.loc[pdb_uniprot['PDB'] == key.lower()]['CHAIN'].tolist()

import os
faa_file = 'human.protein.faa'
db_name = 'human_protdb'
os.system('ncbi-blast-2.9.0+/bin/makeblastdb -dbtype prot -in %s -out %s > /dev/null'%(faa_file,db_name))

for key in tqdm_notebook(pdblist):
    for field in uniprotdict[key]:
        os.system('wget -P ./pdb_fastas/ -nv http://www.uniprot.org/uniprot/%s.fasta'%(field))
os.system('rm pdb_fastas/*.fasta.*')

from Bio.Blast.Applications import NcbiblastpCommandline
from Bio.Blast import NCBIXML

accession_dict = {}
for key in tqdm_notebook(pdblist):
    accession_dict[key] = list()
    for field in uniprotdict[key]:
        xml_file = 'pdb_blasts/%s_blast.xml'%(field)
        query_seq = 'pdb_fastas/' + field + '.fasta'
        blastp_cline = NcbiblastpCommandline(query=query_seq, db=db_name, evalue=100, outfmt=5, out=xml_file)
        stdout, stderr = blastp_cline()
        blast_record = NCBIXML.read(open(xml_file,'r'))
        sname = list()
        hsp_list = list()
        evalue = list()
        for alignment in blast_record.alignments:
            for hsp in alignment.hsps:
                sname.append(alignment.title)
                evalue.append(hsp.expect)
                hsp_list.append(hsp)
        best_hit = sname[evalue.index(min(evalue))].split()[1]
        accession_dict[key].append(best_hit)

from Bio import Entrez
import numpy as np
import xmltodict

Entrez.api_key = "e22265ce0c29b0b382624371a6ebcfefb108"
Entrez.email = "tarasovk49@gmail.com"

HGNC_dict = {}
for key, value in tqdm_notebook(accession_dict.items()):
    HGNC_dict[key] = []
    for field in value:
        handle = Entrez.efetch(db="protein", id=field, retmode="xml")
        result = xmltodict.parse(handle.read(), dict_constructor=dict)
        handle.close()
        string_1 = result['GBSet']['GBSeq']['GBSeq_feature-table']['GBFeature']
        for substring in string_1:
            if substring['GBFeature_key'] == 'CDS':
                sub_substring = substring['GBFeature_quals']['GBQualifier']
                for field in sub_substring:
                    if field['GBQualifier_name'] == 'gene':
                        HGNC_dict[key].append(field['GBQualifier_value'])

with open('pdb_table.csv','w') as f:
    f.write('PDB,Chain,HGNC\n')
    for key, value in chaindict.items():
        for i, field in enumerate(value):
            f.write(key+','+field+','+HGNC_dict[key][i]+'\n')
