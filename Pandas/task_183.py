# SOLUTION
#
# 183. Customers Who Never Order
# https://leetcode.com/problems/customers-who-never-order

import pandas as pd


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:

    return_df = customers.merge(
        orders,
        left_on=['id'],
        right_on=['customerId'],
        how='left',
        indicator=True
    )

    return_df = return_df[return_df['_merge'] == 'left_only'][['name']]

    return_df.rename(
        columns={"name": "Customers"},
        inplace=True
    )

    return return_df
