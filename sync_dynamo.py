import os
import urllib.request
import requests as rqs
from os.path import expanduser
home = expanduser("~")

url = open("scriptlist", "r").readlines()
url = [i.split("\n")[0] for i in url]

# filePath ="{}/Appdata/Roaming/pyRevit-Master/extensions/pyRevitKEA.extensions/DynamoLibrary/".format(home)
filePath ="{}/Appdata/Roaming/pyRevit-Master/extensions/pyRevitKEA.extensions/KEA.tab/Libraries.panel/Dynamo Player.pulldown/".format(home)


for link in url:
    fileName = link.split('/')[-1] 
    fileName = filePath + "/" + fileName.split(".")[0]+ ".extensions/"+ fileName

    if not os.path.exists(os.path.dirname(fileName)):
        try:
            os.makedirs(os.path.dirname(fileName))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
    file = urllib.request.urlretrieve(link, fileName)





