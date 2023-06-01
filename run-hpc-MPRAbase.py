import argparse
import subprocess

# Create the parser
parser = argparse.ArgumentParser(description='Run the MPRAbase Singularity container.')

# Add arguments
parser.add_argument('--container_port', type=str, help='Container port to host port.')
parser.add_argument('--local_dir_mount', type=str, help='Mount local directory as a shared volume to a directory inside the container')
parser.add_argument('--sif', type=str, default='env/MPRAbase-v0.1.1.sif', help='Singularity SIF path for running the MPRAbase container')

# Parse the command-line arguments
args = parser.parse_args()
singularity_cmd = "singularity run --bind " + args.local_dir_mount + ":/home/jovyan/ " + args.sif + \
    " jupyter lab " + " --port=" + args.container_port + " --no-browser --ip=0.0.0.0 --notebook-dir /home/jovyan"

subprocess.call(singularity_cmd, shell=True)
