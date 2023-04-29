import os
import cv2
import random
import string
import numpy as np

# Function to generate a random string
def generate_random_string(length):
    return ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(length))

# Directory containing jpg images
directory = "/images"

# Loop through all files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".jpg"):
        # Read the image
        img_path = os.path.join(directory, filename)
        img = cv2.imread(img_path)

        # Get image dimensions
        height, width, _ = img.shape

        # Calculate number of cells in the image
        num_cells_horizontal = int((width - 6) / 32)
        num_cells_vertical = int((height - 6) / 32)

        # Loop through all cells in the image
        for i in range(num_cells_vertical):
            for j in range(num_cells_horizontal):
                # Calculate cell coordinates
                x = j * 33 + 1
                y = i * 33 + 1
                if x % 33 == 0:
                    x = x + 1
                if y % 33 == 0:
                    y = y + 1
                
                #print(" Cropping from ", x, " and ", y)
                # Crop the cell from the image
                cell = img[y:y+32, x:x+32]

                # Generate a random filename
                random_filename = generate_random_string(10) + ".jpg"

                # Save the cell as a separate image
                cell_path = os.path.join(directory, random_filename)
                cv2.imwrite(cell_path, cell)

        os.remove(img_path)
        #print(f"Cells extracted from '{filename}': {num_cells_horizontal} x {num_cells_vertical}")