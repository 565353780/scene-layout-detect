#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2

from scene_layout_detect.Module.explore_point_extractor import ExplorePointExtractor


def demo():
    explore_map_file_path = "./output/explore_map.jpg"
    render = True

    explore_map = cv2.imread(explore_map_file_path)[:, :, 0]

    explore_point_extractor = ExplorePointExtractor()
    explore_point_extractor.extractExplorePoints(explore_map, render)
    return True
