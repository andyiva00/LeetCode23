import unittest
import pandas as pd
import Pandas.task_2877 as task
from pandas.testing import assert_frame_equal


class TestCases(unittest.TestCase):
    def test_create_dataframe(self):
        student_data = [[1, 15],
                        [2, 11],
                        [3, 11],
                        [4, 20]]

        test_dataframe = pd.DataFrame(
            {
                'student_id': [1, 2, 3, 4],
                'age': [15, 11, 11, 20]
            }
        )

        assert_frame_equal(task.create_dataframe(student_data), test_dataframe)


if __name__ == '__main__':
    unittest.main()
