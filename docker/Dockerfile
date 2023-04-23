# set ubuntu as backend OS
FROM ubuntu:20.04
ARG JDK_VER=openjdk-17-jdk-headless

# Use bash to support string substitution.
SHELL ["/bin/bash", "-c"]

RUN DEBIAN_FRONTEND=noninteractive apt-get update -qy  \
    && apt-get install -qy ca-certificates \
    && apt-get install -qy ${JDK_VER} \
    && apt-get install -qy python3 python3-dev zip hmmer perl wget 

COPY . /app/pprcode

# Install pip packages.
RUN python -m pip install --upgrade pip \
    && pip3 -q install --upgrade pip \
    && pip3 -q install pandas \
    && pip3 -q install biopython \
    && pip3 -q install matplotlib \
    && pip3 -q install dna_features_viewer \
    && pip3 -q install xlsxwriter \
    && pip3 -q install absl-py==0.13.0

# PS_scan setting/ PPRfinder setting
ARG PROSITE_URL='https://ftp.expasy.org/databases/prosite/'
ARG PS_SCAN_URL='https://ftp.expasy.org/databases/prosite/ps_scan/ps_scan_linux_x86_elf.tar.gz'
ARG PPRFINDER_BUILD='https://raw.githubusercontent.com/YaoYinYing/PPRfinder/master/out/production/PPRfinder/PPRfinder.jar'
ARG HMM_PROFILE_URL='https://raw.githubusercontent.com/YaoYinYing/PPRfinder/master/data/'

# setup psscan
RUN wget -qnc ${PS_SCAN_URL} -P /tmp \
    && mkdir -p /app/bin/ \
    && cd /app/bin/ \
    && tar zxf /tmp/ps_scan_linux_x86_elf.tar.gz \
    && rm /tmp/ps_scan_linux_x86_elf.tar.gz

RUN  wget -qnc ${PPRFINDER_BUILD} -P /app/bin/

RUN mkdir /app/profiles \
    && wget -qnc ${PROSITE_URL}/prosite.dat -P /app/profiles/ \
    && wget -qnc ${HMM_PROFILE_URL}/all_PPR.hmm -P /app/profiles/

# Add SETUID bit to the ldconfig binary so that non-root users can run it.
RUN chmod u+s /sbin/ldconfig.real

WORKDIR /app/pprcode

ENV PATH="/app/bin/ps_scan:$PATH"

RUN echo $'#!/bin/bash\n\
ldconfig\n\
python /app/pprcode/docker/run_pprcode.py "$@"' > /app/run_pprcode.sh \
  && chmod +x /app/run_pprcode.sh
ENTRYPOINT ["/app/run_pprcode.sh"]
