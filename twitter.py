from twython import Twython
from config import *

twitter = Twython(APP_KEY, APP_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

# auth = twitter.get_authentication_tokens()
# OAUTH_TOKEN = auth['oauth_token']
# OAUTH_TOKEN_SECRET = auth['oauth_token_secret']
# print auth['auth_url']
# verifier = input("Paste the verifier from the URL")

# twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
# final_step = twitter.get_authorized_tokens(verifier)



def tweet_pic(filename, msg="#jaffucci #selfiestand"):
    twitter.update_status_with_media(status=msg,
                                     media=open(filename, 'rb'))
