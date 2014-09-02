# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import requests
import random
import json
from twapi import *
from time import sleep


def load_json(filename):
    with open(filename) as infile:
        data = json.load(infile)
    return data

# <codecell>

# load the tweets & get a list of all tweet IDs that have nonzero retweets:
tweets = load_json('./data/twitter_posts.json')
tweet_IDs = [t['tweet_id'] for t in tweets if t['n_retweets'] > 5]


# note: considering only tweets with >5 retweets brings this script from 
# 48 to 8 hours runtime.

# <codecell>

print 'total tweets:\t\t\t', len(tweets)
print 'tweets with >5 retweets:\t', len(tweet_IDs)

# <codecell>

# Harvests a list of retweeters for each tweet in a list, as well as the
# number of followers for each retweeter. This can be used as a proxy to
# measure the impact of each tweet.

delta = 100
all_tweet_retweeters = []

for tid in tweet_IDs[353:]:
    
    # get a list of IDs of the re-tweeters:
    sleep(60)    # (rate limit: 15 requests / 15 min)
    req_string = 'https://api.twitter.com/1.1/statuses/retweeters/ids.json?id=' \
                  + tid + '&stringify_ids=true'
    resp = requests.get(req_string, auth=oauth)
    
    try:
        retweeter_list = resp.json()['ids']

        # get the number of followers each re-tweeter has
        start_idx = 0
        retweeter_followers = {}
        while start_idx < len(retweeter_list):

            # request user data for up to 100 retweeters at once:
            sleep(5)    # (rate limit: 180 requests / 15 min)
            req_string = 'https://api.twitter.com/1.1/users/lookup.json?user_id=' \
                          + ','.join(retweeter_list[start_idx:start_idx+delta])
            resp = requests.get(req_string, auth=oauth)

            # get & add the followers count to the summedDC:
            for user in resp.json():
                retweeter_followers[user['screen_name']] = user['followers_count']

            start_idx += delta

        # add the new data & rewrite the output file anew:
        tweet_rewtweeters_followercount = {}
        tweet_rewtweeters_followercount['tweet_id'] = tid
        tweet_rewtweeters_followercount['retweeters'] = retweeter_followers
        all_tweet_retweeters.append(tweet_rewtweeters_followercount)    
        with file('retweeter_info.json','w') as outfile:
            json.dump(all_tweet_retweeters, outfile, indent=4)
    except:
        print 'tweet id:', tid
        print 'reponse code:', resp
        print 'resp.text:', resp.text
        print '\n'

        
    # TODO: add meaningful key/value to retweeter screen_name and followers_count

# <codecell>

478-len(all_tweet_retweeters)

# <codecell>


