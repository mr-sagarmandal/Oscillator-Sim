"""
Copyright (C) 2018 Sagar Mandal - All Rights Reserved
You may use, distribute and modify this code under the
terms of the GNU GPLv3 license.

You should have received a copy of the GNU GPLv3 license with
this file. If not, please write to: sagar187@hotmail.com.
"""

import numpy as np
import cmath


class LorentzFit(object):

    def compute_predictions(self):
        param_length = np.shape(self.parameters.wavelengths)[0]
        peaks_length = np.shape(self.gui_values.peaks)[0]
        e = self.gui_values.e

        n = np.zeros([param_length, 1])
        K = np.zeros([param_length, 1])

        for ii in range(0, param_length):
            w = self.parameters.frequencies[ii]
            for jj in range(0, peaks_length):
                e = (e + self.gui_values.peak_strengths[jj] * (self.gui_values.peaks[jj] ** 2)) \
                    / ((self.gui_values.peaks[jj] ** 2) - (w ** 2) + (w * self.gui_values.delta[jj] * 1j))

            n[ii] = (cmath.sqrt(e)).real
            K[ii] = (cmath.sqrt(e)).imag * -1
            self.prediction_1[ii] = (abs((1 - ((1 - (n[ii] + 1j * K[ii])) / ( 1 + (n[ii] + 1j * K[ii]))) ** 2)
                                         / (cmath.exp(-2j * (n[ii] + 1j * K[ii]) * self.parameters.k[ii]
                                                      * self.gui_values.d[0])
                                            - ((1 - (n[ii] + 1j * K[ii])) / (1 + (n[ii] + 1j * K[ii]))) ** 2))) ** 2

            self.prediction_2[ii] = (abs((1 - ((1 - (n[ii] + 1j * K[ii])) / ( 1 + (n[ii] + 1j * K[ii]))) ** 2)
                                         / (cmath.exp(-2j * (n[ii] + 1j * K[ii]) * self.parameters.k[ii]
                                                      * self.gui_values.d[1])
                                            - ((1 - (n[ii] + 1j * K[ii])) / (1 + (n[ii] + 1j * K[ii]))) ** 2))) ** 2

    def __init__(self, parameters, gui_values):
        self.parameters = parameters
        self.gui_values = gui_values
        self.prediction_1 = np.zeros([np.shape(self.parameters.wavelengths)[0], 1])
        self.prediction_2 = np.zeros([np.shape(self.parameters.wavelengths)[0], 1])


