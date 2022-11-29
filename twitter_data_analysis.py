import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import re

#Reading the twitter data csv file
twitter_data = pd.read_csv('twitter_data.csv')

#Extracting only tweets column text from the data
tweets = twitter_data["tweet"].values
#print(tweets)

#Converting the text column into single string
tweet_string=str(tweets)

#converting all text to lower case

cleaned_tweet_string=tweet_string.lower()

#removing the twitter usernames from the tweet string

cleaned_tweet_string=re.sub(r'@\w+', ' ',cleaned_tweet_string)

#removing the URLs from the tweet string

cleaned_tweet_string=re.sub(r'http\S+', ' ',cleaned_tweet_string)
#removing everything which is not character
cleaned_tweet_string=re.sub(r'[^a-z A-Z]', ' ',cleaned_tweet_string)

#Removing any words that are less than 3-characters mostly those are stopwords
cleaned_tweet_string=re.sub(r'\b\w{1,2}\b', ' ',cleaned_tweet_string)

#removing extra spaces in the text
cleaned_tweet_string=re.sub(r' +', ' ',cleaned_tweet_string)
print(cleaned_tweet_string)

#Plotting the wordColud

wordcloudimage = WordCloud(
                         max_words=100,
                         max_font_size=500,
                         font_step=2,
                         background_color='white',
                         width=1000,
                         height=720
                         ).generate(cleaned_tweet_string)

plt.figure(figsize=(15, 7))
plt.axis("off")
plt.imshow(wordcloudimage)
wordcloudimage
plt.show()
