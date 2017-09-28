import praw
import config

def bot_login():
    r = praw.Reddit(username = config.username,
                password = config.password,
                client_id = config.client_id,
                client_secret = config.client_secret,
                user_agent = "my thing")
    return r

def run_bot(r):
    for soccerPosts in r.subreddit('soccer').hot(limit=5):
        soccerHeadline = soccerPosts.title
        with open("soccerPost.txt", "a") as m:
            m.write(soccerHeadline.encode("utf-8") + "\n")
        print soccerHeadline + "\n"

    print " **************** "
    for wnPosts in r.subreddit('worldnews').hot(limit=5):
        wnHeadline = wnPosts.title
        with open("wnPost.txt", "a") as m:
            m.write(wnHeadline.encode("utf-8") + "\n")
        print wnHeadline + "\n"


r = bot_login()

run_bot(r)

