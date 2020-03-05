import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from textblob import TextBlob
from elasticsearch import Elasticsearch
from config import *
from rich.console import Console
import sys
import csv
import pickle
from pandas import DataFrame
console = Console()
es = Elasticsearch()



class TwitterStreamer(StreamListener):

    def on_data(self, data):
        """Start stream and predict sentiment"""
        try:
            dict_data = json.loads(data)
            tweet = TextBlob(dict_data['text'])
            username = str(dict_data['user']['name'])

            # Take data stream and assign it either Negitive, Netural, Positive sentiment
            if tweet.sentiment.polarity < 0:
                sentment = "Negitive"
            elif tweet.sentiment.polarity == 0:
                sentment = "Netural"
            else:
                sentment = "Positive"

            # Send data stream into a dict then write to csv file
            try:
                C = {   
                    'Username': [dict_data['user']['name']],
                    'Text': [dict_data['text']],
                    'Set': [sentment],
                    }           
                df = DataFrame(C, columns= ['Username', 'Text', 'Set'])
                if "RT" not in tweet:
                    export_csv = df.to_csv ('SetData.csv', index = False, header=False, mode='a')
                else:
                    pass

            # Console can't show emojis so just pass
            except UnicodeTranslateError as e:
                print(e)
                pass
            return True

        except KeyError as e: # Pass KeyError when I reach twitter stream limit and let it catch up
            print(e)
            pass
    def on_error(self, data):
        print("oh no")
        input()
        sys.exit(0)

if __name__ == "__main__":
    # Start Stream
    myStreamListener = TwitterStreamer()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    myStream = Stream(auth = auth, listener=myStreamListener)
    myStream.filter(track=['trump'], is_async=True)
