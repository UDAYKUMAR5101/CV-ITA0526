import cv2

# Load the image
image = cv2.imread(r'C:\Users\deren\OneDrive\Desktop\nature.jpeg')


# Check if the image was loaded successfully
if image is None:
    print("Error: Could not load the image.")
else:
    # Define the coordinates of the region of interest (ROI)
    # Example: Modify a 100x100 square region starting from (50, 50)
    start_x, start_y = 50, 50
    end_x, end_y = start_x + 100, start_y + 100

    # Modify the region by setting it to a specific color (e.g., blue color)
    image[start_y:end_y, start_x:end_x] = [255, 0, 0]  # BGR format for blue

    # Display the original and modified images
    cv2.imshow("Modified Image", image)

    # Wait for a key press and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
