from twython import Twython
import rich
import json
from rich.console import Console

f = open("keys.json", "r")
key = json.load(f)
twitter = Twython(key["app_key"], key["app_sec"],
                  key["acc_key"], key["acc_sec"])
f.close()
console = Console()

x = twitter.search(q='epic')
y = x["statuses"]
console.print(y[0])
