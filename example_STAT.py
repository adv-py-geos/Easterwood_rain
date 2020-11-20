import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# All function imports now come from our package folder Easterwood_rain
from Easterwood_rain import create_df, data_stat, stat_month, stat_plot, draw_hist
# from readdata import create_df # made by 'a-vanderheiden'
# from data_stat import data_stat
# from stat_month import stat_month
# from stat_plot import stat_plot
# from draw_hist import draw_hist

#Example: CLL Station
CLL = create_df('CLL') #Read data made by 'a-vanderheiden'

#use data_stat from data_set.py
CLL_STAT=data_stat(CLL)
CLL_STAT

###Monthly data###
#Mean, Median, Standard deviation, Maximum, and Minimum
CLL_mean_m,CLL_median_m,CLL_std_m,CLL_max_m,CLL_min_m = stat_month(CLL)
CLL_mean_m.head()


#plot the monthly statistics: EX)At CLL station, Temperature data
stat_plot(CLL, "Temp [F]")
plt.title('Monthly data plot ')



#Draw histogram: EX)At CLL station, Temperature histogram
draw_hist(station_df=CLL,nbins=50,value_name="Temp [F]")
plt.title('Example:Historgam of Temperature(CLL station)')
plt.show()
