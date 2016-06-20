# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 14:28:52 2016

@author: dylanbarth
"""

import praw
import pdb
import re
import os
from config_bot import *
version = 0.1

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
sub = r.get_subreddit('pythonforengineers')
for submission in sub.get_hot(limit=10):
    if submission.id not in posts_replied_to:
        if re.search("i love python", submission.title, re.IGNORECASE):
            submission.add_comment("why?")
            print "Bot replying to : ", submission.title
            posts_replied_to.append(submission.id)
            
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")