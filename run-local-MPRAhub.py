import argparse
import subprocess

# Create the parser
parser = argparse.ArgumentParser(description='Run the MPRAbase Docker container.')

# Add arguments
parser.add_argument('--container_port', type=str, help='Container port to host port.')
parser.add_argument('--host_port', type=str, help='Host port to container port.')
parser.add_argument('--iSEE_MPRAbase_container_port', type=str, help='Container port for iSEE-MPRAbase.')
parser.add_argument('--iSEE_MPRAbase_host_port', type=str, help='Host port for iSEE MPRAbase')
parser.add_argument('--local_dir_mount', type=str, help='Mount local directory as a shared volume to a directory inside the container')
parser.add_argument('--image', type=str, default='docker.synapse.org/syn51118207/mprabase:arm64-v0.1.1', help='Docker image name for running a container')

# Parse the command-line arguments
args = parser.parse_args()

docker_cmd = "docker run -p " + args.container_port +":"+ args.host_port + \
    " -p " + args.iSEE_MPRAbase_container_port +":"+ args.iSEE_MPRAbase_host_port + \
        " -v " + args.local_dir_mount+":/home/jovyan/work " + args.image

print(docker_cmd)
subprocess.call(docker_cmd,shell=True)
