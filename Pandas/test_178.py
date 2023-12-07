# UNIT TEST CASES
#
# 178. Rank Scores
# https://leetcode.com/problems/rank-scores

import unittest
import pandas as pd
import Pandas.task_178 as task
from pandas.testing import assert_frame_equal


class TestCases(unittest.TestCase):
    def test_select_1(self):
        scores_data = pd.DataFrame(
            data={
                'id': [1, 2, 3, 4, 5, 6],
                'score': [3.50, 3.65, 4.00, 3.85, 4.00, 3.65]
            }
        )

        test_dataframe = pd.DataFrame(
            data={
                'score': [4.00, 4.00, 3.85, 3.65, 3.65, 3.50],
                'rank': [1, 1, 2, 3, 3, 4]
            }
        )

        assert_frame_equal(task.order_scores(scores_data), test_dataframe)

    def test_select_2(self):
        scores_data = pd.DataFrame(
            data={
                'id': [],
                'score': []
            }
        )

        test_dataframe = pd.DataFrame(
            data={
                'score': [],
                'rank': []
            }
        )

        assert_frame_equal(task.order_scores(scores_data), test_dataframe)


if __name__ == '__main__':
    unittest.main()
