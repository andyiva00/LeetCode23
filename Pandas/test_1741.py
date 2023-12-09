# UNIT TEST CASES
#
# 1741. Find Total Time Spent by Each Employee
# https://leetcode.com/problems/find-total-time-spent-by-each-employee

import unittest
import pandas as pd
import Pandas.task_1741 as task
from pandas.testing import assert_frame_equal


class TestCases(unittest.TestCase):
    def test_select_1(self):
        employees_data = pd.DataFrame(
            data={
                'emp_id': [1, 1, 1, 2, 2],
                'event_day': ['2020-11-28', '2020-11-28', '2020-12-03', '2020-11-28', '2020-12-09'],
                'in_time': [4, 55, 1, 3, 47],
                'out_time': [32, 200, 42, 33, 74]
            }
        )

        test_dataframe = pd.DataFrame(
            data={
                'day': ['2020-11-28', '2020-11-28', '2020-12-03', '2020-12-09'],
                'emp_id': [1, 2, 1, 2],
                'total_time': [173, 30, 41, 27]
            }
        )

        assert_frame_equal(task.total_time(employees_data), test_dataframe)


if __name__ == '__main__':
    unittest.main()
