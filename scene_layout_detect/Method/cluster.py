#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np


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


def clusterPolylines(polylines, print_progress=False):
    for i in range(len(polylines)):
        line_cluster_idx_lists = getCutLineClusterIdxLists(polylines, i)
        print(line_cluster_idx_lists)

    exit()
    return line_cluster_idx_list
