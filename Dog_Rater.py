# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 13:54:58 2016

@author: dylanbarth
"""

import praw
import pdb
import numpy
import re
import os
from config_bot import *
version = 0.2
subreddit_1 = "pics"

search_term_positive= ["dog","dogs","doggy","pup","pups","puppy" 
,"puppies","pupper","doggo","woof","bark"]

def Rate():
    prob = numpy.random.uniform(low=0.0, high=1.0, size=None)
    if prob <=0.3:
        return "7/10, great dog!"
    if prob >0.3 and prob<=0.6:
        return "8/10, this dog is a sassy lassie!"
    if prob >0.6 and prob<=0.9:
        return "9/10, such a cutie!"
    if prob >0.9 and prob<0.95:
        return "10/10, absolutely stunning"
    if prob >=0.95:
        return "11/10, HOT DAMN! That's a cute dog!"

def search_reply(submission, rating):
    for i in search_term_positive:
        if submission.id not in posts_replied_to:
            if re.search(i, submission.title, re.IGNORECASE):
                submission.add_comment(rating)
                print "Bot replying to : ", submission.title
                with open("titles_replied_to.txt","a") as title:
                    title.write("Bot replying to : " + str(submission.title))
                posts_replied_to.append(submission.id)


if not os.path.isfile("config_bot.py"):
    sys.exit("You must create a config file with your username and password.")

user_agent = ("Dog_Rater_" + str(version))
r = praw.Reddit(user_agent=user_agent)
r.login(REDDIT_USERNAME,REDDIT_PW)

if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []

else:
    with open("posts_replied_to.txt","r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split('\n')
        posts_replied_to = filter(None, posts_replied_to)
sub = r.get_subreddit(subreddit_1)
for submission in sub.get_top_from_hour(limit=50):
    if submission.id not in posts_replied_to:
        search_reply(submission, Rate())
            
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")