"""
Copyright (C) 2018 Sagar Mandal - All Rights Reserved
You may use, distribute and modify this code under the
terms of the GNU GPLv3 license.

You should have received a copy of the GNU GPLv3 license with
this file. If not, please write to: sagar187@hotmail.com.
"""

import numpy as np
import math


class GUI_Values(object):

    def fetch_peak_wavelengths(self, values=None):
        if values is not None:
            peaks = values
        peaks = 2 * math.pi * 299792458 * 1000000 / peaks
        return peaks

    def fetch_peak_strengths(self, values=None):
        if values is not None:
            peak_strengths = values
        return peak_strengths

    def fetch_peak_widths(self, values=None):
        if values is not None:
            limit_1 = values[0]
            limit_2 = values[1]
        delta = 2 * math.pi * 299792458 * 1000000 * ((1 / limit_1) - (1 / limit_2))
        return delta

    def fetch_film_thickness(self, values=None):
        d = []
        if values is not None:
            d = values
        return d

    def fetch_E(self, values=None):
        if values is not None:
            e = values
        return e

    def __init__(self, peaks=None, strengths=None, widths=None, thickness=None, e=None):
        self.peaks = self.fetch_peak_wavelengths() if peaks is None else self.fetch_peak_wavelengths(peaks)
        self.peak_strengths = self.fetch_peak_strengths() if strengths is None else strengths
        self.delta = self.fetch_peak_widths() if widths is None else self.fetch_peak_widths(widths)
        self.d = self.fetch_film_thickness() if thickness is None else thickness
        self.e = self.fetch_E() if e is None else e
