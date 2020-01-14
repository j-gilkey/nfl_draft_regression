import data_frame_creation
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = data_frame_creation.create_combine_data_frame()

#df = df.dropna()

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
# print(df.columns)

def columns_to_float(df, column_list):

    for c in column_list:
        df[c] = df[c].astype(float)
    return df

df_numbers = df.loc[:, ['height', 'weight', '40yd', 'vertical', 'bench', 'broad_jump', '3cone', 'shuttle']]
#print(df_numbers)
df_numbers = columns_to_float(df_numbers,['height', 'weight', '40yd','vertical', 'bench', 'broad_jump', '3cone', 'shuttle'])
print(df_numbers.dtypes)



# df_numbers = df.loc[:, ['height', 'weight', '40yd',
#        'vertical', 'bench', 'broad_jump', '3cone', 'shuttle', 'pick_number']]

line_men = ['OT', 'OG', 'DT', 'C', 'NT', 'OL', 'DL', 'DE']
skill_men  = ['OLB', 'RB', 'TE', 'CB', 'K', 'P', 'FS', 'ILB','SS', 'QB', 'WR', 'FB', 'LS','EDGE', 'S', 'LB', 'DB']



def hist_plot(df, to_plot):
    fig = plt.figure()
    plt.style.use('seaborn')
    sns.set_palette('colorblind')
    hist_serial = sns.distplot(df[to_plot].astype(float), kde = False)
    #print(stats.kurtosis(list(df['trees_per_sq_mile'])))
    #print(stats.skew(list(df['trees_per_sq_mile'])))
    #hist_serial.set_xlabel('Trees Per Sq Mile')
    #hist_serial.set_xlabel('Trees per sq Mile')
    plt.show()

#hist_plot(df, 'weight')

#hist_plot(df, 'height')

def simple_box(df):
    fig = plt.figure()
    plt.style.use('seaborn')
    sns.set_palette('colorblind')
    ax = sns.boxplot(x= 'position', y = 'weight', data = df)

    #ax.set_ylabel('Median Home Value')
    ax.set_ylabel('Trees per sq Mile')
    ax.set_xlabel('Borough')
    plt.show()

#simple_box(df)

def pair_plot(df):
    fig = plt.figure()
    #plt.clear()
    plt.style.use('seaborn')
    sns.set_palette('colorblind')
    corr = df.corr()
    #sns.set(rc={'figure.figsize':(11.7,8.27)})
    sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns, annot=True)
    plt.show()

pair_plot(df_numbers)
