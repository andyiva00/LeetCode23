# UNIT TEST CASES
#
# 607. Sales Person
# https://leetcode.com/problems/sales-person

import unittest
import pandas as pd
import Pandas.task_607 as task
from pandas.testing import assert_frame_equal


class TestCases(unittest.TestCase):
    def test_select_1(self):
        sales_person_data = pd.DataFrame(
            data={
                'sales_id': [1, 2, 3, 4, 5],
                'name': ['John', 'Amy', 'Mark', 'Pam', 'Alex'],
                'salary': [100000, 12000, 65000, 25000, 5000],
                'commission_rate': [6, 5, 12, 25, 10],
                'hire_date': ['4/1/2006', '5/1/2010', '12/25/2008', '1/1/2005', '2/3/2007']
            }
        )

        company_data = pd.DataFrame(
            data={
                'com_id': [1, 2, 3, 4],
                'name': ['RED', 'ORANGE', 'YELLOW', 'GREEN'],
                'city': ['Boston', 'New York', 'Boston', 'Austin']
            }
        )

        orders_data = pd.DataFrame(
            data={
                'order_id': [1, 2, 3, 4],
                'order_date': ['1/1/2014', '2/1/2014', '3/1/2014', '4/1/2014'],
                'com_id': [3, 4, 1, 1],
                'sales_id': [4, 5, 1, 4],
                'amount': [10000, 5000, 50000, 25000]
            }
        )

        test_dataframe = pd.DataFrame(
            data={
                'name': ['Amy', 'Mark', 'Alex']
            }
        )

        assert_frame_equal(task.sales_person(sales_person_data, company_data, orders_data),
                           test_dataframe)


if __name__ == '__main__':
    unittest.main()
