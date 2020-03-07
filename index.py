import tweepy, time, sys, codecs
from statics import INTERVAL, INTERVAL_TEST
from credentials import *


# keep the quotes, replace this with your consumer key
CONSUMER_KEY = CONSUMER_KEY
# keep the quotes, replace this with your consumer secret key
CONSUMER_SECRET = CONSUMER_SECRET
# keep the quotes, replace this with your access token
ACCESS_KEY = ACCESS_KEY
# keep the quotes, replace this with your access token secret
ACCESS_SECRET = ACCESS_SECRET


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
        continue
    if line != 'end' and string != '' and line != 'next\n':
        string += '\n' + line
        continue
    if line == 'next\n' or line == 'end':
        api.update_status(string)
        string = ''
        time.sleep(INTERVAL)

