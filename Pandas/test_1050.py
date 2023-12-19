# UNIT TEST CASES
#
# 1050. Actors and Directors Who Cooperated At Least Three Times
# https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times

import unittest
import pandas as pd
import Pandas.task_1050 as task
from pandas.testing import assert_frame_equal


class TestCases(unittest.TestCase):
    def test_select_1(self):
        actor_director_data = pd.DataFrame(
            data={
                'actor_id': [1, 1, 1, 1, 1, 2, 2],
                'director_id': [1, 1, 1, 2, 2, 1, 1],
                'timestamp': [0, 1, 2, 3, 4, 5, 6]
            }
        )

        test_dataframe = pd.DataFrame(
            data={
                'actor_id': [1],
                'director_id': [1]
            }
        )

        assert_frame_equal(task.actors_and_directors(actor_director_data), test_dataframe)


if __name__ == '__main__':
    unittest.main()
