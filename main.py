import praw
from datetime import datetime, timedelta

reddit = praw.Reddit(
    user_agent=True,
    client_id="REDDIT_CLIENT_ID",
    client_secret="REDDIT_CLIENT_SECRET",
    username="CLIENT_USERNAME",
    password="CLIENT_PASSWORD"
)

title_of_reddit = input("Enter your title: ")
content_of_reddit = input('Enter your content: ')

subreddit = reddit.subreddit('pythonsandlot')
title = title_of_reddit
content = content_of_reddit
subreddit.submit(title=title,selftext=content)