import cv2
import numpy as np

# Create a blank 300x300 black image
image = np.zeros((300, 300, 3), dtype=np.uint8)

# Create a window named 'BGR Color Palette'
cv2.namedWindow("BGR Color Palette")

# Trackbar callback function (not used but required by createTrackbar)
def nothing(x):
    pass

# Create trackbars for Blue, Green, and Red components
cv2.createTrackbar("Blue", "BGR Color Palette", 0, 255, nothing)
cv2.createTrackbar("Green", "BGR Color Palette", 0, 255, nothing)
cv2.createTrackbar("Red", "BGR Color Palette", 0, 255, nothing)

while True:
    # Get the current positions of the trackbars
    blue = cv2.getTrackbarPos("Blue", "BGR Color Palette")
    green = cv2.getTrackbarPos("Green", "BGR Color Palette")
    red = cv2.getTrackbarPos("Red", "BGR Color Palette")
    
    # Set the image color based on trackbar positions
    image[:] = [blue, green, red]
    
    # Display the image
    cv2.imshow("BGR Color Palette", image)
    
    # Exit the loop when the user presses the "Esc" key (ASCII 27)
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Destroy all windows
cv2.destroyAllWindows()
