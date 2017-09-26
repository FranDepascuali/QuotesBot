#!/usr/bin/env python
import wikiquotes
import random
import time
import os

from .slack import slack
from .twitter import twitter
from .author import author

bots = []

MIN_MINUTES = 10
MAX_MINUTES = 20

def fetch_all_authors():
    authors_path = os.path.join(os.path.abspath("./quotes_bot/author"), "authors.txt")
    return author.all_authors(authors_path)

authors = fetch_all_authors()

def random_author():
    return random.choice(authors)

def format_quote(quote, author):
    quote_format = ""
    if quote.startswith("\""):
        quote_format = "{} {}"
    else:
        quote_format = "\"{}\" {}"

    output_quote = quote.capitalize()
    output_author = "#{}".format(author.title().replace(" ", ""))

    return quote_format.format(output_quote, output_author)

def start():

    add_bot(slack)
    add_bot(twitter)

    while True:
        post = ""
        while not is_valid_twit(post):
            try:
                author = random_author()
                quote = wikiquotes.random_quote(author.name, author.language)
                post = format_quote(quote, author.name)

                print(post)
            except Exception as e:
                print(e)
                pass

        for bot in bots:
            bot.publish(post)

        time.sleep(random.randint(MIN_MINUTES, MAX_MINUTES) * 60)

def add_bot(bot):
    bots.append(bot)

def is_valid_twit(quote):
    quote_length = len(quote)
    return quote_length > 0 and quote_length <= 140

start()
