import data_frame_creation
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
import statsmodels.api as sm
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.multicomp import MultiComparison

df = data_frame_creation.create_joined_data_frame()

def basic_regression(df):
    #anova_dl = ols('log_salary~three_cone+vertical+bench', data=df).fit()
    #anova_dl = ols('total_value~three_cone', data=df).fit()
    #anova_dl = ols('log_salary~three_cone+vertical+bench+position_DL+position_LB+position_OL+position_SKILL', data=df).fit()
    #anova_dl = ols('log_salary~shuttle+vertical+bench+forty_yd+height+position_DL+position_LB+position_OL+position_SKILL', data=df).fit()
    #anova_dl = ols('log_salary~shuttle+bench+height+position_DL+position_LB+position_OL+position_SKILL', data=df).fit()
    #anova_dl = ols('log_salary~shuttle+broad_jump+bench+position_DL+position_LB+position_OL+position_SKILL', data=df).fit()
    #anova_dl = ols('log_salary~position_DL+position_LB+position_OL+position_QB+position_SKILL+position_ST', data=df).fit()
    anova_dl = ols('log_salary~forty_yd+shuttle+bench+position_DL+position_LB+position_OL', data=df).fit()
    return anova_dl.summary()

print(basic_regression(df))
