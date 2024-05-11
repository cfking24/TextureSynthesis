import os

import matplotlib.pyplot as plt

# Function to get the images from a directory
def get_images_from_directory(directory):
    images = []
    for filename in os.listdir(directory):
        if filename.endswith(".png"):
            images.append(os.path.join(directory, filename))
    images.sort(key=lambda x: int(os.path.splitext(os.path.basename(x))[0].split("_")[0]))
    return images

# Get images 1-6 from the "Images" directory
images = get_images_from_directory("Synthesized Images Small\\kernel11")

# Create the figure with original images and synthesized versions
fig, axs = plt.subplots(3, 4)

# Plot the images in the images list
for i, image_path in enumerate(images):
    img = plt.imread(image_path)
    axs[i // 4, i % 4].imshow(img)
    axs[i // 4, i % 4].axis('off')

# Adjust spacing between subplots
plt.tight_layout()

# Show the figure
plt.show()
