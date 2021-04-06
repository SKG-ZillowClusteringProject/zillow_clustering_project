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

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols


from scipy import stats
from sklearn.metrics import mean_squared_error, r2_score, explained_variance_score

from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import f_regression 
from math import sqrt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
import math

#evaluation funcitons
def plot_residuals(actual, predicted): #target is actual, yhat is predicted
    '''
    plot_residuals will take in actual and prediction series
    and plot the residuals as a scatterplot.
    '''
    
    residual = actual - predicted
    
    plt.scatter(actual, residual)
    plt.hlines(0, actual.min(), actual.max(), ls=':')
    plt.xlabel("Actual")
    plt.ylabel("Residual")
    plt.title('Baseline Residuals')
    plt.show
    





def residuals(actual, predicted):
    return actual - predicted

def sse(actual, predicted):
    return (residuals(actual, predicted) **2).sum()

def mse(actual, predicted):
    n = actual.shape[0]
    return sse(actual, predicted) / n

def rmse(actual, predicted):
    return math.sqrt(mse(actual, predicted))

def ess(actual, predicted):
    return ((predicted - actual.mean()) ** 2).sum()

def tss(actual):
    return ((actual - actual.mean()) ** 2).sum()

def regression_errors(actual, predicted):
    return pd.Series({
        'sse': sse(actual, predicted),
        'ess': ess(actual, predicted),
        'tss': tss(actual),
        'mse': mse(actual, predicted),
        'rmse': rmse(actual, predicted),
    })

def baseline_mean_errors(actual):
    predicted = actual.mean()
    return {
        'sse': sse(actual, predicted),
        'mse': mse(actual, predicted),
        'rmse': rmse(actual, predicted),
    }

def baseline_median_errors(actual):
    predicted = actual.median()
    return {
        'sse': sse(actual, predicted),
        'mse': mse(actual, predicted),
        'rmse': rmse(actual, predicted),
    }



def better_than_baseline(actual, predicted):
    rmse_baseline = rmse(actual, actual.mean())
    rmse_model = rmse(actual, predicted)
    return rmse_model < rmse_baseline

def model_significance(ols_model):
    return {
        'r^2 -- variance explained': ols_model.rsquared,
        'p-value -- P(data|model == baseline)': ols_model.f_pvalue,
    }    


def select_kbest(x, y, k):
    
    # parameters: f_regression stats test, give me 8 features
    f_selector = SelectKBest(f_regression, k=k)
    
    # find the top 8 X's correlated with y
    f_selector.fit(X_train_scaled, y_train)
    
    # boolean mask of whether the column was selected or not. 
    feature_mask = f_selector.get_support()
    
    f_feature = X_train_scaled.iloc[:,feature_mask].columns.tolist()
    
    return f_feature

def rfe(x, y, k):
    
    lm = LinearRegression()
    
    rfe = RFE(lm, k)
    
    # Transforming data using RFE
    X_rfe = rfe.fit_transform(X_train_scaled,y_train)  
    
    mask = rfe.support_
    
    rfe_features = X_train_scaled.loc[:,mask].columns.tolist()
    
    print(str(len(rfe_features)), 'selected features')
    
    return  rfe_features

'''#Not working yet
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

    return lm_pred, lm_rmse, lm_pred_val, lm_rmse_val'''