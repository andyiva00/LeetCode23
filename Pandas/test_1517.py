# UNIT TEST CASES
#
# 1517. Find Users With Valid E-Mails
# https://leetcode.com/problems/find-users-with-valid-e-mails

import unittest
import pandas as pd
import Pandas.task_1517 as task
from pandas.testing import assert_frame_equal


class TestCases(unittest.TestCase):
    def test_validating_emails(self):
        users_data = pd.DataFrame(
            data={
                'user_id': [1, 2, 3, 4, 5, 6, 7],
                'name': ['Winston', 'Jonathan', 'Annabelle', 'Sally', 'Marwan', 'David', 'Shapiro'],
                'mail': ['winston@leetcode.com', 'jonathanisgreat', 'bella-@leetcode.com', 'sally.come@leetcode.com',
                         'quarz#2020@leetcode.com', 'david69@gmail.com', '.shapo@leetcode.com']
            }
        )

        test_dataframe = pd.DataFrame(
            data={
                'user_id': [1, 3, 4],
                'name': ['Winston', 'Annabelle', 'Sally'],
                'mail': ['winston@leetcode.com', 'bella-@leetcode.com', 'sally.come@leetcode.com']
            },
            index=[0, 2, 3]
        )

        assert_frame_equal(task.valid_emails(users_data), test_dataframe)


if __name__ == '__main__':
    unittest.main()
