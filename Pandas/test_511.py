# UNIT TEST CASES
#
# 511. Game Play Analysis I
# https://leetcode.com/problems/game-play-analysis-i

import unittest
import pandas as pd
import Pandas.task_511 as task
from pandas.testing import assert_frame_equal


class TestCases(unittest.TestCase):
    def test_select_1(self):
        activity_data = pd.DataFrame(
            data={
                'player_id': [1, 1, 2, 3, 3],
                'device_id': [2, 2, 3, 1, 4],
                'event_date': ['2016-03-01', '2016-05-02', '2017-06-25', '2016-03-02', '2018-07-03'],
                'games_played': [5, 6, 1, 0, 5]
            }
        )

        test_dataframe = pd.DataFrame(
            data={
                'player_id': [1, 2, 3],
                'first_login': ['2016-03-01', '2017-06-25', '2016-03-02']
            }
        )

        assert_frame_equal(task.game_analysis(activity_data), test_dataframe)


if __name__ == '__main__':
    unittest.main()
