import time
import sys

from subprocess import check_call
from urllib.request import urlopen


check_call(
    "docker run --rm -d --name=smk -p 8080:8080 -p 50000:50000 --user root -v /var/run/docker.sock:/var/run/docker.sock kgrishma/my-jenkins:23".split()
)
# Wait for the server to start. A better implementation
# would poll in a loop:
time.sleep(60)
# Check if the server started (it'll throw an exception
# if not):
try:
    urlopen("http://localhost:8080").read()
finally:
    check_call("docker kill smk".split())
