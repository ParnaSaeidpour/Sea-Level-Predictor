import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    Data = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    x = Data['Year']
    y = Data['CSIRO Adjusted Sea Level']
    plt.scatter(x,y)


    # Create first line of best fit
    result = linregress(x, y)
    slope = result.slope
    intercept = result.intercept
  
    line_x = np.arange(x.min(),2051,1)
    line_y = slope*line_x + intercept

    plt.plot(line_x,line_y)

    # Create second line of best fit

    Data_new = Data[Data['Year'] >= 2000]
    x_new = Data_new['Year']
    y_new = Data_new['CSIRO Adjusted Sea Level']
  
    result = linregress(x_new, y_new)
    slope = result.slope
    intercept = result.intercept
  
    line_x_new = np.arange(2000,2051,1)
    line_y_new = slope*line_x_new + intercept

    plt.plot(line_x_new,line_y_new)


  

    # Add labels and title


    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()