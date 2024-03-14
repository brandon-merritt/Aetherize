import time
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os

def compress_images():
    input_paths = input_entry.get().split('\n')
    output_folder = output_entry.get()
    
    for input_path in input_paths:
        try:
            # Load the image
            with Image.open(input_path) as img:
                # Convert RGBA image to RGB mode if necessary
                if img.mode == 'RGBA':
                    img = img.convert('RGB')
                
                # Compress the image losslessly
                compressed_img = img.copy()

            # Save the compressed image to the output folder
            output_filename = f'{os.path.splitext(os.path.basename(input_path))[0]}_compressed.jpg'
            output_path = os.path.join(output_folder, output_filename)
            compressed_img.save(output_path, quality=50)  # Adjust quality as needed
            original_creation_time = os.path.getctime(input_path)
            os.utime(output_path, (original_creation_time, original_creation_time))
            result_text.insert(tk.END, f'Image compressed and saved to: {output_path}\n')
        except Exception as e:
            result_text.insert(tk.END, f'Error compressing image: {e}\n')


def browse_input():
    filenames = filedialog.askopenfilenames(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
    input_entry.delete(0, tk.END)
    input_entry.insert(0, '\n'.join(filenames))

def browse_output():
    directory = filedialog.askdirectory()
    output_entry.delete(0, tk.END)
    output_entry.insert(0, directory)

# Create main window
window = tk.Tk()
window.title("Aetherize - MadSciProductions")
png_image = Image.open("image_compressor/aetherize_logo.png")
png_image = png_image.resize((16,16))
photo = ImageTk.PhotoImage(png_image)
window.iconphoto(True, photo)
# Input paths
input_label = tk.Label(window, text="Input Images:")
input_label.grid(row=0, column=0)
input_entry = tk.Entry(window, width=50)
input_entry.grid(row=0, column=1)
browse_input_button = tk.Button(window, text="Browse", command=browse_input)
browse_input_button.grid(row=0, column=2)

# Output folder
output_label = tk.Label(window, text="Output Folder:")
output_label.grid(row=1, column=0)
output_entry = tk.Entry(window, width=50)
output_entry.grid(row=1, column=1)
browse_output_button = tk.Button(window, text="Browse", command=browse_output)
browse_output_button.grid(row=1, column=2)

# Compress button
compress_button = tk.Button(window, text="Compress Images", command=compress_images)
compress_button.grid(row=2, column=1)

# Result display
result_text = tk.Text(window, width=50, height=10)
result_text.grid(row=3, column=0, columnspan=3)

# Start the GUI event loop
window.mainloop()