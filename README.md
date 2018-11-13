
A userguide to the PPRCODE server website.

Project site: [PPR Code Prediction Server - From PPR to RNA](http://yinlab.hzau.edu.cn/pprcode/)

**NOTE: This page is still under contruction**

## FAQs

### _Q_: What is PPR and PPR code?
Pentatricopeptide repeat (PPR) proteins constitute a large family whose members serve as single-stranded RNA (ssRNA)-binding proteins; these proteins are particularly abundant in terrestrial plants, as more than 400 members have been identified in Arabidopsis and rice.

PPR proteins are typically characterized by tandem degenerate repeats of a 35-amino acid motif. Within a given repeat, the combinatorial di-residues at the 5th and 35th positions are responsible for specific RNA base recognition. These di-residues are referred to as the **PPR code**. 


### _Q_: What is PPRCODE prediction server?
**PPRCODE** prediction server is aimed to provide services to the PPR community to facilitate PPR code and target RNA prediction. Once a PPR protein sequence is submitted, the server firstly identifies the PPR motifs using the PScan algorithm provided by Prosite, and then outputs the individual PPR motifs that is demarcated based on the PPR structure. PPR code is generally extracted from the 5th and 35th amino acids of each PPR motif, and the best matched RNA base for the PPR code is provided. As a result, the potential RNA target for the PPR sequence is available. 


### _Q_: How do I submit a sequence to the PPRCODE prediction server?

Go to the [PPRCODE prediction server](http://yinlab.hzau.edu.cn/pprcode/) submission form directly and do the following:
  1. Paste your FASTA sequence in the upper text area.
  2. Enter your email address.
  3. Click the Submit button.
 After the submission, the webpage will be automatically refreshed several times until the job is finished. 
 
You may also click the link marked _**"Click here for a sample input sequence"**_ above the sequence area to input a demo.

### _Q_: How long does it take to finish a task?
Less than three minutes.

### _Q_: How many sequences can I submit in one submission?
One sequence per request is recommended. You should always **refresh** the web page before creating another new submission.

### _Q_: How much time do I have before my job is removed in server?
Jobs may be removed **one week after they complete** to conserve disk space, and their result pages will also be unavailable.

### _Q_: What does the prediction result mean?
The result page contains a table like the following:

> This is a demo sequence of PPR10 from *Zea mays*.


Motif Start | Motif End | Motif Sequence | Fifth amino acid | Last amino acid | PPR code | RNA base | Motif Length | ProSite Score
-----|-----|-----|-----|-----|----|----|----|----
138 | 172 | ASALEMVVRALGREGQHDAVCALLDETPLPPGSRL | E | L | EL | ? | 35 | 5.031
174 | 208 | VRAYTTVLHALSRAGRYERALELFAELRRQGVAPT | T | T | TT | A | 35 | 12.989
209 | 244 | LVTYNVVLDVYGRMGRSWPRIVALLDEMRAAGVEPD | N | D | ND | U | 36 | 11.093
245 | 279 | GFTASTVIAACCRDGLVDEAVAFFEDLKARGHAPC | S | C | SC | ? | 35 | 11.411
280 | 314 | VVTYNALLQVFGKAGNYTEALRVLGEMEQNGCQPD | N | D | ND | U | 35 | 12.737
315 | 349 | AVTYNELAGTYARAGFFEEAARCLDTMASKGLLPN | N | N | NN | Y | 35 | 11.477
350 | 384 | AFTYNTVMTAYGNVGKVDEALALFDQMKKTGFVPN | N | N | NN | Y | 35 | 14.096
385 | 419 | VNTYNLVLGMLGKKSRFTVMLEMLGEMSRSGCTPN | N | N | NN | Y | 35 | 10.358
420 | 454 | RVTWNTMLAVCGKRGMEDYVTRVLEGMRSCGVELS | N | S | NS | C | 35 | 9.887
455 | 489 | RDTYNTLIAAYGRCGSRTNAFKMYNEMTSAGFTPC | N | C | NC | U | 35 | 11.674
490 | 524 | ITTYNALLNVLSRQGDWSTAQSIVSKMRTKGFKPN | N | N | NN | Y | 35 | 11.542
525 | 560 | EQSYSLLLQCYAKGGNVAGIAAIENEVYGSGAVFPS | S | S | SS | A | 36 | 6.467
561 | 595 | WVILRTLVIANFKCRRLDGMETAFQEVKARGYNPD | R | D | RD | Y | 35 | 6.445
596 | 630 | LVIFNSMLSIYAKNGMYSKATEVFDSIKRSGLSPD | N | D | ND | U | 35 | 12.419
631 | 666 | LITYNSLMDMYAKCSESWEAEKILNQLKCSQTMKPD | N | D | ND | U | 36 | 8.670
667 | 701 | VVSYNTVINGFCKQGLVKEAQRVLSEMVADGMAPC | N | C | NC | U | 35 | 13.778
702 | 736 | AVTYHTLVGGYSSLEMFSEAREVIGYMVQHGLKPM | H | M | HM | ? | 35 | 10.348
737 | 771 | ELTYRRVVESYCRAKRFEEARGFLSEVSETDLDFD | R | D | RD | Y | 35 | 8.089


**Position**:
> The boundary of each PPR motif.

**Motif Sequences**:
> The detail of PPR motifs sequence.

**PPR-code**:
> Predicted PPR codes.

**RNA**:
> Predicted RNA bases for the corresponding PPR motif. 

### _Q_: Why does the prediction result of my sequence look like a mess?
We identify the sequence and motifs of a PPR protein by its similarity to the general P-type PPR. Sequences with low identity will hardly be predicted. In this circumstance, manual correction is strongly recommended. 

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


