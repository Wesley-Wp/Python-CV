# -*- coding:utf-8 -*-
"""
# @Time  :2020/8/2 15:04
#@Author :Wesley
#@File   :模板匹配.py
#@IDE    :PyCharm
#@Email  :984@qq.com
"""
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('./ImageExample/lena.jpg', 0)
img2 = img.copy()
templeate = cv2.imread('./ImageExample/face.png', 0)
h, w = templeate.shape[:2]
method = ['cv2.TM_SQDIFF', 'cv2.TM_CCORR', 'cv2.TM_CCOEFF', 'cv2.TM_SQDIFF_NORMED', 'cv2.TM_CCORR_NORMED',
          'cv2.TM_CCOEFF_NORMED']


for meth in method:

    # 匹配方法的真值
    method = eval(meth)
    print(method)
    res = cv2.matchTemplate(img, templeate, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # 如果是平方差匹配TM_SQDIFF或归一化平方差匹配TM_SQDIFF_NORMED，取最小值
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    # 画矩形
    cv2.rectangle(img2, top_left, bottom_right, 255, 2)

    plt.subplot(121), plt.imshow(res, cmap='gray')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(img2, cmap='gray')
    plt.suptitle(meth)
    plt.show()
