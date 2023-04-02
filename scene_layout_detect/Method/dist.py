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


def fitLine(point_list):
    point_array = np.array(point_list, dtype=float)

    A_inv, B_inv = optimize.curve_fit(f_line, point_array[:, 1],
                                      point_array[:, 0])[0]

    if A_inv == 0:
        return 1.0, 0.0, -B_inv

    A, B = optimize.curve_fit(f_line, point_array[:, 0], point_array[:, 1])[0]

    return A, -1.0, B


def getPointDistToLine(point, line):
    return 0


def get_distance_from_point_to_line(point, line_point1, line_point2):
    if line_point1 == line_point2:
        point_array = np.array(point)
        point1_array = np.array(line_point1)
        return np.linalg.norm(point_array - point1_array)

    A = line_point2[1] - line_point1[1]
    B = line_point1[0] - line_point2[0]
    C = (line_point1[1] - line_point2[1]) * line_point1[0] + \
        (line_point2[0] - line_point1[0]) * line_point1[1]

    distance = np.abs(A * point[0] + B * point[1] + C) / (np.sqrt(A**2 + B**2))
    return distance
