import tweepy, time, sys, codecs
from statics import INTERVAL
argfile = str(sys.argv[1])
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


for line in f:
    api.update_status(line)
    time.sleep(INTERVAL)

