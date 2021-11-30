# Computer vision
## 용어 정리
- Classification : 이미지 분류
- Localization : 이미지 안에서 하나의 object 찾기
- Object Detection : 하나의 이미지 안에 여러개의 object Bounding Box
  * Localization/Detection은 Bounding box regression(box 좌표값 예측)과 Classification 두개의 문제가 합쳐져 있음
- 영역 추정(Region Proposal) : 객체가 있을만한 곳을 추정, 바운딩 박스 전에
- Segmentation : Pixel단위로 객체 검출

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
