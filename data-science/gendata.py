"""
This app uses Python, numpy, and pandas to generate a set of data points and plot them on a graph.
"""

# Import the required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""
Create a function 'gendata' that generates a set of 'n' data points (x, f(x)) and returns them as a pandas data frame.
Arguments:
- 'x_range' is a tuple of two integers representing the range of x values to generate.
- 'n' is the number of data points to generate. The default value is 100.
- 'f' is a function that takes a single argument and returns a single value. The default function is a non-linear function of x with random noise: x -> x ^ 1.5  + np.random.normal(0, 100).
Returns:
- A pandas data frame with two columns, 'x' and 'y'.
Details:
- 'x' values are generated randomly between x_range[0] and x_range[1].
- 'y' values are generated by applying the 'f' function to the 'x' values.
- The data frame is sorted by the 'x' values.
"""

def gendata(x_range, n=100, f=lambda x: x ** 1.5 + np.random.normal(0, 100)):
    x = np.random.randint(x_range[0], x_range[1], n)
    y = f(x)
    data = pd.DataFrame({'x': x, 'y': y})
    data = data.sort_values('x')
    return data

def display(data):
    print(data)

"""
Create a function 'plot_data' that plots the data points from the data frame.
Arguments:
- 'data' is a pandas data frame with two columns, 'x' and 'y'.
Returns:
- None
Details:
- The data points are plotted as a scatter plot.
- The plot has a title 'Data Points', x-axis label 'x', and y-axis label 'f(x)'.
"""

def plotdata(data):
    plt.scatter(data['x'], data['y'])
    plt.title('Data Points')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.show()
"""
Create a function 'main' that generates data points and plots them.
Arguments:
- None
Returns:
- None
"""

def main():
    data = gendata((0, 100), 75, lambda x: x ** 1.5 + np.random.normal(0, 50))
    plotdata(data)
    display(data)

if __name__ == '__main__':
    main()
