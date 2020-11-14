import numpy as np
import pandas as pd
def mean_d(station):
	''' Takes a pandas dataframe of the station, assuming it's been indexing by Datetime, then outputs its 	daily average'''

	station_daily = station.resample('1d').mean()
	
	return station_daily