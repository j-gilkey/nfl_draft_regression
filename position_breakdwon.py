### create df for drafted players only###

df_drafted = df_combine.dropna(subset=['pick_number'])
df_drafted.head()

### breakdown by position group ###

db_df = df_drafted[(df_drafted['position'] == 'CB') |
                  (df_drafted['position'] == 'FS') |
                  (df_drafted['position'] == 'SS') |
                  (df_drafted['position'] == 'S') |
                  (df_drafted['position'] == 'DB')]

ol_df = df_drafted[(df_drafted['position'] == 'OT') |
                  (df_drafted['position'] == 'OG') |
                  (df_drafted['position'] == 'C') |
                  (df_drafted['position'] == 'OL')]

dl_df = df_drafted[(df_drafted['position'] == 'DE') |
                  (df_drafted['position'] == 'DT') |
                  (df_drafted['position'] == 'DL')]

lb_df = df_drafted[(df_drafted['position'] == 'OLB') |
                  (df_drafted['position'] == 'ILB') |
                  (df_drafted['position'] == 'EDGE') |
                  (df_drafted['position'] == 'LB')]

st_df = df_drafted[(df_drafted['position'] == 'K') |
                  (df_drafted['position'] == 'P') |
                  (df_drafted['position'] == 'LS')]

back_df = df_drafted[(df_drafted['position'] == 'RB') |
                    (df_drafted['position'] == 'FB') |
                    (df_drafted['position'] == 'WR') |
                    (df_drafted['position'] == 'TE')]
qb_df = df_drafted[(df_drafted['position'] == 'QB')]
