# SOLUTION
#
# 1907. Count Salary Categories
# https://leetcode.com/problems/count-salary-categories

import pandas as pd


def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    tmp_table_1 = pd.DataFrame(
        {
            'category': ['Low Salary'],
            'accounts_count': [len(accounts[accounts['income'] < 20000])]
        }
    )
    tmp_table_2 = pd.DataFrame(
        {
            'category': ['Average Salary'],
            'accounts_count': [len(accounts[(accounts['income'] >= 20000) & (accounts['income'] <= 50000)])]
        }
    )

    tmp_table_3 = pd.DataFrame(
        {
            'category': ['High Salary'],
            'accounts_count': [len(accounts[accounts['income'] > 50000])]
        }
    )

    return pd.concat(objs=[tmp_table_1, tmp_table_2, tmp_table_3], ignore_index=True)
