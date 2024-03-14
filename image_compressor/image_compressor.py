import os
from PIL import Image

def compress_image(input_path, output_folder):
    try:
        # Load the image
        with Image.open(input_path) as img:
            # Compress the image losslessly
            compressed_img = img.copy()

        # Save the compressed image to the output folder
        output_filename = f'{os.path.splitext(os.path.basename(input_path))[0]}_compressed.jpg'
        output_path = os.path.join(output_folder, output_filename)
        compressed_img.save(output_path, quality=5)  # Adjust quality as needed
        print(f'Image compressed and saved to: {output_path}')
    except Exception as e:
        print(f'Error compressing image: {e}')


def main():
    # Input and output folders
    input_folder = 'input_images'
    output_folder = 'output_images'

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Iterate over input images
    for filename in os.listdir(input_folder):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            input_path = os.path.join(input_folder, filename)
            compress_image(input_path, output_folder)


if __name__ == '__main__':
    main()
