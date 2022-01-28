import tweepy
import configparser
from pprint import pprint
import time

config = configparser.ConfigParser()
config.read_file(open('config.ini'))
api_key = config.get('TWITTER', 'API_KEY')
api_secret = config.get('TWITTER', 'API_KEY_SECRET')
client_id = config.get('TWITTER', 'CLIENT_ID')
client_secret = config.get('TWITTER', 'CLIENT_SECRET')
access_token = config.get('TWITTER', 'ACCESS_TOKEN')
access_secret = config.get('TWITTER', 'ACCESS_TOKEN_SECRET')
bearer_token = open('bearer_token.txt').readlines()[0]

# Construct the API instance
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)


try:
    api.verify_credentials()
    print("Authentication OK")
except:
    raise Exception("Error during authentication")

print(auth.get_authorization_url())

# public_tweets = api.home_timeline()
# pprint(public_tweets[0])
print()
already_mentioned = list()
for mention in api.mentions_timeline():
    if mention not in already_mentioned:
        screen_name = mention.user.screen_name
        text = mention.text
        text_wo_name = text.replace('@deepdazebot ', '')
        print(text_wo_name)
        already_mentioned.append(mention)
        print()