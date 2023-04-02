#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

from scene_layout_detect.Data.line import Line
from scene_layout_detect.Method.dist import fitLine

mode_list = ['cut', 'merge', 'angle']
mode = 'angle'


def getClusterEnergy(polylines, line_cluster_idx_list):
    cluster_energy = 0
    return cluster_energy


def getClusterIdxList(line_num, cut_idx_list):
    if cut_idx_list == []:
        return [0 for _ in range(line_num)]

    cluster_idx_list = []

    current_idx = 0
    for i in range(line_num):
        cluster_idx_list.append(current_idx)

        if i == max(cut_idx_list):
            current_idx = 0
            continue

        if i in cut_idx_list:
            current_idx += 1
    return cluster_idx_list


def getCutLineClusterIdxLists(polylines,
                              cut_num,
                              current_cut_idx_list=[],
                              start_idx=0):
    line_num = len(polylines)

    if cut_num == 0:
        cluster_idx_list = getClusterIdxList(line_num, current_cut_idx_list)
        return [cluster_idx_list]

    assert cut_num <= line_num - start_idx

    if cut_num == line_num - start_idx:
        cut_idx_list = current_cut_idx_list + [range(start_idx, line_num)]
        cluster_idx_list = getClusterIdxList(line_num, cut_idx_list)
        return [cluster_idx_list]

    cut_line_cluster_idx_lists = []

    for i in range(start_idx, line_num):
        remain_cut_position_num = line_num - i - 1
        if remain_cut_position_num < cut_num - 1:
            break

        new_cut_idx_list = current_cut_idx_list + [i]
        sub_cluster_idx_lists = getCutLineClusterIdxLists(
            polylines, cut_num - 1, new_cut_idx_list, start_idx + 1)
        cut_line_cluster_idx_lists += sub_cluster_idx_lists

    return cut_line_cluster_idx_lists


def clusterPolylinesByCut(polylines, print_progress=False):
    for i in range(len(polylines)):
        line_cluster_idx_lists = getCutLineClusterIdxLists(polylines, i)
        print(line_cluster_idx_lists)
        print(np.array(line_cluster_idx_lists).shape)
        if i > 0:
            exit()

    exit()
    return line_cluster_idx_list


def getLineParallelError(polylines, start_idx, end_idx):
    point_num = len(polylines)

    point_list = []
    for i in range(start_idx, end_idx):
        point_idx = i % point_num
        point_list.append(polylines[point_idx])
        if i == end_idx - 1:
            end_point_idx = end_idx % point_num
            point_list.append(polylines[end_point_idx])

    line = fitLine(point_list)

    parallel_error = 0
    return parallel_error


def mergeLineByIdx(polylines, start_idx, end_idx):
    merged_polylines = []
    return merged_polylines


def mergeLineByParallelError(polylines):
    point_num = len(polylines)

    min_error = float('inf')
    min_error_start_idx = None
    min_error_end_idx = None

    for i in range(point_num):
        for j in range(2, point_num - 1):
            current_error = getLineParallelError(polylines, i, i + j)

            if current_error < min_error:
                min_error = current_error
                min_error_start_idx = i
                min_error_end_idx = i + j

    if min_error_start_idx is None:
        return polylines

    return mergeLineByIdx(polylines, min_error_start_idx, min_error_end_idx)


def clusterPolylinesByMerge(polylines, print_progress=False):
    merged_polylines = mergeLineByParallelError(polylines)
    return merged_polylines


def clusterPolylinesByAngle(polylines, print_progress=False):
    merged_polylines = mergeLineByParallelError(polylines)
    return merged_polylines


def clusterPolylines(polylines, print_progress=False):
    assert mode in mode_list

    if mode == 'cut':
        return clusterPolylinesByCut(polylines, print_progress)
    if mode == 'merge':
        return clusterPolylinesByMerge(polylines, print_progress)
    if mode == 'angle':
        return clusterPolylinesByAngle(polylines, print_progress)
