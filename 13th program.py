import cv2

# Global variable to store clicked points
coordinates = []

# Mouse callback function to capture click events and display coordinates
def mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:  # Left button click
        coordinates.append((x, y))  # Store the coordinates
        print(f"Clicked at: ({x}, {y})")
        # Display the coordinates on the image
        cv2.putText(image, f"({x}, {y})", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
        cv2.circle(image, (x, y), 5, (0, 255, 0), -1)  # Draw a small circle at the click point
        cv2.imshow("Image with Coordinates", image)

# Load the image
image = cv2.imread(r'C:\Users\deren\OneDrive\Desktop\nature.jpeg')

# Check if the image was loaded successfully
if image is None:
    print("Error: Could not load the image.")
else:
    # Display the image first
    cv2.imshow("Image with Coordinates", image)

    # Set the mouse callback function after imshow
    cv2.setMouseCallback("Image with Coordinates", mouse_click)

    # Wait for user interaction (mouse click)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
