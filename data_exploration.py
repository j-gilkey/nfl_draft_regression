import data_frame_creation
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
import statsmodels.api as sm
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.multicomp import MultiComparison

df = data_frame_creation.create_combine_data_frame()

pd.set_option('display.max_columns', None)
#pd.set_option('display.max_rows', None)

def columns_to_float(df, column_list):

    for c in column_list:
        df[c] = df[c].astype(float)
    return df

df = columns_to_float(df,['height', 'weight', '40yd','vertical', 'bench', 'broad_jump', '3cone', 'shuttle'])


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



df['position_grouping'] = df.apply(lambda row: create_position_groupings(row), axis =1)

def hist_plot(df, to_plot):
    #takes a dataframe and a column to create a hist plot on
    df = df.dropna(subset = [to_plot])
    fig = plt.figure()
    plt.style.use('seaborn')
    sns.set_palette('colorblind')
    hist_serial = sns.distplot(df[to_plot].astype(float), kde = False)
    #hist_serial.set_xlabel('Trees Per Sq Mile')
    #hist_serial.set_xlabel('Trees per sq Mile')
    plt.show()

#hist_plot(df, 'weight')
#hist_plot(df, 'height')
#hist_plot(df_numbers, '3cone')


def simple_box_by_position(df, to_plot):
    df = df.dropna(subset = [to_plot])
    fig = plt.figure()
    plt.style.use('seaborn')
    sns.set_palette('colorblind')
    ax = sns.boxplot(x= 'position_grouping', y = to_plot, data = df)

    # ax.set_ylabel('Median Home Value')
    # ax.set_ylabel('Trees per sq Mile')
    # ax.set_xlabel('Borough')
    plt.show()

#simple_box_by_position(df, 'weight')

def pair_plot(df):
    fig = plt.figure()
    #plt.clear()
    plt.style.use('seaborn')
    sns.set_palette('colorblind')
    corr = df.corr()
    #sns.set(rc={'figure.figsize':(11.7,8.27)})
    sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns, annot=True)
    plt.show()

def anova_by_position(df, to_plot):
    df = df.dropna(subset = [to_plot])
    anova_pos = ols((to_plot + '~position_grouping'), data=df).fit()
    anova_table = sm.stats.anova_lm(anova_pos, type=2)
    return anova_table

def multi_by_position(df, to_plot):
    df = df.dropna(subset = [to_plot, 'position_grouping'])
    mc = MultiComparison(df[to_plot], df['position_grouping'])
    mc_results = mc.tukeyhsd()
    return mc_results


#print(df['position_grouping'].unique())

# for i in df['position_grouping'].unique():
#     print(i)
#     print(df[df['position_grouping'] == i]['weight'].describe())
    #print(df[df['position_grouping'] == i].mean)

print(multi_by_position(df, 'height'))
#print(df[])
#print(df[df['position_grouping'].isnull()])
#pair_plot(df_numbers)
