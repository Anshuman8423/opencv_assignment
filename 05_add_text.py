import cv2

img = cv2.imread('sample.jpg')
cv2.putText(img, 'OpenCV Demo', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

cv2.imshow('Text on Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
