# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 16:12:23 2020

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
            print (data)
            saveFile = open('twiDB.csv','a')
            saveFile.write(data)
            saveFile.write('\n')
            saveFile.close()
            return True
        except BaseException as e:
            print (e)
            time.sleep(5)
            
    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=['test positive' , 'covid' , 'covid19' , 'covid-19', 'covid_19' , 'crona' , 'cronavirus' , 'confirmed cases' , 'TrumpMeltdown' , 'Fauci' , 'quarantine' , 'FLATTEN THE CURVE' , 'PanicBuying' , '2019-nCov' , 'Outbreak' , 'Virus' , 'Pandemic' , 'Infection' , 'NIAID' , 'Biogen' , 'CDC' , 'WHO' , 'Chinese American', 'Asian American', 'shutdown','covid','lockdown', 'layoffs','#lifeafterlockup','#ThankYouPresidentTrump','#CoronaCrisis','#CALockdown','#QuarantineLife','#SOCIALDISTANCING','#FLATTENTHECURVE','#CHINESEVIRUS','#Covid19','#Coronavirus','#2019Ncov','#Sarscov2','#Wuhan','#Covid-19','#Covid2019','#Covid_19','#COVIDIOT'])