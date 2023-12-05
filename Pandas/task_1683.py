# SOLUTION
#
# 1683. Invalid Tweets
# https://leetcode.com/problems/invalid-tweets

import pandas as pd


def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    return tweets[tweets.content.map(len) > 15][['tweet_id']]
