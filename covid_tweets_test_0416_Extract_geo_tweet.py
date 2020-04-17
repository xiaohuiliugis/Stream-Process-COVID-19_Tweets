import numpy as np
import pandas as pd
import re
import warnings
import json

#Visualisation
import matplotlib
import matplotlib.pyplot as plt

import seaborn as sns
from IPython.display import display
# 
from mpl_toolkits.basemap import Basemap
from wordcloud import WordCloud, STOPWORDS

import nltk 
from nltk.stem import WordNetLemmatizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.sentiment.util import *
from nltk import tokenize
import pandas.util.testing as tm

matplotlib.style.use('ggplot')
pd.options.mode.chained_assignment = None
warnings.filterwarnings("ignore")

import json
import os
directory = r'C:\data\covid\StreamTweets\0327_0416'
test_dir = r'C:\data\covid\StreamTweets\test_files'

for filename in os.listdir(directory):
    # Open the input file
    input_file = open(os.path.join(directory, filename),'r')

    #input_file = open(r'C:\data\covid\tweets_test_code\TweetDB_03_25_2020.csv','r')
    # Load the first few lines
    geo_tweets=[]
    city_tweets=[]
    for line in input_file:
        if line.strip():
            tweet = json.loads(line)

            try:
                tweet_cont = {}
                    # if tweet is retweet, or not geo_enabled, or place is null, filter out those tweets
                if "RT" in tweet['text'] or not(tweet['user']['geo_enabled']) or not(tweet['place']):
                    pass
                    # if tweet is not from US, filter out
                elif not(tweet['place']['country_code']=='US'):
                    pass
                    # if "geo" field is true, 
                elif tweet['geo']:
                    tweet_cont['user_id'] = tweet['user']['id']
                    tweet_cont['user_name'] = tweet['user']['screen_name']
                    tweet_cont['created_at'] = tweet['created_at']

                    tweet_cont['tweet_text'] = tweet['text']
                    tweet_cont['user_created'] = tweet['user']['created_at']
                    #tweet_cont['hashtag'] = tweet['entities']['hashtags']
                    

                    tweet_cont['Registration_location'] = tweet['user']['location']
                    tweet_cont['Tweet_location'] = tweet['place']['name']

                        #if contains coordinates
                    if tweet['geo']['type']=='Point':
                        lat= tweet['geo']['coordinates'][0]
                        long= tweet['geo']['coordinates'][1]
                        print (lat, long)
                        tweet_cont['coordinates'] = [lat,long]

                        #if contains hashtag, extract the hashtag text and put them into a list
                        if tweet['entities']['hashtags']:
                            hash_list = []
                            for hash_dict in tweet['entities']['hashtags']:
                                hash_list.append(hash_dict['text'])
                                #print (hash_list)
                                tweet_cont['hashtag'] = hash_list

                        geo_tweets.append(tweet_cont)

                        with open(os.path.join(directory, filename +'_geo.txt'),'w') as json_file:
                                json.dump(geo_tweets, json_file, indent =4, sort_keys = True)

    
                    # if no coordinates(not accurate enough) though contains partial geo info(the city name for registration/registration city), 
                    #just use the registration location and city name where the tweet was sent
                else:
                    tweet_cont['user_id'] = tweet['user']['id']
                    tweet_cont['user_name'] = tweet['user']['screen_name']
                    tweet_cont['created_at'] = tweet['created_at']

                    tweet_cont['tweet_text'] = tweet['text']
                    tweet_cont['user_created'] = tweet['user']['created_at']
                    #tweet_cont['hashtag'] = tweet['entities']['hashtags']

                    tweet_cont['Registration_location'] = tweet['user']['location']
                    tweet_cont['Tweet_location'] = tweet['place']['name']
                    
                    #if contains hashtag, extract the hashtag text and put them into a list
                    if tweet['entities']['hashtags']:
                        hash_list = []
                        for hash_dict in tweet['entities']['hashtags']:
                            hash_list.append(hash_dict['text'])
                            #print (hash_list)
                            tweet_cont['hashtag'] = hash_list

                    city_tweets.append(tweet_cont)

                    with open(os.path.join(directory, filename +'_city.txt'),'w') as json_file:
                        json.dump(city_tweets, json_file, indent =4, sort_keys = True)
                    #print(tweet_cont)

            except BaseException as e:
                print (e)

                
    #Close the input file
    input_file.close()
     
     

