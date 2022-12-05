#!/usr/bin/env python
# -*- coding: utf-8 -*-

from copy import deepcopy
from math import ceil

import cv2
import numpy as np


class LayoutMap(object):

    def __init__(self, unit_size=0.01):
        self.unit_size = unit_size

        self.polygon_list = []
        self.map_start_point = None
        self.map = None
        return

    def reset(self):
        self.polygon_list = []
        self.map_start_point = None
        self.map = None
        return True

    def addPolygon(self, polygon):
        self.polygon_list.append(polygon)
        return True

    def generateMap(self, unit_size=0.01):
        self.unit_size = unit_size
        scale = 1.0 / unit_size

        self.map_start_point = None
        self.map = None

        if len(self.polygon_list) == 0:
            return True

        copy_polygon_list = deepcopy(self.polygon_list)

        for i in range(len(copy_polygon_list)):
            copy_polygon_list[i] = copy_polygon_list[i] * scale

        map_x_min = float('inf')
        map_y_min = float('inf')

        for polygon in copy_polygon_list:
            x_min = np.min(polygon[:, 0])
            y_min = np.min(polygon[:, 1])

            map_x_min = min(map_x_min, x_min)
            map_y_min = min(map_y_min, y_min)

        self.map_start_point = np.array(
            [int(map_x_min), int(map_y_min), 0], dtype=int)

        for i in range(len(copy_polygon_list)):
            copy_polygon_list[i] = copy_polygon_list[i] - self.map_start_point

        map_x_max = -float('inf')
        map_y_max = -float('inf')

        for polygon in copy_polygon_list:
            x_max = np.max(polygon[:, 0])
            y_max = np.max(polygon[:, 1])

            map_x_max = max(map_x_max, x_max)
            map_y_max = max(map_y_max, y_max)

        map_width = ceil(map_x_max)
        map_height = ceil(map_y_max)

        self.map = np.zeros((map_width, map_height), dtype=np.uint8)
        print("self.map.shape")
        print(self.map.shape)
        return True
