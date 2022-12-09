#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import open3d as o3d
from copy import deepcopy

from scene_layout_detect.Data.layout_map import LayoutMap

from scene_layout_detect.Method.polygon import getPolygon
from scene_layout_detect.Method.render import renderPolygon


class LayoutMapBuilder(object):

    def __init__(self, delta_angle=2, unit_size=0.01, free_width=50):
        self.delta_angle = delta_angle
        self.unit_size = unit_size
        self.free_width = free_width

        self.layout_map = LayoutMap(self.unit_size, self.free_width)
        self.layout_mesh = None
        return

    def reset(self):
        self.layout_map.reset()
        self.layout_mesh = None
        return True

    def addPoints(self, camera_point, point_array, render=False):
        if render:
            renderPolygon(camera_point, point_array, self.delta_angle)

        polygon = getPolygon(camera_point, point_array, self.delta_angle)
        self.layout_map.addPolygon(polygon)
        return True

    def addBound(self, bound_point_array, render=False):
        polygon = deepcopy(bound_point_array)
        polygon[:, 2] = 0
        self.layout_map.addPolygon(polygon)
        return True

    def updateLayoutMesh(self, render=False):
        self.layout_mesh = self.layout_map.generateLayoutMesh(
            self.unit_size, self.free_width, render)
        return True
