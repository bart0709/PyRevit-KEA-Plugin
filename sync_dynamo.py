import os
import urllib.request
import requests as rqs
from os.path import expanduser
home = expanduser("~")
filePath ="{}/Appdata/Roaming/pyRevit-Master/extensions/pyRevitKEA.extensions/DynamoLibrary/".format(home)
# filePath ="{}/Appdata/Roaming/pyRevit-Master/extensions/pyRevitKEA.extensions/KEA.tab/Libraries.panel/Dynamo.pushbutton/".format(home)
if not os.path.exists(os.path.dirname(filePath)):
    try:
        os.makedirs(os.path.dirname(filePath))
    except OSError as exc: # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise

url = open("scriptlist", "r").readlines()
url = [i.split("\n")[0] for i in url]

for path in url:
    fileName = path.split('/')[-1]
    fileName = filePath + fileName
    file = urllib.request.urlretrieve(path, fileName)




