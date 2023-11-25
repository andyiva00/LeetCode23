# UNIT TEST CASES
#
# 2879. Display the First Three Rows
# https://leetcode.com/problems/display-the-first-three-rows

import unittest
import pandas as pd
import Pandas.task_2879 as task
from pandas.testing import assert_frame_equal


class TestCases(unittest.TestCase):
    def test_getting_top_3(self):
        employees_data = pd.DataFrame(
            {
                'employee_id ': [3, 90, 9, 60, 49, 43],
                'name': ['Bob', 'Alice', 'Tatiana', 'Annabelle', 'Jonathan', 'Khaled'],
                'department ': ['Operations', 'Sales', 'Engineering', 'InformationTechnology', 'HumanResources',
                                'Administration'],
                'salary': [48675, 11096, 33805, 37678, 23793, 40454]
            }
        )

        test_dataframe = pd.DataFrame(
            {
                'employee_id ': [3, 90, 9],
                'name': ['Bob', 'Alice', 'Tatiana'],
                'department ': ['Operations', 'Sales', 'Engineering'],
                'salary': [48675, 11096, 33805]
            }
        )

        assert_frame_equal(task.select_first_rows(employees_data), test_dataframe)


if __name__ == '__main__':
    unittest.main()
