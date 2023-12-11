# SOLUTION
#
# 596. Classes More Than 5 Students
# https://leetcode.com/problems/classes-more-than-5-students

import pandas as pd


def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    tmp_table_1 = pd.DataFrame(
        courses,
        columns=['student', 'class']
    ).groupby(by=['class']).count().reset_index()

    tmp_table_1 = tmp_table_1[tmp_table_1['student'] >= 5]
    tmp_table_1.drop(columns=['student'], inplace=True)
    tmp_table_1.reset_index(drop=True, inplace=True)

    return tmp_table_1
