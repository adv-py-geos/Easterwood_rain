import pandas as pd

def create_df(station, period = '1d'):
    '''
    Takes a 3 letter station abbreviation from the user and
    returns all relevant met data as a dataframe.

    Parameters
    ----------
    station : str, 3 letter code representing the station needed
    period  : str, the time period to average by.  Default is '1d' for daily data
		input lenght followed by period code. Example( 1S, 1T, 1H, 1d, 1M, 1Y)
    Returns
    -------
    dataframe of all relevent met data indexed by day
    '''

    # Column List
    name_list = ["Station ID","Date [UTC]","Temp [F]","DP [F]","RH [%]",
                "W Dir [Deg]","W Spd [Kts]","Alt [inHg]","1Hr-Prcp [mm]",
                "Vis [mi]","SKC1","SKC2","SKC3","Cld Hgt1 [Ft]","Cld Hgt2 [Ft]",
                "Cld Hgt3 [Ft]","Prs Wx"]

    # Data Type List
    dtype_list = {"Station ID":"str","UTC":"str","Temp [F]":"float64",
                  "DP [F]":"float64","RH [%]":"float64","W Dir [Deg]":"float64",
                  "W Spd [Kts]":"float64","Alt [inHg]":"float64",
                  "1Hr-Prcp [mm]":"float64","Vis [mi]":"float64","SKC1":"str",
                  "SKC2":"str","SKC3":"str","Cld Hgt1 [Ft]":"float64",
                  "Cld Hgt2 [Ft]":"float64","Cld Hgt3 [Ft]":"float64",
                  "Prs Wx" : "str"}

    station_data = pd.read_csv('Data/{}.txt'.format(station), sep='\t',
                                header=0, names = name_list, dtype = dtype_list,
                                parse_dates = ['Date [UTC]'], index_col = 1) \
                                .resample(period).mean()

    return(station_data)
