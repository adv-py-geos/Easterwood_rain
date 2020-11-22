import pandas as pd
import numpy as np
import seaborn as sns
sns.set(font_scale = 1.25)
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

# Column List
name_list = ["Station ID","Date [UTC]","Temp [F]","DP [F]","RH [%]","W Dir [Deg]","W Spd [Kts]","Alt [inHg]","1Hr-Prcp [mm]",
             "Vis [mi]","SKC1","SKC2","SKC3","Cld Hgt1 [Ft]","Cld Hgt2 [Ft]","Cld Hgt3 [Ft]","Prs Wx"]

# Data Type List
dtype_list = {"Station ID":"str","UTC":"str","Temp [F]":"float64","DP [F]":"float64","RH [%]":"float64","W Dir [Deg]":"float64",
              "W Spd [Kts]":"float64","Alt [inHg]":"float64","1Hr-Prcp [mm]":"float64","Vis [mi]":"float64","SKC1":"str",
              "SKC2":"str","SKC3":"str","Cld Hgt1 [Ft]":"float64","Cld Hgt2 [Ft]":"float64","Cld Hgt3 [Ft]":"float64",
              "Prs Wx" : "str"}

# Date Column
parse_date = ["Date [UTC]"]

# Import TxT Data
CLL = pd.read_csv('Data/CLL.txt', sep='\t', header=0, names = name_list,
                  dtype = dtype_list, parse_dates = parse_date, index_col = 1).resample('1d').mean()
DFW = pd.read_csv('Data/DFW.txt', sep='\t', header=0, names = name_list,
                  dtype = dtype_list, parse_dates = parse_date, index_col = 1).resample('1d').mean()
AUS = pd.read_csv('Data/AUS.txt', sep='\t', header=0, names = name_list,
                  dtype = dtype_list, parse_dates = parse_date, index_col = 1).resample('1d').mean()
IAH = pd.read_csv('Data/IAH.txt', sep='\t', header=0, names = name_list,
                  dtype = dtype_list, parse_dates = parse_date, index_col = 1).resample('1d').mean()

def make_plot(CLL, DFW, AUS, IAH, ylab, title):

    fig, ax = plt.subplots(4, figsize = (14, 17), sharey=True)


    ax[0].plot(CLL)
    ax[0].set_title('College Station ' + title)
    ax[1].plot(DFW)
    ax[1].set_title('Dallas ' + title)
    ax[2].plot(AUS)
    ax[2].set_title('Austin ' + title)
    ax[3].plot(IAH)
    ax[3].set_title('Houston ' + title)

    for i in range(len(ax)-1):
        ax[i].set_xticklabels('')

    for i in range(len(ax)):
        ax[i].set_ylabel(ylab)

make_plot(CLL['Temp [F]'], DFW['Temp [F]'], AUS['Temp [F]'], IAH['Temp [F]'],
          'Air Temp [$^\circ$F]', 'Air Temperature')


make_plot(CLL['DP [F]'], DFW['DP [F]'], AUS['DP [F]'], IAH['DP [F]'],
          'Dew Point [$^\circ$F]', 'Dew Point')

make_plot(CLL['RH [%]'], DFW['RH [%]'], AUS['RH [%]'], IAH['RH [%]'],
          'RH [%]', 'Relative Humidity')

make_plot(CLL['W Dir [Deg]'], DFW['W Dir [Deg]'], AUS['W Dir [Deg]'], IAH['W Dir [Deg]'],
          'WD [$^\circ$]', 'Wind Direction')

make_plot(CLL['W Spd [Kts]'], DFW['W Spd [Kts]'], AUS['W Spd [Kts]'], IAH['W Spd [Kts]'],
          'WS [kts]', 'Wind Speed')

make_plot(CLL['Alt [inHg]'], DFW['Alt [inHg]'], AUS['Alt [inHg]'], IAH['Alt [inHg]'],
          'Alt [inHg]', 'Altimetry')

make_plot(CLL['1Hr-Prcp [mm]'], DFW['1Hr-Prcp [mm]'], AUS['1Hr-Prcp [mm]'], IAH['1Hr-Prcp [mm]'],
          'Prcp [mm]', '1 Hour Precipitation')

make_plot(CLL['Vis [mi]'], DFW['Vis [mi]'], AUS['Vis [mi]'], IAH['Vis [mi]'],
          'Vis [mi]', 'Visibility')
plt.ylim(0,10)

make_plot(CLL['Cld Hgt1 [Ft]'], DFW['Cld Hgt1 [Ft]'], AUS['Cld Hgt1 [Ft]'], IAH['Cld Hgt1 [Ft]'],
          'CH [Ft]', 'First Cloud Height')

make_plot(CLL['Cld Hgt2 [Ft]'], DFW['Cld Hgt2 [Ft]'], AUS['Cld Hgt2 [Ft]'], IAH['Cld Hgt2 [Ft]'],
          'CH [Ft]', 'Second Cloud Height')

make_plot(CLL['Cld Hgt3 [Ft]'], DFW['Cld Hgt3 [Ft]'], AUS['Cld Hgt3 [Ft]'], IAH['Cld Hgt3 [Ft]'],
          'CH [Ft]', 'Third Cloud Height')
