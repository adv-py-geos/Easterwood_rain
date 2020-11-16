import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np 
pd.options.mode.use_inf_as_na = True

class Prep:
    
    def fill_missing(dataframe, method='linear'):
        if method == 'linear':
            for i in dataframe.columns:
                mask = np.isnan(dataframe[i])
                dataframe[i][mask] = np.interp(np.flatnonzero(mask), np.flatnonzero(~mask), dataframe[i][~mask])
            return dataframe
        elif method == 'zero':
            return dataframe.fillna(0)

    def howdy(dataframe):
        # boolean transform of precipitation
#         prcp = np.zeros(dataframe.shape[0])
#         for i in range(dataframe.shape[0]):
#             if dataframe['1Hr-Prcp [mm]'][i] > 0:
#                 prcp[i] = 1
#         print(dataframe)
        dataframe = dataframe.assign(prcp=abs(dataframe['1Hr-Prcp [mm]'])!=-dataframe['1Hr-Prcp [mm]'])
        return dataframe
    
    def norm(dataframe, method='standard'):
        if method == 'standard':
            scaler = StandardScaler()
            for i in dataframe:
                dataframe = scaler.fit_transform(dataframe)
            return dataframe
        
    def inverse(data):
        return scaler.inverse_transofrm(data)
    
    def train_test(dataset, his = 0.9):
    # split into train and test sets
        train_size = int(len(dataset) * his)
        test_size = len(dataset) - train_size
        train, test = dataset[0:train_size,:], dataset[train_size:len(dataset),:]
        return train, test
    
    def split(data, n_steps):
        X, y = list(), list()
        for i in range(len(data)):
            end_ix = i + n_steps
            if end_ix > len(data):
                break
            seq_x, seq_y = data[i:end_ix, :], data[end_ix-1, 6]
            X.append(seq_x)
            y.append(seq_y)
        return np.array(X), np.array(y)

