#!/usr/bin/env python
# -*- coding: utf-8 -*-

from copy import deepcopy

import cv2
import numpy as np

from scene_layout_detect.Method.cluster import clusterPolylines


def getPolylines(explore_map, dist_max=4):
    image_gray = cv2.cvtColor(explore_map, cv2.COLOR_RGB2GRAY)

    unknown_mask = (image_gray < 192) & (image_gray > 64)

    thresh = np.ones_like(image_gray, dtype=np.uint8) * 255
    thresh[np.where(unknown_mask)] = 0

    contours, _ = cv2.findContours(thresh, 3, 2)
    cnt = contours[0]

    polylines = cv2.approxPolyDP(cnt, dist_max, True)
    return polylines


global render_idx
render_idx = 1


def getBoundary(explore_map, dist_max=4, render=False, print_progress=False):
    polylines = getPolylines(explore_map, dist_max)

    line_cluster = clusterPolylines(polylines, print_progress)

    if render:
        render_image = deepcopy(explore_map)
        cv2.polylines(render_image, [polylines], True, (0, 0, 255), 4)
        global render_idx
        cv2.imshow("polylines " + str(render_idx), render_image)
        render_idx += 1

    print(polylines.shape)

    boundary = []
    return boundary
