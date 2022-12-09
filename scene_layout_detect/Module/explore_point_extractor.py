#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np

from scene_layout_detect.Config.color import UNKNOWN_COLOR, FREE_COLOR, OBSTACLE_COLOR


class ExplorePointExtractor(object):

    def __init__(self):
        self.explore_bound_point_list = []
        self.explore_points = None
        return

    def reset(self):
        self.explore_bound_point_list = []
        self.explore_points = None
        return True

    def extractExploreBoundPoints(self, explore_map, render=False):
        obstacle_idx = np.where(explore_map < 54)
        explore_map[obstacle_idx] = OBSTACLE_COLOR
        unknown_idx = np.where((explore_map < 128 + 54) & (explore_map > 54))
        explore_map[unknown_idx] = UNKNOWN_COLOR
        free_idx = np.where(explore_map > 128 + 54)
        explore_map[free_idx] = FREE_COLOR

        render = True

        unknown_mask = explore_map == UNKNOWN_COLOR
        free_mask = explore_map == FREE_COLOR
        free_idx = np.where(free_mask == True)
        free_map = np.zeros_like(explore_map, dtype=np.uint8)
        free_map[free_idx] = 255

        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

        expand_free_map = cv2.dilate(free_map, kernel)

        expand_free_mask = expand_free_map == FREE_COLOR
        explore_mask = expand_free_mask & unknown_mask
        explore_idx = np.where(explore_mask == True)

        new_map = np.zeros_like(explore_map, dtype=np.uint8)
        new_map[explore_idx] = 255

        if render:
            cv2.imshow("explore_map", explore_map)
            cv2.imshow("free_area", new_map)
            cv2.waitKey(1)

        label_num, label_map, _, _ = cv2.connectedComponentsWithStats(new_map)

        bound_point_set_idx_list = []

        for i in range(1, label_num):
            cluster_idx = np.where(label_map == i)
            bound_point_set_idx_list.append(cluster_idx)

        if render:
            COLORS = np.array(
                [[0, 0, 255], [0, 255, 0], [255, 0, 0], [255, 255, 0],
                 [255, 0, 255], [0, 255, 255], [125, 0, 255], [0, 255, 125],
                 [255, 0, 125], [255, 255, 125], [255, 125, 255],
                 [0, 125, 255]],
                dtype=np.uint8)

            visual_map = np.zeros(
                (explore_map.shape[0], explore_map.shape[1], 3),
                dtype=np.uint8)
            for i, bound_point_set_idx in enumerate(bound_point_set_idx_list):
                visual_map[bound_point_set_idx] = COLORS[i]
            cv2.imshow("connect_area", visual_map)
            cv2.waitKey(0)

        free_expand_mask = free_mask
        return True

    def extractExplorePoints(self, explore_map, render=False):
        self.reset()

        self.extractExploreBoundPoints(explore_map, render)
        return True
