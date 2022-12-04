#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np


class LayoutMap(object):

    def __init__(self):
        self.polygon_list = []
        self.map_start_point = None
        self.map = None
        return

    def reset(self):
        self.polygon_list = []
        self.map_start_point = None
        self.map = None
        return True

    def addPolygon(self, point_list):
        self.polygon_list.append(point_list)
        return True

    def generateMap(self):
        self.map_start_point = None
        self.map = None

        if len(self.polygon_list) == 0:
            return True

        map_x_min = float('inf')
        map_y_min = float('inf')
        map_x_max = -float('inf')
        map_y_max = -float('inf')

        for point_list in self.polygon_list:
            x_min = np.min(point_list[:, 0])
            y_min = np.min(point_list[:, 1])
            x_max = np.max(point_list[:, 0])
            y_max = np.max(point_list[:, 1])

            map_x_min = min(map_x_min, x_min)
            map_y_min = min(map_y_min, y_min)
            map_x_max = max(map_x_max, x_max)
            map_y_max = max(map_y_max, y_max)

        self.map_start_point = [int(map_x_min), int(map_y_min)]
        map_width = ceil(map_x_max - map_x_min)
        map_height = ceil(map_y_max - map_y_min)

        self.map = np.zeros((map_width, map_height), dtype=np.uint8)
        print("self.map.shape")
        print(self.map.shape)
        return True
