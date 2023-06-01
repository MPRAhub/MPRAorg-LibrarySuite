#!/bin/bash
# NOTE: If not already done, please connect your Docker account to your Synapse account
# singularity pull --docker-login docker://docker.synapse.org/syn51118207/mprabase:amd64-v0.1.0
singularity build --docker-login MPRAhub.sif MPRAhub.def 
#docker://docker.synapse.org/syn51118207/mprabase:amd64-v0.1.0
