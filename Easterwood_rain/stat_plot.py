import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#PLot monthly averaged data for mean, std, max, and min
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
