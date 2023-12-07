# SOLUTION
#
# 196. Delete Duplicate Emails
# https://leetcode.com/problems/delete-duplicate-emails

import pandas as pd


def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values(by=['id'], ascending=True, inplace=True)
    person.drop_duplicates(subset=['email'], keep='first', inplace=True)
