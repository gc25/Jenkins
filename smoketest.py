import time
import sys

from subprocess import check_call,run
from urllib.request import urlopen

build =  sys.argv[0]
run(
    "(docker run --rm --name=smk -p 8080:80 -d kgrishma/my-jenkins:%i), build".split()
)
# Wait for the server to start. A better implementation
# would poll in a loop:
time.sleep(60)
# Check if the server started (it'll throw an exception
# if not):
try:
    urlopen("http://localhost:8080").read()
finally:
    run("docker kill smk".split())
