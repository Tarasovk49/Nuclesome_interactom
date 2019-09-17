# Nuclesome_interactom
**Database of histone-protein interactions**

Data about interactions is retrieved from 3 databases: IntAct, STRING, BioGRID. There are scripts that check if database has been updated from the latest download and if so download the new set of data.
[IntAct_update](IntAct_update.ipynb)
[STRING_update](STRING_update.ipynb)
[BioGRID_update](BioGRID_update.ipynb)
There are also processing scripts for those 3 databases that excludes from database the rows which don't represent histone-protein interactions.
[IntAct_processing](IntAct_processing.ipynb)
[STRING_processing](STRING_processing.ipynb)
[BioGRID_processing](BioGRID_processing.ipynb)
