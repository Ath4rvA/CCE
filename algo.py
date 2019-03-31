# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 16:44:57 2019

@author: Atharva
"""
#train, predict, load, store, preprocess
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Insert db
data= pd.read_excel("resultant_dataset.xlsx")
X= data.iloc[:, 1:5].values
y= data.iloc[:, -1].values
y=y.reshape(-1,1)
#Missing Data
from sklearn.preprocessing import Imputer
imputer= Imputer(missing_values= 'NaN', strategy='median', axis=0)
imputer= imputer.fit(X[:, :])
X[:, :]= imputer.transform(X[:, :])

#Cross validate
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test= train_test_split(X, y, test_size= 0.2, random_state=0)

#Feature Scaling
'''
from sklearn.preprocessing import StandardScaler
Sc_x= StandardScaler()
X_train= Sc_x.fit_transform(X_train)
X_test= Sc_x.transform(X_test)
'''

from sklearn.preprocessing import MinMaxScaler
min_max= MinMaxScaler()
X_train= min_max.fit_transform(X_train)
X_test= min_max.transform(X_test)

#Regression
#from sklearn.linear_model import LinearRegression
#Random Forest, Decision tree, SVR, 
from sklearn.ensemble import RandomForestRegressor
regressor= RandomForestRegressor(n_estimators=1000)
regressor.fit(X_train, y_train)

y_pred= regressor.predict(X_test)