import cv2
import matplotlib.pyplot as plt
import numpy as np

# 1. Read the image
image_path = 'Lane_Detection/data/0000000000.png'
img = cv2.imread(image_path)


def canny_edge_detection(image, width, height, weak_th=None, strong_th=None):
    # Calculate gradients using Sobel
    gx = cv2.Sobel(np.float32(image), cv2.CV_64F, 1, 0, 3)
    gy = cv2.Sobel(np.float32(image), cv2.CV_64F, 0, 1, 3)
    mag, ang = cv2.cartToPolar(gx, gy, angleInDegrees=True)

    mag_max = np.max(mag)
    if weak_th is None:
        weak_th = mag_max * 0.1
    if strong_th is None: 
        strong_th = mag_max * 0.5

  
    for i_x in range(width):
        for i_y in range(height):
            grad_ang = ang[i_y, i_x]
            grad_ang = abs(grad_ang - 180) if abs(grad_ang) > 180 else abs(grad_ang)

            if grad_ang <= 22.5:
                neighb_1_x, neighb_1_y = i_x - 1, i_y
                neighb_2_x, neighb_2_y = i_x + 1, i_y
            elif grad_ang > 22.5 and grad_ang <= 67.5:
                neighb_1_x, neighb_1_y = i_x - 1, i_y - 1
                neighb_2_x, neighb_2_y = i_x + 1, i_y + 1
            elif grad_ang > 67.5 and grad_ang <= 112.5:
                neighb_1_x, neighb_1_y = i_x, i_y - 1
                neighb_2_x, neighb_2_y = i_x, i_y + 1
            elif grad_ang > 112.5 and grad_ang <= 157.5:
                neighb_1_x, neighb_1_y = i_x - 1, i_y + 1
                neighb_2_x, neighb_2_y = i_x + 1, i_y - 1
            else:
                neighb_1_x, neighb_1_y = i_x - 1, i_y
                neighb_2_x, neighb_2_y = i_x + 1, i_y

            if 0 <= neighb_1_x < width and 0 <= neighb_1_y < height:
                if mag[i_y, i_x] < mag[neighb_1_y, neighb_1_x]:
                    mag[i_y, i_x] = 0
                    continue

            if 0 <= neighb_2_x < width and 0 <= neighb_2_y < height:
                if mag[i_y, i_x] < mag[neighb_2_y, neighb_2_x]:
                    mag[i_y, i_x] = 0
                    continue   
    

    ids = np.zeros_like(image)
    
    for i_x in range(width):
        for i_y in range(height):
            grad_mag = mag[i_y, i_x]
            if grad_mag < weak_th:
                mag[i_y, i_x] = 0
            elif strong_th > grad_mag >= weak_th:
                ids[i_y, i_x] = 1
            else:
                ids[i_y, i_x] = 2
                
 
    mag_display = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    
    return mag_display



if img is None:
    print(f"Error: Could not read the image at {image_path}")
else:
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    canny_img = canny_edge_detection(img_gray, img_gray.shape[1], img_gray.shape[0])

    lines = cv2.HoughLinesP(canny_img, 1, np.pi/180, 50, minLineLength=15, maxLineGap=20
                            )
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

    
    cv2.imshow('OpenCV Window', img)

 
    cv2.waitKey(0) 

    
    cv2.destroyAllWindows()