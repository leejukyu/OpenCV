import cv2
import sys

print("Hello OpenCV", cv2.__version__)
img = cv2.imread('cat.bmp') # 파일을 불러와 img변수에 저장

if img is None: # 불러오기가 실패하면 에러메시지 출력하고 종료
    print('Image load failed!')
    sys.exit()

cv2.namedWindow('image', cv2.WINDOW_NORMAL) 
cv2.imshow('image', img) # image새창 만들고 이창에 img출력 후 키보드 입력까지 대기
# cv2.imwrite('catzz.png',img) # catzz 파일 만들기
# cv2.waitKey()
while True: # q가 들어가야 종료
    if cv2.waitKey() == ord('q'):
        break

cv2.destroyAllWindows() # 생성된 모든 창을 닫음