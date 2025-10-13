import cv2
import numpy as np    
import matplotlib.pyplot as plt


#Reading from the image file
img = cv2.imread("Rust detection\\rust_surface.jpg") 

#Convert the gray scale
gray_convert  = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
rows, cols = gray_convert.shape


#Image netagive (Revese intensity transform)
gray_convert = 255 - gray_convert


# Heavy rust is a red
# Yellow is a light rust
# Ornage is a medium rust
for i in range(rows):
    for j in range(cols):
        pixel_val = gray_convert[i, j]
       
        if 100 <= pixel_val < 150:
            img[i, j] = [0, 255, 255]  # yellow
     
        elif 150 <= pixel_val < 200:
            img[i, j] = [0, 165, 255]  # orange
 
        elif pixel_val >= 200:
            img[i, j] = [0, 0, 255]  # red

# Heatmap the image
heatmap = cv2.applyColorMap(gray_convert, cv2.COLORMAP_TURBO)

# Thershold the image
#if greher than thershold make a array point is a black is less than theshold make a array point white at the gray scale
"""""
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
        
"""""

# Show the image in a window
cv2.imshow("Rust detected picture", heatmap)

cv2.imshow("Gray scale", img)

#image save
cv2.imwrite("rust_detected.jpg", img)
cv2.imwrite("thresholded_gray.jpg", gray_convert)



# Wait until a key is pressed
cv2.waitKey(0)
