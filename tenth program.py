import cv2
import numpy as np
# Load the image
image = cv2.imread(r'C:\Users\deren\OneDrive\Desktop\nature.jpeg')


# Check if the image was loaded successfully
if image is None:
    print("Error: Could not load the image.")
else:
    height, width = image.shape[:2]

    # Define the translation values for x and y (shift by 100 pixels along x and 50 pixels along y)
    tx, ty = 100, 50

    # Create the translation matrix
    M = np.float32([[1, 0, tx], [0, 1, ty]])

    # Apply the translation using warpAffine
    translated_image = cv2.warpAffine(image, M, (width, height))

    # Display the original and translated images
    cv2.imshow("Original Image", image)
    cv2.imshow("Translated Image", translated_image)

    # Wait for a key press and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
