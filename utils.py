# -*- coding: utf-8 -*-
# @Time : 2022/10/21 10:18
# @Author : Xu Bai
# @Email : 1373953675@qq.com
# @File : utils.py.py
# @Desc : ...
import cv2


def cv_show(name, img):
    cv2.imshow(name, img)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
