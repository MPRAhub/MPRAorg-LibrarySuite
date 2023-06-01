![BuildStatus-MPRAhub](https://github.com/MPRAhub/MPRAorg-LibrarySuite/actions/workflows/build-MPRAhub.yml/badge.svg?event=push)

# MPRAorg-LibrarySuite
MPRAorg-LibrarySuite provides a comprehensive collection of libraries and tools for analyzing and sharing MPRA data.

# Prerequistes 

Before proceeding with the installation, please ensure that you have fulfilled making the following accounts:

* [GitHub](https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home): required to create & add their public ssh key.

* [Synapse](https://www.synapse.org/): required to complete certification and email <> to request addition to the project.

* [Docker](https://www.docker.com/): (optionally) required to have a Docker account, which will enable you to pull the MPRAbase Docker image from the Synapse registry.

* [Singularity](https://cloud.sylabs.io/?_gl=1*zlt1gk*_ga*MTU1Mzg2OTQxNy4xNjg0MTkxMzM5*_ga_X710KLJKK6*MTY4NDE5MTMzOS4xLjEuMTY4NDE5MTM0Ni4wLjAuMA..&_ga=2.118074254.606116961.1684191339-1553869417.1684191339): (optionally) required to have a Synapse account if you are operating on a high performance compute cluster without root access.

For more information, please review our onboarding documentation for a smooth installation ([link here](https://docs.google.com/document/d/1d23PDeozSP36U-4aWNFhE1knIbZ2HUiWTan9AsKQ-KY/edit?usp=sharing)).

# Installation

Once you've completed the prerequiste accounts, please clone the MPRAorg-LibrarySuite repository:

**TODO**: Add estimated file cache size

```bash
git clone git@github.com:MPRAhub/MPRAorg-LibrarySuite.git
cd MPRAorg-LibrarySuite
bash build-MPRAhub.sh
```

## Setup JupyterLab Workspace for MPRAhub
### Local

To setup a JupyterLab workspace for MPRAhub, users can hit the ground running with the MPRAbase Docker container. We provide a Python executable called **run-local-MPRAbase.py**, which will launch a Docker container with user provided command line arguments. Here is an example:

```bash
cd MPRAorg-LibrarySuite
python3 run-local-MPRAbase.py --container_port 8888 --host_port 8888 \
--iSEE_MPRAbase_container_port 3838 --iSEE_MPRAbase_host_port 3838 \
--local_dir_mount /local/dir/path --image docker.synapse.org/syn51118207/mprabase:arm64-v0.1.1
```

### High Performance Compute (HPC) cluster

For users on a High Performance Compute (HPC) cluster, we also provide a Singularity definition file and bash script called **build-singularity-sif.sh**, which builds the Singularity Image Format (SIF) file for the iSEE-MPRAbase Singularity container.

```bash
cd MPRAorg-LibrarySuite/env
bash build-MPRAbase-sif.sh
```

After building the MPRAbase SIF, navigate to the MPRAbase working directory and launch an instance with **run-hpc-MPRAbase.py**.

```bash
cd MPRAorg-LibrarySuite/
python3 run-hpc-MPRAbase.py  --container_port 9595 --local_dir_mount /local/dir/path --sif env/MPRAbase.sif
```

## Install MPRAbase Developer Dependencies

In a running MPRAbase JupyterLab container, open a terminal and follow these commands:

```bash
$ cd /home/jovyan/
$ Rscript build-iSEEindex-fork.R
```

After a successful iSEEindex installation, open the following Jupyter Notebook and execute all of the cells: 

```bash
MPRAhub/MPRAbase/notebooks/demo-MRAbase-v0.1.1.ipynb 
```

Finally, paste the link in your browser search bar: http://0.0.0.0:3838/

# MPRAbase API Development (**WorkAround**) 


In a running MPRAbase JupyterLab container, open a terminal and follow these commands:

```bash
$ cd /home/jovyan/
$ Rscript build-MPRAbase-API.R
```
