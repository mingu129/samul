import cv2


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("CameraOpenfailed")
    exit()


# fourcc = cv2.VideoWriter_fourcc(*'DIVX')

# out = cv2.VideoWriter('output.avi', fourcc, 30, (640,480))


while True:
    ret,frame= cap.read()
    if not ret:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edge1 = cv2.Canny(frame, 50, 100)
    cv2.imshow('frame1', frame)
    cv2.imshow('frame2', edge1)
    cv2.imshow('frame3', gray)
    # out.write(frame)

    if cv2.waitKey(10) == 13:   
        break


# cv2.imwrite('output.jpg', frame)

# cv2.waitkey(0)

# out.release()
cap.release()
cv2.destroyAllWindows
