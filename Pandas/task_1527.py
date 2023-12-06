# SOLUTION
#
# 1527. Patients With a Condition
# https://leetcode.com/problems/patients-with-a-condition

import pandas as pd


def find_patients(patients: pd.DataFrame) -> pd.DataFrame:

    return patients[
        patients['conditions'].str.startswith('DIAB1', na=False) |
        patients['conditions'].str.contains(' DIAB1', na=False)]
