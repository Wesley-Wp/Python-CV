# -*- coding:utf-8 -*-
"""
# @Time  :2020/8/2 15:04
#@Author :Wesley
#@File   :直方图均衡化.py
#@IDE    :PyCharm
#@Email  :984@qq.com
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('./ImageExample/clahe.jpg', 0)

plt.hist(img.ravel(), 256)
eqv = cv2.equalizeHist(img)
plt.hist(eqv.ravel(), 256)
cla = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
res_cla = cla.apply(img)
res = np.hstack((img, eqv, res_cla))
# plt.show()
cv2.imshow('123', res)
cv2.waitKey()
