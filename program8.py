import cv2 
import numpy as np 
kernel = np.ones((5,5),np.uint8) 
img = cv2.imread(r'C:\Computer Vision\test_image.jpeg')
img = cv2.resize(img,(600,400)) 
cv2.imshow("image",img) 
cv2.waitKey(0)
