from sklearn.neighbors import KNeighborsRegressor
import numpy as np
import data_frame_creation

def find_nearest_neighbors(df, dep_var, indep_list):
    train_df = df.dropna(subset = [dep_var] + indep_list)
    y_df = train_df.loc[:, dep_var]
    train_df =train_df.loc[:, indep_list]

    predict_df = df[df[dep_var].isnull()]
    predict_df = predict_df.dropna(subset = indep_list)
    predict_df = predict_df.loc[:, indep_list]

    neigh = KNeighborsRegressor(n_neighbors=2)
    neigh.fit(train_df,y_df)

    return neigh.predict(predict_df)

# df = data_frame_creation.create_joined_data_frame()
# train_df = df.dropna(subset = ['shuttle', 'forty_yd'])
# y_df = train_df.loc[:, 'shuttle']
# train_df =train_df.loc[:, ['weight','forty_yd']]
#
# neigh = KNeighborsRegressor(n_neighbors=2)
# neigh.fit(train_df,y_df)
#
# def estimate_shuttle(df):
#
#     return neigh.predict(df)
#
# predict_df = df[df['shuttle'].isnull()]
# predict_df = predict_df.dropna(subset = ['forty_yd'])
# predict_df = predict_df.loc[:, ['weight','forty_yd']]

# print(df.isnull().sum())
#
# predict_df = df[df['shuttle'].isnull()]
# print(predict_df.shape)



# def find_nearest_neighbors(df, dep_var, indep_list):
#     train_df = df.dropna(subset = [dep_var] + indep_list)
#     y_df = train_df.loc[:, dep_var]
#     train_df =train_df.loc[:, indep_list]
#
#     predict_df = df[df[dep_var].isnull()]
#     predict_df = predict_df.dropna(subset = indep_list)
#     predict_df = predict_df.loc[:, indep_list]
#
#     neigh = KNeighborsRegressor(n_neighbors=2)
#     neigh.fit(train_df,y_df)
#
#     return neigh.predict(predict_df)
