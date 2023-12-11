# UNIT TEST CASES
#
# 1484. Group Sold Products By The Date
# https://leetcode.com/problems/group-sold-products-by-the-date

import unittest
import pandas as pd
import Pandas.task_1484 as task
from pandas.testing import assert_frame_equal


class TestCases(unittest.TestCase):
    def test_select_1(self):
        activities_data = pd.DataFrame(
            data={
                'sell_date': ['2020-05-30', '2020-06-01', '2020-06-02', '2020-05-30', '2020-06-01', '2020-06-02',
                              '2020-05-30'],
                'product': ['Headphone', 'Pencil', 'Mask', 'Basketball', 'Bible', 'Mask', 'T-Shirt']
            }
        )

        test_dataframe = pd.DataFrame(
            data={
                'sell_date': ['2020-05-30', '2020-06-01', '2020-06-02'],
                'num_sold': [3, 2, 1],
                'products': ['Basketball,Headphone,T-Shirt', 'Bible,Pencil', 'Mask']
            }
        )

        assert_frame_equal(task.categorize_products(activities_data), test_dataframe)


if __name__ == '__main__':
    unittest.main()
