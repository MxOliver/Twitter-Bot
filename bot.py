import random
import numpy as np
import tweepy 
from time import sleep, time 
from credentials import *

from os import environ
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

STATE_LEN = 5 

words = open('source.txt').read()

corpus = words.split()

def make_pairs(corpus):
    for i in range(len(corpus)-1):
        yield (corpus[i], corpus[i+1])

pairs = make_pairs(corpus) 

word_dict = {}

for word_1, word_2 in pairs:
    if word_1 in word_dict.keys():
        word_dict[word_1].append(word_2)
    else:
        word_dict[word_1] = [word_2]

first_word = np.random.choice(corpus)

chain = [first_word]

n_words = 15

for i in range(n_words):
    chain.append(np.random.choice(word_dict[chain[-1]]))

line = (' '.join(chain))

INTERVAL = 30

result = line.find('.')

if result > 0:
    tweet = line[0:result + 1]
    print(tweet)
    api.update_status(tweet)
    time.sleep(INTERVAL)
else:
    pass 
