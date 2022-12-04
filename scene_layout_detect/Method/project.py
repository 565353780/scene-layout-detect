#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from copy import deepcopy


def getProjectPoints(point_array, dim=2):
    assert dim in [2, 3]

    points = point_array[np.where(point_array[:, 0] != float("inf"))[0]]
    project_points = deepcopy(points)

    if dim == 2:
        project_points = project_points[:, 2]
        return project_points

    project_points[:, 2] = 0
    return project_points
