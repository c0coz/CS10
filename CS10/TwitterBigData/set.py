import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from textblob import TextBlob
from elasticsearch import Elasticsearch
from config import *
from rich.console import Console
import sys

console = Console()
es = Elasticsearch()



class TwitterStreamer(StreamListener):

    def on_data(self, data):
        dict_data = json.loads(data)
        tweet = TextBlob(dict_data['text'])

        if tweet.sentiment.polarity < 0:
            sentment = "Negitive"
        elif tweet.sentiment.polarity == 0:
            sentment = "Netural"
        else:
            sentment = "Positive"

        console.print(sentment + " " + str(tweet.sentiment.polarity), style="bold green")
        console.print(dict_data['text'] + "\n", style="bold red")
        return True
    def on_error(self, data):
        print("oh no")
        sys.exit(0)

        # print(data.text)

if __name__ == "__main__":
    myStreamListener = TwitterStreamer()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    myStream = Stream(auth = auth, listener=myStreamListener)
    myStream.filter(track=['congress'])