import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

from .regress import linreg

def linplot(df, x, y):
    '''
    Uses the linreg function from regress.py to produce the model_dict that
    contains the model, values, and variable names. Values from model_dict are
    then used to create simple plots.

    Parameters
    ----------
    df : dataframe
        the shared dataframe for x and y

    x : string
        column title for the independent variable

    y : string
        column title for the dependent variable

    Returns
    -------
    fig : matplotlib figure object
    '''

    model_dict = linreg(df, x, y)
    # Unpack model_dict
    # get model object
    model = model_dict['model']
    # get values
    x_val = model_dict['values']['x']
    y_val = model_dict['values']['y']
    # get variable names from model_dict
    x_name = model_dict['var_names']['x']
    y_name = model_dict['var_names']['y']


    # Create figure canvas
    fig = plt.figure(figsize=(6,4))
    ax = fig.add_subplot(111)

    # Plot Data
    ax.scatter(x_val, y_val, color = (), edgecolors='k', linewidths = 0.5, s=6)
    ax.plot(x_val, model.predict(x_val), color='r')

    # Label Elements
    ax.set_title('{} vs Precipitation'.format(x_name.split(' [')[0]))
    ax.set_xlabel(x_name)
    ax.set_ylabel(y_name)
    ax.grid(True)

    # Annotate Plot
    lin_string = 'f(x) = {slope:.3f}x + {intercept:.3f} \nr^2 = {r2:.4f}' \
    .format(slope = model.coef_[0], intercept = model.intercept_, r2 = model.score(x_val,y_val))
    ax.annotate(lin_string, xy=(0.05, 0.85), xycoords='axes fraction')

    return(fig)


#Plot monthly averaged data for mean, std, max, and min
def stat_plot(station_df,value_name):
    mean_m = station_df.resample('M').mean()
    median_m  = station_df.resample('M').median()
    std_m  = station_df.resample('M').std()
    max_m  =  station_df.resample('M').max()
    min_m  =  station_df.resample('M').min()

    fig, ax = plt.subplots(figsize=(15,9))
    ax.plot(mean_m[value_name], 'r',label='Mean')
    ax.fill_between(mean_m.index,mean_m[value_name]-std_m[value_name],mean_m[value_name]+std_m[value_name],facecolor='burlywood',label='1 sigma range')
    ax.plot(max_m[value_name],'g--',label='Max')
    ax.plot(min_m[value_name], 'b--',label='Min')
    ax.legend(loc='lower left')

    return(fig)


def draw_hist(station_df,nbins,value_name):
    #######Example##########
    #draw_hist(CLL,50,'Temp [F]')

    fig, ax = plt.subplots(figsize = (5, 5))

    ax.hist(station_df[value_name],bins=nbins)
    ax.set_title('Histogram of ' + value_name)
    ax.set_xlabel(value_name)
    ax.axvline(station_df[value_name].mean(), color='r', linestyle='dashed', linewidth=1)
    ax.axvline(station_df[value_name].median(), color='k', linestyle='dashed', linewidth=1)
    ax.axvline(station_df[value_name].mean()+station_df[value_name].std(), color='b', linestyle='dashed', linewidth=1)
    ax.axvline(station_df[value_name].mean()-station_df[value_name].std(), color='b', linestyle='dashed', linewidth=1)
    ax.legend(['Mean','Median','Std'])

    return(fig)
