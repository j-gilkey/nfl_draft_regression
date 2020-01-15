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

position_groups = {'WR': 'BK', 'DE': 'DL', 'OLB': 'LB', 'RB': 'BK', 'OT': 'OL', 'CB': 'BK', 'QB': 'QB',
                  'FS': 'BK', 'DT': 'DL', 'C': 'OL', 'P': 'ST', 'TE': 'BK', 'SS': 'BK', 'ILB': 'LB', 'OG': 'OL',
                  'EDGE': 'LB', 'S': 'BK', 'FB': 'BK', 'LB': 'LB', 'DB': 'BK', 'OL': 'OL', 'DL': 'DL',
                  'K': 'ST'}

### replace position column with position group column
df_joined['pos_grp'] = df_joined['position'].map(position_groups)
cols = df_joined.columns.tolist()
cols = cols[:5] + cols[-1:] + cols[5:-1]
cols.pop(7)
df_joined = df_joined[cols]

#### add dummies 
position_dummy = pd.get_dummies(df_joined['pos_grp'],prefix = 'position', drop_first=True)
df_with_dummies = pd.concat([df_joined, position_dummy], axis = 1)
