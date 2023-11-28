# SOLUTION
#
# 2891. Method Chaining
# https://leetcode.com/problems/method-chaining

import pandas as pd


def find_heavy_animals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals[['name', 'weight']][animals['weight'] > 100]\
        .sort_values(by=['weight'], ascending=False)\
        .drop(columns=['weight'])
