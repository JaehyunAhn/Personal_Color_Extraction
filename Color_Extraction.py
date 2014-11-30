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
targetImage = cv2.imread('./Test_Images/YH334_face.jpg')

skinCandidates = []
# found color range and count it from skin color range
for x in range(len(targetImage)):
    for y in range(len(targetImage[x])):
        skinColor = color_detector(targetImage[x][y])
        if skinColor is not -1:
            skinCandidates.append(skinColor)
# found a mean color
a = Counter(skinCandidates).most_common(4)
# print out BGR
color1 = (skinMap[a[0][0]][2], skinMap[a[0][0]][1], skinMap[a[0][0]][0])
color2 = (skinMap[a[1][0]][2], skinMap[a[1][0]][1], skinMap[a[1][0]][0])
color3 = (skinMap[a[2][0]][2], skinMap[a[2][0]][1], skinMap[a[2][0]][0])
color4 = (skinMap[a[3][0]][2], skinMap[a[3][0]][1], skinMap[a[3][0]][0])
colorWinodw = np.zeros((200, 200, 3), np.uint8)
cv2.rectangle(colorWinodw, (0, 0), (99, 99), color1, -1)
cv2.rectangle(colorWinodw, (100, 0), (199, 99), color2, -1)
cv2.rectangle(colorWinodw, (0, 100), (99, 199), color3, -1)
cv2.rectangle(colorWinodw, (100, 100), (199, 199), color4, -1)
cv2.imshow("Image", targetImage)
cv2.imshow("Color", colorWinodw)
cv2.waitKey(0)