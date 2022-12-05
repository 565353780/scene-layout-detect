#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import open3d as o3d

from scene_layout_detect.Data.layout_map import LayoutMap

from scene_layout_detect.Method.polygon import getPolygon
from scene_layout_detect.Method.render import renderPolygon


class LayoutMapBuilder(object):

    def __init__(self):
        self.layout_map = LayoutMap()
        return

    def reset(self):
        self.layout_map.reset()
        return True

    def addPoints(self, camera_point, point_array):
        delta_angle = 2

        renderPolygon(camera_point, point_array, delta_angle)

        polygon = getPolygon(camera_point, point_array, delta_angle)
        self.layout_map.addPolygon(polygon)
        return True

    def generateMap(self):
        assert self.layout_map.generateMap()
        return True
