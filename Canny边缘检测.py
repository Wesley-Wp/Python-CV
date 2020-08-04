# -*- coding:utf-8 -*-
"""
# @Time  :2020/8/2 15:03
#@Author :Wesley
#@File   :Canny边缘检测.py
#@IDE    :PyCharm
#@Email  :984@qq.com
"""
import cv2
import numpy as np

img = cv2.imread('./ImageExample/car.png', 0)
v1 = cv2.Canny(img, 80, 150)
v2 = cv2.Canny(img, 50, 100)

res = np.hstack((v1, v2))
cv2.imshow('res', res)

cv2.waitKey(0)