# -*- coding:utf-8 -*-
"""
# @Time  :2020/8/2 15:04
#@Author :Wesley
#@File   :轮库检测.py
#@IDE    :PyCharm
#@Email  :984@qq.com
"""
import cv2

img = cv2.imread('./ImageExample/contours.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
cnt = contours[0]
draw_img = img.copy()
res = cv2.drawContours(draw_img, cnt, -1, (0, 0, 255), 2)

epsilon = 0.15 * cv2.arcLength(cnt, True)
approx = cv2.approxPolyDP(cnt, epsilon, True)
draw_img = img.copy()
a = cv2.drawContours(draw_img, [approx], -1, (0, 0, 255), 2)

x, y, w, h = cv2.boundingRect(cnt)
dst = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.imshow('c', dst)
cv2.imshow('b', a)
cv2.imshow('res', res)

cv2.waitKey(0)
