import pandas as pd
import matplotlib.pyplot as plt

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
