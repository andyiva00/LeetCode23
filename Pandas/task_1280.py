# SOLUTION
#
# 1280. Students and Examinations
# https://leetcode.com/problems/students-and-examinations

import pandas as pd


def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    tmp_table_1 = students.merge(
        subjects,
        how='cross'
    )

    tmp_table_2 = examinations.copy()
    tmp_table_2['attended_exams'] = 1
    tmp_table_2 = tmp_table_2.groupby(['student_id', 'subject_name']).count().reset_index()

    tmp_table_3 = tmp_table_1.merge(
        tmp_table_2,
        left_on=['student_id', 'subject_name'],
        right_on=['student_id', 'subject_name'],
        how='left', sort=True
    )

    tmp_table_3['attended_exams'] = tmp_table_3['attended_exams'].fillna(0)
    tmp_table_3 = tmp_table_3.astype({'attended_exams': 'int64'})

    tmp_table_3 = tmp_table_3[['student_id', 'student_name', 'subject_name', 'attended_exams']]

    return tmp_table_3
