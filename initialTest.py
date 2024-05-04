from synthesis import synthesize_texture, initialize_texture_synthesis
import cv2

# Example usage
if __name__ == '__main__':
    # Load your input image (replace with your actual image path)
    input_image_path = 'path/to/your/input/image.jpg'
    sample = cv2.imread(input_image_path)

    # Display the image
    cv2.imshow("Input Image", sample)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Set parameters (window size, kernel size, etc.)
    window_height, window_width = 50, 50
    kernel_size = 11

    # Initialize texture synthesis
    (sample, window, mask, padded_window,
        padded_mask, result_window) = initialize_texture_synthesis(sample, (window_height, window_width), kernel_size)

    # Perform texture synthesis
    synthesized_texture = synthesize_texture(sample, (window_height, window_width), kernel_size)

    # Save the synthesized texture (replace with your desired output path)
    output_image_path = 'path/to/your/output/synthesized_texture.jpg'
    cv2.imwrite(output_image_path, synthesized_texture)
    print(f"Synthesized texture saved to {output_image_path}")