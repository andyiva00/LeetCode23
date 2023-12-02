# UNIT TEST CASES
#
# 183. Customers Who Never Order
# https://leetcode.com/problems/customers-who-never-order

import unittest
import pandas as pd
import Pandas.task_183 as task
from pandas.testing import assert_frame_equal


class TestCases(unittest.TestCase):
    def test_select(self):
        customers_data = pd.DataFrame(
            data={
                'id': [1, 2, 3, 4],
                'name': ['Joe', 'Henry', 'Sam', 'Max']
            }
        )

        orders_data = pd.DataFrame(
            data={
                'id': [1, 2],
                'customerId': [3, 1]
            }
        )

        test_dataframe = pd.DataFrame(
            data={
                'Customers': ['Henry', 'Max']
            },
            index=[1, 3]
        )

        assert_frame_equal(task.find_customers(customers_data, orders_data), test_dataframe)


if __name__ == '__main__':
    unittest.main()
