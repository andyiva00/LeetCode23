# UNIT TEST CASES
#
# 1683. Invalid Tweets
# https://leetcode.com/problems/invalid-tweets

import unittest
import pandas as pd
import Pandas.task_1683 as task
from pandas.testing import assert_frame_equal


class TestCases(unittest.TestCase):
    def test_select(self):
        tweets_data = pd.DataFrame(
            data={
                'tweet_id': [1, 2],
                'content': ['Vote for Biden', 'Let us make America great again!']
            }
        )

        test_dataframe = pd.DataFrame(
            data={
                'tweet_id': [2]
            },
            index=[1]
        )

        assert_frame_equal(task.invalid_tweets(tweets_data), test_dataframe)


if __name__ == '__main__':
    unittest.main()
