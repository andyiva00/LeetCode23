# SOLUTION
#
# 178. Rank Scores
# https://leetcode.com/problems/rank-scores

import pandas as pd


def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    tmp_table_1 = pd.DataFrame(
        scores,
        columns=['score']
    ).drop_duplicates(subset=['score'], keep='first').sort_values(by=['score'], ascending=False)

    tmp_table_1['rank'] = tmp_table_1['score'].rank(ascending=False)

    tmp_table_2 = pd.DataFrame(
        scores,
        columns=['score']
    ).sort_values(by=['score'], ascending=False)

    tmp_table_1 = tmp_table_2.merge(
        tmp_table_1,
        left_on='score',
        right_on='score',
        how='inner'
    ).astype({'rank': 'int64'})

    return tmp_table_1
