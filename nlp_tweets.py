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



## to make a new environment, python -m venv env
## to activate environment, do source env/bin/activate
## to get out of virtual environment, do deactivate
## to delete the environment, rm -rf env
## https://www.earthdatascience.org/courses/use-data-open-source-python/intro-to-apis/twitter-data-in-python/
