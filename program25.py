import cv2
import numpy as np

# Load the image
image = cv2.imread(r'C:\Computer Vision\blur img.jpeg', cv2.IMREAD_GRAYSCALE)

# Compute gradients using Sobel filters
gradient_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
gradient_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

# Compute magnitude of gradient
magnitude = np.sqrt(gradient_x ** 2 + gradient_y ** 2)

# Normalize magnitude to the range [0, 255]
magnitude_normalized = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

# Combine gradient magnitude with original image
sharpened_image = cv2.addWeighted(image, 1.5, magnitude_normalized, -0.5, 0)

# Display the original image and sharpened image
cv2.imshow('Original Image', image)
cv2.imshow('Sharpened Image', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
