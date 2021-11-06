import os
import urllib.request
import requests as rqs
url = ""
savePath = os.path.expanduser
file = urllib.request.urlretrieve(url, savePath)
file = open(savePath+"/test.txt","w")


