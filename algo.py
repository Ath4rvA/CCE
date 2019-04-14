# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 16:44:57 2019

@author: Atharva
"""
#train, predict, load, store, preprocess
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import joblib

#Insert db
def load_data():
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
    #random_seed=1
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test= train_test_split(X, y, test_size= 0.2, random_state=0)
    return X_train, X_test, y_train, y_test
    #Feature Scaling
    '''
from sklearn.preprocessing import MinMaxScaler
min_max= MinMaxScaler()
X_train= min_max.fit_transform(X_train)
X_test= min_max.transform(X_test)
'''
#
#def scale():
#    
#    from sklearn.preprocessing import StandardScaler
#    Sc_x= StandardScaler()
#    X_train= Sc_x.fit_transform(X_train)
#    X_test= Sc_x.transform(X_test)
#    return X_train,X_test,y_train,y_test


def train(X_train, X_test, y_train, y_test):
    from sklearn.ensemble import RandomForestRegressor
    regressor1= RandomForestRegressor(n_estimators=500)
    regressor1.fit(X_train, y_train)
    joblib.dump(regressor1,'regressor1.joblib')

def predict(x):
    y=x.iloc[:, 1:].values
    regressor=joblib.load('regressor1.joblib')
    prediction=regressor.predict(y)
    df_new=pd.DataFrame({"score":prediction})
    return pd.concat([x,df_new],axis=1)
    
#y_pred= regressor1.predict(X_test)
'''
test=pd.read_csv("try.csv")
T_test= test.iloc[:,1:].values
T_test= Sc_x.fit_transform(T_test)
new_pred= regressor1.predict(T_test)
'''
'''
from sklearn.tree import DecisionTreeRegressor
dtr= DecisionTreeRegressor()
dtr.fit(X_train, y_train)
predict= dtr.predict(X_test)
'''
'''
from sklearn import linear_model
reg= linear_model.BayesianRidge()
reg.fit(X_train, y_train)
y_prediction= reg.predict(X_test)
'''
'''
from sklearn import linear_model
regressor= linear_model.ARDRegression()
regressor.fit(X_train, y_train)
y_pred= regressor.predict(X_test)
'''
'''
from sklearn import linear_model
regressor= linear_model.HuberRegressor()
regressor.fit(X_train, y_train)
y_pred= regressor.predict(X_test)
'''
'''
from sklearn import svm
regressor= svm.SVR()
regressor.fit(X_train, y_train)
y_pred= regressor.predict(X_test)
'''
