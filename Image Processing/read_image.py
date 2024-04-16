import cv2 

img = cv2.imread("butterfly.jpg")

cv2.imshow("Display Image ", img)
print(img)

gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
cv2.imshow("Grayscale Image", gray_img)
print(gray_img)

cv2.waitKey(0)