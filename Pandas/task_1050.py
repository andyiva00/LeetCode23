# SOLUTION
#
# 1050. Actors and Directors Who Cooperated At Least Three Times
# https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times

import pandas as pd


def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    tmp_table_1 = pd.DataFrame(
        actor_director,
        columns=['actor_id', 'director_id', 'timestamp']
    ).groupby(by=['actor_id', 'director_id']).count().reset_index()

    tmp_table_1 = tmp_table_1[tmp_table_1.timestamp >= 3][['actor_id', 'director_id']]

    return tmp_table_1
