# UNIT TEST CASES
#
# 196. Delete Duplicate Emails
# https://leetcode.com/problems/delete-duplicate-emails

import unittest
import pandas as pd
import Pandas.task_196 as task
from pandas.testing import assert_frame_equal


class TestCases(unittest.TestCase):
    def test_select_1(self):
        person_data = pd.DataFrame(
            data={
                'id': [1, 2, 3],
                'email': ['john@example.com', 'bob@example.com', 'john@example.com']
            }
        )

        test_dataframe = pd.DataFrame(
            data={
                'id': [1, 2],
                'email': ['john@example.com', 'bob@example.com']
            }
        )

        task.delete_duplicate_emails(person_data)
        assert_frame_equal(person_data, test_dataframe)


if __name__ == '__main__':
    unittest.main()
