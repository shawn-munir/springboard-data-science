import pandas as pd
import numpy as np
import os
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import __version__ as sklearn_version
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale
from sklearn.model_selection import train_test_split, cross_validate, GridSearchCV, learning_curve
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.feature_selection import SelectKBest, f_regression
import datetime


ski_data = pd.read_csv('DataScienceGuidedCapstone/data/ski_data_step3_features.csv')

ski_data = ski_data.copy()

ski_data = ski_data[ski_data.yearsOpen < 1000]

ski_data.loc[ski_data.Name=='Silverton Mountain', 'SkiableTerrain_ac'] = 1819


ski_data.dropna(subset=['AdultWeekend'], inplace=True)

ski_data = ski_data[ski_data.Name != 'Big Mountain Resort']

X = ski_data.drop(columns='AdultWeekend')
y = ski_data.AdultWeekend

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=47)

names_list = ['Name', 'state', 'Region']

X_train.drop(columns=names_list, inplace=True)
X_test.drop(columns=names_list, inplace=True)

train_mean = y_train.mean()


y_tr_pred_ = train_mean * np.ones(len(y_train))

y_te_pred = train_mean * np.ones(len(y_test))



X_defaults_median = X_train.median()


X_tr = X_train.fillna(X_defaults_median)
X_te = X_test.fillna(X_defaults_median)


scaler = StandardScaler()

scaler.fit(X_tr)

X_tr_scaled = scaler.transform(X_tr)

X_te_scaled = scaler.transform(X_te)

lm = LinearRegression().fit(X_tr_scaled, y_train)


y_tr_pred = lm.predict(X_tr_scaled)
y_te_pred = lm.predict(X_te_scaled)


median_r2 = r2_score(y_train, y_tr_pred), r2_score(y_test, y_te_pred)
print(median_r2)


