# UNIT TEST CASES
#
# 2882. Drop Duplicate Rows
# https://leetcode.com/problems/drop-duplicate-rows

import unittest
import pandas as pd
import Pandas.task_2882 as task
from pandas.testing import assert_frame_equal


class TestCases(unittest.TestCase):
    def test_creating_column(self):
        customers_data = pd.DataFrame(
            {
                'customer_id': [1, 2, 3, 4, 5, 6],
                'name': ['Ella', 'David', 'Zachary', 'Alice', 'Finn', 'Violet'],
                'email': ['emily@example.com', 'michael@example.com', 'sarah@example.com', 'john@example.com',
                          'john@example.com', 'alice@example.com']
            }
        )

        test_dataframe = pd.DataFrame(
            data={
                'customer_id': [1, 2, 3, 4, 6],
                'name': ['Ella', 'David', 'Zachary', 'Alice', 'Violet'],
                'email': ['emily@example.com', 'michael@example.com', 'sarah@example.com', 'john@example.com',
                          'alice@example.com']
            },
            index=[0, 1, 2, 3, 5]
        )

        assert_frame_equal(task.drop_duplicate_emails(customers_data), test_dataframe)


if __name__ == '__main__':
    unittest.main()
