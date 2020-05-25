import pandas as pd
import re
import json
from pandas.io.json import json_normalize

# input_file = r'C:\data\covid\COVID_analysis\0327_0503_geo_2.json'
# '0327_0503_geo_txt.txt' can be mapped,but the there was limited # for each race or career group, thus was not used and adopted the file with city name
#input_file = r'C:\data\covid\COVID_analysis\0327_0503_geo_txt.txt'

f = open(input_file,'r')
geo_tweets=[]

for line in f:
    if line.strip():
        tweet = json.loads(line)
        try:
            tweet_cont = {}
                # if tweet is retweet, or not geo_enabled, or place is null, filter out those tweets
            tweet_cont['user_id'] = tweet['user_id']
            tweet_cont['user_name'] = tweet['user_name']
            tweet_cont['Registration_location'] = tweet['Registration_location']
            tweet_cont['Tweet_location'] = tweet['Tweet_location']
            tweet_cont['created_at'] = tweet['created_at']
            tweet_cont['tweet_text'] = tweet['tweet_text']
            tweet_cont['user_created'] = tweet['user_created']
            tweet_cont['user_id'] = tweet['user_id']
            tweet_cont['user_name'] = tweet['user_name']
            
            if 'coordinates' in tweet.keys():
                tweet_cont['coordinates']= tweet['coordinates']
            else:
                tweet_cont['coordinates']= ''
            
            if 'hashtag' in tweet.keys():
                tweet_cont['hashtag']= tweet['hashtag']
            else:
                tweet_cont['hashtag']= ''
            
            geo_tweets.append(tweet_cont)

        except BaseException as e:
            print (e)
df = pd.DataFrame(geo_tweets)
df.to_csv('geotweets_df.csv')
#Close the input file
f.close()              
