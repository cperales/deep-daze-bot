import tweepy
import configparser
from deep_daze import Imagine
from deep_translator import GoogleTranslator
import torch
import gc

config = configparser.ConfigParser()
config.read_file(open('config.ini'))
api_key = config.get('TWITTER', 'API_KEY')
api_secret = config.get('TWITTER', 'API_KEY_SECRET')
client_id = config.get('TWITTER', 'CLIENT_ID')
client_secret = config.get('TWITTER', 'CLIENT_SECRET')
access_token = config.get('TWITTER', 'ACCESS_TOKEN')
access_secret = config.get('TWITTER', 'ACCESS_TOKEN_SECRET')
bearer_token = open('bearer_token.txt').readlines()[0]



class MyStreamListener(tweepy.Stream):
    def on_status(self, status):
        # properties of the tweet
        text = status.text
        tweet_id = status.id
        screen_name = status.user.screen_name

        # Extract the text
        text = text.lower()
        text_wo_name = text.replace('@deepdazebot', '')
        text_wo_name = GoogleTranslator(source='auto',
                                        target='en').translate(text_wo_name)
        filename = text_wo_name.replace(' ', '_') + '.jpg'

        # Imagine
        self.dream(text_wo_name)

        # Reply
        # Construct the API instance for replying tweets
        auth = tweepy.OAuthHandler(api_key, api_secret)
        auth.set_access_token(access_token, access_secret)
        api = tweepy.API(auth)

        try:
            api.verify_credentials()
            print("Authentication OK")
        except:
            raise Exception("Error during authentication")

        api.update_status_with_media(filename=filename,
                                     status='.@' + screen_name + ' Your words were dreamt',
                                     in_reply_to_status_id=tweet_id)

    def on_error(self, status_code):
        if status_code == 420:
            # Reply
            # Construct the API instance for replying tweets
            auth = tweepy.OAuthHandler(api_key, api_secret)
            auth.set_access_token(access_token, access_secret)
            api = tweepy.API(auth)

            try:
                api.verify_credentials()
                print("Authentication OK")
            except:
                raise Exception("Error during authentication")

            api.update_status(status='@Relampague bot goes offline')

            #returning False in on_data disconnects the stream
            return False

    @staticmethod
    def dream(text):
        imagine = Imagine(
            text=text,
            image_width=256,
            num_layers=24,
            batch_size=4,
            epochs=3,
            iterations=800,
            save_progress=True,
            open_folder=False,
            gradient_accumulate_every=1
        )
        imagine()
        del imagine
        gc.collect()
        torch.cuda.empty_cache()

# Instance the stream
myStream = MyStreamListener(consumer_key=api_key,
                                    consumer_secret=api_secret,
                                    access_token=access_token,
                                    access_token_secret=access_secret)
myStream.filter(track=['@deepdazebot'])
