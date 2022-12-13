#!/usr/bin/env python
# -*- coding: utf-8 -*-

from copy import deepcopy
from multiprocessing import Process

import numpy as np
import open3d as o3d
from scannet_sim_manage.Method.render import drawGeometries

from scene_layout_detect.Method.polygon import getPolygon
from scene_layout_detect.Method.project import getProjectPoints


def getPointsPCD(point_array, color=None):
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(point_array)
    if color is not None:
        colors = np.zeros_like(point_array)
        colors[:] = color
        pcd.colors = o3d.utility.Vector3dVector(colors)
    return pcd


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
    drawGeometries([pcd])
    return True


def renderPolygon(camera_point, point_array, delta_angle):
    points = point_array[np.where(point_array[:, 0] != float("inf"))[0]]
    pcd = getPointsPCD(points)
    drawGeometries([pcd])

    pcd = getProjectPCD(camera_point, point_array)
    polygon_pcd = getPolygonPCD(camera_point, point_array, delta_angle)

    drawGeometries([pcd, polygon_pcd])
    return True


def renderPolygonList(polygon_list):
    pcd_list = []
    for polygon in polygon_list:
        pcd = getPointsPCD(polygon)
        pcd_list.append(pcd)

    drawGeometries(pcd_list)
    return True


def renderPolygonAndFloor(polygon_list, floor_array):
    pcd_list = []
    for polygon in polygon_list:
        pcd = getPointsPCD(polygon)
        pcd_list.append(pcd)

    floor_pcd = getPointsPCD(floor_array, [1, 0, 0])
    pcd_list.append(floor_pcd)

    drawGeometries(pcd_list)
    return True


def drawMeshList(mesh_list, window_name="Open3D"):
    process = Process(target=o3d.visualization.draw_geometries,
                      args=(mesh_list, window_name))
    process.start()
    #  process.join()
    #  process.close()
    return True
