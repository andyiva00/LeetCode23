# SOLUTION
#
# 595. Big Countries
# https://leetcode.com/problems/big-countries

import pandas as pd


def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    output_columns = ['name', 'population', 'area']
    df1 = world[world.area >= 3000000][output_columns]
    df2 = world[world.population >= 25000000][output_columns]
    return pd.concat([df1, df2], ignore_index=True).drop_duplicates()
