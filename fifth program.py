import cv2
import matplotlib.pyplot as plt
# Load the image
image = cv2.imread(r'C:\Users\deren\OneDrive\Desktop\nature.jpeg')


# Check if the image was loaded successfully
if image is None:
    print("Error: Could not load the image.")
else:
    # Split the image into B, G, R channels
    channels = cv2.split(image)
    colors = ('b', 'g', 'r')
    channel_names = ('Blue', 'Green', 'Red')

    # Plot the histogram for each channel
    plt.figure()
    plt.title("Color Histogram")
    plt.xlabel("Intensity Value")
    plt.ylabel("Pixel Count")

    for (channel, color, name) in zip(channels, colors, channel_names):
        histogram = cv2.calcHist([channel], [0], None, [256], [0, 256])
        plt.plot(histogram, color=color, label=name)
        plt.xlim([0, 256])

    # Add a legend to indicate each channel
    plt.legend()
    plt.show()
