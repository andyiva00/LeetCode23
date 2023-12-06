# UNIT TEST CASES
#
# 184. Department Highest Salary
# https://leetcode.com/problems/department-highest-salary

import unittest
import pandas as pd
import Pandas.task_184 as task
from pandas.testing import assert_frame_equal


class TestCases(unittest.TestCase):
    def test_select_1(self):
        employee_data = pd.DataFrame(
            data={
                'id': [1, 2, 3, 4, 5],
                'name': ['Joe', 'Jim', 'Henry', 'Sam', 'Max'],
                'salary': [70000, 90000, 80000, 60000, 90000],
                'departmentId': [1, 1, 2, 2, 1]
            }
        )

        department_data = pd.DataFrame(
            data={
                'id': [1, 2],
                'name': ['IT', 'Sales']
            }
        )

        test_dataframe = pd.DataFrame(
            data={
                'Department': ['IT', 'Sales', 'IT'],
                'Employee': ['Jim', 'Henry', 'Max'],
                'Salary': [90000, 80000, 90000],
            }
        )

        assert_frame_equal(task.department_highest_salary(employee_data, department_data), test_dataframe)

    def test_select_2(self):
        employee_data = pd.DataFrame(
            data={
                'id': [1, 2, 4],
                'name': ['Joe', 'Sam', 'Max'],
                'salary': [60000, 50000, 50000],
                'departmentId': [1, 1, 2]
            }
        )

        department_data = pd.DataFrame(
            data={
                'id': [1, 2],
                'name': ['IT', 'HR']
            }
        )

        test_dataframe = pd.DataFrame(
            data={
                'Department': ['IT', 'HR'],
                'Employee': ['Joe', 'Max'],
                'Salary': [60000, 50000],
            }
        )

        assert_frame_equal(task.department_highest_salary(employee_data, department_data), test_dataframe)


if __name__ == '__main__':
    unittest.main()
