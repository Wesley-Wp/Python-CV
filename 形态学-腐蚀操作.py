# -*- coding:utf-8 -*-
"""
# @Time  :2020/8/2 15:01
#@Author :Wesley
#@File   :形态学-腐蚀操作.py
#@IDE    :PyCharm
#@Email  :984@qq.com
"""

import cv2
import numpy as np

img = cv2.imread('./ImageExample/dige.png')
Kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(img, Kernel, iterations=1)

dige_dilate = cv2.dilate(erosion, Kernel, iterations=1)
cv2.imshow('dia', dige_dilate)
cv2.imshow('img', img)
cv2.imshow('ero', erosion)
cv2.waitKey(0)
