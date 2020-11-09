import pandas as pd

def stat_month(station_df):
    #Monthly mean, median,stdm,maximum and minimum
    mean_month = station_df.resample('M').mean()
    median_month  = station_df.resample('M').median()
    std_month  = station_df.resample('M').std()
    max_month  =  station_df.resample('M').max()
    min_month  =  station_df.resample('M').min()

    return mean_month, median_month, std_month, max_month , min_month
