#!/usr/bin/env python
# -*- coding: utf-8 -*-


def getClusterEnergy(polylines, line_cluster_idx_list):
    cluster_energy = 0
    return cluster_energy


def getCutLineClusterIdxLists(polylines, cut_num, start_idx=0, end_idx=-1):
    if end_idx == -1:
        end_idx = len(polylines)

    if cut_num > end_idx - start_idx:
        return []

    if cut_num == end_idx - start_idx:
        return [range(start_idx, end_idx)]

    cut_line_cluster_idx_lists = []

    for i in range(cut_num):


def clusterPolylines(polylines):
    line_cluster_idx_list = range(len(polylines))

    while len(line_cluster_idx_list) > 1:
        for i in range(len(line_cluster_idx_list)):
            next_idx = (i + 1) % len(line_cluster_idx_list)

    return line_cluster_idx_list
