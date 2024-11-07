import cv2

# Load the image
image = cv2.imread(r'C:\Users\deren\OneDrive\Desktop\nature.jpeg')

# Check if the image was loaded successfully
if image is None:
    print("Error: Could not load the image.")
else:
    # Rotate the image 90 degrees clockwise
    rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

    # Display the original and rotated images
    cv2.imshow("Original Image", image)
    cv2.imshow("90-Degree Clockwise Rotated Image", rotated_image)

    # Wait for a key press and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
