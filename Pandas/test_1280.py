# UNIT TEST CASES
#
# 1280. Students and Examinations
# https://leetcode.com/problems/students-and-examinations

import unittest
import pandas as pd
import Pandas.task_1280 as task
from pandas.testing import assert_frame_equal


class TestCases(unittest.TestCase):
    def test_select_1(self):
        students_data = pd.DataFrame(
            data={
                'student_id': [1, 2, 13, 6],
                'student_name': ['Alice', 'Bob', 'John', 'Alex']
            }
        )

        subjects_data = pd.DataFrame(
            data={
                'subject_name': ['Math', 'Physics', 'Programming']
            }
        )

        examinations_data = pd.DataFrame(
            data={
                'student_id': [1, 1, 1, 2, 1, 1, 13, 13, 13, 2, 1],
                'subject_name': ['Math', 'Physics', 'Programming', 'Programming', 'Physics', 'Math', 'Math',
                                 'Programming', 'Physics', 'Math', 'Math']
            }
        )

        test_dataframe = pd.DataFrame(
            data={
                'student_id': [1, 1, 1, 2, 2, 2, 6, 6, 6, 13, 13, 13],
                'student_name': ['Alice', 'Alice', 'Alice',
                                 'Bob', 'Bob', 'Bob',
                                 'Alex', 'Alex', 'Alex',
                                 'John', 'John', 'John'],
                'subject_name': ['Math', 'Physics', 'Programming',
                                 'Math', 'Physics', 'Programming',
                                 'Math', 'Physics', 'Programming',
                                 'Math', 'Physics', 'Programming'],
                'attended_exams': [3, 2, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1]
            }
        )

        assert_frame_equal(task.students_and_examinations(students_data, subjects_data, examinations_data),
                           test_dataframe)


if __name__ == '__main__':
    unittest.main()
