# SOLUTION
#
# 2878. Get the Size of a DataFrame
# https://leetcode.com/problems/get-the-size-of-a-dataframe


import pandas as pd
from typing import List


def get_dataframe_size(players: pd.DataFrame) -> List[int]:
    return list(players.shape)
