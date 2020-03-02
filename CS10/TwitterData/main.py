from twython import Twython
import rich
import json
from rich.console import Console

def auth():
    f = open("keys.json", "r")
    key = json.load(f)
    twitter = Twython(
    key["app_key"], key["app_sec"],
    key["acc_key"], key["acc_sec"])
    f.close()
    return twitter
def CanadaCount(twitter):
    apple = 0
    android = 0
    auth()
    console = Console()
    searching = twitter.search(q="Fortnite", count=100)
    tweets = searching['statuses']
    xxxxxx = tweets

    for tweet in xxxxxx[::-1]:
        if 'iPhone' in tweet['source']:
            apple = apple + 1
        elif "Android" in tweet['source']:
            android = android + 1
        else:
            pass
    console.print("Android: ", android)
    console.print("iPhone: ", apple)
    # console.print(searching)
CanadaCount(auth())
