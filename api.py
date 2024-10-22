import requests
import json

def getapi():
    ds = requests.get("https://api.waifu.pics/sfw/neko").content
    image = json.loads(ds)["url"]
    return image