import tweepy
import gspread
import random   
from apikeys import *

gc = gspread.service_account('credentials.json')

# Open a sheet from a spreadsheet in one go
wks = gc.open("lupe-bot").sheet1

# Gets all values in sheet
values = wks.get_all_values()

# Selects one row from sheet
row = (random.choice(values))

# Clear empty values from row
lyrics = list(filter(None, row))

# Authenticate to twitter with v2.0
client = tweepy.Client(bearer_token = btoken , consumer_key = ckey, consumer_secret = csecret, access_token = atoken, access_token_secret= atokensecret)

# Select a value from the clean list
next_tweet = (random.choice(lyrics))

# Post tweet using version 2.0
client.create_tweet(text=next_tweet)

