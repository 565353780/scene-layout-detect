#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np


def getPointsAngle(start_point, point_array, return_angle=True):
    diff_point = point_array - start_point
    rad_array = np.arctan2(diff_point[:, 1], diff_point[:, 0])

    if not return_angle:
        return rad_array

    angle_array = rad_array * 180.0 / np.pi
    return angle_array
