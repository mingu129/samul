import cv2
img = cv2.imread('mcr.jpg')

img2 = cv2.resize(img, (600, 400))

gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)


cv2.imshow('MCR', img2)
cv2.imshow('MCR_GRAY', gray)

while True:
    if cv2.waitKey() == 13:
        break

cv2.imwrite('BTS_GRAY.jpg', gray)



# cv2.waitKey(0)

cv2.destroyAllWindows()