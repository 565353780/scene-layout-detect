#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from scipy import optimize


def fLine(xy, A, B, C):
    x, y = xy
    return A * x + B * y + C


def fitLine(point_list):
    print("point_list is")
    print(point_list)
    print(np.array(point_list))
    zero_list = np.zeros(len(point_list))
    print(zero_list)

    A, B, C = optimize.curve_fit(fLine, point_list, zero_list)
    print(A, B, C)
    exit()
    return A, B, C


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
