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
images_1_6 = get_images_from_directory("Images")[:6]

# Get images 7-12 from the "Images" directory
images_7_12 = get_images_from_directory("Images")[6:]

# Concatenate the lists
all_images = images_1_6 + images_7_12

# Get images from the "Synthesized Images/Slow" directory that end in "_kernel11"
synthesized_images_kernel11 = []
synthesized_images_kernel31 = []
synthesized_images_kernel51 = []

for i in range(1, 13):
    directory = f"Synthesized Images/Fast/{i}"
    image_path_kernel11 = os.path.join(directory, "synthesized_image_kernel11.jpg")
    image_path_kernel31 = os.path.join(directory, "synthesized_image_kernel31.jpg")
    image_path_kernel51 = os.path.join(directory, "synthesized_image_kernel51.jpg")
    
    synthesized_images_kernel11.append(image_path_kernel11)
    synthesized_images_kernel31.append(image_path_kernel31)
    synthesized_images_kernel51.append(image_path_kernel51)

# Create the figure with original images and synthesized versions
fig, axs = plt.subplots(3, 4)

# Plot original images 1, 5, and 9 in the top row
for i, ax in enumerate(axs[:, 0]):
    img = plt.imread(all_images[i * 4])
    ax.imshow(img)
    ax.axis("off")

# Plot synthesized versions of each kernel size below each original image
for i in range(3):
    img11 = plt.imread(synthesized_images_kernel11[i * 4])
    img31 = plt.imread(synthesized_images_kernel31[i * 4])
    img51 = plt.imread(synthesized_images_kernel51[i * 4])
    
    axs[i, 1].imshow(img11)
    axs[i, 2].imshow(img31)
    axs[i, 3].imshow(img51)
    # Turn off axes for all subplots
    for ax in axs.flatten():
        ax.axis("off")

# Adjust spacing between subplots
plt.tight_layout()

# Show the figure
plt.show()
