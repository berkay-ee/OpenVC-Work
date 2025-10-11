import cv2
import numpy as np    
import matplotlib.pyplot as plt


#Reading from the image file
img = cv2.imread("rust_surface.jpg") 

#Convert the gray scale
gray_convert  = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
rows, cols = gray_convert.shape


#Image netagive (Revese intensity transform)
gray_convert = 255 - gray_convert

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
        

for i in range(rows):
    for j in range(cols):
        
"""""
heatmap_rgb = cv2.cvtColor(heatmap, cv2.COLOR_BGR2RGB)


# Color bar to rust surface intensity
plt.figure(figsize=(10, 6))
plt.imshow(heatmap_rgb)
plt.title("Rust Detection Heatmap")

# Colorbar 
plt.colorbar(label='Rust  intensity')

plt.show()

#image save
cv2.imwrite("rust_detected.jpg", img)
cv2.imwrite("thresholded_gray.jpg", gray_convert)



# Wait until a key is pressed
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()




