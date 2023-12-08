# SOLUTION
#
# 1795. Rearrange Products Table
# https://leetcode.com/problems/rearrange-products-table

import pandas as pd


def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    return pd.melt(
        products,
        id_vars=['product_id'],
        value_vars=['store1', 'store2', 'store3'],
        var_name='store',
        value_name='price'
    ).dropna().sort_values(by=['product_id', 'store'], ascending=True).astype({'price': 'int64'})
