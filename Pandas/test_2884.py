# UNIT TEST CASES
#
# 2884. Modify Columns
# https://leetcode.com/problems/modify-columns

import unittest
import pandas as pd
import Pandas.task_2884 as task
from pandas.testing import assert_frame_equal


class TestCases(unittest.TestCase):
    def test_modify_salary_column(self):
        employees_data = pd.DataFrame(
            {
                'name': ['Jack', 'Piper', 'Mia', 'Ulysses'],
                'salary': [19666, 74754, 62509, 54866]
            }
        )

        test_dataframe = pd.DataFrame(
            data={
                'name': ['Jack', 'Piper', 'Mia', 'Ulysses'],
                'salary': [39332, 149508, 125018, 109732]
            }
        )

        assert_frame_equal(task.modify_salary_column(employees_data), test_dataframe)


if __name__ == '__main__':
    unittest.main()
