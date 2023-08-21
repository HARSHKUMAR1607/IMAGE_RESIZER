import cv2

source = "m2.png"
destination = "new image.jpeg"
scale_percent = 50

src =  cv2.imread("m2.png", cv2.IMREAD_UNCHANGED)

scale_percent = 50


width = int (src. shape[1] * scale_percent / 100)
height = int(src.shape[0] * scale_percent / 100)

dsize = (width, height)

output = cv2.resize(src, dsize)

cv2.imwrite('D:/cv2-resize-image-50.png' ,output)
cv2.waitKey (0)