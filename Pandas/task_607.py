# SOLUTION
#
# 607. Sales Person
# https://leetcode.com/problems/sales-person

import pandas as pd


def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    tmp_table_1 = orders.merge(
        company[company['name'] == 'RED'],
        left_on='com_id',
        right_on='com_id',
        how='inner'
    )

    tmp_table_2 = sales_person.merge(
        tmp_table_1,
        left_on='sales_id',
        right_on='sales_id',
        how='left',
        indicator=True
    )

    tmp_table_3 = pd.DataFrame(
        tmp_table_2[tmp_table_2['_merge'] == 'left_only'],
        columns=['name_x']
    ).reset_index(drop=True)

    tmp_table_3.rename(
        columns=
        {
            'name_x': 'name'
        },
        inplace=True
    )

    return tmp_table_3
