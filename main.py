import cv2

#parameters
source = "train.jpeg"
destination = "newImage.jpeg"
scale_percent = 50

#to open the image
src = cv2.imread(source, cv2.IMREAD_UNCHANGED)
# cv2.imshow("title", src)

#to resize the image
new_width = int(src.shape[1] * scale_percent /100)
new_height = int(src.shape[0] * scale_percent /100)
output = cv2.resize(src, (new_width,new_height))
#set a new image to the destination
cv2.imwrite(destination, output)
cv2.waitKey(0)

