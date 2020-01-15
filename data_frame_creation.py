import mysql_functions
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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

def create_combine_data_frame():
    data = mysql_functions.get_all_combine_data()
    df = pd.DataFrame(data, columns = ['row_id', 'player', 'year', 'position', 'school', 'height', 'weight', 'forty_yd', 'vertical', 'bench', 'broad_jump', 'three_cone', 'shuttle', 'pick_number'])
    df = df.set_index('row_id')
    df = columns_to_float(df,['height', 'weight', 'forty_yd','vertical', 'bench', 'broad_jump', '3cone', 'shuttle'])
    df['position_grouping'] = df.apply(lambda row: create_position_groupings(row), axis =1)
    return df

def create_joined_data_frame():
    data = mysql_functions.get_joined_data()
    df = pd.DataFrame(data, columns = ['row_id', 'player', 'duration_years', 'total_value', 'initial_guaratees', 'total_gaurantees', 'year', 'position', 'height', 'weight', 'forty_yd', 'vertical', 'bench', 'broad_jump', 'three_cone', 'shuttle', 'pick_number'])
    df = df.set_index('row_id')

    df = columns_to_float(df,['duration_years', 'total_value', 'initial_guaratees', 'total_gaurantees', 'height', 'weight', 'forty_yd','vertical', 'bench', 'broad_jump', 'three_cone', 'shuttle'])
    df['position_grouping'] = df.apply(lambda row: create_position_groupings(row), axis =1)
    return df

df = create_joined_data_frame()
