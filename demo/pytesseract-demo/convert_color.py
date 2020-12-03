# 灰度化处理测试

import cv2

img = cv2.imread("tesseract-ocr-3.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("tesseract-ocr-3.gray.jpg", gray_img)
cv2.imshow("Image", img)
cv2.imshow("Gray", gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()