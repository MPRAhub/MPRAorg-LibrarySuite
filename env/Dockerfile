FROM jupyter/datascience-notebook:latest

USER jovyan
ENV PATH="/home/jovyan/.local/bin:${PATH}"

RUN R -e "install.packages('BiocManager', repos='http://cran.us.r-project.org')"
RUN R -e "install.packages(c('tidyr', 'dplyr'), repos='http://cran.us.r-project.org')"
RUN R -e "install.packages(c('dbplyr', 'RSQLite', 'DBI'), repos='http://cran.us.r-project.org')"
RUN R -e "BiocManager::install(c('SummarizedExperiment','BiocStyle','iSEE', 'BSgenome.Hsapiens.UCSC.hg38', 'BSgenome.Hsapiens.UCSC.hg19'), dependencies=TRUE)"
RUN R -e "install.packages(c('roxygen2','devtools'), repos='http://cran.us.r-project.org')"
RUN R -e "BiocManager::install(c('MultiAssayExperiment'), dependencies=TRUE)"
RUN R -e "install.packages('synapser', repos = c('http://ran.synapse.org', 'http://cran.fhcrc.org'))"
USER root
RUN apt-get update && \
    apt-get install -y libcairo2-dev && \
    rm -rf /var/lib/apt/lists/*
USER $NB_UID
RUN R -e 'BiocManager::install("scater", dependencies=TRUE)'
RUN R -e "install.packages(c('paws.storage', 'urltools', 'testthat'), dependencies=TRUE)"
RUN R -e "BiocManager::install('MPRAnalyze')"

RUN pip install --user pytest
RUN pip install --user synapseclient
RUN conda update conda
RUN conda install -c conda-forge pandoc
