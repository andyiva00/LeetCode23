# UNIT TEST CASES
#
# 1378. Replace Employee ID With The Unique Identifier
# https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier

import unittest
import pandas as pd
import Pandas.task_1378 as task
from pandas.testing import assert_frame_equal


class TestCases(unittest.TestCase):
    def test_select_1(self):
        employees_data = pd.DataFrame(
            data={
                'id': [1, 7, 11, 90, 3],
                'name': ['Alice', 'Bob', 'Meir', 'Winston', 'Jonathan']
            }
        )

        employee_uni_data = pd.DataFrame(
            data={
                'id': [3, 11, 90],
                'unique_id': [1, 2, 3]
            }
        )

        test_dataframe = pd.DataFrame(
            data={
                'unique_id': [None, None, 2, 3, 1],
                'name': ['Alice', 'Bob', 'Meir', 'Winston', 'Jonathan']
            }
        )

        assert_frame_equal(task.replace_employee_id(employees_data, employee_uni_data), test_dataframe)


if __name__ == '__main__':
    unittest.main()
