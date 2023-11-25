# SOLUTION
#
# 2882. Drop Duplicate Rows
# https://leetcode.com/problems/drop-duplicate-rows

import pandas as pd


def drop_duplicate_emails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset=['email'], keep='first')
