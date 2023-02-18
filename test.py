#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2

image_file_path = ""

image = cv2.imread(image_file_path)

_, thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
contours, hierarchy = cv2.findContours(thresh, 3, 2)
cnt = contours[0]

approx = cv2.approxPolyDP(cnt, 3, True)

render_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
cv2.polylines(render_image, [approx], True, (255, 0, 0), 2)

print("len(approx) = " + str(len(approx)))
cv2.imshow('approxPloyDP', render_image)
cv2.waitKey(0)
