import data_frame_creation
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
import statsmodels.api as sm
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.multicomp import MultiComparison

#df = data_frame_creation.create_combine_data_frame()
df_joined = data_frame_creation.create_joined_data_frame()

pd.set_option('display.max_columns', None)
#pd.set_option('display.max_rows', None)


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
#hist_plot(df_joined, 'forty_yd')
#hist_plot(df_numbers, '3cone')

#hist_plot(df_joined, 'log_salary')
#hist_plot(df_joined, 'total_gaurantees')

def scatter_plot(df, to_plot):
    df = df.dropna(subset = [to_plot])
    fig = plt.figure()
    plt.style.use('seaborn')
    sns.set_palette('colorblind')
    ax = sns


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

def heat_corr(df, name):
    fig = plt.figure()
    #plt.clear()
    plt.style.use('seaborn')
    sns.set_palette('colorblind')
    corr = df.corr()
    sns.set(rc={'figure.figsize':(11.7,8.27)})
    sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns, annot=True).set_title(name)
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

#print(multi_by_position(df, 'height'))
#print(df[])
#print(df[df['position_grouping'].isnull()])
#pair_plot(df_numbers)

def check_corr_for_group(df):
    position_groups_list = list(df['position_grouping'].unique())
    #df = df['position_grouping', 'height', 'weight', 'forty_yd', 'vertical', 'bench', 'broad_jump', 'three_cone', 'shuttle']
    df = df.loc[:, ['position_grouping', 'avg_salary', 'height', 'weight', 'forty_yd', 'vertical', 'bench', 'broad_jump', 'three_cone', 'shuttle']]


    heat_corr(df, 'Overall')


check_corr_for_group(df_joined)
