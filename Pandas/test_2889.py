# UNIT TEST CASES
#
# 2889. Reshape Data: Pivot
# https://leetcode.com/problems/reshape-data-pivot

import unittest
import pandas as pd
import Pandas.task_2889 as task
from pandas.testing import assert_frame_equal


class TestCases(unittest.TestCase):
    def test_pivoting_table(self):
        weather_data = pd.DataFrame(
            data={
                'city': ['Jacksonville', 'Jacksonville', 'Jacksonville', 'Jacksonville', 'Jacksonville', 'ElPaso',
                         'ElPaso', 'ElPaso', 'ElPaso', 'ElPaso'],
                'month': ['January', 'February', 'March', 'April', 'May', 'January', 'February', 'March', 'April',
                          'May'],
                'temperature': [13, 23, 38, 5, 34, 20, 6, 26, 2, 43]
            }
        )

        test_dataframe = pd.DataFrame(
            data={
                'month': ['April', 'February', 'January', 'March', 'May'],
                'ElPaso': [2, 6, 20, 26, 43],
                'Jacksonville': [5, 23, 13, 38, 34]
            }
        )

        assert_frame_equal(task.pivot_table(weather_data), test_dataframe)


if __name__ == '__main__':
    unittest.main()
