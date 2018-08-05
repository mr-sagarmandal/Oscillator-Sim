"""
Copyright (C) 2018 Sagar Mandal - All Rights Reserved
You may use, distribute and modify this code under the
terms of the GNU GPLv3 license.

You should have received a copy of the GNU GPLv3 license with
this file. If not, please write to: sagar187@hotmail.com.
"""

import matplotlib as plt
import numpy as np
import math


def fetch_wavelength_array():
    wavelengths = np.linspace(start=1, stop=17.5, num=3301)
    return wavelengths

def fetch_k():
    k = (2 * math.pi) / get_wavelength_array()
    return k

def fetch_frequencies():
    frequencies = (2 * math.pi * 299792458 * 1000000) / get_wavelength_array()
    return frequencies