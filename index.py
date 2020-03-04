import tweepy, time, sys, codecs
from credentials import *
from statics import INTERVAL
argfile = str(sys.argv[1])


# keep the quotes, replace this with your consumer key
CONSUMER_KEY = CONSUMER_KEY_T
# keep the quotes, replace this with your consumer secret key
CONSUMER_SECRET = CONSUMER_SECRET_T
# keep the quotes, replace this with your access token
ACCESS_KEY = ACCESS_KEY_T
# keep the quotes, replace this with your access token secret
ACCESS_SECRET = ACCESS_SECRET_T


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
filename = codecs.open('test', 'r', 'utf-8')

f = filename.readlines()
filename.close()


for line in f:
    api.update_status(line)
    time.sleep(INTERVAL)

