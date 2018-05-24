# PPRCODE_Guideline
A userguide of the PPRCODE server website.
**in contruction**

## Introduction
**PPRCODE** server is an approach to PPR code and target RNA sequence predition. It first identifies the PPR motifs in an submitted sequence by PScan algorithm provided by [ProSite](https://prosite.expasy.org/). By the discrepancies between traditional and structural definitions of **PPR motif** and **PPR CODE**, the analysis result is refined to improve the quality of motif detection. After the determination of PPR motif and PPR code, the RNA sequence targeted by the protein is then generated, providing a sequence reference to any researcher interested in the PPR proteins with unknown function.

## Required information
**We only requires your protein sequence in FASTA format and your email address.**
However, we would like to gather the sequences and location information for the usage statistics and improvement of this website.

## FAQs
### _Q_: How do I submit a sequence to the PPRCODE predition server?

The registration of user is not required to the server. To submit your sequence, go to the [PPRCODE server](http://yinlab.hzau.edu.cn/pprcode/) submission form and do the following:
  1. Paste your FASTA sequence in the upper text area.
  2. Enter your email address.
  3. Click the Submit button.
 After the submission, the webpage will be automatically refreshed several times until the job is finished. 
 
You may also click the link marked _**"Click here for a sample input sequence"**_ above the sequence area to input a demo.

### _Q_: How long does a sequence take to process?
Less than three minutes.

### _Q_: Is my submission job accessible to others?
Before the submission, an identical job ID is generated to specify your sequence. The job is invisible without the job ID.

### _Q_: How much sequences can I submit in one submission?
One sequence per request is recommended. You should always **refresh** the web page before submission.

### _Q_: How much time do I have before my job is removed in server?
Jobs may be removed **one week after they complete** to conserve disk space, and their result pages will also be unavailable.

## Analysis of the result
The result page contains a table like the following:

> This is a demo sequence of PPR.


Positions | Motif Sequences | PPR-code | RNA
----------|-----------------|----------|-----
108-142 | ASALEMVVRALGREGQHDAVCALLDETPLPPGSRL | EL | ?
144-178 | VRAYTTVLHALSRAGRYERALELFAELRRQGVAPT | TT | A
179-213 | VVTYNTLIDGLCKAGKLDEALKLFEEMVEKGIKPD | ND | U
214-248 | VVTYNTLIDGLCKAGKLDEALKLFEEMVEKGIKPD | ND | U
249-283 | VVTYNTLIDGLCKAGKLDEALKLFEEMVEKGIKPD | ND | U
284-318 | VVTYNTLIDGLCKAGKLDEALKLFEEMVEKGIKPD | ND | U
319-353 | VVTYNTLIDGLCKAGKLDEALKLFEEMVEKGIKPD | ND | U
354-388 | VVTYNTLIDGLCKAGKLDEALKLFEEMVEKGIKPD | ND | U
389-423 | VVTYNTLIDGLCKAGKLDEALKLFEEMVEKGIKPD | ND | U
424-458 | VVTYNTLIDGLCKAGKLDEALKLFEEMVEKGIKPD | ND | U
459-493 | VVTYNTLIDGLCKAGKLDEALKLFEEMVEKGIKPD | ND | U
494-528 | VVTYNTLIDGLCKAGKLDEALKLFEEMVEKGIKPD | ND | U
529-563 | ELTYRRVVESYCRAKRFEEARGFLSEVSETDLDFD | RD | Y

**Position**:
> The boundary of every PPR motif refined on the bases of structural and functional research result.

**Motif Sequences**:
> The detail of PPR motifs sequence.

**PPR-code**:
> Predicted PPR codes.

**RNA**:
> Predicted RNA bases the PPR code may conbined with.

## Troubleshoot

If there is any problem and advice with the website, you are welcome to contact us via [email](mailto:yaoyy@webmail.hzau.edu.cn).

## Contributers:
* Yinying Yao
* Zeyuan Guan
* Junjie Yan
* Xiang Wang

## Cite information


## 
