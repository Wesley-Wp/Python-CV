# -*- coding:utf-8 -*-
"""
# @Time  :2020/8/2 15:03
#@Author :Wesley
#@File   :开运算与闭运算.py
#@IDE    :PyCharm
#@Email  :984@qq.com
"""
# 开：先腐蚀，再膨胀
import cv2
import numpy as np

img = cv2.imread('./ImageExample/dige.png')
Kernel = np.ones((5, 5), np.uint8)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, Kernel)
cv2.imshow('opening', opening)

# # 闭：先膨胀，再腐蚀
# closing = cv2.morphologyEx(img,cv2.MORPH_CLOSE,Kernel)
# cv2.imshow('a',closing)
#
# cv2.waitKey(0)
