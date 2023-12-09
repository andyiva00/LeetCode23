# SOLUTION
#
# 1741. Find Total Time Spent by Each Employee
# https://leetcode.com/problems/find-total-time-spent-by-each-employee

import pandas as pd


def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    tmp_table_1 = employees.copy()
    tmp_table_1['total_time'] = tmp_table_1['out_time'] - tmp_table_1['in_time']

    tmp_table_1 = pd.DataFrame(
        tmp_table_1,
        columns=['event_day', 'emp_id', 'total_time']
    ).groupby(by=['event_day', 'emp_id']).sum().reset_index()

    tmp_table_1.rename(
        columns={"event_day": "day"},
        inplace=True
    )

    return tmp_table_1
