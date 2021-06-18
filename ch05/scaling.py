import sys
import numpy as np
import cv2
from matplotlib import pyplot as plt

src = cv2.imread('rose.bmp') # src.shape=(320, 480)

if src is None:
    print('Image load failed!')
    sys.exit()

dst1 = cv2.resize(src, (0, 0), fx=4, fy=4, interpolation=cv2.INTER_NEAREST)
dst2 = cv2.resize(src, (1920, 1280))  # cv2.INTER_LINEAR
dst3 = cv2.resize(src, (1920, 1280), interpolation=cv2.INTER_CUBIC)
dst4 = cv2.resize(src, (1920, 1280), interpolation=cv2.INTER_LANCZOS4)


# cv2.imshow('src', src)
# cv2.imshow('dst1', dst1[500:900, 400:800])
# cv2.imshow('dst2', dst2[500:900, 400:800])
# cv2.imshow('dst3', dst3[500:900, 400:800])
# cv2.imshow('dst4', dst4[500:900, 400:800])

# cv2.waitKey()
# cv2.destroyAllWindows()

# plt는 cv2와 달리 RGB로 받아와 RGB로 변환 필수
src = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
dst1 = cv2.cvtColor(dst1, cv2.COLOR_BGR2RGB)
dst2 = cv2.cvtColor(dst2, cv2.COLOR_BGR2RGB)
dst3 = cv2.cvtColor(dst3, cv2.COLOR_BGR2RGB)
dst4 = cv2.cvtColor(dst4, cv2.COLOR_BGR2RGB)

plt.subplot(221), plt.axis('off'), plt.imshow(dst1[500:900, 400:800], 'gray'), plt.title('dst1')
plt.subplot(222), plt.axis('off'), plt.imshow(dst2[500:900, 400:800], 'gray'), plt.title('dst2')
plt.subplot(223), plt.axis('off'), plt.imshow(dst3[500:900, 400:800], 'gray'), plt.title('dst3')
plt.subplot(224), plt.axis('off'), plt.imshow(dst4[500:900, 400:800], 'gray'), plt.title('dst4')
plt.show()