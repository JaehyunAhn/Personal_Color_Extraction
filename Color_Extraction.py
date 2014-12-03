# -*- coding: utf-8 -*-
"""
    Sogang University Datamining Laboratory
    title: Personal color Extratcion
    author: sogo
"""
# Personal Color Extraction
import cv2
import numpy as np
from collections import Counter
from find_suitable_color import *

# read image
imgName = 'YH5_face.jpg'
targetImage = cv2.imread('./Test_Images/'+imgName, cv2.CV_LOAD_IMAGE_COLOR)
skinCandidates = []
# found color range and count it from skin color range
for x in range(45):
    for y in range(40):
        skinColor = color_detector(targetImage[35+x][95+y])
        if skinColor is not -1:
            skinCandidates.append(skinColor)
        skinColor = color_detector(targetImage[130+x][95+y])
        if skinColor is not -1:
            skinCandidates.append(skinColor)

# found a mean color
a = Counter(skinCandidates).most_common(8)
# print out Weather
find_suitable_weather(a)
# const: 보정을 위한 추가 값
const = 0
color1 = (skinMap[a[0][0]][2]+const, skinMap[a[0][0]][1]+const, skinMap[a[0][0]][0]+const)
color2 = (skinMap[a[1][0]][2]+const, skinMap[a[1][0]][1]+const, skinMap[a[1][0]][0]+const)
color3 = (skinMap[a[2][0]][2]+const, skinMap[a[2][0]][1]+const, skinMap[a[2][0]][0]+const)
color4 = (skinMap[a[3][0]][2]+const, skinMap[a[3][0]][1]+const, skinMap[a[3][0]][0]+const)
colorWinodw = np.zeros((200, 200, 3), np.uint8)
cv2.rectangle(colorWinodw, (0, 0), (99, 99), color1, -1)
cv2.rectangle(colorWinodw, (100, 0), (199, 99), color2, -1)
cv2.rectangle(colorWinodw, (0, 100), (99, 199), color3, -1)
cv2.rectangle(colorWinodw, (100, 100), (199, 199), color4, -1)
cv2.imshow("Image", targetImage)
cv2.imshow("Color", colorWinodw)
cv2.waitKey(0)
cv2.imwrite(imgName, colorWinodw)