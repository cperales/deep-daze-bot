import tweepy
import configparser

config = configparser.ConfigParser()
config.read_file(open('config.ini'))
api_key = config.get('TWITTER', 'API_KEY')
api_key_secret = config.get('TWITTER', 'API_KEY_SECRET')
bearer_token = open('bearer_token.txt').readlines()[0]
auth = tweepy.OAuth2BearerHandler(bearer_token=bearer_token)

# Create API object
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

api.update_status("Test tweet from Deep Daze Bot. Hello world!")
