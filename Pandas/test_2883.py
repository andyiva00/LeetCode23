# UNIT TEST CASES
#
# 2883. Drop Missing Data
# https://leetcode.com/problems/drop-missing-data

import unittest
import pandas as pd
import Pandas.task_2883 as task
from pandas.testing import assert_frame_equal


class TestCases(unittest.TestCase):
    def test_drop_missing_data(self):
        students_data = pd.DataFrame(
            {
                'student_id': [32, 217, 779, 849],
                'name': ['Piper', None, 'Georgia', 'Willow'],
                'age': [5, 19, 20, 14]
            }
        )

        test_dataframe = pd.DataFrame(
            data={
                'student_id': [32, 779, 849],
                'name': ['Piper', 'Georgia', 'Willow'],
                'age': [5, 20, 14]
            },
            index=[0, 2, 3]
        )

        assert_frame_equal(task.drop_missing_data(students_data), test_dataframe)


if __name__ == '__main__':
    unittest.main()
