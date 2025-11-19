import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("failed to turn on the camera")
    exit()

# 建立姿態辨識物件
mpPose = mp.solutions.pose
pose = mpPose.Pose()

while True:
    sucess, imgBGR = cap.read()
    if not sucess:
        print("failed to capture img")
        break

    imgBGR = cv2.flip(imgBGR, 1) # 解決左右相反
    # 0 是上下翻轉，1 是左右翻轉，2 是上下且左右翻轉。
    
    imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB) # MediaPipe 需要 RGB 格式
    results = pose.process(imgRGB)
    if results.pose_landmarks:
        # 畫出骨架
        mpDraw.draw_landmarks(imgBGR, results.pose_landmarks, mpPose.POSE_CONNECTIONS)

    cv2.imshow("camera", imgBGR)
    if cv2.waitKey(10) in [ord('q'), ord('Q')]:
        break
    
cap.release()
cv2.destroyAllWindows()
