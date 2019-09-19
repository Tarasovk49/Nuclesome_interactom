# Lab journal

### 19.09.19 Thursday
#### Features of database
**Tables = django classes:**
1. Histone_gene
2. Histone_variant
3. Histone_type
4. Interaction

| PK | Type | Method | Database | Probability |
|:---:|:---:|:---:|:---:|:---:|
|-|-|-|-|-|
5. Interactor_gene

| PK | Gene id | Protein id | Node1 | Node2 |
|:---:|:---:|:---:|:---:|:---:|
|-|-|-|-|-|
6. Classification

| Node | Parent | Rank | Description |
|:---:|:---:|:---:|:---:|
|1|-|0|Interactors|
|2|1|1|Subinteractors1|
|3|1|1|Subinteractors2|
|-|-|-|-|

Must contain methods *Get_parent*, *Get_children*.

7. 3D_interaction
8. 3D_structure
9. PDB_homology
10. DB_info

Plan is to create first six classes - *browse/models.py*.
- *browse/views.py* - generate pages.
- *browse/templates.py* - scaffold of web-pages, where data is uploaded.
- *browse/urls.py* - manage queries.
- *browse/management/commands/buildvariants.py* - functions to rebuild database.

Some basic principles:
- Every table is some kinf of entity - histone genes, interactor genes, interactions between histones and interactors.
- Every table must contain column with unique values - primary key table (PK).
- Any kind of information must not be redundant. It must be stored in single copy.
- Defaults for columns must be specified and columns that cannot be empty must be specified.

### 17.09.19 Tuesday
#### Fixed issues concerning deletion of rows containing no HGNC identifiers for interacting proteins (82 rows out of 2720) for IntAct processing script.
#### H1 histone interactions are now also counted for all databases.

### 13.09.19 Friday
#### [Processing script](IntAct_processing.ipynb) for IntAct rewritten.
#### [Processing script](STRING_processing.ipynb) for STRING rewritten.

### 12.09.19 Thursday
#### [Processing script](BioGRID_processing.ipynb) for BioGRID rewritten.

### 11.09.19 Wednesday
#### Updating scripts for BioGRID, IntAct, STRING are finally written.
They check if a new version of databases are available for download and downloads them if so.
1. [BioGRID](BioGRID_update.ipynb).
2. [IntAct](IntAct_update.ipynb).
3. [STRING](STRING_update.ipynb).
