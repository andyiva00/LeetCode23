# UNIT TEST CASES
#
# 1907. Count Salary Categories
# https://leetcode.com/problems/count-salary-categories

import unittest
import pandas as pd
import Pandas.task_1907 as task
from pandas.testing import assert_frame_equal


class TestCases(unittest.TestCase):
    def test_select_1(self):
        accounts_data = pd.DataFrame(
            data={
                'account_id': [3, 2, 8, 6],
                'income': [108939, 12747, 87709, 91796]
            }
        )

        test_dataframe = pd.DataFrame(
            data={
                'category': ['Low Salary', 'Average Salary', 'High Salary'],
                'accounts_count': [1, 0, 3]
            }
        )

        assert_frame_equal(task.count_salary_categories(accounts_data), test_dataframe)


if __name__ == '__main__':
    unittest.main()
