#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import open3d as o3d
from copy import deepcopy

from scene_layout_detect.Data.layout_map import LayoutMap
from scene_layout_detect.Data.explore_map import ExploreMap

from scene_layout_detect.Method.polygon import getPolygon
from scene_layout_detect.Method.render import renderPolygon

from scene_layout_detect.Module.explore_point_extractor import ExplorePointExtractor


class LayoutMapBuilder(object):

    def __init__(self, delta_angle=2, unit_size=0.01, free_width=50):
        self.delta_angle = delta_angle
        self.unit_size = unit_size
        self.free_width = free_width

        self.layout_map = LayoutMap(self.unit_size, self.free_width)
        self.explore_map = ExploreMap(self.unit_size, self.free_width)
        self.layout_mesh = None

        self.explore_point_extractor = ExplorePointExtractor()
        self.explore_point_idx_array = None
        return

    def reset(self):
        self.layout_map.reset()
        self.explore_map.reset()
        self.layout_mesh = None
        self.explore_point_idx_array = None
        return True

    def addPoints(self,
                  camera_point,
                  point_array,
                  explore_paint_radius=0.1,
                  render=False):
        if render:
            renderPolygon(camera_point, point_array, self.delta_angle)

        polygon = getPolygon(camera_point, point_array, self.delta_angle)
        self.explore_map.updateFree(polygon)
        self.explore_map.addPoints(point_array, explore_paint_radius, render)
        self.layout_map.addPolygon(polygon)
        return True

    def addBound(self, bound_point_array, render=False):
        polygon = deepcopy(bound_point_array)
        polygon[:, 2] = 0
        self.layout_map.addPolygon(polygon)
        return True

    def updateLayoutMesh(self, wall_height=3, render=False):
        self.layout_mesh = self.layout_map.generateLayoutMesh(
            self.unit_size, self.free_width, wall_height, render)
        return True

    def updateExplorePointIdx(self, min_explore_point_dist=5, render=False):
        self.explore_point_idx_array = self.explore_point_extractor.extractExplorePoints(
            self.explore_map.map, min_explore_point_dist, render)
        return True
