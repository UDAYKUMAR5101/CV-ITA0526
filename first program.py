import cv2

# Load the image
image = cv2.imread(r'C:\Users\deren\OneDrive\Desktop\nature.jpeg')

# Check if the image was loaded successfully
if image is None:
    print("Error: Could not load the image.")
else:
    # Convert the image to grayscale
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Display the original and grayscale images
    cv2.imshow("Original Image", image)
    cv2.imshow("Grayscale Image", grayscale_image)

    # Wait until a key is pressed
    cv2.waitKey(0)

    # Close all OpenCV windows
    cv2.destroyAllWindows()
