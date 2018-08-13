"""
Copyright (C) 2018 Sagar Mandal - All Rights Reserved
You may use, distribute and modify this code under the
terms of the GNU GPLv3 license.

You should have received a copy of the GNU GPLv3 license with
this file. If not, please write to: sagar187@hotmail.com.
"""
import sys

sys.path.append('../')

import os
import pytest
import numpy as np
from GUI.GUI_Values import GUI_Values




def get_test_values():
    test_values = {
        'peaks': np.array([
            1.2, 1.73, 1.76, 2.312, 2.352, 2.38, 2.45, 2.74,
            2.77, 3.23, 3.43, 3.51, 3.66, 3.8, 3.95, 4.95, 6.1,
            6.8, 6.82, 6.95, 7.26, 7.31, 7.395, 9.85, 13.7, 13.9, 14.9
        ]),
        'strengths': np.array([
            0.0000001, 0.0000003, 0.00000015, 0.0000055, 0.0000015, 0.000006,
            0.00004, 0.00001, 0.00001, 0.000001, 0.0022, 0.0009, 0.00003,
            0.00003, 0.000001, 0.00000015, 0.000001, 0.0015, 0.00035, 0.00005,
            0.000012, 0.00001, 0.00001, 0.00015, 0.00068, 0.00075, 0.00015
        ]),
        'widths': [
            np.array([
                1.195, 1.725, 1.755, 2.307, 2.342, 2.33, 2.4, 2.73, 2.76, 3.2,
                3.411, 3.5, 3.63, 3.77, 3.945, 4.945, 6.05, 6.784, 6.77, 6.915,
                7.255, 7.305, 7.39, 9.7, 13.63, 13.82, 14.65
            ]),
            np.array([
                1.205, 1.735, 1.765, 2.317, 2.362, 2.43, 2.5, 2.75, 2.78, 3.26,
                3.449, 3.52, 3.69, 3.83, 3.955, 4.955, 6.15, 6.816, 6.87, 6.985,
                7.265, 7.315, 7.4, 10, 13.77, 13.98, 15.15
            ])
        ],
        'thickness': [23, 45],
        'e': complex(1.49 ** 2, 0)
    }
    return test_values


def test_instantiation():
    test_values = get_test_values()
    test_gui = GUI_Values(peaks=test_values['peaks'], 
                          strengths=test_values['strengths'], widths=test_values[''],
                          thickness=test_values['thickness'], e=test_values['e'])
    assert test_gui.peaks == test_values['peaks ']
    assert test_gui.peak_strengths == test_values['strengths']
    assert test_gui.d == test_values['thickness']
    assert test_gui.e == test_values['e']


if __name__ == '__main__':
    pytest
