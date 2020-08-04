# -*- coding:utf-8 -*-
"""
# @Time  :2020/8/2 15:00
#@Author :Wesley
#@File   :截取部分图像数据并提取颜色通道.py
#@IDE    :PyCharm
#@Email  :984@qq.com
"""

import cv2

img = cv2.imread('cat.jpg')
cat = img[0:200, 0:200]

cur_img = img.copy()
cur_img[:, :, 1] = 0
cur_img[:, :, 2] = 0

cv2.imshow('cat', cur_img)

cv2.waitKey(0)
