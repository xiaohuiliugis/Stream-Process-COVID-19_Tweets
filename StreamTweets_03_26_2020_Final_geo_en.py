# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 16:12:23 2020
The script only download geo-tagged tweets or tweets with country and city location, and English, and excluded retweets
Twitter reject the download request after a very short time of streaming. So had to remove all filters to download all tweets

!!! Before execute, need to update the generated filename !!!
!!! Also, check the consumer key, consumer secret, access token, access secret!!!
@author: liux29
"""


from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import json


#consumer key, consumer secret, access token, access secret.
ckey="ovY5NsMZkJrJaJ8ICCs3RlZDB"
csecret="iQEL4ftPWqGwy6NOOCRh4UzlIFkNBnJcFcYGIUeYNWvIG3HQWE"
atoken="752330143-0xXaj1mUXdmiRpypct6jwE1UrfVsW7ON6znTfaV4"
asecret="9yriOtNqOFomDf0GXt1EPzODeuID4U4ENTgQHgMNt9fmD"

tweets = []
geo_tweets=[]

class listener(StreamListener):

    def on_data(self, data):
      
        try:
            tweet = json.loads(data)
            tweet_cont = {}
            if "RT" in tweet['text'] or not(tweet['user']['geo_enabled']) or not(tweet['place']):
                pass
            
            elif not(tweet['place']['country_code']=='US'):
                pass
            elif tweet['geo']:
                tweet_cont['user_id'] = tweet['user']['id']
                tweet_cont['user_name'] = tweet['user']['screen_name']
                tweet_cont['created_at'] = tweet['created_at']
            
                tweet_cont['tweet_text'] = tweet['text']
                tweet_cont['user_created'] = tweet['user']['created_at']
                tweet_cont['lang'] = tweet['lang']
                tweet_cont['hashtag'] = tweet['entities']['hashtags']
            
                tweet_cont['location_1'] = tweet['user']['location']
                tweet_cont['location_2'] = tweet['place']['name']
                
                if tweet['geo']['type']=='Point':
                    lat= tweet['geo']['coordinates'][0]
                    long= tweet['geo']['coordinates'][1]
                    print (lat, long)
                    tweet_cont['coordinates'] = [lat,long]
                       
                    geo_tweets.append(tweet_cont)
                    
                    with open('tweets_geo_2.txt','w') as json_file:
                        json.dump(geo_tweets, json_file, indent =4, sort_keys = True)
            else:
                                
                tweet_cont['user_id'] = tweet['user']['id']
                tweet_cont['user_name'] = tweet['user']['screen_name']
                tweet_cont['created_at'] = tweet['created_at']
            
                tweet_cont['tweet_text'] = tweet['text']
                tweet_cont['user_created'] = tweet['user']['created_at']
                tweet_cont['lang'] = tweet['lang']
                tweet_cont['hashtag'] = tweet['entities']['hashtags']
            
                tweet_cont['location_1'] = tweet['user']['location']
                tweet_cont['location_2'] = tweet['place']['name']
                tweets.append(tweet_cont)
                
                with open('tweet_json_7.txt','w') as json_file:
                    json.dump(tweets, json_file, indent =4, sort_keys = True)
           
        except BaseException as e:
            print (e)
            time.sleep(5)
            

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=['test positive' , 'covid' , 'covid19' , 'covid-19', 'covid_19' , 'crona' , 'cronavirus' , 'confirmed cases' , 'TrumpMeltdown' , 'Fauci' , 'quarantine' , 'FLATTEN THE CURVE' , 'PanicBuying' , '2019-nCov' , 'Outbreak' , 'Virus' , 'Pandemic' , 'Infection' , 'NIAID' , 'Biogen' , 'CDC' , 'WHO' , 'Chinese American', 'Asian American', 'shutdown','covid','lockdown', 'layoffs','#lifeafterlockup','#ThankYouPresidentTrump','#CoronaCrisis','#CALockdown','#QuarantineLife','#SOCIALDISTANCING','#FLATTENTHECURVE','#CHINESEVIRUS','#Covid19','#Coronavirus','#2019Ncov','#Sarscov2','#Wuhan','#Covid-19','#Covid2019','#Covid_19','#COVIDIOT'])