# UNIT TEST CASES
#
# 2886. Change Data Type
# https://leetcode.com/problems/change-data-type

import unittest
import pandas as pd
import Pandas.task_2886 as task
from pandas.testing import assert_frame_equal


class TestCases(unittest.TestCase):
    def test_changing_datatype(self):
        students_data = pd.DataFrame(
            {
                'student_id': [1, 2],
                'name': ['Ava', 'Kate'],
                'age': [6, 15],
                'grade': [73.0, 87.0]
            }
        )

        test_dataframe = pd.DataFrame(
            data=
            {
                'student_id': [1, 2],
                'name': ['Ava', 'Kate'],
                'age': [6, 15],
                'grade': [73, 87]
            }
        )

        assert_frame_equal(task.change_datatype(students_data), test_dataframe)


if __name__ == '__main__':
    unittest.main()
