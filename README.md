# Easterwood_rain
Machine learning predictor based on linear regression for rainfall at several locations in TX. 

All relevant .py files are stored in the Easterwood_rain folder. The model is very simple to run. An example script (ExampleScript.py) is stored in the root directory along with different working examples of Jupyter Notebooks based off of functions in the .py files. 

### To read in the data: 
df = create_df('CLL')

### To do the linear regression: 
my_model = linreg(df, 'Temp [F]', '1Hr-Prcp [mm]')

### To get the resulting fit from the linear regression:
eq_string = 'f(x) = {slope:.3f}x + {intercept:.3f} \nr^2 = {r2:.4f}' \
.format(slope = my_model['model'].coef_[0],
        intercept = my_model['model'].intercept_,
        r2 = my_model['model'].score(my_model['values']['x'], my_model['values']['y']))

print(eq_string)

### Plot the data:
fig = lin_plot(df, 'Temp [F]', '1Hr-Prcp [mm]')
plt.show()

