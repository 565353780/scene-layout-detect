#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from scipy import optimize


def line(x, A, B):
    return A * x + B


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
