# File under GNU GPL (v3) licence, see LICENSE file for details.
# This software is distributed WITHOUT ANY WARRANTY; without even
# the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
# PURPOSE.

import pytest
import numpy as np
from os import system
from pathlib import Path


def compare(one, two):
    if one < 1e-7 or two < 1e-7:
        return '{:0.5e}'.format(one) == '{:0.5e}'.format(two)
    else:
        return '{:0.6e}'.format(one) == '{:0.6e}'.format(two)


def test_cfd():
    cmd = ("turtleFSI --problem TF_cfd -dt 0.01 -T 0.05 --verbose True" +
           " --folder tmp --sub-folder 1")
    d = system(cmd)

    drag = np.loadtxt(Path.cwd().joinpath("tmp/1/Drag.txt"))[-1]
    lift = np.loadtxt(Path.cwd().joinpath("tmp/1/Lift.txt"))[-1]
    drag_reference = 2.5637554331614054
    lift_reference = -0.02078995609237899

    assert compare(drag, drag_reference)
    assert compare(lift, lift_reference)


def test_csm():
    cmd = ("turtleFSI --problem TF_csm -dt 0.01 -T 0.05 --verbose True" +
           " --folder tmp --sub-folder 2")
    d = system(cmd)

    distance_x = np.loadtxt("tmp/2/dis_x.txt")[-1]
    distance_y = np.loadtxt("tmp/2/dis_y.txt")[-1]
    distance_x_reference = -6.13487990897633e-06
    distance_y_reference = -3.9398599897576816e-05

    assert compare(distance_x, distance_x_reference)
    assert compare(distance_y, distance_y_reference)


def test_fsi():
    cmd = ("turtleFSI --problem TF_fsi -dt 0.01 -T 0.05 --verbose True --theta 0.51" +
           " --folder tmp --sub-folder 3")
    d = system(cmd)

    drag = np.loadtxt("tmp/3/Drag.txt")[-1]
    lift = np.loadtxt("tmp/3/Lift.txt")[-1]
    distance_x = np.loadtxt("tmp/3/dis_x.txt")[-1]
    distance_y = np.loadtxt("tmp/3/dis_y.txt")[-1]
    distance_x_reference = -3.0193475393178104e-06
    distance_y_reference = -2.6594621765280973e-08
    drag_reference = 2.472928697982334
    lift_reference = -0.003950732063025264

    assert compare(distance_x, distance_x_reference)
    assert compare(distance_y, distance_y_reference)
    assert compare(drag, drag_reference)
    assert compare(lift, lift_reference)


@pytest.mark.parametrize("extrapolation_sub_type", ["volume", "volume_change",
                                                    "constant", "small_constant"])
def test_laplace(extrapolation_sub_type):
    cmd = ("turtleFSI --problem TF_fsi -dt 0.01 -T 0.05 --verbose True --theta 0.51" +
           " --folder tmp --sub-folder 4")
    d = system(cmd)

    drag = np.loadtxt("tmp/4/Drag.txt")[-1]
    lift = np.loadtxt("tmp/4/Lift.txt")[-1]
    distance_x = np.loadtxt("tmp/4/dis_x.txt")[-1]
    distance_y = np.loadtxt("tmp/4/dis_y.txt")[-1]
    distance_x_reference = -3.0193475393178104e-06
    distance_y_reference = -2.6594621765280973e-08
    drag_reference = 2.472928697982334
    lift_reference = -0.003950732063025264

    assert compare(distance_x, distance_x_reference)
    assert compare(distance_y, distance_y_reference)
    assert compare(drag, drag_reference)
    assert compare(lift, lift_reference)


@pytest.mark.parametrize("extrapolation_sub_type", ["constrained_disp", "constrained_disp_vel"])
def test_biharmonic(extrapolation_sub_type):
    cmd = ("turtleFSI --problem TF_fsi -dt 0.01 -T 0.05 --verbose True --theta 0.51" +
           " --extrapolation biharmonic --folder tmp --sub-folder 5")
    d = system(cmd)

    drag = np.loadtxt("tmp/5/Drag.txt")[-1]
    lift = np.loadtxt("tmp/5/Lift.txt")[-1]
    distance_x = np.loadtxt("tmp/5/dis_x.txt")[-1]
    distance_y = np.loadtxt("tmp/5/dis_y.txt")[-1]
    distance_x_reference = -3.0193475393178104e-06
    distance_y_reference = -2.6594621765280973e-08
    drag_reference = 2.472928697982334
    lift_reference = -0.003950732063025264

    assert compare(distance_x, distance_x_reference)
    assert compare(distance_y, distance_y_reference)
    assert compare(drag, drag_reference)
    assert compare(lift, lift_reference)


def test_elastic():
    cmd = ("turtleFSI --problem TF_fsi -dt 0.01 -T 0.05 --verbose True --theta 0.51" +
           " -e elastic -et constant --folder tmp --sub-folder 6")
    d = system(cmd)

    drag = np.loadtxt("tmp/6/Drag.txt")[-1]
    lift = np.loadtxt("tmp/6/Lift.txt")[-1]
    distance_x = np.loadtxt("tmp/6/dis_x.txt")[-1]
    distance_y = np.loadtxt("tmp/6/dis_y.txt")[-1]
    distance_x_reference = -3.019356900018008e-06
    distance_y_reference = -2.659921700576888e-08
    drag_reference = 2.472926160030297
    lift_reference = -0.0039508769183140835

    assert compare(distance_x, distance_x_reference)
    assert compare(distance_y, distance_y_reference)
    assert compare(drag, drag_reference)
    assert compare(lift, lift_reference)
