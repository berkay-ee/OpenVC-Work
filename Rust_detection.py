import cv2
import numpy as np


#Reading from the image file
img = cv2.imread("rust_surface.jpg") 

#Convert the gray scale
gray_convert  = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

orange = (0, 165, 255)  # BGR orange

rows, cols = gray_convert.shape


# Thershold the image
#if greher than thershold make a array point is a black is less than theshold make a array point white at the gray scale
for i in range(rows):
    for j in range(cols):
        if gray_convert[i,j] < 75:
          gray_convert[i,j] = 0
        else:
            gray_convert[i,j] = 255


# point the rust locaiton at the RGB image
for i in range(rows):
    for j in range(cols):
        if gray_convert[i,j] == 0:
          cv2.circle(img, (j,i),1,orange,-1)
        


# Show the image in a window
cv2.imshow("Rust detected picture", img)

cv2.imshow("Gray scale", gray_convert)

# Wait until a key is pressed
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()

