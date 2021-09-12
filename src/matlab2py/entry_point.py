"""
Development entry point.
"""
from time import sleep

import numpy as np

from matlab2py.matlab import figure, axes, gca, gcf, groot, plot

if __name__ == "__main__":

    f = figure(5)
    ax = gca()
    x = np.linspace(0, 10, num=100)
    y = np.sin(x)
    plot(ax, x, y)
    sleep(5)
    f.Color = [0.5, 0.5, 0.5]