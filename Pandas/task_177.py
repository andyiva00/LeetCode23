# SOLUTION
#
# 177. Nth Highest Salary
# https://leetcode.com/problems/nth-highest-salary

import pandas as pd


def nth_highest_salary(employee: pd.DataFrame, n: int) -> pd.DataFrame:
    return_pd = employee.copy()
    return_pd.drop_duplicates(subset=['salary'], keep='first', inplace=True)
    return_pd.sort_values(by=['salary'], ascending=False, inplace=True)

    if len(return_pd) >= n:
        return pd.DataFrame(
            data=return_pd[n-1:n]['salary'].values,
            columns=['getNthHighestSalary(' + str(n) + ')'])
    else:
        return pd.DataFrame(
            data=[None],
            columns=['getNthHighestSalary(' + str(n) + ')'])
