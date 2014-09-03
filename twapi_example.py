
# To use 'get_tweet_info.py', modify the OAuth1 object below to include valid 
# key/secret values for the Twitter API and then rename this file to be 'twapi.py'.

from requests_oauthlib import OAuth1

# for twitter API authentication:
oauth = OAuth1('aaaAaaAA111a1aAA11AAAaaaa', \
               client_secret='BBbBBbB22BbbbbB2bb2b2b2b2b2bBBB2b2b2bB2b2bbbbBBBBB', \
               resource_owner_key='3333333333-c3c3c3c3c3cCCcCCCc33cc3cCC3ccc3ccc33cCC', \
               resource_owner_secret='D4D4DddD44D4DddddDDDD444DdddddDDDD44d4d4d444DDD4dd')
