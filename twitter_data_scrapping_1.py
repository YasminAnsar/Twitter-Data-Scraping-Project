#importing libraries
import tweepy as tw    #to access twitter api
import configparser    #to keep crediental save in saperate file
import json
import pandas as pd    # for making data frames and stroing data after retrieving

#api keys are stored in a seprate file for data security reasons
from keys import *

#Authantication with twitter api keys
auth = tw.OAuthHandler(api_key, api_key_secret)
#giving access token to the authantication 
auth.set_access_token(access_token, access_secret_token)
#api instance that gives us access to the twitter account
api = tw.API(auth)

#search word and limiting the items
search_query = "#inflation #europe -filter:retweets"
# get tweets from the API
tweets = tw.Cursor(api.search_tweets,
              q=search_query,
              lang="en").items(500)
tweet_result = [api.get_status(data.id, tweet_mode="extended") for data in tweets]
tweet_list = [[status.user, status.full_text] for status in tweet_result]    

#Creating a dataframe of twitter data 
tweet_df = pd.DataFrame(data = tweet_list, columns=["user_id","tweet"])
tweet_df
#Converting dataframe to csv file
tweet_df.to_csv(r'twitter_inflation_data.csv', index=False)
