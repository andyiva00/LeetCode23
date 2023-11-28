# UNIT TEST CASES
#
# 2888. Reshape Data: Concatenate
# https://leetcode.com/problems/reshape-data-concatenate

import unittest
import pandas as pd
import Pandas.task_2888 as task
from pandas.testing import assert_frame_equal


class TestCases(unittest.TestCase):
    def test_filling_missing_values(self):
        df1_data = pd.DataFrame(
            data={
                'student_id': [1, 2, 3, 4],
                'name': ['Mason', 'Ava', 'Taylor', 'Georgia'],
                'age': [8, 6, 15, 17]
            }
        )

        df2_data = pd.DataFrame(
            data={
                'student_id': [5, 6],
                'name': ['Leo', 'Alex'],
                'age': [7, 7]
            }
        )

        test_dataframe = pd.DataFrame(
            data={
                'student_id': [1, 2, 3, 4, 5, 6],
                'name': ['Mason', 'Ava', 'Taylor', 'Georgia', 'Leo', 'Alex'],
                'age': [8, 6, 15, 17, 7, 7]
            }
        )

        assert_frame_equal(task.concatenate_tables(df1_data, df2_data), test_dataframe)


if __name__ == '__main__':
    unittest.main()
