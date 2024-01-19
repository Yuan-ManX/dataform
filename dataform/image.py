# MIT License

# Copyright (c) 2024 Yuan-Man

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import os
import numpy as np
from PIL import Image


def read_image_file(file_path):
    """
    Read image file and return the image data as a NumPy array.

    Parameters:
    - file_path (str): The path to the image file.

    Returns:
    - image_array (numpy.ndarray): NumPy array containing the image data.
    """
    try:
        # Determine file type based on extension
        file_extension = file_path.split('.')[-1].lower()
        supported_image_types = ['png', 'jpeg', 'jpg', 'gif', 'bmp', 'tiff', 'svg']

        if file_extension not in supported_image_types:
            raise ValueError(f"Unsupported image file type. Supported types are: {', '.join(supported_image_types)}")

        # Read image data
        image = Image.open(file_path)
        image_data = np.array(image)
        return image_data
    except Exception as e:
        raise ValueError(f"Error reading image file: {e}")


def write_image_file(output_file, image_data):
    """
    Write image data to a file in the specified format.

    Parameters:
    - output_file (str): The path to the output image file.
    - image_array (numpy.ndarray): NumPy array containing the image data.

    Returns:
    - None
    """
    try:
        # Determine output file type based on extension
        file_extension = output_file.split('.')[-1].lower()
        supported_image_types = ['png', 'jpeg', 'jpg', 'gif', 'bmp', 'tiff', 'svg']

        if file_extension not in supported_image_types:
            raise ValueError(f"Unsupported image file type. Supported types are: {', '.join(supported_image_types)}")

        # Write image data
        image = Image.fromarray(image_data)
        image.save(output_file)
    except Exception as e:
        raise ValueError(f"Error writing image file: {e}")


def read_image_folder(folder_path):
    """
    Read image files from a folder and return a dictionary.

    Parameters:
    - folder_path (str): The path to the folder containing image files.

    Returns:
    - image_data_dict (dict): Dictionary with file names as keys and NumPy arrays as values.
    """
    image_data_dict = {}

    try:
        # Iterate through files in the folder
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)

            # Check if the file is a regular file
            if os.path.isfile(file_path):
                try:
                    # Use the read_image_file function to read image data
                    image_data = read_image_file(file_path)
                    image_data_dict[file_name] = image_data
                except ValueError as e:
                    print(f"Error reading {file_name}: {e}")

        return image_data_dict

    except Exception as e:
        raise ValueError(f"Error reading image folder: {e}")

