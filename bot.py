import tweepy
import time
import random

# Authenticate to Twitter
auth = tweepy.OAuthHandler("TOKEN")
auth.set_access_token("TOKEN")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

def suffle():

    with open('jurons.csv', 'r') as r, open('new_jurons.csv', 'w') as w:
        data = r.readlines()
        header, rows = data[0], data[1:]
        random.shuffle(rows)
        rows = '\n'.join([row.strip() for row in rows])
        w.write(header + rows)

def get_random_juron():

    with open('jurons.csv', 'r') as file:
        data = file.readlines()
        for line in data:
            word = line.capitalize()
            print(word)
            post_tweet(juron=word)
            time.sleep(10800)

def post_tweet(juron):
    # Create a tweet
    api.update_status(juron)

if __name__ == "__main__":
    get_random_juron()
