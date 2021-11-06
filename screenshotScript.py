from PIL import ImageGrab
import requests as rqs
import os.path 
from base64 import b64encode
home = os.path.expanduser("~")
username = "dummy"
# filepath = os.path.normpath(home +"/Desktop/{}.png".format(username))
filepath = os.path.normpath(home +"/Desktop/test.png")
# screenshot  = ImageGrab.grab()
# # screenshot.show()
# screenshot.save(filepath, "PNG")

clientID = "fee5cb3d1441be2"
url = "https://api.imgur.com/3/upload"
headers = {"Authorization": "Client-ID {}".format(clientID)}
payload = {
    'image': b64encode(open(filepath, 'rb').read()),
    'type': 'base64',
    'name': "test.png",
    'title': "Screenshot of the {}".format(username)
    }
response = rqs.request("POST", url, headers = headers, data=payload)

print(response)

