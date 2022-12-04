#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import open3d as o3d
from copy import deepcopy

from scene_layout_detect.Data.layout_map import LayoutMap

from scene_layout_detect.Method.project import getProjectPoints
from scene_layout_detect.Method.angle import getPointsAngle
from scene_layout_detect.Method.render import renderProjectPoints


class LayoutMapBuilder(object):

    def __init__(self):
        self.layout_map = LayoutMap()
        return

    def reset(self):
        self.layout_map.reset()
        return True

    def addPoints(self, camera_point, point_array):
        #  renderProjectPoints(camera_point, point_array)

        points = getProjectPoints(point_array)
        copy_camera_point = deepcopy(camera_point).reshape(3)[:2]
        angle_array = getPointsAngle(copy_camera_point, points)
        return True
