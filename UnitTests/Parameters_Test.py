"""
Copyright (C) 2018 Sagar Mandal - All Rights Reserved
You may use, distribute and modify this code under the
terms of the GNU GPLv3 license.

You should have received a copy of the GNU GPLv3 license with
this file. If not, please write to: sagar187@hotmail.com.
"""
import sys
sys.path.append('..')
import math
import numpy as np
from Oscillator_Sim.Utilities.Parameters import Parameters


def get_test_values():
    test_values = dict(
        wavelengths=np.linspace(start=1, stop=17.5, num=3301),
        k=(2 * math.pi) / np.linspace(start=1, stop=17.5, num=3301),
        frequencies=(2 * math.pi * 299792458 * 1000000) /
        np.linspace(start=1, stop=17.5, num=3301))
    return test_values


def test_constructor():
    test_values = get_test_values()
    params = Parameters()
    assert(params.wavelengths == test_values['wavelengths']).all()
    assert(params.k == test_values['k']).all()
    assert(params.frequencies == test_values['frequencies']).all()


if __name__ == '__main__':
    test_constructor()
