# UNIT TEST CASES
#
# 586. Customer Placing the Largest Number of Orders
# https://leetcode.com/problems/customer-placing-the-largest-number-of-orders

import unittest
import pandas as pd
import Pandas.task_586 as task
from pandas.testing import assert_frame_equal


class TestCases(unittest.TestCase):
    def test_select_1(self):
        orders_data = pd.DataFrame(
            data={
                'order_number': [1, 2, 3, 4],
                'customer_number': [1, 2, 3, 3]
            }
        )

        test_dataframe = pd.DataFrame(
            data={
                'customer_number': [3]
            }
        )

        assert_frame_equal(task.largest_orders(orders_data), test_dataframe)


if __name__ == '__main__':
    unittest.main()
