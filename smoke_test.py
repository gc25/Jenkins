from shlex import split
from subprocess import check_call
from urllib.request import urlopen

command_line = "docker run -d --name db --health-cmd "curl --fail http://localhost:8080/ || exit 1" --health-interval=5s --timeout=3s arungupta/couchbase"
docker_args = split(command_line)

check_call(docker_args)

inspect_command = "docker inspect --format='{{json .State.Health}}' db"
inspect_args =  split(inspect_command)

check_call(inspect_args)
