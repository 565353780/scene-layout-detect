#!/usr/bin/env python
# -*- coding: utf-8 -*-

from copy import deepcopy

import numpy as np
import open3d as o3d


def generateLayoutMesh(floor_array, height=3):
    top_floor_array = deepcopy(floor_array)
    top_floor_array[:, 2] += height

    verts = np.vstack((floor_array, top_floor_array))

    triangles = np.array([
        [0, 1, 2],
        [2, 3, 0],
        [0, 4, 5],
        [5, 1, 0],
        [1, 5, 6],
        [6, 2, 1],
        [2, 6, 7],
        [7, 3, 2],
        [3, 7, 4],
        [4, 0, 3],
        [4, 7, 6],
        [6, 5, 4],
    ])

    mesh = o3d.geometry.TriangleMesh()
    mesh.vertices = o3d.utility.Vector3dVector(verts)
    mesh.triangles = o3d.utility.Vector3iVector(triangles)
    mesh.compute_vertex_normals()
    return mesh
