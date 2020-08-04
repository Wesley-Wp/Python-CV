# -*- coding:utf-8 -*-
"""
# @Time  :2020/8/2 15:04
#@Author :Wesley
#@File   :直方图与傅里叶变换.py
#@IDE    :PyCharm
#@Email  :984@qq.com
"""
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('./ImageExample/cat.jpg', 0)
# hist=cv2.calcHist([img],[0],None,[256],[0,255])
# plt.hist(img.ravel(),256)
color = ('b', 'g', 'r')

for i, col in enumerate(color):
    histr = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(histr, color=col)
    plt.xlim([0, 256])
    plt.show()