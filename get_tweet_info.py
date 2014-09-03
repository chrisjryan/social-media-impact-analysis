#! /usr/bin/env python

import requests
import random
import json
import argparse
import sys
from twapi import *       # contains OAuth keys/secrets for Twitter API
from time import sleep    # manages API request rate limits


def tweet_get_retweeter_followers(tweet_IDs, maxbatchsize = None, \
                                  outfilename = 'retweeter_info.json'):
    """
    Given a list of tweet ID numbers, harvests a list of retweeters for
    each correpsonding tweet, as well as the number of followers for
    each retweeter. This information can be used as a proxy to measure
    the impact of each tweet.

    arguments:
    tweet_IDs -- A list of Twitter ID numbers, encoded as strings 
        (not ints).

    Keyword arguments:
    maxbatchsize -- The maximum number of tweets you wish to get
        retweeter info for (even if the total tweet list is longer).
    outfilename -- The name of the output file.
    """

    harvesttime_hours = len(tweet_IDs[:maxbatchsize])/60.0

    print 'Harvesting retweeter info for %i tweets will take ~%.2f ' \
          'hours due to Twitter API request rate limits (15 requests ' \
          'per 15 minute window).\n' \
          % (len(tweet_IDs[:maxbatchsize]), harvesttime_hours)

    delta = 100 # the GET users/lookup API request takes in up to 100 user_id numbers at once.
    all_tweet_retweeters = []

    # for each tweet in our list...:
    for tid in tweet_IDs[:maxbatchsize]:
        
        # get a list of IDs of the re-tweeters:
        req_string = 'https://api.twitter.com/1.1/statuses/retweeters/ids.json?id=' \
                      + tid + '&stringify_ids=true'
        resp = requests.get(req_string, auth = oauth) # (rate limit: 15 requests / 15 min)
        
        try:
            retweeter_list = resp.json()['ids']

            # get the number of followers each re-tweeter has
            start_idx = 0
            retweeter_followers = {}
            while start_idx < len(retweeter_list):

                # request user data for up to 100 retweeters at once:
                req_string = 'https://api.twitter.com/1.1/users/lookup.json?user_id=' \
                              + ','.join(retweeter_list[start_idx:start_idx+delta])
                resp = requests.get(req_string, auth = oauth) # (rate limit: 180 requests / 15 min)

                # for each retweeter of the tweet, save their followers_count
                # in the dict we're building:
                for user in resp.json():
                    retweeter_followers[user['screen_name']] = user['followers_count']

                start_idx += delta
                sleep(5) # pause for GET users/lookup rate limit

            # add the data for this new tweet & rewrite the output file anew:
            tweet_rewtweeters_followercount = {}
            tweet_rewtweeters_followercount['tweet_id'] = tid
            tweet_rewtweeters_followercount['retweeters'] = retweeter_followers
            all_tweet_retweeters.append(tweet_rewtweeters_followercount)    
            with file(outfilename,'w') as outfile:
                json.dump(all_tweet_retweeters, outfile, indent = 4)
        except:
            # Info for some tweets, e.g. the one with id# 438693264359968768, 
            # cannot be accessed. (TODO: find out why.)
            print 'tweet id:', tid
            print 'reponse code:', resp
            print 'resp.text:', resp.text
            print '\n'

        sys.stdout.write('.')
        sys.stdout.flush()
        sleep(60) # pause for GET statuses/retweeters/ids rate limit

    sys.stdout.write('\n')

    # TODO: add meaningful key/value to retweeter screen_name and
    # followers_count.


def main(infilename, outfilename, maxbatchsize, maxretweetcount):
    """
    A 'main' function that may be loaded from this module. Takes in 
    command line arguments for specifying parameters for the 
    tweet_get_retweeter_followers() function.

    arguments:
    infilename -- JSON file containing data about tweets. Can be 
        constructed using the GET statuses/retweets/:id from the
        Twitter REST API.
    outfilename -- The name of the output file.
    maxbatchsize -- The maximum number of tweets you wish to get
        retweeter info for (even if the total tweet list is longer).
    maxretweetcount -- Information regarding only the subset of data 
        with retweet counts greater than this number 
        will be harvested.
    """

    # load the tweets & get a list of all tweet IDs that have >5 retweets:
    with open(args.infilename) as infile:
        tweets = json.load(infile)
    tweet_IDs_morethan5 = [t['tweet_id'] for t in tweets \
                           if t['n_retweets'] > maxretweetcount]

    print '\ntotal tweets:\t\t\t%i' % len(tweets)
    print 'tweets with >5 retweets:\t%i' % len(tweet_IDs_morethan5)
    print 'maxbatchsize:\t\t\t%i\n' % maxbatchsize

    # How many tweets with >5 rewteets are from "The Square"'s account?
    # tweets_sq = [t['tweet_id'] for t in tweets \
    #      if t['n_retweets'] > 5 \
    #     and t['user']['screen_name'] == 'TheSquareFilm']

    tweet_get_retweeter_followers(tweet_IDs_morethan5, maxbatchsize,\
                                  outfilename)


if __name__ == '__main__':
    # note: twitter_posts.json contains data for both films.

    desc = """ """ 
    parser = argparse.ArgumentParser(description = desc, \
                                     formatter_class = argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('infilename', help = 'JSON file containing data about tweets. Can be constructed using the GET statuses/retweets/:id from the Twitter REST API.')
    parser.add_argument('-outfilename', help = 'The name of the output file.', \
                        type = str, default = 'retweeter_info.json')
    parser.add_argument('-maxbatchsize', help = 'The maximum number of tweets you wish to get retweeter info for (even if the total tweet list is longer).', \
                        type = int)
    parser.add_argument('-maxretweetcount', help='Information regarding only the subset of data with retweet counts greater than this number will be harvested.', \
                        type = int, default = 5)
    args = parser.parse_args()

    main(args.infilename, args.outfilename, args.maxbatchsize, args.maxretweetcount)
