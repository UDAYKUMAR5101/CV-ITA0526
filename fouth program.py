import cv2

# Load the image
image = cv2.imread(r'C:\Users\deren\OneDrive\Desktop\nature.jpeg',cv2.IMREAD_GRAYSCALE)

# Check if the image was loaded successfully
if image is None:
    print("Error: Could not load the image.")
else:
    # Apply histogram equalization
    equalized_image = cv2.equalizeHist(image)

    # Display the original and equalized images
    cv2.imshow("Original Grayscale Image", image)
    cv2.imshow("Histogram Equalized Image", equalized_image)

    # Wait for a key press and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
