#!/usr/bin/python
import tweepy
import csv

# All credentials that i generated from twitter developer account
access_token = '1143562756160917504-U5ollAZV6K6n2VvHooeZh5Z15llEgc'
access_token_secret = 'CRJuuhTLn5ldtd90kSWVUOX0wTLDRtG0UxVoLX9iwVr4p'
consumer_key = 'hFicrEXKbIJbMgVVRiaccJSzN'
consumer_secret = 'xRHtAWbo9UxK1gpOKlq4u6vBMS6QFnaQf7AH3sMr4CzBVBeHlW'

#
auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):

        #print(status.author.screen_name, status.created_at, status.text)
        with open('Stream_Tweets.csv', 'a', newline='', encoding="utf-8") as csvFile:
            csv_writer = csv.writer(csvFile, delimiter=',')
            csv_writer.writerow([status.created_at, status.text, status.user.location])

    def on_error(self, status_code):

        print("Error found.! Code is :- ", status_code)
        return True

    def on_timeout(self):

        print("Timed out.!")
        return True


counter = 1
if counter <= 1:
    with open('Stream_Tweets.csv', 'a', newline='', encoding="utf-8") as csvHeader:
        csvf = csv.writer(csvHeader, delimiter=',')
        csvf.writerow(["Tweet_Time", "Tweet_Text", "Tweet_Location"])
    counter += 1

myStream = tweepy.streaming.Stream(auth, MyStreamListener())
myStream.filter(track=['Canada import', 'Canada export', 'Canada vehicle sales', 'Canada Education', 'Canada'])




