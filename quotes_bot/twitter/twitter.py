from .. import secrets
import tweepy
# import textract
# import Library
import json
from time import sleep

import requests

def publish(quote):
    publish_tweet(quote)

def start_twitting():
    quotes = []

    quote = get_new_quote()

    if twit_is_valid(quote):
        print(quote)
    else:
        print ("Incorrect length: {}".format(len(quote)))

def get_new_quote():
    request = requests.get('http://quotes.stormconsultancy.co.uk/random.json')
    answer = request.json()
    (quote, author) = (answer['quote'], answer['author'])

    quote = "\"{}\" - {}".format(quote.encode("utf-8"), author.encode("utf-8"))
    return quote

def twit_is_valid(twit):
    return len(twit) <= 280

def publish_tweet(twit):
    # create an OAuthHandler instance
    # Twitter requires all requests to use OAuth for authentication
    auth = tweepy.OAuthHandler(secrets.consumer_key, secrets.consumer_secret)
    auth.set_access_token(secrets.access_token, secrets.access_secret)

     #Construct the API instance
    api = tweepy.API(auth) # create an API object

    api.update_status(twit)
