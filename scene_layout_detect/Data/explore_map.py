#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ExploreMap(object):

    def __init__(self, unit_size=0.01, free_width=50):
        self.unit_size = unit_size
        self.free_width = free_width

        self.polygon_list = []
        self.map_start_point = None
        self.floor_array = []
        self.map = None
        return

    def reset(self):
        self.polygon_list = []
        self.map_start_point = None
        self.floor_array = []
        self.map = None
        return True
