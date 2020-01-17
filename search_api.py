#!/usr/bin/python
import tweepy
import csv

# All credentials that i generated from twitter developer account
access_token = '1143562756160917504-U5ollAZV6K6n2VvHooeZh5Z15llEgc'
access_token_secret = 'CRJuuhTLn5ldtd90kSWVUOX0wTLDRtG0UxVoLX9iwVr4p'
consumer_key = 'hFicrEXKbIJbMgVVRiaccJSzN'
consumer_secret = 'xRHtAWbo9UxK1gpOKlq4u6vBMS6QFnaQf7AH3sMr4CzBVBeHlW'

# Giving the credentials
auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Creating the csv file if not already present
csvFile = open('Search_Tweets.csv', 'wt', newline='', encoding="utf-8")

csvWriter = csv.writer(csvFile, delimiter=',')
csvWriter.writerow(["Tweet_Time", "Tweet_Text", "Tweet_Location"])

# Specific keywords that i need to retrieve
my_keywords = "(Canada AND Education) OR (Canada AND import) OR (Canada AND export) OR (Canada vehicle sales) OR Canada"

# Storing 1000 tweets
myList = tweepy.Cursor(api.search, q=my_keywords, lang="en").items(1000)
for tweet in myList:
    csvWriter.writerow([tweet.created_at, tweet.text, tweet.user.location])
    #print(tweet)

# Finally closing my  csvfile
csvFile.close()
