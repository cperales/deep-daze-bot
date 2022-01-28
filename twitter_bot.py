import tweepy
import configparser

config = configparser.read('config.ini')
api_key = config.get('API_KEY')
api_key_secret = config.get('API_KEY_SECRET')
bearer_token = config.get('BEARER_TOKEN')
auth = tweepy.Client(bearer_token=bearer_token)

# Create API object
api = tweepy.API(auth)

api = tweepy.API(auth)