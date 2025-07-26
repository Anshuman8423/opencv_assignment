import cv2

img = cv2.imread('sample.jpg')
cv2.rectangle(img, (50, 50), (200, 200), (0, 255, 0), 3)
cv2.circle(img, (300, 300), 50, (255, 0, 0), 3)
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 0, 255), 3)

cv2.imshow('Shapes', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
