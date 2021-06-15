import sys
import numpy as np
import cv2


src = cv2.imread('candies.png')
#src = cv2.imread('candies2.png')

if src is None:
    print('Image load failed!')
    sys.exit()

src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

dst1 = cv2.inRange(src, (0, 128, 0), (100, 255, 100)) 
# 튜플형식으로 0<=R<=100, 128<=G<=255, 0<=B<=100
dst2 = cv2.inRange(src_hsv, (50, 150, 0), (80, 255, 255))
# 튜플형식으로 50<=H<=150, 150<=S<=255, 0<=V<=225

cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()

cv2.destroyAllWindows()
