import tweepy, time, sys, codecs
from statics import INTERVAL_TEST
from os import environ


# keep the quotes, replace this with your consumer key
CONSUMER_KEY = environ['CONSUMER_KEY']
# keep the quotes, replace this with your consumer secret key
CONSUMER_SECRET = environ['CONSUMER_SECRET']
# keep the quotes, replace this with your access token
ACCESS_KEY = environ['ACCESS_KEY']
# keep the quotes, replace this with your access token secret
ACCESS_SECRET = environ['ACCESS_SECRET']


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
filename = codecs.open('test', 'r', 'utf-8')

f = filename.readlines()
filename.close()

string = ''
for line in f:
    if string == '':
        string = line
    else:
        string = string + '\n' + line
    if line == '':
        api.update_status(string)
        time.sleep(INTERVAL_TEST)

