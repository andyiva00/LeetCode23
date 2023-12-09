# SOLUTION
#
# 511. Game Play Analysis I
# https://leetcode.com/problems/game-play-analysis-i

import pandas as pd


def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    tmp_table_1 = pd.DataFrame(
        activity,
        columns=['player_id', 'event_date']
    ).groupby(by=['player_id']).min().reset_index()

    tmp_table_1.rename(
        columns={"event_date": "first_login"},
        inplace=True
    )

    return tmp_table_1
