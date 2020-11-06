import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def linreg(df, x, y):
    '''
    Takes two columns in a shared dataframe and returns a sklearn linear model
    object and its coefficeints.

    Parameters
    ------------------------
    df : dataframe
        the shared dataframe for x and y

    x : string
        column title for the independent variable

    y : string
        column title for the dependent variable
    '''

    # sklearn doesnt like nans in the LinearRegression function
    no_nans = df[df[x].notna() & df[y].notna()]

    # Reshape for sklearn
    x_val = no_nans[x].values.reshape((-1,1))
    y_val = no_nans[y].values

    # model object holds all of our linear regression coefficeints and whatnot
    model = LinearRegression().fit(x_val,y_val)

    model_dict = {
        'model': model,
        'values': {'x': x_val, 'y':y_val},
        'var_names':{'x':x, 'y':y}
        }

    return(model_dict)
