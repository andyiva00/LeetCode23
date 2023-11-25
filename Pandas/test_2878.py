# UNIT TEST CASES
#
# 2878. Get the Size of a DataFrame
# https://leetcode.com/problems/get-the-size-of-a-dataframe

import unittest
import pandas as pd
import Pandas.task_2878 as task


class TestCases(unittest.TestCase):
    def test_getting_size(self):
        test_dataframe = pd.DataFrame(
            {
                'player_id ': [846, 749, 155, 583, 388, 883, 355, 247, 761, 642],
                'name': ['Mason', 'Riley', 'Bob', 'Isabella', 'Zachary', 'Ava', 'Violet', 'Thomas', 'Jack', 'Charlie'],
                'age': [21, 30, 28, 32, 24, 23, 18, 27, 33, 36],
                'position': ['Forward', 'Winger', 'Striker', 'Goalkeeper', 'Midfielder', 'Defender', 'Striker',
                             'Striker', 'Midfielder', 'Center-back'],
                'team': ['RealMadrid', 'Barcelona', 'ManchesterUnited', 'Liverpool', 'BayernMunich', 'Chelsea',
                         'Juventus', 'ParisSaint-Germain', 'ManchesterCity', 'Arsenal']
            }
        )

        self.assertEqual(task.get_dataframe_size(test_dataframe), [10, 5])


if __name__ == '__main__':
    unittest.main()
