# UNIT TEST CASES
#
# 1873. Calculate Special Bonus
# https://leetcode.com/problems/calculate-special-bonus

import unittest
import pandas as pd
import Pandas.task_1873 as task
from pandas.testing import assert_frame_equal


class TestCases(unittest.TestCase):
    def test_select(self):
        employees_data = pd.DataFrame(
            data={
                'employee_id': [2, 3, 7, 8, 9],
                'name': ['Meir', 'Michael', 'Addilyn', 'Juan', 'Kannon'],
                'salary': [3000, 3800, 7400, 6100, 7700]
            }
        )

        test_dataframe = pd.DataFrame(
            data={
                'employee_id': [2, 3, 7, 8, 9],
                'bonus': [0, 0, 7400, 0, 7700]
            }
        )

        assert_frame_equal(task.calculate_special_bonus(employees_data), test_dataframe)


if __name__ == '__main__':
    unittest.main()
