#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2


def test():
    image_idx = 0

    image_file_folder = "../auto-cad-recon/output/explore/"
    image_file_path = image_file_folder + str(image_idx) + ".png"

    image = cv2.imread(image_file_path)
    image_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    cv2.imshow('image_gray', image_gray)

    _, thresh = cv2.threshold(image_gray, 0, 255,
                              cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    contours, hierarchy = cv2.findContours(thresh, 3, 2)
    cnt = contours[0]

    cv2.imshow('thresh', thresh)

    approx = cv2.approxPolyDP(cnt, 3, True)

    render_image = cv2.cvtColor(image_gray, cv2.COLOR_GRAY2BGR)
    cv2.polylines(render_image, [approx], True, (255, 0, 0), 2)

    print("len(approx) = " + str(len(approx)))
    cv2.imshow('approxPloyDP', render_image)
    cv2.waitKey(0)
    return True
