#import time
from shlex import split
from subprocess import check_call
from urllib.request import urlopen

command_line = "docker run --rm -d --name=smk -p 8181:8080 -p 50350:50000 --user root kgrishma/jenkins:v1 sleep 10"
args = split(command_line)

check_call(args)
# Wait for the server to start. A better implementation
# would poll in a loop:
# time.sleep(10)
# Check if the server started (it'll throw an exception
# if not):
try:
    urlopen("http://localhost:8181").read()
finally:
    check_call("docker kill smk".split())
