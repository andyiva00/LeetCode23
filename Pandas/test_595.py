# UNIT TEST CASES
#
# 595. Big Countries
# https://leetcode.com/problems/big-countries

import unittest
import pandas as pd
import Pandas.task_595 as task
from pandas.testing import assert_frame_equal


class TestCases(unittest.TestCase):
    def test_select(self):
        world_data = pd.DataFrame(
            data={
                'name': ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola'],
                'continent': ['Asia', 'Europe', 'Africa', 'Europe', 'Africa'],
                'area': [652230, 28748, 2381741, 468, 1246700],
                'population': [25500100, 2831741, 37100000, 78115, 20609294],
                'gdp': [20343000000, 12960000000, 188681000000, 3712000000, 100990000000]
            }
        )

        test_dataframe = pd.DataFrame(
            data={
                'name': ['Afghanistan', 'Algeria'],
                'population': [25500100, 37100000],
                'area': [652230, 2381741]
            }
        )

        assert_frame_equal(task.big_countries(world_data), test_dataframe)


if __name__ == '__main__':
    unittest.main()
