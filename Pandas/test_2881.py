# UNIT TEST CASES
#
# 2881. Create a New Column
# https://leetcode.com/problems/create-a-new-column

import unittest
import pandas as pd
import Pandas.task_2881 as task
from pandas.testing import assert_frame_equal


class TestCases(unittest.TestCase):
    def test_creating_column(self):
        employees_data = pd.DataFrame(
            {
                'name': ['Piper', 'Grace', 'Georgia', 'Willow', 'Finn', 'Thomas'],
                'salary': [4548, 28150, 1103, 6593, 74576, 24433]
            }
        )

        test_dataframe = pd.DataFrame(
            {
                'name': ['Piper', 'Grace', 'Georgia', 'Willow', 'Finn', 'Thomas'],
                'salary': [4548, 28150, 1103, 6593, 74576, 24433],
                'bonus': [9096, 56300, 2206, 13186, 149152, 48866]
            }
        )

        assert_frame_equal(task.create_bonus_column(employees_data), test_dataframe)


if __name__ == '__main__':
    unittest.main()
