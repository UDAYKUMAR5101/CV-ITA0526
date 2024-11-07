import cv2

# Load the image
image = cv2.imread(r'C:\Users\deren\OneDrive\Desktop\nature.jpeg')


# Check if the image was loaded successfully
if image is None:
    print("Error: Could not load the image.")
else:
    # Apply the averaging filter (smoothing)
    # (5x5 kernel is used here for averaging)
    smoothed_image = cv2.blur(image, (5, 5))

    # Display the original and smoothed images
    cv2.imshow("Original Image", image)
    cv2.imshow("Smoothed Image", smoothed_image)

    # Wait for a key press and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
