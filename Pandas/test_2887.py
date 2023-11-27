# UNIT TEST CASES
#
# 2887. Fill Missing Data
# https://leetcode.com/problems/fill-missing-data

import unittest
import pandas as pd
import Pandas.task_2887 as task
from pandas.testing import assert_frame_equal


class TestCases(unittest.TestCase):
    def test_filling_missing_values(self):
        products_data = pd.DataFrame(
            data=
            {
                'name': pd.Series(data=['Wristwatch', 'WirelessEarbuds', 'GolfClubs', 'Printer']),
                'quantity': pd.Series(data=[None, None, 779, 849]),
                'price': pd.Series(data=[135, 821, 9319, 3051])
            }
        )

        test_dataframe = pd.DataFrame(
            data=
            {
                'name': pd.Series(
                    data=['Wristwatch', 'WirelessEarbuds', 'GolfClubs', 'Printer'],
                    dtype='str'),
                'quantity': pd.Series(
                    data=[0, 0, 779, 849],
                    dtype='int'),
                'price': pd.Series(
                    data=[135, 821, 9319, 3051],
                    dtype='int64')
            }
        )

        assert_frame_equal(task.fill_missing_values(products_data), test_dataframe)


if __name__ == '__main__':
    unittest.main()
