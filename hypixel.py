import requests
import os



API_KEY = os.environ['API_KEY']


def getinfo(call):
    r = requests.get(call)
    return r.json()


def mwplayercount():
    url = f'https://api.hypixel.net/counts?key={API_KEY}'
    data = getinfo(url)
    playercount = data["games"]["WALLS3"]["modes"]["standard"]
    return mw, playercount
