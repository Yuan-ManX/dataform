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


import audio
import image


def input_file(file_path, file_type):
    """
    Read file and return the data as a NumPy array.

    Parameters:
    - file_path (str): The path to the file.
    - file_type (str): Type of the file ('audio', 'image', or 'other').

    Returns:
    - data_array (numpy.ndarray): NumPy array containing the file data.
    """
    if file_type == 'audio':
        return audio.read_audio_file(file_path)
    elif file_type == 'image':
        return image.read_image_file(file_path)
    else:
        raise ValueError(f"Unsupported file type: {file_type}. Supported types are: 'audio', 'image'")
    

def input_folder(folder_path, folder_type):
    """
    Read folder and return the data as a NumPy array.

    Parameters:
    - folder_path (str): The path to the folder.
    - folder_type (str): Type of the folder ('audio', 'image', or 'other').

    Returns:
    - data_array (numpy.ndarray): NumPy array containing the folder data.
    """
    if folder_type == 'audio':
        return audio.read_audio_file(folder_path)
    elif folder_type == 'image':
        return image.read_image_file(folder_path)
    else:
        raise ValueError(f"Unsupported file type: {folder_type}. Supported types are: 'audio', 'image'")



