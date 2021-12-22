import cv2


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("CameraOpenfailed")
    exit()


ret,frame= cap.read()
cv2.imwrite('output.jpg', frame)

# cv2.waitkey(0)


cap.release()
cv2.destroyAllWindows
