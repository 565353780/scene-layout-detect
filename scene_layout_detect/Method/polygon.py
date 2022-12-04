#!/usr/bin/env python
# -*- coding: utf-8 -*-


from copy import deepcopy

import numpy as np

from scene_layout_detect.Method.angle import getInRangeAngleIdx, getPointsAngle
from scene_layout_detect.Method.project import getProjectPoints


def getPolygon(camera_point, point_array, delta_angle):
    point_list = []

    points = getProjectPoints(point_array)

    copy_camera_point = deepcopy(camera_point).reshape(3)[:2]
    angle_array = getPointsAngle(copy_camera_point, points)

    angle_num = int(360.0 / delta_angle)
    delta_angle = 360.0 / angle_num
    for i in range(angle_num):
        angle_min = i * delta_angle
        angle_max = (i + 1) * delta_angle
        in_range_point_idx = getInRangeAngleIdx(angle_array, angle_min,
                                                angle_max)
        if in_range_point_idx.shape[0] == 0:
            continue
        angle_mean = (angle_min + angle_max) / 2.0
        rad_mean = angle_mean * np.pi / 180.0
    return point_list
