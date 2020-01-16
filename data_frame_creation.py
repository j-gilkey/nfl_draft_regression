import mysql_functions
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.neighbors import KNeighborsRegressor

pd.set_option('display.max_columns', None)

def columns_to_float(df, column_list):

    for c in column_list:
        df[c] = df[c].astype(float)
    return df

def create_position_groupings(row):
    position_dict = {
    'DB' : ['CB', 'FS', 'SS', 'S', 'DB'],
    'OL' : ['OT', 'OG', 'C', 'OL'],
    'DL' : ['DE', 'DT', 'DL'],
    'LB' : ['OLB', 'ILB', 'EDGE', 'LB'],
    'ST' : ['K', 'P', 'LS'],
    'SKILL' : ['RB', 'FB', 'WR', 'TE'],
    'QB' : ['QB']}

    for key in position_dict:
        if row['position'] in position_dict[key]:
            return key

def get_avg_salary(row):
    return row['total_value']/row['duration_years']

def fill_missing_shuttle(row, neigh):
    if np.isnan(row['shuttle']):
        if np.isnan(row['forty_yd']):
            #print(row['shuttle'])
            return row['shuttle']
        else:
            return neigh.predict([[row['weight'],row['forty_yd']],[row['weight'],row['forty_yd']]])[0]
            #for some reason predict only accepts lists of length > 2, so here I'm arbitrarily passing it the same val twice
    else: return row['shuttle']


def create_combine_data_frame():
    data = mysql_functions.get_all_combine_data()
    df = pd.DataFrame(data, columns = ['row_id', 'player', 'year', 'position', 'school', 'height', 'weight', 'forty_yd', 'vertical', 'bench', 'broad_jump', 'three_cone', 'shuttle', 'pick_number'])
    df = df.set_index('row_id')
    df = columns_to_float(df,['height', 'weight', 'forty_yd','vertical', 'bench', 'broad_jump', '3cone', 'shuttle'])
    df['position_grouping'] = df.apply(lambda row: create_position_groupings(row), axis =1)
    return df

def create_joined_data_frame():
    data = mysql_functions.get_joined_data()
    df = pd.DataFrame(data, columns = ['row_id', 'duration_years', 'total_value', 'year', 'position', 'height', 'weight', 'forty_yd', 'vertical', 'bench', 'broad_jump', 'three_cone', 'shuttle', 'pick_number'])
    df = df.set_index('row_id')
    #initial call and column selection

    df = columns_to_float(df,['duration_years', 'total_value', 'height', 'weight', 'forty_yd','vertical', 'bench', 'broad_jump', 'three_cone', 'shuttle'])
    #convert all numerics to floats

    df['position_grouping'] = df.apply(lambda row: create_position_groupings(row), axis =1)
    #group positions into categories

    df = df[~df['position_grouping'].isin(['QB', 'ST'])]
    #remove QB and ST

    position_dummy = pd.get_dummies(df['position_grouping'],prefix = 'position', drop_first=True)
    df = pd.concat([df, position_dummy], axis = 1)
    #create and add in dummies for position groups

    df['avg_salary'] = df.apply(lambda row: get_avg_salary(row), axis =1)
    #add average yearly salary

    df['log_salary'] = df.apply(lambda row: np.log(row['avg_salary']), axis =1)
    #log it

    train_df = df.dropna(subset = ['shuttle', 'forty_yd'])
    y_df = train_df.loc[:, 'shuttle']
    train_df =train_df.loc[:, ['weight','forty_yd']]
    neigh = KNeighborsRegressor(n_neighbors=2)
    neigh.fit(train_df,y_df)
    #train nearest_neighbors data in order to predict missing shuttle values


    #df['shuttle'] = df.apply(lambda row: fill_missing_shuttle(row, neigh), axis =1)
    #create and fill in predictions

    #add average yearly salary
    #df['log_salary'] = df.apply(lambda row: np.log(row['avg_salary']), axis =1)
    #log it
    # df = df.drop('position', 1)
    # df = df.drop('position_grouping', 1)
    # df = df.drop('duration_years', 1)
    # df = df.drop('pick_number', 1)


    return df

df= create_joined_data_frame()
#print(df.head)
