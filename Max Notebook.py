# Databricks notebook source
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
consumer_key = "sf0JmcXPSOD51e3JwK6IVVPH8" #twitter app’s API Key
consumer_secret = "WLa6l2rAjCHptRPGnwE6s6MGhT3ditDNYReaQLxPrMM2FO0l5u" #twitter app’s API secret Key
access_token = "602357821-Dyn6cKGyLCQ7GsLAwMqyayQHN1zf0eNN31ZuT5s0" #twitter app’s Access token
access_token_secret = "9bJbqugj6xQtN0zi7ywP4ynrLG1OVhFor315x8mWtCVDu" #twitter app’s access token secret

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth_api = API(auth)

trump_tweets = auth_api.user_timeline(screen_name = 'TwitterA11y', count = 600, include_rts = False, tweet_mode = 'extended')

final_tweets = [each_tweet.full_text for each_tweet in trump_tweets]

with open('/dbfs/FileStore/tables/twitter_tweets.txt', 'w') as f:
  for item in final_tweets:
   f.write("%s\n" % item)

read_tweets = []
with open('/dbfs/FileStore/tables/twitter_tweets.txt','r') as f:
  read_tweets.append(f.read())


# COMMAND ----------

final_tweets

# COMMAND ----------


