import cv2 # 匯入 OpenCV 套件

cap = cv2.VideoCapture(0) # 開啟攝影機
if not cap.isOpened():
    print("Failed to turn on the camera. Please check WebCam.")
    exit()

while True:
    success, imgBGR = cap.read() # cap.read() 回傳的影像是 BGR 格式
    if success:
        cv2.imshow("camera", imgBGR) # 左右相反
    else:
        print("capture failed!")
        break

    if cv2.waitKey(1) == ord('q'):
        break

# 釋放資源
cap.release()
cv2.destroyAllWindows()
