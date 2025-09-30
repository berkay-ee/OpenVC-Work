import cv2
import numpy as np


blank = np.zeros((500, 500, 3), dtype=np.uint8)


cv2.imshow("Empty Screen", blank)


cv2.waitKey(0)


cv2.destroyAllWindows()
