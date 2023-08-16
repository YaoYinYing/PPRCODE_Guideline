# @title Install packages
from __future__ import division

import glob
import os
import pathlib
import pickle
import re
import tempfile
import time

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import xlsxwriter as xw
from Bio import SeqIO
from absl import app
from absl import flags
from absl import logging
from dna_features_viewer import GraphicFeature, GraphicRecord


# updated at 2018/12/20 for pulication, experimentally validated.
code2rna_multi = {"ND": "U>C>G", "NN": "C>U", "TD": "G>A>U", "SD": "G>>C", "TN": "A>G", "SN": "A", "NS": "C>U>A",
                  "NT": "C>U", "GN": "A>C", "TS": "A>G", "GD": "G", "TT": "A>G", "RD": "-", "SS": "A", "AD": "G",
                  "KD": "-", "ST": "A", "NE": "U>C", "DS": "-", "CD": "G", "DD": "-", "NG": "C>U>A", "AN": "A>>U",
                  "GS": "-", "ES": "-", "LD": "-", "SG": "A>G", "GT": "C", "HD": "-", "CN": "A>>G", "VD": "G",
                  "ID": "-", "SE": "-", "NC": "U>C>>A", "AS": "-", "RS": "-", "MD": "-", "NK": "C>U", "NL": "C",
                  "DT": "-", "RN": "-", "TG": "A>>G", "GG": "-", "LN": "-", "LS": "-", "VN": "A", "TE": "G", "SP": "-",
                  "KN": "C>U", "NR": "-", "DN": "C", "CS": "A", "QD": "-", "NV": "C>U", "ED": "-", "IN": "-",
                  "VS": "-", "HN": "-", "AT": "-", "NH": "U>C", "AG": "-", "NI": "C", }

BENCHMARK_DATA = 'https://raw.githubusercontent.com/YaoYinYing/PPRCODE_Guideline/main/ATPPR.fasta'

# PS_scan setting
PS_MOTIF = 'PS51375'

banner = '''
!           _          _          _            _             _            _            _      
!          /\ \       /\ \       /\ \        /\ \           /\ \         /\ \         /\ \    
!         /  \ \     /  \ \     /  \ \      /  \ \         /  \ \       /  \ \____   /  \ \   
!        / /\ \ \   / /\ \ \   / /\ \ \    / /\ \ \       / /\ \ \     / /\ \_____\ / /\ \ \  
!       / / /\ \_\ / / /\ \_\ / / /\ \_\  / / /\ \ \     / / /\ \ \   / / /\/___  // / /\ \_\ 
!      / / /_/ / // / /_/ / // / /_/ / / / / /  \ \_\   / / /  \ \_\ / / /   / / // /_/_ \/_/ 
!     / / /__\/ // / /__\/ // / /__\/ / / / /    \/_/  / / /   / / // / /   / / // /____/\    
!    / / /_____// / /_____// / /_____/ / / /          / / /   / / // / /   / / // /\____\/    
!   / / /      / / /      / / /\ \ \  / / /________  / / /___/ / / \ \ \__/ / // / /______    
!  / / /      / / /      / / /  \ \ \/ / /_________\/ / /____\/ /   \ \___\/ // / /_______\   
!  \/_/       \/_/       \/_/    \_\/\/____________/\/_________/     \/_____/ \/__________/   
!                                                                                                                                                                                    
!                         Reimplemented by Yinying Yao (github.com/YaoYinYing)                                                                    
'''

citations_banner = '''
**If you find this tool useful to your research, please cite the following**:

- [PPRCODE (whether webserver, notebook or related standalone script)](https://doi.org/10.1093/nar/gkz075) and its required packages([BioPython](https://doi.org/10.1093/bioinformatics/btp163), [Dna Features Viewer](https://doi.org/10.1093/bioinformatics/btaa213), [Matplotlib](https://doi.org/10.1109/MCSE.2007.55)).
- Use default algorithm [PS_scan](https://doi.org/10.1093/nar/gkl124) with [Prosite profile](https://doi.org/10.1093/nar/gks1067) operated by Swiss Institute of Bioinformatics.
- Use optional algorithm [PPRfinder](https://doi.org/10.1016/j.molp.2019.11.002) from Small's lab and its required [HMMER](http://hmmer.org/publications.html) package developed by Eddy's lab.
'''

flags.DEFINE_string(
  'fasta', None, 'input FASTA file(s) for scan.')
flags.DEFINE_enum(
  'program', 'ps_scan', ['ps_scan', 'pprfinder'],
  'Choose a proper algorithm to process your sequence. PPRCODE use PS_Scan(ps_scan) by default. However, you may use PPRfinder(pprfinder) from Small\'s Lab')
flags.DEFINE_string(
  'bin_dir', '/app/bin/', 'Where additional required binaries locate.')
flags.DEFINE_string(
  'profile_dir', '/app/profiles/', 'Where additional required profiles locate.')
flags.DEFINE_bool(
  'report', True, 'Generate a human-friendly report file in xlsx format')
flags.DEFINE_string(
  'save_dir', './results', 'Path to save run results.')
flags.DEFINE_enum(
  'plot_color_scheme', 'RdBu',
  ['Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap',
   'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r',
   'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r',
   'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples',
   'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r',
   'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia',
   'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot',
   'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r',
   'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix',
   'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat',
   'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r',
   'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r',
   'hsv', 'hsv_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'nipy_spectral', 'nipy_spectral_r',
   'ocean'],
  'Color scheme for plot')
flags.DEFINE_list(
  'plot_item', ['bar', 'ppr', 'rna', 'type', 'edge'], 'plot PPRCODE results in what ways.')

flags.DEFINE_bool(
  'run_benchmark', False, 'Fetch a benchmark dataset. **This could make your job running messy.**')

flags.DEFINE_bool(
  'debug', False, 'debug messages')

flags.DEFINE_bool(
  'fix_gap', False, 'Fix gap in sequence scanning results. Turn it off so that the results will not be weird.')

FLAGS = flags.FLAGS


def ps_scan(sequence, RES_DIR_SCAN, profile_dir, bin_dir, fix_gap):
  """
  Run PS_Scan on the given sequence.

  Parameters:
  sequence (SeqRecord): The sequence to scan.
  RES_DIR_SCAN (str): The directory to save the scan results.
  profile_dir (str): The directory containing the Prosite profile.
  bin_dir (str): The directory containing the PS_Scan binary.
  fix_gap (bool): Whether to fix gaps in the sequence scanning results.

  Returns:
  list: A list of SeqRecord objects representing the PPR motifs found in the sequence.
  """
  logging.debug(sequence.id)
  with tempfile.NamedTemporaryFile(suffix=f'_{sequence.id}.fasta', delete=True) as tmp_fasta_file:
    SeqIO.write(sequence, tmp_fasta_file.name, "fasta")
    ps_out_file = f"{RES_DIR_SCAN}/{sequence.id}_PPR_PSSCAN_pff.log"
    cmd = f"perl {bin_dir}/ps_scan/ps_scan.pl -e {sequence.id} -p {PS_MOTIF} -o pff -d {profile_dir}/prosite.dat {tmp_fasta_file.name} | sort -n -k 2 > {ps_out_file}"
    os.system(cmd)
    ps_out_file_scan = f"{RES_DIR_SCAN}/{sequence.id}_PPR_PSSCAN_scan.log"
    cmd = f"perl {bin_dir}/ps_scan/ps_scan.pl -e {sequence.id} -p {PS_MOTIF} -o scan -d {profile_dir}/prosite.dat {tmp_fasta_file.name} | sort -n -k 2 > {ps_out_file_scan}"
    os.system(cmd)
    try:
      # this is totally bullshit but working
      result_response_pff = open(ps_out_file, 'r').read()
      matchpos = re.findall(r'(\d+)\t(\d+)\t%s' % PS_MOTIF, result_response_pff)
      refinedpos = [[], []]


      match_motif = []

      # get original match motifs
      for pos in matchpos:
        mypos = sequence[int(pos[0]) - 1:int(pos[1])]
        mypos.id = f'{sequence.id}_{int(pos[0]) - 1}_{pos[1]}'
        match_motif.append(mypos)

      logging.debug(match_motif)
      # find the motif sequence deletion by ProSite and refine the positions

      result_response_scan = open(ps_out_file_scan, 'r').read()
      for origin_motif, origin_pos in zip([str(x.seq) for x in match_motif], matchpos):
        try:
          logging.debug(origin_motif)
          if fix_gap:
            motif_delete_find = re.findall(r'' + origin_motif + '(-+)', result_response_scan)[0]
          else:
            motif_delete_find = ''
          logging.debug(
            f"orginal Motif= {origin_motif}\t motif deletion={motif_delete_find}\t deletion length={len(motif_delete_find)}")
          refinedpos[0].append(int(origin_pos[0]))

          # V1.3.1 solve the motif boundary overlap
          if (len(refinedpos[1]) > 0 and refinedpos[1][-1] > refinedpos[0][-1]):
            logging.debug(
              f"==>refine pos 0 = {refinedpos[0][-1]}\t refine pos 1 = {refinedpos[1][-1]}")
            refinedpos[1][-1] = refinedpos[0][-1]
            logging.debug(
              f"-->refine pos 0 = {refinedpos[0][-1]}\t refine pos 1 = {refinedpos[1][-1]}")

          refinedpos[1].append(int(origin_pos[1]) + 1 + len(motif_delete_find))

        except Exception as e:
          logging.debug(f"original Motif= {origin_motif}\t motif deletion= deletion not found.")
          refinedpos[0].append(int(origin_pos[0]))
          refinedpos[1].append(int(origin_pos[1]) + 1)

      # the second round of refinement of position: the conserved "P" and the 36 aa length motif  # the conserved "P" label is based on weblogo results
      # Eureka!
      refindpos_end_2nd = []
      try:
        pos_index = 0
        for refinedpos_start_slide, refinedpos_end_slide in zip(refinedpos[0], refinedpos[1]):
          logging.debug(f"refined pos[{pos_index}]: {refinedpos_start_slide} -> {refinedpos_end_slide}")
          logging.debug(sequence[refinedpos_start_slide:refinedpos_end_slide])
          logging.debug(f"Scanning the {pos_index + 1}/{refinedpos[0].__len__()} motif...")
          if pos_index < (refinedpos[0].__len__() - 1):
            try:
              if (refinedpos[0][pos_index + 1] - refinedpos[1][
                pos_index] == 1 and
                  sequence[refinedpos_start_slide:refinedpos_end_slide][-1] == "P"):
                logging.debug("Find P!")
                logging.debug(len(sequence[refinedpos_start_slide:refinedpos_end_slide]))
                logging.debug(sequence[refinedpos_start_slide:refinedpos_end_slide][-1])
                refindpos_end_2nd.append(refinedpos_end_slide + 1)
                pass
              else:
                logging.debug("No P find!")
                refindpos_end_2nd.append(refinedpos_end_slide)
            except:
              refindpos_end_2nd.append(refinedpos_end_slide)
          elif pos_index == (refinedpos[0].__len__() - 1):
            if sequence[refinedpos_start_slide:refinedpos_end_slide][-1] == "P":
              logging.debug("Find P in the last motif...")
              logging.debug(len(sequence[refinedpos_start_slide:refinedpos_end_slide]))
              logging.debug(sequence[refinedpos_start_slide:refinedpos_end_slide][-1])
              refindpos_end_2nd.append(refinedpos_end_slide + 1)

            else:
              logging.debug("No P find in the last motif...")
              refindpos_end_2nd.append(refinedpos_end_slide)
          pos_index += 1
      except Exception as e:
        logging.error("Oops! Something wrong happens with the following sequence!")
        logging.error(f"--->{sequence.id}")
        logging.error(e)
      finally:
        logging.debug(refindpos_end_2nd)

      logging.debug(match_motif)
      logging.debug(refinedpos)

      # extract motifs scores according to the match positions
      motif_score = []

      for line in open(ps_out_file, 'r'):
        motif_score.append(float(line.split("\t")[-2]))
      logging.debug(motif_score)

      parsed_ppr = []
      for pos_start, pos_end, score in zip(refinedpos[0], refindpos_end_2nd, motif_score):
        mypos = sequence[pos_start:pos_end]
        mypos.id = f'{sequence.id}'
        mypos.annotations = {
          "PS_SCORE": score,
          "PPR_STARTS": pos_start + 1,
          "PPR_ENDS": pos_end,
          "FIFTH_AA": sequence[pos_start + 4],
          "LAST_AA": sequence[pos_end - 1],
          "PPR_CODE": sequence[pos_start + 4] + sequence[pos_end - 1],
          "RNA_BASE": code2rna_multi[sequence[pos_start + 4] + sequence[pos_end - 1]]
          if sequence[pos_start + 4] + sequence[pos_end - 1] in code2rna_multi.keys() else '?',
        }
        parsed_ppr.append(mypos)

      return parsed_ppr
    except Exception as e:
      logging.error("Oops! Something wrong happens with the following sequence!")
      logging.error(f"--->{sequence.id}")
      logging.error(e)


def pprfinder(sequence, RES_DIR_FIND, profile_dir, bin_dir, ):
  """
  Run PPRfinder on the given sequence.

  Parameters:
  sequence (SeqRecord): The sequence to scan.
  RES_DIR_FIND (str): The directory to save the find results.
  profile_dir (str): The directory containing the PPRfinder profile.
  bin_dir (str): The directory containing the PPRfinder binary.

  Returns:
  list: A list of SeqRecord objects representing the PPR motifs found in the sequence.
  """
  logging.debug(sequence.id)
  with tempfile.NamedTemporaryFile(suffix=f'_{sequence.id}.fasta', delete=True) as tmp_fasta_file:
    SeqIO.write(sequence, tmp_fasta_file.name, "fasta")

    # run scanning
    hmmsearch_out_file = pathlib.Path(f"{RES_DIR_FIND}/{sequence.id}_PPR_HMMSEARCH.domt").resolve()

    # recommended setting from Small's Lab. see https://github.com/ian-small/OneKP
    cmd_1 = f"hmmsearch --domtblout {hmmsearch_out_file} --noali -E 0.1 --cpu 2 {profile_dir}/all_PPR.hmm {tmp_fasta_file.name} > /dev/null"
    os.system(cmd_1)
    cmd_2 = f"java -jar {bin_dir}/PPRfinder.jar {tmp_fasta_file.name} {pathlib.Path(hmmsearch_out_file).resolve()} > /dev/null"
    os.system(cmd_2)

    # expected output: f'{}{s.id}_PPR_HMMSEARCH.domt_motifs.txt'}
    ppr_df = pd.read_table(f'{RES_DIR_FIND}/{sequence.id}_PPR_HMMSEARCH.domt_motifs.txt',
                           names=['id', 'start', 'end', 'score', 'motif_seq', 'second', 'fifth_aa', 'last_aa',
                                  'motif_type'])
    logging.debug(ppr_df)
    parsed_ppr = []
    for pos_start, pos_end, score, motif_type, fifth, last, motif_seq in zip(ppr_df.start, ppr_df.end, ppr_df.score,
                                                                             ppr_df.motif_type, ppr_df.fifth_aa,
                                                                             ppr_df.last_aa, ppr_df.motif_seq):
      mypos = sequence[pos_start:pos_end]
      mypos.id = f'{sequence.id}'
      mypos.annotations = {
        "PPR_TYPE": motif_type,
        "PS_SCORE": score,
        "PPR_STARTS": pos_start,
        "PPR_ENDS": pos_end,
        "FIFTH_AA": fifth,
        "LAST_AA": last,
        "PPR_CODE": fifth + last,
        "RNA_BASE": code2rna_multi[fifth + last] if fifth + last in code2rna_multi.keys() else '?',
      }
      parsed_ppr.append(mypos)

  return parsed_ppr


def renormalize(n, range1, range2):
  """
  Renormalize a number from one range to another.

  Parameters:
  n (float): The number to renormalize.
  range1 (tuple): The original range.
  range2 (tuple): The new range.

  Returns:
  float: The renormalized number.
  """
  delta1 = range1[1] - range1[0]
  delta2 = range2[1] - range2[0]
  return (delta2 * (n - range1[0]) / delta1) + range2[0]


def draw_my_ppr(s, ppr, features, cmap, scores, program, fixed_plot_width, RES_DIR_FIGURE):
  """
  Draw a plot of the PPR motifs in the sequence.

  Parameters:
  s (SeqRecord): The sequence.
  ppr (list): A list of SeqRecord objects representing the PPR motifs.
  features (list): A list of features to include in the plot.
  cmap (Colormap): The colormap to use for the plot.
  scores (list): A list of scores for the PPR motifs.
  program (str): The program used to find the PPR motifs.
  fixed_plot_width (int): The fixed width of the plot.
  RES_DIR_FIGURE (str): The directory to save the figure.

  Returns:
  None
  """
  draw_features = {
    'Motif': [
      GraphicFeature(start=a, end=b, color=cmap(renormalize(float(c), [min(scores), max(scores)], [0, 1])),
                     strand=+1,
                     label=d) for p in ppr for a, b, c, d in
      zip([p.annotations["PPR_STARTS"]], [p.annotations["PPR_ENDS"]], [p.annotations["PS_SCORE"]],
          [p.annotations["PPR_CODE"]])],
    'RNA': [GraphicFeature(start=a, end=b, color=cmap(renormalize(float(c), [min(scores), max(scores)], [0, 1])),
                           strand=+1,
                           label=d) for p in ppr for a, b, c, d in
            zip([p.annotations["PPR_STARTS"]], [p.annotations["PPR_ENDS"]], [p.annotations["PS_SCORE"]],
                [p.annotations["RNA_BASE"]])],
    'Score': [
      GraphicFeature(start=a, end=b, color=cmap(renormalize(float(c), [min(scores), max(scores)], [0, 1])),
                     strand=+1,
                     label=str(d)) for p in ppr for a, b, c, d in
      zip([p.annotations["PPR_STARTS"]], [p.annotations["PPR_ENDS"]], [p.annotations["PS_SCORE"]],
          [p.annotations["PS_SCORE"]])],
    'Edge': [
      GraphicFeature(start=a, end=b, color=cmap(renormalize(float(c), [min(scores), max(scores)], [0, 1])),
                     strand=+1,
                     label="-".join([str(a), str(b)])) for p in ppr for a, b, c in
      zip([p.annotations["PPR_STARTS"]], [p.annotations["PPR_ENDS"]], [p.annotations["PS_SCORE"]])],
    'Type': [
      GraphicFeature(start=a, end=b, color=cmap(renormalize(float(c), [min(scores), max(scores)], [0, 1])),
                     strand=+1,
                     label=str(d)) for p in ppr for a, b, c, d in
      zip([p.annotations["PPR_STARTS"]], [p.annotations["PPR_ENDS"]], [p.annotations["PS_SCORE"]],
          [p.annotations["PPR_TYPE"]])] if program == "PPRfinder" else [],
  }

  title = {'Motif': 'PPR Motif',
           'RNA': 'RNA bases',
           'Score': f'{program} Score',
           'Edge': 'Motif Edge',
           'Type': 'Type'}
  for feature in features:

    record = GraphicRecord(sequence_length=len(s.seq), features=draw_features[feature])
    ax, _ = record.plot(figure_width=fixed_plot_width if fixed_plot_width != 0 else len(s.seq) / 20)

    ax.set_title(f"{title[feature]}: {s.id}", loc='left', weight='bold')
    ax.figure.savefig(f'{RES_DIR_FIGURE}/{feature}-{s.id}.png')


def generate_full_report(RES_DIR_PICKLE, RES_DIR_REPORT, plot_feature, program):
  """
  Generate a full report of the PPR motifs found in all sequences.

  Parameters:
  RES_DIR_PICKLE (str): The directory containing the pickled PPR motifs.
  RES_DIR_REPORT (str): The directory to save the report.
  plot_feature (list): A list of features to include in the plot.
  program (str): The program used to find the PPR motifs.

  Returns:
  None
  """
  pkls_files = glob.glob(f'{RES_DIR_PICKLE}/*.pkl')
  process_id = time.strftime("%Y%m%d_%H%M%S", time.localtime())
  xlsx_filename = f"{RES_DIR_REPORT}/PPRCODE_RESULTS_{process_id}.xlsx"
  test_book = xw.Workbook(xlsx_filename)

  # set workbook property
  test_book.set_properties({
    'title': 'PPRCODE PREDICTION',
    'subject': 'https://github.com/YaoYinYing/PPRCODE_Guideline',
    'author': 'PPRCODE project',
    'manager': 'Yan et al.',
    'comments': 'Created with PPRCODE project.'})

  total = len(pkls_files)

  report_md_write_handle = open(f'{RES_DIR_REPORT.parent}/PPRCODE_results.md', 'w')

  report_md_write_handle.write(f'# PPRCODE Report\n'
                               f'_created at {time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime())}_\n\n')

  report_md_write_handle.write(f'## Summary\n'
                               f'**Sequence Number**: {total}\n\n'
                               f'**Program**: {program}\n\n')

  report_md_write_handle.write(f'## Details of Results\n')

  for pf in pkls_files:
    try:
      data = pickle.load(open(pf, 'rb'))
      motif_starts = [x.annotations["PPR_STARTS"] for x in data]
      motif_ends = [x.annotations["PPR_ENDS"] for x in data]
      motif_sequence = [str(x.seq) for x in data]
      fifth_code = [x.annotations["FIFTH_AA"] for x in data]
      last_code = [x.annotations["LAST_AA"] for x in data]
      ppr_code = [x.annotations["PPR_CODE"] for x in data]
      rna_base = [x.annotations["RNA_BASE"] for x in data]
      motif_length = [len(str(x.seq)) for x in data]
      motif_score = [x.annotations["PS_SCORE"] for x in data]
      motif_type = [x.annotations["PPR_TYPE"] for x in data] if program == 'PPRfinder' else ['' for x in data]
      data_list = [[a, b, c, d, e, f, g, h, i, j]
                   for a, b, c, d, e, f, g, h, i, j in zip(
          motif_starts,
          motif_ends,
          motif_sequence,
          fifth_code,
          last_code,
          ppr_code,
          rna_base,
          motif_length,
          motif_score,
          motif_type)]
      seq_id = pathlib.Path(pf).resolve().stem
      try:
        write_excel_tables(test_book=test_book, sequence_name=seq_id, ppr_total_list_reversed=data_list,
                           program=program)
        report_md_write_handle.write(f'### {seq_id}\n'
                                     f'#### Table\n'
                                     f'Start | End | Sequence | #5  | #35 | PPR Code | RNA base | Length | Score | Type \n'
                                     '----  |-----|   :---   | ---- | ---- | ----  |  ----  | ---- |  ---- | ---- \n')
        for motif_info in data_list:
          report_md_write_handle.write(f"{' | '.join([str(x) for x in motif_info])}\n")

        report_md_write_handle.write(f'\n#### Plots\n')
        report_md_write_handle.write(f'![Colorbar](figure/Colorbar-{program}.png)\n')
        for feature in plot_feature:
          report_md_write_handle.write(f'![{feature}-{seq_id}](figure/{feature}-{seq_id}.png)\n')
        report_md_write_handle.write('\n\n')
      except Exception as e:
        logging.error("Oops! Something wrong happens when writing in to excel report!")
        logging.error(seq_id)
        logging.error(e)


    except Exception as e:
      logging.error("Oops! Something wrong happens when loading pickle file!")
      logging.error(seq_id)
      logging.error(e)

  report_md_write_handle.write(f'---\n\n'
                               f'**End of the report**\n\n'
                               f'## Citation\n'
                               f'Yan Junjie#, Yao Yinying#, Hong Sixing, Yang Yan, Shen Cuicui, Zhang Qunxia, '
                               f'Zhang Delin, Zou Tingting, Yin Ping*. Delineation of pentatricopeptide repeat '
                               f'codes for target RNA prediction, Nucleic Acids Research. '
                               f'2019 February 11. doi: doi.org/10.1093/nar/gkz075\n\n')

  logging.info("All jobs are accomplished.")
  test_book.close()


def write_excel_tables(test_book, sequence_name, ppr_total_list_reversed, program):
  """
  Write the PPR motifs of a sequence to an Excel workbook.

  Parameters:
  test_book (Workbook): The Excel workbook.
  sequence_name (str): The name of the sequence.
  ppr_total_list_reversed (list): A list of PPR motifs in reverse order.
  program (str): The program used to find the PPR motifs.

  Returns:
  None
  """
  # reversed ppr code result list for making xlsx file

  code_count_result_name = f"PPR motifs and PPR codes: {sequence_name}"
  format_title = test_book.add_format()
  format_content = test_book.add_format()
  format_title.set_font("Times New Roman")
  format_title.set_font_size(11)
  format_title.set_bold()
  format_title.set_bottom(2)

  format_content.set_font("Times New Roman")
  format_content.set_font_size(11)
  sheet_name = sequence_name
  for c in "[]:*?/\\+@!^'{}()|#%&~`\"":
    sheet_name = sheet_name.replace(c, "_")
  worksheet = test_book.add_worksheet(sheet_name)
  worksheet.set_column(0, 1, 10)
  worksheet.set_column(2, 2, 50)
  worksheet.set_column(3, 8, 10)

  worksheet.write(0, 0, code_count_result_name, format_title)
  for n in range(1, 9):
    worksheet.write(0, n, "", format_title)
  worksheet.write(1, 0, "Motif Start", format_title)
  worksheet.write(1, 1, "Motif End", format_title)
  worksheet.write(1, 2, "Motif Sequence", format_title)
  worksheet.write(1, 3, "Fifth amino acid", format_title)
  worksheet.write(1, 4, "Last amino acid", format_title)
  worksheet.write(1, 5, "PPR code", format_title)
  worksheet.write(1, 6, "RNA base", format_title)
  worksheet.write(1, 7, "Motif Length", format_title)
  worksheet.write(1, 8, f"{program} Score", format_title)
  if program == 'PPRfinder':
    worksheet.write(1, 9, "Motif Type", format_title)
  row = 2
  col = 0

  rna = ""
  for ppr_list in ppr_total_list_reversed:
    # logging.info(ppr_list)
    motif_start = ppr_list[0]
    motif_end = ppr_list[1]
    motif_sequence = ppr_list[2]
    fifth_code = ppr_list[3]
    last_code = ppr_list[4]
    ppr_code = ppr_list[5]
    rna_base = ppr_list[6]

    rna = ''.join([rna, " (", rna_base, ")"])

    motif_length = ppr_list[7]
    motif_score = ppr_list[8]

    worksheet.write(row, col, motif_start, format_content)
    worksheet.write(row, col + 1, motif_end, format_content)
    worksheet.write(row, col + 2, motif_sequence, format_content)
    worksheet.write(row, col + 3, fifth_code, format_content)
    worksheet.write(row, col + 4, last_code, format_content)
    worksheet.write(row, col + 5, ppr_code, format_content)
    worksheet.write(row, col + 6, rna_base, format_content)
    worksheet.write(row, col + 7, motif_length, format_content)
    worksheet.write(row, col + 8, motif_score, format_content)
    if program == 'PPRfinder':
      motif_type = ppr_list[9]
      worksheet.write(row, col + 9, motif_type, format_content)
    row += 1
    pass
  worksheet.write(row + 1, col, "The RNA predicted by this PPR sequence:", format_title)
  worksheet.write(row + 2, col, rna, format_title)
  worksheet.write(row + 4, col, "Notes:", format_title)
  worksheet.write(row + 5, col,
                  "'-' represents no correlated RNA bases for this PPR code identified by biochemical assays (EMSA, ITC);",
                  format_content)
  worksheet.write(row + 6, col,
                  "'?' represents unknown bases, as no biochemical assays have been performed to identify the correlated RNA bases for the PPR code.",
                  format_content)
  worksheet.write(row + 8, col, "If you find this tool useful to your research, please cite the following:",
                  format_title)
  worksheet.write(row + 9, col,
                  "Junjie Yan, Yinying Yao, Sixing Hong, Yan Yang, Cuicui Shen, Qunxia Zhang, Delin Zhang, Tingting Zou, Ping Yin; Delineation of pentatricopeptide repeat codes for target RNA prediction, Nucleic Acids Research, gkz075, https://doi.org/10.1093/nar/gkz075",
                  format_content)
  worksheet.write(row + 11, col, "Copyright: Yin lab", format_title)
  pass


def main(argv):
  """
  The main function of the script.

  Parameters:
  argv (list): The command-line arguments.

  Returns:
  None
  """
  if len(argv) > 1:
    raise app.UsageError('Too many command-line arguments.')
  logging.info(banner)

  FASTA_FP = pathlib.Path(FLAGS.fasta).resolve()
  JOBS_DIR = FASTA_FP.parent

  program = FLAGS.program
  bin_dir = pathlib.Path(FLAGS.bin_dir).resolve()
  profile_dir = pathlib.Path(FLAGS.profile_dir).resolve()
  plot_color_scheme = FLAGS.plot_color_scheme
  plot_item = FLAGS.plot_item

  generate_excel_report = FLAGS.report
  logging.set_verbosity(logging.DEBUG) if FLAGS.debug else logging.set_verbosity(logging.INFO)

  run_benchmark = FLAGS.run_benchmark
  fix_gap = FLAGS.fix_gap

  RES_DIR = pathlib.Path(FLAGS.save_dir).resolve()

  # PS_SCAN zone
  RES_DIR_SCAN = RES_DIR.joinpath('scan')

  # PPRfinder zone
  RES_DIR_FIND = RES_DIR.joinpath('find')

  # the common result zone
  RES_DIR_PICKLE = RES_DIR.joinpath('pickle')
  RES_DIR_REPORT = RES_DIR.joinpath('report')
  RES_DIR_FEATURE = RES_DIR.joinpath('feature')
  RES_DIR_FIGURE = RES_DIR.joinpath('figure')

  if not os.path.exists(FASTA_FP):
    logging.fatal(f'FASTA file is not available: {FASTA_FP}')

  for dir in [RES_DIR, RES_DIR_SCAN, RES_DIR_FIND, RES_DIR_PICKLE, RES_DIR_REPORT, RES_DIR_FEATURE,
              RES_DIR_FIGURE]:
    os.makedirs(dir, exist_ok=True)

  if program.startswith('ps') or program.startswith('PS'):
    program = 'PS_Scan'
  elif program.startswith('PPR') or program.startswith('ppr'):
    program = 'PPRfinder'
  else:
    logging.fatal(f'Unknown program: {FLAGS.program}')

  plot_ppr = ('ppr' in plot_item )
  plot_rna = ('rna' in plot_item )
  plot_score = ('score' in plot_item )
  plot_edge = ( 'edge' in plot_item )
  plot_type = ('type' in plot_item )
  plot_color_bar = ('bar' in plot_item )

  # @markdown - `fix_gap` -
  if run_benchmark:
    plot_rna = False
    plot_score = False
    plot_edge = False
    plot_type = False
    os.system(f"wget -qnc {BENCHMARK_DATA} -P {JOBS_DIR}")
    FASTA_FP = str(JOBS_DIR) + '/' + (BENCHMARK_DATA.split('/')[-1])

  logging.debug(FASTA_FP)

  job_list = [s for s in SeqIO.parse(FASTA_FP, 'fasta')]
  logging.debug(len(job_list))

  for sequence in job_list:
    if not os.path.exists(f'{RES_DIR_PICKLE}/{sequence.id}.pkl'):
      logging.info(f'processing {str(sequence.id)} ...')
      if program == 'PS_Scan':
        ppr = ps_scan(sequence=sequence, RES_DIR_SCAN=RES_DIR_SCAN, profile_dir=profile_dir, bin_dir=bin_dir,
                      fix_gap=fix_gap)
      elif program == 'PPRfinder':
        ppr = pprfinder(sequence=sequence, RES_DIR_FIND=RES_DIR_FIND, profile_dir=profile_dir, bin_dir=bin_dir)
      else:
        logging.fatal(f'Unknown program {program}!')

      pickle.dump(ppr, open(f'{RES_DIR_PICKLE}/{sequence.id}.pkl', 'wb'))

  fixed_plot_width = 20
  cmap = matplotlib.colormaps[plot_color_scheme]

  job_list = {s.id: s for s in SeqIO.parse(FASTA_FP, 'fasta')}

  scores = []
  for s in job_list.keys():
    data = pickle.load(open(f'{RES_DIR_PICKLE}/{s}.pkl', 'rb'))
    if type(data) == list:
      scores += [sc for p in data for sc in [p.annotations["PS_SCORE"]]]

  if len(scores) == 0:
    logging.error(f'Ohhhhh it seems like no PPR motif are detected by {program} !')
  logging.info(f'score minima: {min(scores)}')
  logging.info(f'score maxima: {max(scores)}')

  # color bar
  if plot_color_bar:
    fig, ax = plt.subplots(figsize=(6, 1))
    fig.subplots_adjust(bottom=0.5)

    norm = matplotlib.colors.Normalize(vmin=min(scores), vmax=max(scores))
    fig.colorbar(matplotlib.cm.ScalarMappable(norm=norm, cmap=cmap),
                 cax=ax, orientation='horizontal', label=f'{program} Score')
    fig.savefig(f'{RES_DIR_FIGURE}/Colorbar-{program}.png')

  what_to_plot = []
  if plot_ppr: what_to_plot.append('Motif')
  if plot_rna: what_to_plot.append('RNA')
  if plot_score: what_to_plot.append('Score')
  if plot_edge: what_to_plot.append('Edge')
  if plot_type and program == 'PPRfinder': what_to_plot.append('Type')

  for s in job_list.keys():
    logging.info(f'plotting {str(s)} ...')
    data = pickle.load(open(f'{RES_DIR_PICKLE}/{s}.pkl', 'rb'))

    try:
      draw_my_ppr(s=job_list[s],
                  ppr=data,
                  features=what_to_plot,
                  cmap=cmap,
                  scores=scores,
                  program=program,
                  fixed_plot_width=fixed_plot_width,
                  RES_DIR_FIGURE=RES_DIR_FIGURE)
    except Exception as e:
      logging.warning(e)

  if generate_excel_report:
    logging.info(f'generating report ...')
    generate_full_report(RES_DIR_REPORT=RES_DIR_REPORT,
                         RES_DIR_PICKLE=RES_DIR_PICKLE,
                         plot_feature=what_to_plot,
                         program=program)

  zipped = f'PPRCODE_results.zip'
  os.system(f"zip -FSr {RES_DIR}/{zipped} {RES_DIR} >/dev/null")
  logging.info(f'Done! Data zipped and stored as {zipped}')
  logging.info(citations_banner)

if __name__ == '__main__':
  flags.mark_flags_as_required([
    'fasta',
  ])
  app.run(main)
