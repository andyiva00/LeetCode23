# UNIT TEST CASES
#
# 177. Nth Highest Salary
# https://leetcode.com/problems/nth-highest-salary

import unittest
import pandas as pd
import Pandas.task_177 as task
from pandas.testing import assert_frame_equal


class TestCases(unittest.TestCase):
    def test_select_1(self):
        patients_data = pd.DataFrame(
            data={
                'id': [1, 2, 3],
                'salary': [100, 200, 300]
            }
        )

        test_dataframe = pd.DataFrame(
            data={
                'getNthHighestSalary(2)': [200]
            }
        )

        assert_frame_equal(task.nth_highest_salary(patients_data, 2), test_dataframe)

    def test_select_2(self):
        patients_data = pd.DataFrame(
            data={
                'id': [1],
                'salary': [100]
            }
        )

        test_dataframe = pd.DataFrame(
            data={
                'getNthHighestSalary(2)': [None]
            }
        )

        assert_frame_equal(task.nth_highest_salary(patients_data, 2), test_dataframe)

    def test_select_3(self):
        patients_data = pd.DataFrame(
            data={
                'id': [1, 2],
                'salary': [100, 100]
            }
        )

        test_dataframe = pd.DataFrame(
            data={
                'getNthHighestSalary(2)': [None]
            }
        )

        assert_frame_equal(task.nth_highest_salary(patients_data, 2), test_dataframe)

    def test_select_4(self):
        patients_data = pd.DataFrame(
            data={
                'id': [1, 2, 3],
                'salary': [100, 200, 300]
            }
        )

        test_dataframe = pd.DataFrame(
            data={
                'getNthHighestSalary(1)': [300]
            }
        )

        assert_frame_equal(task.nth_highest_salary(patients_data, 1), test_dataframe)


if __name__ == '__main__':
    unittest.main()
