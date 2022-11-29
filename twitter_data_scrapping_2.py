#importing libraries
import tweepy as tw    #to access twitter api
import pandas as pd    # for making data frames and stroing data after retrieving

#Reading file keys.py that stores all the keys seprately
from keys import *
import requests

client = tw.Client( bearer_token=bearer_token,
                    consumer_key=api_key,
                    consumer_secret=api_key_secret,
                    access_token=access_token,
                    access_token_secret=access_secret_token,
                    return_type= requests.Response,
                    wait_on_rate_limit=True)

#making a query 
query = '#music  -is:retweet'
#get max of 100 tweets from last 7days 

tweets = client.search_recent_tweets(query=query,
                                     max_results=100)

#saving data as dictionary
tweets_dict = tweets.json()

# extracting data from dictionary
tweets_data = tweets_dict['data']

#Transforming to pandas dataframe
df = pd.json_normalize(tweets_data)

#saving the dataframe for analysis 
df.to_csv("music_twitter_data.csv")
