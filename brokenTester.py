from synthesis_broken import synthesize_texture
import cv2
import os

# Example usage
if __name__ == '__main__':
    # Load your input image (replace with your actual image path)
    input_image_path = 'C:\\Users\\Conor King\\Documents\\School\\EEC 289A\\HW 2 - 2nd Attempt\\TextureSynthesis\\Images\\1.png'
    
    sample = cv2.imread(input_image_path)

    # Decrease the resolution of the image
    new_width = 64  # Replace with your desired width
    new_height = 64  # Replace with your desired height
    sample = cv2.resize(sample, (new_width, new_height), interpolation=cv2.INTER_AREA)

    # Display the image
    cv2.imshow("Input Image", sample)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Set parameters (window size, kernel size, etc.)
    window_height, window_width = 50, 50
    kernel_size = 11

    # # Assuming 'original_sample' is loaded correctly
    # # Check if the image has an alpha channel (RGBA format)
    # if sample.shape[2] == 4:
    #     # Remove the alpha channel
    #     original_sample = sample[:, :, :3]

    # # Convert to grayscale
    # greysample = cv2.cvtColor(sample, cv2.COLOR_BGR2GRAY)


    # Initialize texture synthesis
    # (sample, window, mask, padded_window,
    #     padded_mask, result_window) = initialize_texture_synthesis(sample, (window_height, window_width), kernel_size)

    visualize = True
    # Perform texture synthesis

    synthesized_texture = synthesize_texture(sample, (window_height, window_width), kernel_size, visualize=visualize)

    # Save the synthesized texture (replace with your desired output path)
    output_image_path = 'C:\\Users\\Conor King\\Documents\\School\\EEC 289A\\HW 2 - 2nd Attempt\\TextureSynthesis\\BrokenSynths\\bestN\\weighted\\best4.jpg'
    # Create the output folder if it doesn't exist
    os.makedirs(os.path.dirname(output_image_path), exist_ok=True)

    # Save the synthesized texture
    cv2.imwrite(output_image_path, synthesized_texture)
    print(f"Synthesized texture saved to {output_image_path}")