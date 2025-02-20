"""
测试摄像头是否可用的代码
"""

import cv2

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("无法打开摄像头")
    exit()
while True:
    ret, frame = cap.read()

    if not ret:
        print("无法接收帧 (流结束？)")
        break

    cv2.imshow("摄像头视频", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
