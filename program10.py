import cv2 
path = r'C:\Web Dev\CSS Tutorial\Coffee\coffee-cup.png'
src = cv2.imread(path) 
window_name = 'Image' 
image = cv2.rotate(src, cv2.ROTATE_90_COUNTERCLOCKWISE) 
# Displaying the image 
cv2.imshow(window_name, image) 
cv2.waitKey(0) 
