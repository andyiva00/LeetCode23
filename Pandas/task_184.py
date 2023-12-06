# SOLUTION
#
# 184. Department Highest Salary
# https://leetcode.com/problems/department-highest-salary

import pandas as pd


def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    tmp_table_1 = pd.DataFrame(
        employee,
        columns=['salary', 'departmentId']
    ).groupby(by='departmentId').max()

    tmp_table_2 = employee.merge(
        tmp_table_1,
        left_on=['departmentId', 'salary'],
        right_on=['departmentId', 'salary'],
        how='inner'
    ).sort_values(['id'])

    tmp_table_3 = tmp_table_2.merge(
        department,
        left_on='departmentId',
        right_on='id',
        how='left'
    )[['name_y', 'name_x', 'salary']]

    tmp_table_3.rename(
        columns=
        {
            'name_y': 'Department',
            'name_x': 'Employee',
            'salary': 'Salary'
        },
        inplace=True
    )

    return tmp_table_3
