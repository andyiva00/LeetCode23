# SOLUTION
#
# 183. Customers Who Never Order
# https://leetcode.com/problems/customers-who-never-order

import pandas as pd


def article_views(views: pd.DataFrame) -> pd.DataFrame:
    return_df = views[views.author_id == views.viewer_id][['author_id']].drop_duplicates()

    return_df.rename(
        columns={"author_id": "id"},
        inplace=True
    )

    return_df.sort_values(
        by='id',
        inplace=True
    )

    return return_df
