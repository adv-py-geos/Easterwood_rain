import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

from regress import linreg

def linplot(model_dict):
    '''
    Takes the model_dict output from regress.py and returns a simple plot of the
    original data with the newly created model.

    Parameters
    ----------
    model_dict : dictionary
        output from regress.py containing the model object, values used to create
        the model, and variable names of the values.

    Returns
    -------
    fig : matplotlib figure object
    '''

    # Unpack model_dict
    # get model object
    model = model_dict['model']
    # get values
    x_val = model_dict['values']['x']
    y_val = model_dict['values']['y']
    # get variable names from model_dict
    x_name = model_dict['var_names']['x']
    y_name = model_dict['var_names']['y']


    # Create figure canvas
    fig = plt.figure(figsize=(6,4))
    ax = fig.add_subplot(111)

    # Plot Data
    ax.scatter(x_val, y_val, color = (), edgecolors='k', linewidths = 0.5, s=6)
    ax.plot(x_val, model.predict(x_val), color='r')

    # Label Elements
    ax.set_title('{} vs Precipitation'.format(x_name.split(' [')[0]))
    ax.set_xlabel(x_name)
    ax.set_ylabel(y_name)
    ax.grid(True)

    # Annotate Plot
    lin_string = 'f(x) = {slope:.3f}x + {intercept:.3f} \nr^2 = {r2:.4f}' \
    .format(slope = model.coef_[0], intercept = model.intercept_, r2 = model.score(x_val,y_val))
    ax.annotate(lin_string, xy=(0.05, 0.85), xycoords='axes fraction')

    return(fig)
