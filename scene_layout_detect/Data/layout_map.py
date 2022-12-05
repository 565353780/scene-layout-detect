#!/usr/bin/env python
# -*- coding: utf-8 -*-

from copy import deepcopy
from math import ceil

import cv2
import numpy as np


class LayoutMap(object):

    def __init__(self, unit_size=0.01, free_width=50):
        self.unit_size = unit_size
        self.free_width = free_width

        self.polygon_list = []
        self.map_start_point = None
        self.map = None
        return

    def reset(self):
        self.polygon_list = []
        self.map_start_point = None
        self.map = None
        return True

    def getPixelFromPoint(self, point):
        scale_point = point / self.unit_size
        diff = scale_point - self.map_start_point
        pixel = np.array(int(diff[0]), int(diff[1]), dtype=int)
        return pixel

    def getPointFromPixel(self, x, y):
        translate_x = x + self.map_start_point[0]
        translate_y = y + self.map_start_point[1]
        point = np.array(translate_x * self.unit_size,
                         translate_y * self.unit_size,
                         0,
                         dtype=float)
        return point

    def addPolygon(self, polygon):
        self.polygon_list.append(polygon)
        return True

    def generateMap(self, unit_size=0.01, free_width=50):
        self.unit_size = unit_size
        self.free_width = free_width
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

        self.map_start_point = np.array([
            int(map_x_min) - self.free_width,
            int(map_y_min) - self.free_width, 0
        ],
                                        dtype=int)

        for i in range(len(copy_polygon_list)):
            copy_polygon_list[i] = copy_polygon_list[i] - self.map_start_point

        map_x_max = -float('inf')
        map_y_max = -float('inf')

        for polygon in copy_polygon_list:
            x_max = np.max(polygon[:, 0])
            y_max = np.max(polygon[:, 1])

            map_x_max = max(map_x_max, x_max)
            map_y_max = max(map_y_max, y_max)

        map_width = ceil(map_x_max) + self.free_width
        map_height = ceil(map_y_max) + self.free_width

        self.map = np.zeros((map_width, map_height), dtype=np.uint8)

        for polygon in copy_polygon_list:
            pts = polygon[:, :2].astype(int)
            pts = pts[..., ::-1]
            #  cv2.fillPoly(self.map, [pts], 255)
            cv2.polylines(self.map, [pts], True, 255)

        cv2.imshow("map_" + str(len(self.polygon_list)), self.map)
        cv2.waitKey(1)
        return True
