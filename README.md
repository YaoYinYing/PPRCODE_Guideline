# PPRCODE_Guideline
A userguide of the PPRCODE server website.
**in contruction**

## Introduction
**PPRCODE** server is an approach to PPR code and target RNA sequence predition. It first identifies the PPR motifs in an submitted sequence by PScan algorithm provided by [ProSite](https://prosite.expasy.org/). By the discrepancies between traditional and structural definitions of **PPR motif** and **PPR CODE**, the analysis result is refined to improve the quality of motif detection. After the determination of PPR motif and PPR code, the RNA sequence targeted by the protein is then generated, providing a sequence reference to any researcher interested in the PPR protein with unknow function.

## Required information
**We only requires your protein sequence in FASTA format and your email address.**
However, we would like to gather the sequences and location information for the usage statistics and improvement of this website.

### How do I submit a sequence to the PPRCODE predition server?
The registration of user is not required to the server. To submit your sequence, go to the [PPRCODE server](http://yinlab.hzau.edu.cn/pprcode/) submission form and do the following:
  1. Paste your FASTA sequence in the upper text area.
  2. Enter your email address.
  3. Click the Submit button.
 After the submission, the webpage will be automatically refreshed several times until the job finished. 
 
You may also click the link marked *Click here for a sample input sequence* above the sequence area to input a demo.

### How long does a sequence take to process?
Less than three minutes.

### Is my submission job accessible to others?
Before the submission, an identical job ID is generated to specify your sequence. 

### How much sequence can I submit in one submission?
One sequence per request is recommended. You should **refresh** the web page before submission.

### How much time do I have before my job is removed in server?
Jobs may be removed **one week after they complete** to conserve disk space, and their result pages will also be unavailable.

### 

## Analysis of the result
The result page contains a table like the following:

Positions | Motif Sequences | PPR-code | RNA
----------|-----------------|----------|-----
108-142 | ASALEMVVRALGREGQHDAVCALLDETPLPPGSRL | EL | ?
144-178 | VRAYTTVLHALSRAGRYERALELFAELRRQGVAPT | TT | A
179-213	| VVTYNTLIDGLCKAGKLDEALKLFEEMVEKGIKPD | ND | U



## Troubleshoot

If there is any problem and advice with the website, you are welcome to contact us by [email](mailto:yaoyy@webmail.hzau.edu.cn) 

## Cite information


## 
