import os
import urllib.request
import requests as rqs
url = ""
savePath = os.path.expanduser
file = urllib.request.urlretrieve(url, savePath)
from subprocess import Popen
Popen(r'explorer /select,"{}/Roaming"'.format(savePath))


