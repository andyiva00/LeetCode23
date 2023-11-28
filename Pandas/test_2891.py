# UNIT TEST CASES
#
# 2891. Method Chaining
# https://leetcode.com/problems/method-chaining

import unittest
import pandas as pd
import Pandas.task_2891 as task
from pandas.testing import assert_frame_equal


class TestCases(unittest.TestCase):
    def test_select(self):
        animals_data = pd.DataFrame(
            data={
                'name': ['Tatiana', 'Khaled', 'Alex', 'Jonathan', 'Stefan', 'Tommy'],
                'species': ['Snake', 'Giraffe', 'Leopard', 'Monkey', 'Bear', 'Panda'],
                'age': [98, 50, 6, 45, 100, 26],
                'weight': [464, 41, 328, 463, 50, 349]
            }
        )

        test_dataframe = pd.DataFrame(
            data={
                'name': ['Tatiana', 'Jonathan', 'Tommy', 'Alex']
            },
            index=[0, 3, 5, 2]
        )

        assert_frame_equal(task.find_heavy_animals(animals_data), test_dataframe)


if __name__ == '__main__':
    unittest.main()
