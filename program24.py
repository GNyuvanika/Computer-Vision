import cv2
import numpy as np

image = cv2.imread(r'C:\Computer Vision\test image.jpg', cv2.IMREAD_GRAYSCALE)

k = 1.5  
size = 3 

kernel = np.ones((size, size), np.float32) * -1
kernel[size // 2, size // 2] = size * size
high_boost_mask = np.zeros_like(kernel)
high_boost_mask = kernel + high_boost_mask

high_pass_image = cv2.filter2D(image, -1, high_boost_mask)

sharpened_image = cv2.addWeighted(image, 1, high_pass_image, k, 0)

cv2.imshow('Original Image', image)
cv2.imshow('Sharpened Image', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
