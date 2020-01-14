import mysql_functions
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def create_combine_data_frame():
    data = mysql_functions.get_all_combine_data()
    df = pd.DataFrame(data, columns = ['row_id', 'player', 'year', 'position', 'school', 'height', 'weight', '40yd', 'vertical', 'bench', 'broad_jump', '3cone', 'shuttle', 'pick_number'])
    df = df.set_index('row_id')
    return df
