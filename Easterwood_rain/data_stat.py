import pandas as pd

def data_stat(station_df):
#mean, median,stdm,maximum and minimum for whole time
#Generate a data frame for the statistical values
    mean =  station_df.mean().to_frame().T
    med  =  station_df.median().to_frame().T
    std  =  station_df.std().to_frame().T
    maxi  =  station_df.max().to_frame().T
    mini  =  station_df.min().to_frame().T

    STAT_df = mean
    STAT_df=    STAT_df.append([med.loc[0],std.loc[0],maxi.loc[0],mini.loc[0]], ignore_index=True)
    STAT_df.insert(0,"STAT",['MEAN','MEDIAN' ,'STD','MAX','MIN'])

    return STAT_df

def stat_month(station_df):
    #Monthly mean, median,stdm,maximum and minimum
    mean_month = station_df.resample('M').mean()
    median_month  = station_df.resample('M').median()
    std_month  = station_df.resample('M').std()
    max_month  =  station_df.resample('M').max()
    min_month  =  station_df.resample('M').min()

    return mean_month, median_month, std_month, max_month , min_month
