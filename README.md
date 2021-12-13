# Computer vision
## 용어 정리
- Classification : 이미지 분류
- Localization : 이미지 안에서 하나의 object 찾기
- Object Detection : 하나의 이미지 안에 여러개의 object Bounding Box
  * Localization/Detection은 Bounding box regression(box 좌표값 예측)과 Classification 두개의 문제가 합쳐져 있음
- 영역 추정(Region Proposal) : 객체가 있을만한 곳을 추정, 바운딩 박스 전에
- Segmentation : Pixel단위로 객체 검출
- Annotation : 
- GT(Ground Truth) : 우리가 정한 정답
- SPP(Spatial pyramid Pooling) : Image classification에서 서로 다른 이미지의 크기를 고정된 크기로 변환하는 기법, conv와 dense layer를 유연하게 연결

## Object Detection
- 방식
  - 2_Stage Detector : 위치를 찾기, 분류를 순차적으로 ex) Faster RCNN
  - 1_Stage Detector : 한버에 위치를 찾고 분류를 해결 ex) YoLo
- Region Proposal
  - Sliding Window : 다양한 형태의 윈도우를 슬라이딩하며 존재 확인, 너무 많은 영역을 확인함 ex) Faster RCNN
  - Selective Search : 이접한 영역끼리 유사성을 측정해 큰 영역으로 통합 ex) RCNN, Fast RCNN
- mAP 성능지표 : 하나의 클래스 마다 AP(Recall을 증가시켜 나온 Precision 값의 평균)값을 계산하여 전체 클래스 갯수에 대한 평균
  - IoU(Intersection over Union) : 두 바운딩 박스가 겹치는 비율
  - NMS(Non Maximum Suppression) : 같은 클래스 끼리 IoU가 50% 이상일 때 낮은 confidence의 box를 제거
 
 ## OpenCV 사용시 주의할점
 - imread()를 이용한 이미지 로딩은 이미지 배열이 RGB에서 BGR로 바뀜, imread로 이미지를 제대로 보려면 RGB형태로 변환
 ```
  import cv2
  import matplotlib.pyplot as plt
  
  bgr_img_array = cv2.imread('파일명')
  rgb_img_array = cv2.cvtColor(bgr_img_array, cv2.COLOR_BGR2RGB)
  plt.imshow(rgb_img_array)
``` 
- imwrite()를 이용하여 저장하면 RGB형태로 변환되어 저장
```
 import cv2
 import matplotlib.pyplot as plt
 
 img_array = cv2.imread('파일명') # BGR
 cv2.imwrite('출력파일명', img_array) # RGB
```
## R-CNN(Regions with CNN)
- selective search(~2k), 이미지 크기는 동일해야함(227 X 227)
- FC Layer 이후 softmax 대신 SVM Classifier 적용
- Ground Truth로만 학습, Background도 학습
- 동시대의 다른 알고리즘에 비해 매우 높은 Detection 정확도
- 너무 느린 시간과 복잡한 아키텍처 및 학습 프로세스
