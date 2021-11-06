import os
import urllib.request
import requests as rqs
url = ""
savePath = "%userprofile%"
file = urllib.request.urlretrieve(url, savePath)
from subprocess import popen
Popen(r'explorer /select,"{}"'.format_map(savePath))


