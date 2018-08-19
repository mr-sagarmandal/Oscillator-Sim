"""
Copyright (C) 2018 Sagar Mandal - All Rights Reserved
You may use, distribute and modify this code under the
terms of the GNU GPLv3 license.

You should have received a copy of the GNU GPLv3 license with
this file. If not, please write to: sagar187@hotmail.com.
"""
import sys
sys.path.append('..')

import os
import csv
import numpy as np
from Oscillator_Sim.UnitTests.GUI_Values_Test import get_sample_gui
from Oscillator_Sim.Utilities.Parameters import Parameters
from Oscillator_Sim.Utilities.LorentzFit import LorentzFit


def get_file_location():
    PATH_TO_RESULTS = "..\\Files\\UnitTest_Results"
    PATH_TO_RESULTS_2 = ".\\Files\\UnitTest_Results"
    RESULTS_FILE_NAME = "lorentz_out.csv"
    if os.path.exists(os.path.join(PATH_TO_RESULTS, RESULTS_FILE_NAME)):
        return os.path.join(PATH_TO_RESULTS, RESULTS_FILE_NAME)
    elif os.path.exists(os.path.join(PATH_TO_RESULTS_2, RESULTS_FILE_NAME)):
        return os.path.join(PATH_TO_RESULTS_2, RESULTS_FILE_NAME)


def get_result_values():
    file = get_file_location()
    raw_data = list(csv.reader(open(file), delimiter=','))
    test_results = dict(
        prediction_1=np.array(list(raw_data))[:, 0].astype('float'),
        prediction_2=np.array(list(raw_data))[:, 1].astype('float')
    )
    return test_results


def test_computed_predictions():
    lorentz_fit = LorentzFit(Parameters(), get_sample_gui())
    lorentz_fit.compute_predictions()
    expected_output_val = get_result_values()
    difference_1 = np.mean((expected_output_val['prediction_1'] - lorentz_fit.prediction_1) ** 2)
    difference_2 = np.mean((expected_output_val['prediction_2'] - lorentz_fit.prediction_2) ** 2)
    assert(difference_1 < 1)
    assert(difference_2 < 1)


if __name__ == "__main__":
    test_computed_predictions()