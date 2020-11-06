'''
Example script to showcase functions defined in newly created .py files.

Workflow:
 1. Create df from our downloaded data
 2. Create a linear model for temperature and precipitation
 3. Show linear model
'''

from readdata import create_df
from regress import linreg
from plot_util import linplot

import matplotlib.pyplot as plt

# Create the df with create_df from readdata.py
#  - Reads data from Data directory
df = create_df('CLL')

# Create a linear model with linreg from regress.py
#  - takes dataframe output from from create_df
#  - creates a dictionary output with the model object, values, and variable names
my_model = linreg(df, 'Temp [F]', '1Hr-Prcp [mm]')

eq_string = 'f(x) = {slope:.3f}x + {intercept:.3f} \nr^2 = {r2:.4f}' \
.format(slope = my_model['model'].coef_[0],
        intercept = my_model['model'].intercept_,
        r2 = my_model['model'].score(my_model['values']['x'], my_model['values']['y']))

print(eq_string)

# Create a figure with linplot from plot_util.py
#  - Creates plot from linereg dictionary output
fig = linplot(my_model)
plt.show()
