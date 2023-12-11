# UNIT TEST CASES
#
# 596. Classes More Than 5 Students
# https://leetcode.com/problems/classes-more-than-5-students

import unittest
import pandas as pd
import Pandas.task_596 as task
from pandas.testing import assert_frame_equal


class TestCases(unittest.TestCase):
    def test_select_1(self):
        courses_data = pd.DataFrame(
            data={
                'student': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
                'class': ['Math', 'English', 'Math', 'Biology', 'Math', 'Computer', 'Math', 'Math', 'Math']
            }
        )

        test_dataframe = pd.DataFrame(
            data={
                'class': ['Math']
            }
        )

        assert_frame_equal(task.find_classes(courses_data), test_dataframe)


if __name__ == '__main__':
    unittest.main()
