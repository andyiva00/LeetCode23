# UNIT TEST CASES
#
# 2880. Select Data
# https://leetcode.com/problems/select-data

import unittest
import pandas as pd
import Pandas.task_2880 as task
from pandas.testing import assert_frame_equal


class TestCases(unittest.TestCase):
    def test_selecting_data(self):
        students_data = pd.DataFrame(
            {
                'student_id': [101, 53, 128, 3],
                'name': ['Ulysses', 'William', 'Henry', 'Henry'],
                'age': [13, 10, 6, 11]
            }
        )

        test_dataframe = pd.DataFrame(
            {
                'name': ['Ulysses'],
                'age': [13]
            }
        )

        assert_frame_equal(task.select_data(students_data), test_dataframe)


if __name__ == '__main__':
    unittest.main()
