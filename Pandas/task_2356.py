# SOLUTION
#
# 2356. Number of Unique Subjects Taught by Each Teacher
# https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher

import pandas as pd


def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    tmp_table_1 = pd.DataFrame(
        teacher,
        columns=['teacher_id', 'subject_id']
    ).groupby(by=['teacher_id']).nunique().reset_index()

    tmp_table_1.rename(
        columns={"subject_id": "cnt"},
        inplace=True
    )

    return tmp_table_1
