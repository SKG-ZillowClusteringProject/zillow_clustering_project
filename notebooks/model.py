import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from math import sqrt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import mean_squared_error, explained_variance_score, mean_absolute_error
from sklearn.linear_model import LinearRegression, TweedieRegressor, LassoLars
from sklearn.feature_selection import RFE
from sklearn.preprocessing import PolynomialFeatures

'''
*------------------*
|                  |
|     MODEL        |
|                  |
*------------------*
'''
def get_LROLS(X, y, X_val, y_val):
    '''
    This function will create the model object, fit the model, predict on train,
    predict on validate, and print RMSE for SKlearn algorithm LinearRegression
    '''
    #make the thing
    lm = LinearRegression(normalize=True)
    #fit the thing
    #only fit on training data
    #X=X_train #Y= y_train.logerror
    lm.fit(X, y) 
    #use the thing (predict on train)
    lm_predict = lm.predict(X)
    # Evaluate: rmse (root mean squared error)
    lm_rmse = mean_squared_error(y, lm_pred) ** 0.5
    # predict on validate
    #X_val=lm.predict(X_validate)
    lm_pred_val = lm.predict(X_val)
    # compute root mean squared error
    lm_rmse_val = mean_squared_error(y_val, lm_pred_val) ** 0.5

    print("RMSE for OLS using LinearRegression\n\nOn train data:\n", round(lm_rmse, 6), '\n\n', 
    "On validate data:\n", round(lm_rmse_v, 6))

    return lm_pred, lm_rmse, lm_pred_val, lm_rmse_val