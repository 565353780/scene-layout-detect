#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import open3d as o3d
from copy import deepcopy

from scannet_sim_manage.Method.render import render

from scene_layout_detect.Method.project import getProjectPoints
from scene_layout_detect.Method.polygon import getPolygon


def getProjectPCD(camera_point, point_array):
    copy_camera_point = deepcopy(camera_point).reshape(1, 3)
    copy_camera_point[0][2] = 0.0
    points = getProjectPoints(point_array)
    points = np.vstack((points, copy_camera_point))

    colors = np.zeros_like(points)
    colors[:, 1] = 1.0
    colors[-1] = [1.0, 0.0, 0.0]

    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)
    pcd.colors = o3d.utility.Vector3dVector(colors)
    return pcd


def getPolygonPCD(camera_point, point_array, delta_angle):
    points = getPolygon(camera_point, point_array, delta_angle)

    colors = np.zeros_like(points)
    colors[:, 2] = 1.0

    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)
    pcd.colors = o3d.utility.Vector3dVector(colors)
    return pcd


def renderProjectPoints(camera_point, point_array):
    pcd = getProjectPCD(camera_point, point_array)
    render([pcd])
    return True


def renderPolygon(camera_point, point_array, delta_angle):
    pcd = getProjectPCD(camera_point, point_array)
    polygon_pcd = getPolygonPCD(camera_point, point_array, delta_angle)

    render([pcd, polygon_pcd])
    return True
