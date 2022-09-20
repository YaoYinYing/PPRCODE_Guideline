
# A userguide to the PPRCODE project.

Original Project site: [PPR Code Prediction Server - From PPR to RNA](http://yinlab.hzau.edu.cn/pprcode/)

## NOTE
This original website is Down.

Please switch to Colab release or docker release or Biolib release.

## Three ways to run PPRCODE
 1. [WebServer from BioLib](https://biolib.com/YaoYinYing/pprcode/); 
 **the [original webserver](http://yinlab.hzau.edu.cn/pprcode/) provided by [Yin Lab](http://yinlab.hzau.edu.cn/) is down and will be no longer maintained.**
 2. [Colab Reimplementation](https://colab.research.google.com/github/YaoYinYing/PPRCODE_Guideline/blob/master/PPRCODE.ipynb)
 3. Docker image

## Run PPRCODE locally in docker
 1. Install docker daemon following the [official getting-started page](https://www.docker.com/get-started/)
 2. Clone this repo
    ```shell
    git clone https://github.com/YaoYinYing/PPRCODE_Guideline
    ```
 3. Create PPRCODE docker image
 
    **from scratch:**
    ```shell
    cd PPRCODE_Guideline
    docker build -f docker/Dockerfile -t pprcode . 
    ```
    **_if you are a victim of GFW, please use the following instead:_**
    ```shell
    docker build -f docker/Dockerfile_asia -t pprcode . --add-host raw.githubusercontent.com:<IP> # consult this IP to a public DNS provider 
    ```
    **or fetch a prebuild image**
    ```shell
    docker pull yaoyinying/pprcode:latest
    ```
 4. Create Conda environment for run this docker image in an instance container
    ```shell
    conda create -y -n pprcode python pip
    conda activate pprcode
    cd <repo>/PPRCODE_Guideline
    pip install -r docker/requirements.txt
    ```
 5. Run `run_docker.py` to an example data
    ```shell
    conda activate pprcode
    mkdir test
    
    # fetch an example dataset 
    wget -qnc http://yinlab.hzau.edu.cn/pprcode/ppr_example.fasta -P test
    
    # use PS_Scan as default program
    python /repo/PPRCODE_Guideline/docker/run_docker.py --fasta test/PPR_example.fasta --save_dir ./save-1  --plot_item=bar,score,edge,ppr,rna
    
    # or use pprfinder provided by Small's Lab
    python  /repo/PPRCODE_Guideline/docker/run_docker.py --fasta test/PPR_example.fasta --save_dir ./save-2 --plot_item=bar,score,edge,ppr,rna --program=pprfinder
    ```
 6. Advance options
    ```shell
    python  /repo/PPRCODE_Guideline/docker/run_docker.py --helpfull
    Docker launch script for PPRCODE docker image.
    flags:
    
    /repo/PPRCODE_Guideline/docker/run_docker.py:
      --bin_dir: Where additional required binaries locate.
        (default: '/app/bin/')
      --[no]debug: debug messages
        (default: 'false')
      --docker_image_name: Name of the PPRCODE Docker image.
        (default: 'pprcode')
      --docker_user: UID:GID with which to run the Docker container. The output directories will be owned by this user:group. By default, this is the current user. Valid options are: uid or uid:gid, non-numeric values
        are not recognised by Docker unless that user has been created within the container.
        (default: '1005:50')
      --fasta: input FASTA file(s) for scan.
      --[no]fix_gap: Fix gap in sequence scanning results. Turn it off so that the results will not be weird.
        (default: 'false')
      --plot_color_scheme: <Accent|Accent_r|Blues|Blues_r|BrBG|BrBG_r|BuGn|BuGn_r|BuPu|BuPu_r|CMRmap|CMRmap_r|Dark2|Dark2_r|GnBu|GnBu_r|Greens|Greens_r|Greys|Greys_r|OrRd|OrRd_r|Oranges|Oranges_r|PRGn|PRGn_r|Paired|Pai
        red_r|Pastel1|Pastel1_r|Pastel2|Pastel2_r|PiYG|PiYG_r|PuBu|PuBuGn|PuBuGn_r|PuBu_r|PuOr|PuOr_r|PuRd|PuRd_r|Purples|Purples_r|RdBu|RdBu_r|RdGy|RdGy_r|RdPu|RdPu_r|RdYlBu|RdYlBu_r|RdYlGn|RdYlGn_r|Reds|Reds_r|Set1|S
        et1_r|Set2|Set2_r|Set3|Set3_r|Spectral|Spectral_r|Wistia|Wistia_r|YlGn|YlGnBu|YlGnBu_r|YlGn_r|YlOrBr|YlOrBr_r|YlOrRd|YlOrRd_r|afmhot|afmhot_r|autumn|autumn_r|binary|binary_r|bone|bone_r|brg|brg_r|bwr|bwr_r|civi
        dis|cividis_r|cool|cool_r|coolwarm|coolwarm_r|copper|copper_r|cubehelix|cubehelix_r|flag|flag_r|gist_earth|gist_earth_r|gist_gray|gist_gray_r|gist_heat|gist_heat_r|gist_ncar|gist_ncar_r|gist_rainbow|gist_rainbo
        w_r|gist_stern|gist_stern_r|gist_yarg|gist_yarg_r|gnuplot|gnuplot2|gnuplot2_r|gnuplot_r|gray|gray_r|hot|hot_r|hsv|hsv_r|inferno|inferno_r|jet|jet_r|magma|magma_r|nipy_spectral|nipy_spectral_r|ocean>: Color
        scheme for plot
        (default: 'RdBu')
      --plot_item: plot PPRCODE results in what ways.
        (default: 'bar,ppr,rna,type,edge')
        (a comma separated list)
      --profile_dir: Where additional required profiles locate.
        (default: '/app/profiles/')
      --program: <ps_scan|pprfinder>: Choose a proper algorithm to process your sequence. PPRCODE use PS_Scan(ps_scan) by default. However, you may use PPRfinder(pprfinder) from Small's Lab
        (default: 'ps_scan')
      --[no]report: Generate a human-friendly report file in xlsx format
        (default: 'true')
      --[no]run_benchmark: Fetch a benchmark dataset. **This could make your job running messy.**
        (default: 'false')
      --save_dir: Path to save run results.
        (default: './results')
    
    absl.app:
      -?,--[no]help: show this help
        (default: 'false')
      --[no]helpfull: show full help
        (default: 'false')
      --[no]helpshort: show this help
        (default: 'false')
      --[no]helpxml: like --helpfull, but generates XML output
        (default: 'false')
      --[no]only_check_args: Set to true to validate args and exit.
        (default: 'false')
      --[no]pdb: Alias for --pdb_post_mortem.
        (default: 'false')
      --[no]pdb_post_mortem: Set to true to handle uncaught exceptions with PDB post mortem.
        (default: 'false')
      --profile_file: Dump profile information to a file (for python -m pstats). Implies --run_with_profiling.
      --[no]run_with_pdb: Set to true for PDB debug mode
        (default: 'false')
      --[no]run_with_profiling: Set to true for profiling the script. Execution will be slower, and the output format might change over time.
        (default: 'false')
      --[no]use_cprofile_for_profiling: Use cProfile instead of the profile module for profiling. This has no effect unless --run_with_profiling is set.
        (default: 'true')
    
    absl.logging:
      --[no]alsologtostderr: also log to stderr?
        (default: 'false')
      --log_dir: directory to write logfiles into
        (default: '')
      --logger_levels: Specify log level of loggers. The format is a CSV list of `name:level`. Where `name` is the logger name used with `logging.getLogger()`, and `level` is a level name  (INFO, DEBUG, etc). e.g.
        `myapp.foo:INFO,other.logger:DEBUG`
        (default: '')
      --[no]logtostderr: Should only log to stderr?
        (default: 'false')
      --[no]showprefixforinfo: If False, do not prepend prefix to info messages when it's logged to stderr, --verbosity is set to INFO level, and python logging is used.
        (default: 'true')
      --stderrthreshold: log messages at this level, or more severe, to stderr in addition to the logfile.  Possible values are 'debug', 'info', 'warning', 'error', and 'fatal'.  Obsoletes --alsologtostderr. Using
        --alsologtostderr cancels the effect of this flag. Please also note that this flag is subject to --verbosity and requires logfile not be stderr.
        (default: 'fatal')
      -v,--verbosity: Logging verbosity level. Messages logged at this level or lower will be included. Set to 1 for debug logging. If the flag was not set or supplied, the value will be changed from the default of -1
        (warning) to 0 (info) after flags are parsed.
        (default: '-1')
        (an integer)
    
    absl.flags:
      --flagfile: Insert flag definitions from the given file into the command line.
        (default: '')
      --undefok: comma-separated list of flag names that it is okay to specify on the command line even if the program does not define a flag with that name.  IMPORTANT: flags in this list that have arguments MUST use
        the --flag=value format.
        (default: '')
    ```


## FAQs

### _Q_: What is PPR and PPR code?
Pentatricopeptide repeat (PPR) proteins constitute a large family whose members serve as single-stranded RNA (ssRNA)-binding proteins; these proteins are particularly abundant in terrestrial plants, as more than 400 members have been identified in Arabidopsis and rice.

PPR proteins are typically characterized by tandem degenerate repeats of a 35-amino acid motif. Within a given repeat, the combinatorial di-residues at the 5th and 35th positions are responsible for specific RNA base recognition. These di-residues are referred to as the **PPR code**. 


### _Q_: What is PPRCODE prediction server?
**PPRCODE** prediction server is aimed to provide services to the PPR community to facilitate PPR code and target RNA prediction. Once a PPR protein sequence is submitted, the server firstly identifies the PPR motifs using the PScan algorithm provided by Prosite, and then outputs the individual PPR motifs that is demarcated based on the PPR structure. PPR code is generally extracted from the 5th and 35th amino acids of each PPR motif, and the best matched RNA base for the PPR code is provided. As a result, the potential RNA target for the PPR sequence is available. 

![PPRCODE Prediction Server: Interface](https://raw.githubusercontent.com/YaoYinYing/PPRCODE_Guideline/master/image/pprcode_biolib.png)


### _Q_: How do I submit a sequence to the PPRCODE prediction server?

Go to the [PPRCODE prediction server in BioLib](https://biolib.com/YaoYinYing/pprcode/) submission form directly and do the following:
  1. Paste your FASTA sequence in the upper text area.
  2. Modify the options if needed.
  3. Click the Run button.
 After the submission, the webpage will be automatically run for several second until the job is finished. 
 
### _Q_: How long does it take to finish a task?
Less than three second for each sequence.

### _Q_: How many sequences can I submit in one submission?
As many as you want.


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
## V1.6.11 @ 2020.03.30
### features
1. Add user map based on pyecharts

## V1.6.10 @ 2019.04.23
### bug fix
1. Network problem with ProSite. Retry the job 3 times at most.
2. Inform users to re-submit their sequences when network exception still occurs in auto-retrying.

### features
1. Attach Result sheet download link to every sequence.
2. Add data properties to workbook.


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




