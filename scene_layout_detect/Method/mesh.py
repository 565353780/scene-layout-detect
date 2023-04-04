#!/usr/bin/env python
# -*- coding: utf-8 -*-

from copy import deepcopy

import numpy as np
import open3d as o3d
import calfem.geometry as cfg
import calfem.mesh as cfm
import calfem.vis as cfv


def generateLayoutMesh(floor_array, wall_height=3, top_floor_array=None):
    point_num = len(floor_array)

    if top_floor_array is None:
        top_floor_array = deepcopy(floor_array)
        top_floor_array[:, 2] += wall_height

    verts = np.vstack((floor_array, top_floor_array))

    triangles = []
    for i in range(point_num):
        next_idx = (i + 1) % point_num
        triangles.append([i, next_idx, next_idx + point_num])
        triangles.append([next_idx + point_num, i + point_num, i])

    g = cfg.Geometry()
    for i in range(point_num):
        g.point([floor_array[i][0], floor_array[i][1]])
        next_idx = (i + 1) % point_num
        g.spline([i, next_idx])

    cfv.drawGeometry(g)
    cfv.showAndWait()
    exit()

    #  triangles = np.array([
    #  [0, 1, 2],
    #  [2, 3, 0],
    #  [0, 4, 5],
    #  [5, 1, 0],
    #  [1, 5, 6],
    #  [6, 2, 1],
    #  [2, 6, 7],
    #  [7, 3, 2],
    #  [3, 7, 4],
    #  [4, 0, 3],
    #  [4, 7, 6],
    #  [6, 5, 4],
    #  ])

    mesh = o3d.geometry.TriangleMesh()
    mesh.vertices = o3d.utility.Vector3dVector(verts)
    mesh.triangles = o3d.utility.Vector3iVector(triangles)
    mesh.compute_vertex_normals()
    return mesh
