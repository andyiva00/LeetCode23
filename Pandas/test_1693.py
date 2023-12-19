# UNIT TEST CASES
#
# 1693. Daily Leads and Partners
# https://leetcode.com/problems/daily-leads-and-partners

import unittest
import pandas as pd
import Pandas.task_1693 as task
from pandas.testing import assert_frame_equal


class TestCases(unittest.TestCase):
    def test_select_1(self):
        daily_sales_data = pd.DataFrame(
            data={
                'date_id': ['2020-12-8', '2020-12-8', '2020-12-8', '2020-12-7', '2020-12-7', '2020-12-8',
                            '2020-12-8', '2020-12-7', '2020-12-7', '2020-12-7'],
                'make_name': ['toyota', 'toyota', 'toyota', 'toyota', 'toyota',
                              'honda', 'honda', 'honda', 'honda', 'honda'],
                'lead_id': [0, 1, 1, 0, 0, 1, 2, 0, 1, 2],
                'partner_id': [1, 0, 2, 2, 1, 2, 1, 1, 2, 1]
            }
        )

        test_dataframe = pd.DataFrame(
            data={
                'date_id': ['2020-12-8', '2020-12-7', '2020-12-8', '2020-12-7'],
                'make_name': ['toyota', 'toyota', 'honda', 'honda'],
                'unique_leads': [2, 1, 2, 3],
                'unique_partners': [3, 2, 2, 2]
            }
        )

        assert_frame_equal(task.daily_leads_and_partners(daily_sales_data), test_dataframe)


if __name__ == '__main__':
    unittest.main()
