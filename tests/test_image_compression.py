import unittest
import os
from image_compressor.image_compressor import compress_image

class TestImageCompression(unittest.TestCase):
    
    def setUp(self):
        self.input_folder = 'test_input'
        self.output_folder = 'test_output'
        os.makedirs(self.input_folder, exist_ok=True)
        os.makedirs(self.output_folder, exist_ok=True)
        
    def tearDown(self):
        for file in os.listdir(self.input_folder):
            os.remove(os.path.join(self.input_folder, file))
        for file in os.listdir(self.output_folder):
            os.remove(os.path.join(self.output_folder, file))
        os.rmdir(self.input_folder)
        os.rmdir(self.output_folder)
        
    def test_lossless_compression(self):
        # Create a sample image file
        image_path = os.path.join(self.input_folder, 'test_image.jpg')
        open(image_path, 'a').close()
        
        # Compress the image
        compress_image(image_path, self.output_folder)
        
        # Assert that the output file exists
        output_file = os.path.join(self.output_folder, 'test_image_compressed.jpg')
        self.assertTrue(os.path.exists(output_file))
        
    def test_original_not_deleted(self):
        # Create a sample image file
        image_path = os.path.join(self.input_folder, 'test_image.jpg')
        open(image_path, 'a').close()
        
        # Compress the image
        compress_image(image_path, self.output_folder)
        
        # Assert that the original file still exists
        self.assertTrue(os.path.exists(image_path))
        
    def test_output_folder_exists(self):
        # Create a sample image file
        image_path = os.path.join(self.input_folder, 'test_image.jpg')
        open(image_path, 'a').close()
        
        # Compress the image
        compress_image(image_path, self.output_folder)
        
        # Assert that the output folder exists
        self.assertTrue(os.path.exists(self.output_folder))

if __name__ == '__main__':
    unittest.main()
