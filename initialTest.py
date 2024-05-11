import cv2
import os
import cv2
import os
from synthesis import synthesize_texture

# Example usage
if __name__ == '__main__':
    # Load your input images from the Images directory
    input_images_dir = 'C:\\Users\\Conor King\\Documents\\School\\EEC 289A\\HW 2 - 2nd Attempt\\TextureSynthesis\\Images'
    input_image_paths = [os.path.join(input_images_dir, filename) for filename in os.listdir(input_images_dir)]

    # Set kernel sizes and runtime
    kernel_sizes = [11]
    runtime_minutes = 25

    for input_image_path in input_image_paths:
        # Load input image
        sample = cv2.imread(input_image_path)

        # Decrease the resolution of the image
        new_width = 64
        new_height = 64
        sample = cv2.resize(sample, (new_width, new_height), interpolation=cv2.INTER_AREA)

        # Display the input image
        # cv2.imshow("Input Image", sample)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        # Get the filename without extension
        filename = os.path.splitext(os.path.basename(input_image_path))[0]

        for kernel_size in kernel_sizes:
            # Set runtime in seconds
            runtime = runtime_minutes * 60

            # Perform texture synthesis
            synthesized_texture = synthesize_texture(sample, (1000, 1000), kernel_size, visualize=False, runtime=runtime)

            # Create the output directory if it doesn't exist
            output_dir = os.path.join('C:\\Users\\Conor King\\Documents\\School\\EEC 289A\\HW 2 - 2nd Attempt\\TextureSynthesis\\Synthesized Images Small', f'kernel{kernel_size}')
            os.makedirs(output_dir, exist_ok=True)

            # Generate a unique name for the output image
            output_image_name = f'{filename}_synthesized_image_{kernel_size}.jpg'

            # Save the synthesized texture
            output_image_path = os.path.join(output_dir, output_image_name)
            cv2.imwrite(output_image_path, synthesized_texture)
            print(f"Synthesized texture saved to {output_image_path}")