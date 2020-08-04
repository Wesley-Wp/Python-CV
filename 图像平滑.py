# -*- coding:utf-8 -*-
"""
# @Time  :2020/8/2 15:01
#@Author :Wesley
#@File   :图像平滑.py
#@IDE    :PyCharm
#@Email  :984@qq.com
"""

import cv2
import numpy as np

img = cv2.imread('./ImageExample/LenaNoise.png', 1)
cv2.imshow('img', img)

blur = cv2.blur(img, (3, 3))  # 均值滤波

box = cv2.boxFilter(img, -1, (3, 3), normalize=False)  # 方框滤波

aussian = cv2.GaussianBlur(img, (5, 5), 1)  # 高斯滤波

median = cv2.medianBlur(img, 5)  # 中值滤波

res = np.hstack((blur, aussian, median))
print(res)
cv2.imshow('all', res)

cv2.imshow('box', box)
cv2.imshow('blur', blur)
cv2.imshow('aussion', aussian)
cv2.imshow('median', median)
cv2.waitKey(0)
