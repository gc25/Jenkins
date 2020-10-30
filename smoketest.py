import time
import sys

from urllib.request import urlopen

# Check if the server started (it'll throw an exception
# if not):
try:
    urlopen("http://localhost:8181").read()
finally:
    print("Jenkins server is accessible")
