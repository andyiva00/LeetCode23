# UNIT TEST CASES
#
# 2356. Number of Unique Subjects Taught by Each Teacher
# https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher

import unittest
import pandas as pd
import Pandas.task_2356 as task
from pandas.testing import assert_frame_equal


class TestCases(unittest.TestCase):
    def test_select_1(self):
        teacher_data = pd.DataFrame(
            data={
                'teacher_id': [1, 1, 1, 2, 2, 2, 2],
                'subject_id': [2, 2, 3, 1, 2, 3, 4],
                'dept_id': [3, 4, 3, 1, 1, 1, 1]
            }
        )

        test_dataframe = pd.DataFrame(
            data={
                'teacher_id': [1, 2],
                'cnt': [2, 4]
            }
        )

        assert_frame_equal(task.count_unique_subjects(teacher_data), test_dataframe)


if __name__ == '__main__':
    unittest.main()
