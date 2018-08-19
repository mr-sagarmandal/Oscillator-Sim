"""
Copyright (C) 2018 Sagar Mandal - All Rights Reserved
You may use, distribute and modify this code under the
terms of the GNU GPLv3 license.

You should have received a copy of the GNU GPLv3 license with
this file. If not, please write to: sagar187@hotmail.com.
"""

from Utilities.Plotter import plot_predictions
from UnitTests.GUI_Values_Test import get_sample_gui
from Utilities.Parameters import Parameters
from Utilities.LorentzFit import LorentzFit


def test_plot_predictions():
    lorentz_fit = LorentzFit(Parameters(), get_sample_gui())
    lorentz_fit.compute_predictions()
    plot_predictions([lorentz_fit.prediction_1, lorentz_fit.prediction_2],
                     lorentz_fit.parameters.wavelengths)


if __name__ == "__main__":
    test_plot_predictions()