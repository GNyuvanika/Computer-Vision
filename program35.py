import cv2
import numpy as np
kernel=np.ones((5,5),np.uint8)
print(kernel)
path=r"C:\Computer Vision\test image.jpg"
img=cv2.imread(path)
Sblack=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
morph=cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)
cv2.imshow("Original image",img)
cv2.imshow("Morph",morph)


                                                                                                                                                                                                   
