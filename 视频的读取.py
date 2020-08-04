# -*- coding:utf-8 -*-
"""
# @Time  :2020/8/2 14:58
#@Author :Wesley
#@File   :视频的读取.py
#@IDE    :PyCharm
#@Email  :984@qq.com
"""
import cv2
vc = cv2.VideoCapture('./ImageExample/test.mp4')

if vc.isOpened():
    open, frame = vc.read()
else:
    open = False

while open:
    ret, frame = vc.read()
    if frame is None:
        break
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('result', gray)
        if cv2.waitKey(50) & 0xFF == 27:
            break
vc.release()
cv2.destroyAllWindows()
