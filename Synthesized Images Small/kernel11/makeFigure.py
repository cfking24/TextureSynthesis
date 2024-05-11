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

# Get images from the "Synthesized Images/Slow" directory that end in "_kernel11"
synthesized_images = []
for i in range(1, 13):
    directory = f"Synthesized Images\\Slow\\{i}_kernel11"
    image_path = os.path.join(directory, "synthesized_image.jpg")
    synthesized_images.append(image_path)

# Create the first figure with images 1-6
fig1, axs1 = plt.subplots(2, 6)
for i, ax in enumerate(axs1[0]):
    img = plt.imread(images_1_6[i])
    ax.imshow(img)
    ax.axis("off")
for i, ax in enumerate(axs1[1]):
    img = plt.imread(synthesized_images[i])
    ax.imshow(img)
    ax.axis("off")
plt.tight_layout()

# Create the second figure with images 7-12 and synthesized images
fig2, axs2 = plt.subplots(2, 6)
for i, ax in enumerate(axs2[0]):
    img = plt.imread(images_7_12[i])
    ax.imshow(img)
    ax.axis("off")
    #ax.set_aspect('equal')  # Set aspect ratio to equal for consistent scaling
for i, ax in enumerate(axs2[1]):
    img = plt.imread(synthesized_images[i + 6])
    ax.imshow(img)
    ax.axis("off")
    ax.set_aspect('equal')  # Set aspect ratio to equal for consistent scaling
plt.tight_layout()

# Show the figures
plt.show()