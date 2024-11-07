import cv2
import numpy as np
# Load the image
image = cv2.imread(r'C:\Users\deren\OneDrive\Desktop\nature.jpeg')


# Check if the image was loaded successfully
if image is None:
    print("Error: Could not load the image.")
else:
    # Convert the image to grayscale (if not already binary or grayscale)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Create a structuring element (a 5x5 square kernel)
    kernel = np.ones((5, 5), np.uint8)

    # Apply erosion to the image
    eroded_image = cv2.erode(gray_image, kernel, iterations=1)

    # Display the original and eroded images
    cv2.imshow("Original Image", gray_image)
    cv2.imshow("Eroded Image", eroded_image)

    # Wait for a key press and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
