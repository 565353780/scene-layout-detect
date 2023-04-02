#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from scipy import optimize


def fLine(xy, A, B, C):
    x = xy[:, 0]
    y = xy[:, 1]
    return A * x + B * y + C


def f_line(x, A, B):
    return A * x + B


def f_line_inv(y, A_inv, B_inv):
    return A_inv * y + B_inv


def getPointDistToPoint(point_1, point_2):
    point_1_array = np.array(point_1, dtype=float)
    point_2_array = np.array(point_2, dtype=float)
    return np.linalg.norm(point_1_array - point_2_array)


def isSamePoint(point_list):
    point_num = len(point_list)

    if point_num < 2:
        return True

    first_point = point_list[0]

    for i in range(1, point_num):
        point = point_list[i]
        if point[0] != first_point[0] or point[1] != first_point[1]:
            return False
    return True


def fitLine(point_list):
    assert len(point_list) > 0

    if isSamePoint(point_list):
        return None, None, None

    point_array = np.array(point_list, dtype=float)

    A_inv, B_inv = optimize.curve_fit(f_line, point_array[:, 1],
                                      point_array[:, 0])[0]

    if A_inv == 0:
        return 1.0, 0.0, -B_inv

    A, B = optimize.curve_fit(f_line, point_array[:, 0], point_array[:, 1])[0]

    return A, -1.0, B


def getPointDistToLine(point, line_param):
    A, B, C = line_param

    if A is None:
        line_point = [B, C]

        return getPointDistToPoint(point, line_point)

    line_weight = A * A + B * B

    assert line_weight > 0

    distance = np.abs(A * point[0] + B * point[1] + C) / np.sqrt(line_weight)
    return distance
