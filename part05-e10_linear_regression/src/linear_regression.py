#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def fit_line(x, y):
    regression = LinearRegression(fit_intercept=True)
    regression.fit(x[:, np.newaxis],y)
    return (regression.coef_[0], regression.intercept_)


def main():
    np.random.seed(0)
    n=20  
    line_space=np.linspace(0, 10, n)
    m = line_space*2 + 1 + 1*np.random.randn(n) 
    a, b= fit_line(line_space,m)
    print(f"Slope: {a}")
    print(f"Intercept: {b}")
    #for each value of x, plot the value of y where the line will intercept
    abline_values = [a * i + b for i in line_space]
    plt.plot(line_space,m, 'x')
    plt.plot(line_space,abline_values,'b')
    plt.show()

    
if __name__ == "__main__":
    main()