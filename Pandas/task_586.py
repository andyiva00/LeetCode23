# SOLUTION
#
# 586. Customer Placing the Largest Number of Orders
# https://leetcode.com/problems/customer-placing-the-largest-number-of-orders

import pandas as pd


def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    tmp_table_1 = pd.DataFrame(
        orders,
        columns=['order_number', 'customer_number']
    ).groupby(by=['customer_number']).count().reset_index()

    tmp_table_2 = tmp_table_1[tmp_table_1['order_number'] == tmp_table_1['order_number'].max()][['customer_number']]
    tmp_table_2.reset_index(drop=True, inplace=True)

    return tmp_table_2
