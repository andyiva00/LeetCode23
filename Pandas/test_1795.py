# UNIT TEST CASES
#
# 1795. Rearrange Products Table
# https://leetcode.com/problems/rearrange-products-table

import unittest
import pandas as pd
import Pandas.task_1795 as task
from pandas.testing import assert_frame_equal


class TestCases(unittest.TestCase):
    def test_select_1(self):
        products_data = pd.DataFrame(
            data={
                'product_id': [0, 1],
                'store1': [95, 70],
                'store2': [100, None],
                'store3': [105, 80]
            }
        )

        test_dataframe = pd.DataFrame(
            data={
                'product_id': [0, 0, 0, 1, 1],
                'store': ['store1', 'store2', 'store3', 'store1', 'store3'],
                'price': [95, 100, 105, 70, 80]
            },
            index=[0, 2, 4, 1, 5]
        )

        assert_frame_equal(task.rearrange_products_table(products_data), test_dataframe)


if __name__ == '__main__':
    unittest.main()
