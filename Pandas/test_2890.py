# UNIT TEST CASES
#
# 2890. Reshape Data: Melt
# https://leetcode.com/problems/reshape-data-melt

import unittest
import pandas as pd
import Pandas.task_2890 as task
from pandas.testing import assert_frame_equal


class TestCases(unittest.TestCase):
    def test_melting_table(self):
        report_data = pd.DataFrame(
            data={
                'product': ['Umbrella', 'SleepingBag'],
                'quarter_1': [417, 800],
                'quarter_2': [224, 936],
                'quarter_3': [379, 93],
                'quarter_4': [611, 875]
            }
        )

        test_dataframe = pd.DataFrame(
            data={
                'product': ['Umbrella', 'SleepingBag', 'Umbrella', 'SleepingBag', 'Umbrella', 'SleepingBag',
                            'Umbrella', 'SleepingBag'],
                'quarter': ['quarter_1', 'quarter_1', 'quarter_2', 'quarter_2', 'quarter_3', 'quarter_3',
                            'quarter_4', 'quarter_4'],
                'sales': [417, 800, 224, 936, 379, 93, 611, 875]
            }
        )

        assert_frame_equal(task.melt_table(report_data), test_dataframe)


if __name__ == '__main__':
    unittest.main()
