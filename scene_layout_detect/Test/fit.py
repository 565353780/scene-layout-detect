#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scene_layout_detect.Method.dist import fitLine


def outputLine(line_param):
    A, B, C = line_param
    if A is None:
        print('this line is a single point')
    else:
        print(str(A) + ' x + ' + str(B) + ' y + ' + str(C) + ' = 0')
    return True


def test():
    outputLine(fitLine([[0, 1], [1, 2], [2, 3]]))
    outputLine(fitLine([[322, 74], [304, 63], [303, 56]]))
    outputLine(fitLine([[0, 0], [1, 0], [2, 0]]))
    outputLine(fitLine([[0, 0], [0, 1], [0, 2]]))
    return True
