
A userguide to the PPRCODE server website.

Project site: [PPR Code Prediction Server - From PPR to RNA](http://yinlab.hzau.edu.cn/pprcode/)

## FAQs

### _Q_: What is PPR and PPR code?
Pentatricopeptide repeat (PPR) proteins constitute a large family whose members serve as single-stranded RNA (ssRNA)-binding proteins; these proteins are particularly abundant in terrestrial plants, as more than 400 members have been identified in Arabidopsis and rice.

PPR proteins are typically characterized by tandem degenerate repeats of a 35-amino acid motif. Within a given repeat, the combinatorial di-residues at the 5th and 35th positions are responsible for specific RNA base recognition. These di-residues are referred to as the **PPR code**. 


### _Q_: What is PPRCODE prediction server?
**PPRCODE** prediction server is aimed to provide services to the PPR community to facilitate PPR code and target RNA prediction. Once a PPR protein sequence is submitted, the server firstly identifies the PPR motifs using the PScan algorithm provided by Prosite, and then outputs the individual PPR motifs that is demarcated based on the PPR structure. PPR code is generally extracted from the 5th and 35th amino acids of each PPR motif, and the best matched RNA base for the PPR code is provided. As a result, the potential RNA target for the PPR sequence is available. 

![PPRCODE Prediction Server: Interface](https://raw.githubusercontent.com/YaoYinYing/PPRCODE_Guideline/master/snipaste20190212_194723.jpg)


### _Q_: How do I submit a sequence to the PPRCODE prediction server?

Go to the [PPRCODE prediction server](http://yinlab.hzau.edu.cn/pprcode/) submission form directly and do the following:
  1. Paste your FASTA sequence in the upper text area.
  2. Enter your email address.
  3. Click the Submit button.
 After the submission, the webpage will be automatically refreshed several times until the job is finished. 
 
You may also click the link marked _**"Click here for a sample input sequence"**_ above the sequence area to input a demo, in which we have prepared a ZmPPR10 and an non-PPR for program testing.

### _Q_: How long does it take to finish a task?
Less than three minutes.

### _Q_: How many sequences can I submit in one submission?
One sequence per request is recommended. You should always **refresh** the web page before creating another new submission.

### _Q_: How much time do I have before my job is removed in server?
Jobs may be removed **one week after they complete** to conserve disk space, and their result pages will also be unavailable.

### _Q_: What does the prediction result mean?
The result page contains a table like the following:

> This is a demo sequence of PPR10 from *Zea mays*.


Motif Start | Motif End | Motif Sequence | Fifth amino acid | Last amino acid | PPR Code | RNA base | Motif Length | ProSite Score
 -----|-----|-----|-----|-----|----|----|----|----
138 | 172 | ASALEMVVRALGREGQHDAVCALLDETPLPPGSRL | E | L | EL | ? | 35 | 5.031
174 | 208 | VRAYTTVLHALSRAGRYERALELFAELRRQGVAPT | T | T | TT | A>G | 35 | 12.989
209 | 244 | LVTYNVVLDVYGRMGRSWPRIVALLDEMRAAGVEPD | N | D | ND | U>C>G | 36 | 11.093
245 | 279 | GFTASTVIAACCRDGLVDEAVAFFEDLKARGHAPC | S | C | SC | ? | 35 | 11.411
280 | 314 | VVTYNALLQVFGKAGNYTEALRVLGEMEQNGCQPD | N | D | ND | U>C>G | 35 | 12.737
315 | 349 | AVTYNELAGTYARAGFFEEAARCLDTMASKGLLPN | N | N | NN | C>U | 35 | 11.477
350 | 384 | AFTYNTVMTAYGNVGKVDEALALFDQMKKTGFVPN | N | N | NN | C>U | 35 | 14.096
385 | 419 | VNTYNLVLGMLGKKSRFTVMLEMLGEMSRSGCTPN | N | N | NN | C>U | 35 | 10.358
420 | 454 | RVTWNTMLAVCGKRGMEDYVTRVLEGMRSCGVELS | N | S | NS | C>U>A | 35 | 9.887
455 | 489 | RDTYNTLIAAYGRCGSRTNAFKMYNEMTSAGFTPC | N | C | NC | U>C>>A | 35 | 11.674
490 | 524 | ITTYNALLNVLSRQGDWSTAQSIVSKMRTKGFKPN | N | N | NN | C>U | 35 | 11.542
525 | 560 | EQSYSLLLQCYAKGGNVAGIAAIENEVYGSGAVFPS | S | S | SS | A | 36 | 6.467
561 | 595 | WVILRTLVIANFKCRRLDGMETAFQEVKARGYNPD | R | D | RD | - | 35 | 6.445
596 | 630 | LVIFNSMLSIYAKNGMYSKATEVFDSIKRSGLSPD | N | D | ND | U>C>G | 35 | 12.419
631 | 666 | LITYNSLMDMYAKCSESWEAEKILNQLKCSQTMKPD | N | D | ND | U>C>G | 36 | 8.67
667 | 701 | VVSYNTVINGFCKQGLVKEAQRVLSEMVADGMAPC | N | C | NC | U>C>>A | 35 | 13.778
702 | 736 | AVTYHTLVGGYSSLEMFSEAREVIGYMVQHGLKPM | H | M | HM | ? | 35 | 10.348
737 | 771 | ELTYRRVVESYCRAKRFEEARGFLSEVSETDLDFD | R | D | RD | - | 35 | 8.089


and finally you will also get a predicted sequence like this:
>(?) (A>G) (U>C>G) (?) (U>C>G) (C>U) (C>U) (C>U) (C>U>A) (U>C>>A) (C>U) (A) (-) (U>C>G) (U>C>G) (U>C>>A) (?) (-)


### _Q_: Why does the prediction result of my sequence look like a mess?
ProSite identifies the sequence and motifs of a PPR protein by its similarity to the general P-type PPR. Sequences with low identity will hardly be predicted. In this circumstance, manual correction is strongly recommended. 

### _Q_: What do the error codes mean?
#### error code: 404
The result is not found in database, which may be deleted, or the submission id contained in address is not complete.
You need to resubmit your sequence, or check the right job id.

#### error code: 500
An internal error occurs in our program. This is often caused by the input sequence or email address. 
**The server only accept sequences in FASTA format.**

## Troubleshoot
If there is any problem and advice with the website, you are welcome to contact us via [email](mailto:yaoyy@webmail.hzau.edu.cn).

## Contributers:
* Yinying Yao
* Zeyuan Guan
* Junjie Yan
* Xiang Wang

## Cite information
Yan Junjie#, Yao Yinying#, Hong Sixing, Yang Yan, Shen Cuicui, Zhang Qunxia, Zhang Delin, Zou Tingting, Yin Ping*. Delineation of pentatricopeptide repeat codes for target RNA prediction, Nucleic Acids Research. 2019 February 11. doi: doi.org/10.1093/nar/gkz075

----

# **Changelog of ppr code server main program, version for release**
## V1.6.10 @2019.04-23
### bug fix
1. Network problem with ProSite.


## V1.6.9 @ 2019.03.22
### bug fix
1. problem btw ajax and submit function of button, which occurs mostly in firefox.
2. repeated job submission caused by some unknown reason. 
3. fail to send email and create result page caused by syntax error in email address. email will be the last now.

## V1.6.8 @ 2019.03.16
### bug fix
1. connection error to ProSite with timeout limit.

## V1.6.7 @ 2019.03.08
### bug fix
1. redirect to error_500 when data is failed to post by ajax. this is often caused by brower version or disabled javascript by users setting.
>I will try post function with cgi.

## V1.6.6 @ 2019.02.21
### features
1. change license to CC BY-NC-SA 4.0

### bug fix
1. exception treatment: raise exception from wrong input. threads will be stopped and the page redirected to 500 error code 

## v1.6.5 @ 2019.02.20
### features
1. add citation and notes to results
2. licensed by CC BY-NC-ND 4.0
## v1.6.2 @ 2019.02.11
### features
1. email for administrator for checking exceptions
2. sequence uploading: save sequence as file to support long input


## v 1.6.1 @ 2019.02.10
### bug fix
1. invalid chars in sequence and fasta name are removed


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
### Description: the first online version working with php normally.
#### features:
1. The program directly posts the sequences to ProSite one by one, get the result path, read and refine the matched positions, and return the RNA
2. Email and website results for prediction
3. in result, the positions, motif sequences, PPR codes and matched RNA bases are printed line by line.
4. database-depended in-processing and result display page 




