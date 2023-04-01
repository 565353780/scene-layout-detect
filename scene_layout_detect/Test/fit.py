#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scipy import optimize


def f_line(x, A, B):
    return A * x + B


def fLine(xy, A, B, C):
    x = xy[:, 0]
    y = xy[:, 1]
    return A * x + B * y + C


def test():
    x_list = [0, 1, 2]
    y_list = [1, 2, 3]

    A, B = optimize.curve_fit(f_line, x_list, y_list)[0]
    print('y=' + str(A) + 'x+' + str(B))

    xy_list = [[0, 1], [1, 2], [2, 3]]
    zero_list = [0, 0, 0]

    A, B, C = optimize.curve_fit(fLine, xy_list, zero_list)[0]
    if A != 0:
        B /= A
        C /= A
        A = 1.0
    elif B != 0:
        A /= B
        C /= B
        B = 1.0
    else:
        C = 0.0

    print(str(A) + 'x+' + str(B) + 'y+' + str(C) + '=0')
    return True
