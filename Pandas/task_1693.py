# SOLUTION
#
# 1693. Daily Leads and Partners
# https://leetcode.com/problems/daily-leads-and-partners

import pandas as pd


def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    tmp_table_1 = pd.DataFrame(
        daily_sales,
        columns=['date_id', 'make_name', 'lead_id', 'partner_id']
    ).groupby(by=['date_id', 'make_name']).nunique()\
        .sort_values(by=['make_name', 'date_id'], ascending=[False, False])\
        .reset_index()

    tmp_table_1.rename(
        columns=
        {
            'lead_id': 'unique_leads',
            'partner_id': 'unique_partners'
        },
        inplace=True
    )

    return tmp_table_1
