### import libraries

import requests
import config
from bs4 import BeautifulSoup as BS
import mysql.connector
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
import statsmodels.api as sm

cnx = mysql.connector.connect(
  host=config.hostj,
  user=config.userj,
  passwd=config.pwj,
  database = 'nfl_draft_info')

cursor = cnx.cursor()

## import DataFrame

df_joined = pd.read_csv('df_joined.csv')
df_joined = df_joined.set_index('id')
df_joined = df_joined.drop(df_joined.columns[0], axis=1)

## create position group map
## remove QB and ST players

position_groups = {'WR': 'BK', 'DE': 'DL', 'OLB': 'LB', 'RB': 'BK', 'OT': 'OL', 'CB': 'BK', 'QB': 'ST',
                  'FS': 'BK', 'DT': 'DL', 'C': 'OL', 'P': 'ST', 'TE': 'BK', 'SS': 'BK', 'ILB': 'LB', 'OG': 'OL',
                  'EDGE': 'LB', 'S': 'BK', 'FB': 'BK', 'LB': 'LB', 'DB': 'BK', 'OL': 'OL', 'DL': 'DL',
                  'K': 'ST'}

### replace position column with position group column
df_joined['pos_grp'] = df_joined['position'].map(position_groups)
cols = df_joined.columns.tolist()
cols = cols[:5] + cols[-1:] + cols[5:-1]
cols.pop(7)
df_joined = df_joined[cols]

df_joined2 = df_joined[(df_joined['pos_grp'] != 'ST')]

### create log_salary column
df_joined2['avg_salary'] = df_joined2.apply(lambda row: row['total_value']/row['contract_years'], axis=1)
df_joined2['log_salary'] = df_joined2.apply(lambda row: np.log(row['avg_salary']), axis =1)

#### add dummies
position_dummy = pd.get_dummies(df_joined2['pos_grp'],prefix = 'position', drop_first=True)
df_with_dummies = pd.concat([df_joined2, position_dummy], axis = 1)

### potential logistic regression model
log_reg_ = ols('log_salary~forty+shuttle+bench+position_DL+position_LB+position_OL', data=df_with_dummies).fit()
log_reg_.summary()
