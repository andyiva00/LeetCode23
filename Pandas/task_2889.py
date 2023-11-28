# SOLUTION
#
# 2889. Reshape Data: Pivot
# https://leetcode.com/problems/reshape-data-pivot

import pandas as pd


def pivot_table(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot(index='month', columns='city', values='temperature')
