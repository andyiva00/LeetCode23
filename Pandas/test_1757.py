# UNIT TEST CASES
#
# 1757. Recyclable and Low Fat Products
# https://leetcode.com/problems/recyclable-and-low-fat-products

import unittest
import pandas as pd
import Pandas.task_1757 as task
from pandas.testing import assert_frame_equal


class TestCases(unittest.TestCase):
    def test_select(self):
        products_data = pd.DataFrame(
            data={
                'product_id': [0, 1, 2, 3, 4],
                'low_fats': ['Y', 'Y', 'N', 'Y', 'N'],
                'recyclable': ['N', 'Y', 'Y', 'Y', 'N']
            }
        )

        test_dataframe = pd.DataFrame(
            data={
                'product_id': [1, 3]
            },
            index=[1, 3]
        )

        assert_frame_equal(task.find_products(products_data), test_dataframe)


if __name__ == '__main__':
    unittest.main()
