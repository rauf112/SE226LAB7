import cv2


# Read the image
image = cv2.imread('C:/Users/rauf1/Desktop/ce/Gradient_color_wheel.png')
blue_channel, green_channel, red_channel = cv2.split(image)
cv2.imshow('Blue Channel', blue_channel)
cv2.imshow('Green Channel', green_channel)
cv2.imshow('Red Channel', red_channel)

cv2.waitKey(0)
cv2.destroyAllWindows()
green_channel[:] = 0
modified_image = cv2.merge((blue_channel, green_channel, red_channel))
cv2.imshow('Modified Image', modified_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

