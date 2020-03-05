import requests, time
from statics import WAKER_INTERVAL


def timer():
    requests.post(url="https://twitter-bot-wishwork.herokuapp.com/")
    time.sleep(WAKER_INTERVAL)


timer()
