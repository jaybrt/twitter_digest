import credentials
from tweepy import OAuthHandler, API

if __name__ == '__main__':
    auth = OAuthHandler(credentials.CONSUMER_KEY, credentials.CONSUMER_SECRET)
    auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)

    api = API(auth)

    public_tweets = api.home_timeline()

    for tweet in public_tweets:
        print(tweet.text)
