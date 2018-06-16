# PPRCODE prediction server - Guideline
A userguide to the PPRCODE server website.

Project site: [PPR Code Prediction Server - From PPR to RNA](http://yinlab.hzau.edu.cn/pprcode/)

**NOTE: This page is in contruction**

## FAQs

### _Q_: What is PPR and PPR code?
Pentatricopeptide repeat (PPR) proteins constitute a large family whose members serve as single-stranded RNA (ssRNA)-binding proteins; these proteins are particularly abundant in terrestrial plants, as more than 400 members have been identified in Arabidopsis and rice.

PPR proteins are typically characterized by tandem degenerate repeats of a 35-amino acid motif. Within a given repeat, the combinatorial di-residues at the 5th and 35th positions are responsible for specific RNA base recognition, which is consistent with bioinformatics studies. These di-residues are referred to as the **PPR code**. 


### _Q_:What is PPRCODE prediction server?
**PPRCODE** prediction server is an approach to PPR code and target RNA sequence predition. It first identifies the PPR motifs in an submitted sequence by PScan algorithm provided by [ProSite](https://prosite.expasy.org/). By the discrepancies between traditional and structural definitions of **PPR motif** and **PPR CODE**, the analysis result is refined to improve the quality of motif detection. After the determination of PPR motif and PPR code, the RNA sequence targeted by the protein is then generated, providing a sequence reference to any researcher interested in the PPR proteins with unknown function.


### _Q_: How do I submit a sequence to the PPRCODE prediction server?

The registration of user is not required to the server. To submit your sequence, go to the [PPRCODE prediction server](http://yinlab.hzau.edu.cn/pprcode/) submission form and do the following:
  1. Paste your FASTA sequence in the upper text area.
  2. Enter your email address.
  3. Click the Submit button.
 After the submission, the webpage will be automatically refreshed several times until the job is finished. 
 
You may also click the link marked _**"Click here for a sample input sequence"**_ above the sequence area to input a demo.

### _Q_: How long does a sequence take to process?
Less than three minutes.

### _Q_: Is my submission job accessible to others?
Before the submission, an identical job ID is generated to specify your sequence. The job is invisible without the job ID.

### _Q_: How many sequences can I submit in one submission?
One sequence per request is recommended. You should always **refresh** the web page before creating another new submission.

### _Q_: How much time do I have before my job is removed in server?
Jobs may be removed **one week after they complete** to conserve disk space, and their result pages will also be unavailable.

### _Q_: What does the prediction result mean to me?
The result page contains a table like the following:

> This is a demo sequence of PPR10 from *Zea maize*.


Positions | Motif Sequences | PPR-code | RNA
----------|-----------------|----------|-----
138-172 | ASALEMVVRALGREGQHDAVCALLDETPLPPGSRL | EL | ?
174-208 | VRAYTTVLHALSRAGRYERALELFAELRRQGVAPT | TT | A
209-244 | LVTYNVVLDVYGRMGRSWPRIVALLDEMRAAGVEPD | ND | U
245-279 | GFTASTVIAACCRDGLVDEAVAFFEDLKARGHAPC | SC | ?
280-314 | VVTYNALLQVFGKAGNYTEALRVLGEMEQNGCQPD | ND | U
315-349 | AVTYNELAGTYARAGFFEEAARCLDTMASKGLLPN | NN | Y
350-384 | AFTYNTVMTAYGNVGKVDEALALFDQMKKTGFVPN | NN | Y
385-419 | VNTYNLVLGMLGKKSRFTVMLEMLGEMSRSGCTPN | NN | Y
420-454 | RVTWNTMLAVCGKRGMEDYVTRVLEGMRSCGVELS | NS | C
455-489 | RDTYNTLIAAYGRCGSRTNAFKMYNEMTSAGFTPC | NC | Y
490-524 | ITTYNALLNVLSRQGDWSTAQSIVSKMRTKGFKPN | NN | Y
525-559 | EQSYSLLLQCYAKGGNVAGIAAIENEVYGSGAVFP | SP | ?
561-595 | WVILRTLVIANFKCRRLDGMETAFQEVKARGYNPD | RD | Y
596-630 | LVIFNSMLSIYAKNGMYSKATEVFDSIKRSGLSPD | ND | U
631-665 | LITYNSLMDMYAKCSESWEAEKILNQLKCSQTMKP | NP | ?
667-701 | VVSYNTVINGFCKQGLVKEAQRVLSEMVADGMAPC | NC | Y
702-736 | AVTYHTLVGGYSSLEMFSEAREVIGYMVQHGLKPM | HM | ?
737-771 | ELTYRRVVESYCRAKRFEEARGFLSEVSETDLDFD | RD | Y


**Position**:
> The boundary of every PPR motif refined on the bases of structural and functional research result.

**Motif Sequences**:
> The detail of PPR motifs sequence.

**PPR-code**:
> Predicted PPR codes.

**RNA**:
> Predicted RNA bases which the PPR codes may conbined with.

### _Q_: Why the PPR code and RNA prediction result of my sequence looks like a mess?
We identify the sequence and motifs of a PPR protein by its similarity to the general P-type PPR. Sequences with low identity will hardly be predicted. So it is recommended to make your own manual correction of the analysis result if there still exist problems. 
The program cannot make everything as perfect as we wish to.

### _Q_: What do the error pages mean?
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


## 
