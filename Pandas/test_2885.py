# UNIT TEST CASES
#
# 2885. Rename Columns
# https://leetcode.com/problems/rename-columns

import unittest
import pandas as pd
import Pandas.task_2885 as task
from pandas.testing import assert_frame_equal


class TestCases(unittest.TestCase):
    def test_renaming_column(self):
        students_data = pd.DataFrame(
            {
                'id': [1, 2, 3, 4, 5],
                'first': ['Mason', 'Ava', 'Taylor', 'Georgia', 'Thomas'],
                'last': ['King', 'Wright', 'Hall', 'Thompson', 'Moore'],
                'age': [6, 7, 16, 18, 10]
            }
        )

        test_dataframe = pd.DataFrame(
            data=
            {
                'student_id': [1, 2, 3, 4, 5],
                'first_name': ['Mason', 'Ava', 'Taylor', 'Georgia', 'Thomas'],
                'last_name': ['King', 'Wright', 'Hall', 'Thompson', 'Moore'],
                'age_in_years': [6, 7, 16, 18, 10]
            }
        )

        assert_frame_equal(task.rename_columns(students_data), test_dataframe)


if __name__ == '__main__':
    unittest.main()
