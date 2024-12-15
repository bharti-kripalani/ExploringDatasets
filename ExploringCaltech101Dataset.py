import os
import matplotlib.pyplot as plt
from PIL import Image
import random

# Path to the Caltech 101 dataset (replace with your local path)
dataset_path = "*/Desktop/ParentDir/"

# List all the class names (folders in the dataset)
class_names = os.listdir(dataset_path)

# Select a random class (category)
#selected_class = random.choice(class_names)

#For testing purpose I just have created one subfolder so I am selecting that directly
selected_class = class_names[0]  # Directly select the only class
class_path = os.path.join(dataset_path, selected_class)

#In case you have multiple subfolders of images then use this piece of code
#selected_class = random.choice(class_names)
#class_path = os.path.join(dataset_path, selected_class)


# Get a list of image files in the selected class folder
image_files = os.listdir(class_path)
image_files = [f for f in image_files if f.endswith('.jpg')]  # Filtering only .jpg files

# Select a random image file from the selected class
selected_image_file = random.choice(image_files)
image_path = os.path.join(class_path, selected_image_file)

# Open and display the image using PIL
image = Image.open(image_path)

# Display the image using matplotlib
plt.imshow(image)
plt.title(f"Class: {selected_class}, Image: {selected_image_file}")
plt.axis('off')  # Hide axes
plt.show()
