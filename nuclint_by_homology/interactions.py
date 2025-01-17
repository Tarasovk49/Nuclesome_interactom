# Script works both for PDB and EMDB entries. Select the one here
database = 'pdb'
#database = 'emdb'

# Read list of pdbs and file with uniprot identifiers
import pandas as pd
import xmltodict
# emdbdumps.xml is the output for emdb query 'histone'
with open('emdbdumps.xml') as f:
    result = xmltodict.parse(f.read(), dict_constructor=dict)
emdb_list = []
entryid_list = []
for field in result['EMDBEntries']['Entry']:
    try:
        emdb_list.append(field['FittedPDBs']['PDB'])
        entryid_list.append(field['EntryID'])
    except:
        continue

with open('pdb_list.csv') as f:
    pdb_list = f.read().splitlines() 

lists = {'pdb':pdb_list, 'emdb':emdb_list}

with open('pdb_chain_uniprot.csv') as f:
    pdb_uniprot = pd.read_csv(f, dtype=str, skiprows=1)

# Find Uniprot identifiers of proteins listed in pdb
uniprotdict = {}
chaindict = {}
for key in lists[database]:
    uniprotdict[key] = pdb_uniprot.loc[pdb_uniprot['PDB'] == key.lower()]['SP_PRIMARY'].tolist()
    chaindict[key] = pdb_uniprot.loc[pdb_uniprot['PDB'] == key.lower()]['CHAIN'].tolist()

# Create database with all known human genes
import os
os.system('rm -f human.protein.faa')
os.system('cat human.protein.faa* > human.protein.faa')
faa_file = 'human.protein.faa'
db_name = 'human_protdb'
os.system('ncbi-blast-2.9.0+/bin/makeblastdb -dbtype prot -in %s -out %s > /dev/null'%(faa_file,db_name))

# Download FASTA sequences matching Uniprot identifiers
os.system('rm -f ' + database + '_fastas')
os.system('mkdir ' + database + '_fastas')
for key in lists[database]:
    for field in uniprotdict[key]:
        os.system('wget -P ./' + database + '_fastas/ -nv http://www.uniprot.org/uniprot/%s.fasta'%(field))
os.system('rm ' + database + '_fastas/*.fasta.*')

# Align those FASTA sequences across human genes database and keep accession numbers of best hits
from Bio.Blast.Applications import NcbiblastpCommandline
from Bio.Blast import NCBIXML

os.system('rm -f ' + database + '_blasts')
os.system('mkdir ' + database + '_blasts')
accession_dict = {}
for key in lists[database]:
    accession_dict[key] = list()
    for field in uniprotdict[key]:
        xml_file = database + '_blasts/%s_blast.xml'%(field)
        query_seq = database + '_fastas/' + field + '.fasta'
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

# Derive HGNC gene names by accession numbers
from Bio import Entrez
import numpy as np
import xmltodict
# Register on NCBI site and get your api_key
Entrez.api_key = "your_api_key"
Entrez.email = "your@mail.xyz"

HGNC_dict = {}
for key, value in accession_dict.items():
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

# Write a table with human genes for each pdb\emdb structure
if database=='pdb':
    with open('pdb_table.csv','w') as f:
        f.write('PDB,Chain,HGNC\n')
        for key, value in chaindict.items():
            for i, field in enumerate(value):
                f.write(key+','+field+','+HGNC_dict[key][i]+'\n')
elif database=='emdb':
    with open('emdb_table.csv','w') as f:
        f.write('EMDB,PDB,Chain,HGNC\n')
        for key, value in chaindict.items():
            for i, field in enumerate(value):
                f.write(entryid_list[i]+','+key+','+field+','+HGNC_dict[key][i]+'\n')
