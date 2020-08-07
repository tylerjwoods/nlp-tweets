# import the necessary packages
import os 
import tweepy as tw 
import pandas as pd 

# import class that contains secret keys
from secret_keys import Secret_Keys

# initiliaze a class from secret_keys that contains
# attributes for the secret keys
keys = Secret_Keys()

auth = tw.OAuthHandler(keys.consumer_key, keys.consumer_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)