# import cv2
# import numpy as np

# # Load the image
# image = cv2.imread('sugarcane_image.jpg')

# # Convert to RGB
# image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# # Define coordinates manually (as an example)
# nodes = [(100, 150), (200, 250)]  # Replace with actual coordinates

# # Extract color and convert to hex
# for (x, y) in nodes:
#     color = image_rgb[y, x]
#     hex_color = "#{:02x}{:02x}{:02x}".format(color[0], color[1], color[2])
#     print(f"Color at ({x},{y}): {hex_color}")

# import cv2
# import numpy as np

# # Load the image
# image = cv2.imread('sugarcane_image.jpg')

# # Convert to RGB
# image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# # Display image and get coordinates manually
# # Alternatively, use image processing to find nodes
# nodes = [(x1, y1), (x2, y2), ...]

# # Extract color and convert to hex
# for (x, y) in nodes:
#     color = image_rgb[y, x]
#     hex_color = "#{:02x}{:02x}{:02x}".format(color[0], color[1], color[2])
#     print(f"Color at ({x},{y}): {hex_color}")


import cv2
import numpy as np

# Function to extract color and convert to hex
def extract_color(image_path, nodes):
    # Load the image
    image = cv2.imread(image_path)
    
    # Check if the image is loaded correctly
    if image is None:
        print("Error: Image not found.")
        return
    
    # Convert to RGB (OpenCV loads images in BGR format)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Iterate through the list of coordinates (nodes)
    for (x, y) in nodes:
        # Ensure the coordinates are within the image dimensions
        if 0 <= x < image_rgb.shape[1] and 0 <= y < image_rgb.shape[0]:
            # Extract the color at (x, y)
            color = image_rgb[y, x]
            # Convert the color to hex
            hex_color = "#{:02x}{:02x}{:02x}".format(color[0], color[1], color[2])
            print(f"Color at ({x},{y}): {hex_color}")
        else:
            print(f"Warning: Coordinates ({x},{y}) are out of bounds.")

# Define the path to your image
image_path = 'sugarcane_image.jpg'

# Define the coordinates
nodes = [(100, 150), (200, 250), (300, 350)]  

# Call the function to extract and print the color values
extract_color(image_path, nodes)
