# -*- coding:utf-8 -*-
"""
# @Time  :2020/8/2 15:00
#@Author :Wesley
#@File   :图像阈值.py
#@IDE    :PyCharm
#@Email  :984@qq.com
"""

import cv2
import matplotlib.pyplot as plt

img = cv2.imread('cat.jpg', 0)

ret, dst1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret, dst2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
ret, dst3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
ret, dst4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
ret, dst5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

titles = ['Original', '2', '3', '4', '5', '6']
image = [img, dst1, dst2, dst3, dst4, dst5]
for i in range(6):
    plt.subplot(2, 3, i + 1), plt.imshow(image[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
