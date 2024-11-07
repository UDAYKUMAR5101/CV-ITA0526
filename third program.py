import cv2

# Load the image
image = cv2.imread(r'C:\Users\deren\OneDrive\Desktop\nature.jpeg')
if image is None:
    print("Error: Could not load the image.")
else:
    # Resize the image to larger dimensions (2x)
    larger_image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

    # Resize the image to smaller dimensions (0.5x)
    smaller_image = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

    # Display the original, larger, and smaller images
    cv2.imshow("Original Image", image)
    cv2.imshow("Larger Image", larger_image)
    cv2.imshow("Smaller Image", smaller_image)

    # Wait for a key press and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
