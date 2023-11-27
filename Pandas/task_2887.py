# SOLUTION
#
# 2887. Fill Missing Data
# https://leetcode.com/problems/fill-missing-data

import pandas as pd


def fill_missing_values(products: pd.DataFrame) -> pd.DataFrame:
    return products.fillna(value={'quantity': 0}).astype({'quantity': 'int'})
