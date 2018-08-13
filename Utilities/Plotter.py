"""
Copyright (C) 2018 Sagar Mandal - All Rights Reserved
You may use, distribute and modify this code under the
terms of the GNU GPLv3 license.

You should have received a copy of the GNU GPLv3 license with
this file. If not, please write to: sagar187@hotmail.com.
"""


import matplotlib.pyplot as plt
from cycler import cycler
import numpy as np


def plot_predictions(predictions, wavelengths):

    default_cycle = (cycler(color=['r', 'g', 'b', 'y']))
    plt.rc('lines', linewidth=1)
    plt.rc('axes', prop_cycle=default_cycle)

    for prediction in predictions:
        plt.plot(wavelengths, prediction)

    plt.show()


if __name__ == '__main__':
    x = np.linspace(0, 2 * np.pi, 50)
    yy = [np.array(np.sin(x)), np.array(np.cos(x))]
    print(yy[0].shape)
    print(x.shape)
    plot_predictions(yy, x)
