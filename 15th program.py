import cv2

# Load the image
image = cv2.imread(r'C:\Users\deren\OneDrive\Desktop\nature.jpeg')

# Check if the image was loaded successfully
if image is None:
    print("Error: Could not load the image.")
else:
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply binary thresholding
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Loop through each contour
    for i, contour in enumerate(contours):
        print(f"Contour #{i+1} coordinates:")
        for point in contour:
            x, y = point[0]  # Extract x, y coordinates
            print(f"({x}, {y})")
        
        # Optionally, draw each contour on the original image
        cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)

    # Display the image with contours drawn
    cv2.imshow("Contours", image)

    # Wait for user interaction and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
