<!-- badges: start -->

[![GitHub
Issues](https://img.shields.io/github/issues/MPRAhub/MPRAorg-LibrarySuite)](https://github.com/MPRAhub/iSEEhub/MPRAorg-LibrarySuite)

![BuildStatus-MPRAhub](https://github.com/MPRAhub/MPRAorg-LibrarySuite/actions/workflows/build-MPRAhub.yml/badge.svg?event=push)

<!-- badges: end -->



# MPRAorg-LibrarySuite
MPRAorg-LibrarySuite provides a comprehensive collection of libraries and tools for analyzing and sharing MPRA data.

# Prerequistes & Installation

Before proceeding with the installation, please ensure that you have fulfilled making the following accounts:

* [GitHub](https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home): required to create & add their public ssh key.

* [Synapse](https://www.synapse.org/): required to complete certification and create a Git issue to request addition to the Synapse project workspace.

* [Docker](https://www.docker.com/): (optionally) required to have a Docker account, which will enable you to pull the MPRAbase Docker image from the Synapse registry.

* [Singularity](https://cloud.sylabs.io/?_gl=1*zlt1gk*_ga*MTU1Mzg2OTQxNy4xNjg0MTkxMzM5*_ga_X710KLJKK6*MTY4NDE5MTMzOS4xLjEuMTY4NDE5MTM0Ni4wLjAuMA..&_ga=2.118074254.606116961.1684191339-1553869417.1684191339): (optionally) required to have a Synapse account if you are operating on a high performance compute cluster without root access.

For more information, please review our onboarding documentation for a smooth installation ([link here](https://docs.google.com/document/d/1d23PDeozSP36U-4aWNFhE1knIbZ2HUiWTan9AsKQ-KY/edit?usp=sharing)).

Once you've completed the prerequiste accounts, please clone the MPRAorg-LibrarySuite repository:

```bash
git clone git@github.com:MPRAhub/MPRAorg-LibrarySuite.git
cd MPRAorg-LibrarySuite
bash build-MPRAhub.sh
```

## Setup JupyterLab Workspace for MPRAhub
### Local

To setup a JupyterLab workspace for MPRAhub, users can hit the ground running with the MPRAbase Docker container. We provide a Python executable called **run-local-MPRAhub.py**, which will launch a Docker container with user provided command line arguments. Here is an example:

```bash
cd MPRAorg-LibrarySuite
python3 run-local-MPRAhub.py --container_port 8888 --host_port 8888 \
--iSEE_MPRAbase_container_port 3838 --iSEE_MPRAbase_host_port 3838 \
--local_dir_mount /local/dir/path --image docker.synapse.org/syn51118207/mprabase:arm64-v0.1.1
```

### High Performance Compute (HPC) cluster

For users on a High Performance Compute (HPC) cluster, we also provide a Singularity definition file and bash script called **build-MPRAbhub-sif.sh** to build the Singularity Image Format (SIF) file. We recommend using a Linux Screen session when building the MPRAhub.sif file, because the estimated build time is one hour.

```bash
cd MPRAorg-LibrarySuite/env
bash MPRAhub-build-sif.sh
```

We assume HPC users are required to ssh tunnel to a devolpment or compute node to launch an interactive Jupyter Lab workspace. Here's an example ssh tunnel command for UCSF's HPC where the user is running the Jupyter Lab workspace on **dev1**:

```bash
ssh mprahub_user@dev1.wynton.ucsf.edu -J mprahub_user@log1.wynton.ucsf.edu \
-L <host port Jupyter Lab>:localhost:<container port Jupyter Lab> \
-L <host port iSEE MPRAbase>:localhost:<container port iSEE MPRAbase>
```

For a specific example for **mprahub_user**, we set **9797** as the local host port to access Jupyter Lab on a user's local web browser and **9595** as the container port to allow the user to access the Jupyter Lab workspace on the local host port. Finally, we set **3838** as the local host and container port to access an iSEE MPRAbase instance that was launched in the Jupyter Lab workspace.


```bash
ssh mprahub_user@dev1.wynton.ucsf.edu -J mprahub_user@log1.wynton.ucsf.edu -L 9797:localhost:9595 -L 3838:localhost:3838
```

After users ssh tunnel into the HPC and build the MPRAhub SIF file, navigate to the MPRAorg-LibrarySuite (working) directory and launch the Jupyter Lab workspace using **run-hpc-MPRAhub.py**. Please note, the local directory mount for the Jupyter Lab workspace should be the full path to the MPRAorg-LibrarySuite (working) directory.

```bash
cd MPRAorg-LibrarySuite/
python3 run-hpc-MPRAhub.py  --container_port 9595 --local_dir_mount /local/path/to/MPRAorg-LibrarySuite \
--sif env/MPRAhub.sif
```

## Install iSEE-MPRAbase Developer Dependencies

In a Jupyter Lab workspace running from the MPRAhub Singularity container, open a terminal and follow these commands to install our iSEEindex fork for launching iSEE-MPRAbase instances:

```bash
cd /home/jovyan/ # Assumes user launched a JupyterLab workspace using the Singularity MPRAbase SIF
Rscript build-iSEEindex-fork.R
```

After a successful iSEEindex installation, open the following Jupyter Notebook and execute all of the cells: 

```bash
MPRAhub/MPRAbase/notebooks/demo-MRAbase-v0.1.1.ipynb 
```

Finally, paste the link in your browser search bar: http://0.0.0.0:3838/

## Install MPRAbase Bioconductor Library for Developers

In the MPRAhub Singularity container running a JupyterLab workspace, open a terminal and follow these commands:

```bash
cd /home/jovyan/
Rscript build-MPRAbase-API.R
```
