# UNIT TEST CASES
#
# 183. Customers Who Never Order
# https://leetcode.com/problems/customers-who-never-order

import unittest
import pandas as pd
import Pandas.task_1148 as task
from pandas.testing import assert_frame_equal


class TestCases(unittest.TestCase):
    def test_select(self):
        views_data = pd.DataFrame(
            data={
                'article_id': [1, 1, 2, 2, 4, 3, 3],
                'author_id': [3, 3, 7, 7, 7, 4, 4],
                'viewer_id': [5, 6, 7, 6, 1, 4, 4],
                'view_date': ['2019-08-01', '2019-08-02', '2019-08-01', '2019-08-02', '2019-07-22', '2019-07-21',
                              '2019-07-21']
            }
        )

        test_dataframe = pd.DataFrame(
            data={
                'id': [4, 7]
            },
            index=[5, 2]
        )

        assert_frame_equal(task.article_views(views_data), test_dataframe)


if __name__ == '__main__':
    unittest.main()
