from PIL import ImageGrab
import requests as rqs
import os.path 
from base64 import b64encode
import json

def takeScreenshot(filepath):
    screenshot  = ImageGrab.grab()
    # screenshot.show()
    screenshot.save(filepath, "PNG")

def uploadImage(username, filepath):
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
    # response = """{"status":200,"success":true,"data":{"id":"UiT0D83","deletehash":"pFTC4iBAhLO6XPM","account_id":null,"account_url":null,"ad_type":null,"ad_url":null,"title":"Screenshot of the dummy","description":null,"name":"test.png","type":"image/png","width":360,"height":360,"size":30493,"views":0,"section":null,"vote":null,"bandwidth":0,"animated":false,"favorite":false,"in_gallery":false,"in_most_viral":false,"has_sound":false,"is_ad":false,"nsfw":null,"link":"https://i.imgur.com/UiT0D83.png","tags":[],"datetime":1636226909,"mp4":"","hls":""}}"""
    response = json.loads(response.text)
    return str(response["data"]["link"])



home = os.path.expanduser("~")
username = "dummy" # ! change it so it takes it from Revit 
# filepath = os.path.normpath(home +"/Desktop/{}.png".format(username)) # ! turn it on when you want to upload a screen
filepath = os.path.normpath(home +"/Desktop/test.png")
# takeScreenshot(filepath) # ! turn it on later
print(uploadImage(username, filepath))