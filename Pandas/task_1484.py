# SOLUTION
#
# 1484. Group Sold Products By The Date
# https://leetcode.com/problems/group-sold-products-by-the-date

import pandas as pd


def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:

    tmp_table_1 = activities.drop_duplicates().sort_values('product')

    tmp_table_2 = pd.DataFrame(
        tmp_table_1,
        columns=['sell_date', 'product']
    ).groupby(by=['sell_date']).count().reset_index()

    tmp_table_3 = tmp_table_2.merge(
        tmp_table_1,
        left_on='sell_date',
        right_on='sell_date',
        how='left'
    )

    tmp_table_3.rename(
        columns=
        {
            'product_x': 'num_sold',
            'product_y': 'products'
        },
        inplace=True
    )

    tmp_table_3 = tmp_table_3.groupby(['sell_date', 'num_sold'])['products'].apply(','.join).reset_index()

    return tmp_table_3
