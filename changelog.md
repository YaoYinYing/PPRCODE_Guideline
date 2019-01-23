#**Changelog of ppr code server main program, version for release**
## v 1.6.0 @ 2019.01.20
###  bugfix
1. exception for no hits. Result from ProSite is shown if no hit is found in a sequence.
2. invalid chars in fasta name are removed before creating xlsx file.


## v 1.5.0 @ 2018.11.09
### features
1. Redesigned email style of PPR CODE SERVER with xlsx format file as attachment
2. Use SSL to encrypt the email transferring pathway.
3. "P" problem of 36aa is solved
4. Threading for multiple sequence, which means every ten sequences can be processed by ProSite
5. The online version of python is changed to py3.
6. Change Email address
7. A job distributor for threading
8. format the project files and directories.
9. inputs and results are encoded before writen into database to prevent insertion.
    
## 1.4 
### 
some other improvements



## v1.3.3 @2018.04.10
### features
1. update the ppr-code table based on the current result.


## v1.3.2 @2018.03.14
### features
1. fix motifi boundary overlap of one amino acid 
2. add global map 
3. insert **[>undefined]** in the first line when the user input one sequence without a fasta format


## v1.3.1 @ 2018.03.07
### features
1. fix motif boundary overlap, although it fails in treating PLS. ProSite does not care about the subtypes at all.
2. remove ";" in result page 
3. update for running page and animation 
4. in urls, "hash=xxx" is replaced by "jobid=xxx" 


## v1.3 @ 2018.02.23
### features:
1. remove score column in result page 
2. fix motif sequence deletion caused by ProSite 


## v1.2.1 @ 2018.02.22
### features:
1. Result website font 
2. Result website table: left alignment of motif sequences 


## v1.2 @ 2018.02.09
### features:
1. score added 


## v1.1 @ 2018.02.08
### Describe: the first online version working with php normally.
#### features:
1. The program directly posts the sequences to ProSite one by one, get the result path, read and refine the matched positions, and return the RNA
2. Email and website results for prediction
3. in result, the positions, motif sequences, PPR codes and matched RNA bases are printed line by line.
4. database-depended in-processing and result display page 



