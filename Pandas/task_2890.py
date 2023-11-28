# SOLUTION
#
# 2890. Reshape Data: Melt
# https://leetcode.com/problems/reshape-data-melt

import pandas as pd


def melt_table(report: pd.DataFrame) -> pd.DataFrame:
    return pd.melt(
        report,
        id_vars=['product'],
        value_vars=['quarter_1', 'quarter_2', 'quarter_3', 'quarter_4'],
        var_name='quarter',
        value_name='sales'
    )
