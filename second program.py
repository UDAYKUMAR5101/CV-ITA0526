import cv2

# Load the image
image = cv2.imread(r'C:\Users\deren\OneDrive\Desktop\nature.jpeg')

# Check if the image was loaded successfully
if image is None:
    print("Error: Could not load the image.")
else:
    # Apply Gaussian blur
    kernel_size = (5, 5)
    blurred_image = cv2.GaussianBlur(image, kernel_size, 0)

    # Display the original and blurred images
    cv2.imshow("Original Image", image)
    cv2.imshow("Gaussian Blurred Image", blurred_image)

    # Wait for a key press and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
