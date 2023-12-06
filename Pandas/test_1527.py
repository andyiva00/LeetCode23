# UNIT TEST CASES
#
# 1527. Patients With a Condition
# https://leetcode.com/problems/patients-with-a-condition

import unittest
import pandas as pd
import Pandas.task_1527 as task
from pandas.testing import assert_frame_equal


class TestCases(unittest.TestCase):
    def test_select(self):
        patients_data = pd.DataFrame(
            data={
                'patient_id': [1, 2, 3, 4, 5],
                'patient_name': ['Daniel', 'Alice', 'Bob', 'George', 'Alain'],
                'conditions': ['YFEV COUGH', '', 'DIAB100 MYOP', 'ACNE DIAB100', 'DIAB201']
            }
        )

        test_dataframe = pd.DataFrame(
            data={
                'patient_id': [3, 4],
                'patient_name': ['Bob', 'George'],
                'conditions': ['DIAB100 MYOP', 'ACNE DIAB100']
            },
            index=[2, 3]
        )

        assert_frame_equal(task.find_patients(patients_data), test_dataframe)


if __name__ == '__main__':
    unittest.main()
