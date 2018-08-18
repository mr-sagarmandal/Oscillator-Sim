"""
Copyright (C) 2018 Sagar Mandal - All Rights Reserved
You may use, distribute and modify this code under the
terms of the GNU GPLv3 license.

You should have received a copy of the GNU GPLv3 license with
this file. If not, please write to: sagar187@hotmail.com.
"""

import numpy as np
import math


class Parameters(object):

    def fetch_wavelength_array(self):
        wavelengths = np.linspace(start=1, stop=17.5, num=3301)
        return wavelengths

    def fetch_k(self):
        k = (2 * math.pi) / self.fetch_wavelength_array()
        return k

    def fetch_frequencies(self):
        frequencies = (2 * math.pi * 299792458 * 1000000) / \
                      self.fetch_wavelength_array()
        return frequencies

    def __init__(self):
        self.wavelengths = self.fetch_wavelength_array()
        self.k = self.fetch_k()
        self.frequencies = self.fetch_frequencies()