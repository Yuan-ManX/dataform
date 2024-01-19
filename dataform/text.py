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


import numpy as np
from PyPDF2 import PdfReader


def read_text_file(file_path, delimiter=',', num_columns=None):
    """
    Read text file (including PDF) and return the data as a NumPy array.

    Parameters:
    - file_path (str): The path to the text file.
    - delimiter (str, optional): The delimiter used in the text file (e.g., ',', ';'). Default is ','.
    - num_columns (int, optional): The expected number of columns in the resulting data. Default is None.

    Returns:
    - data_array (numpy.ndarray): NumPy array containing the data.
    """
    try:
        file_extension = get_file_extension(file_path)
        if file_extension == 'txt':
            data_array = np.loadtxt(file_path, delimiter=delimiter)
        elif file_extension == 'csv':
            data_array = np.genfromtxt(file_path, delimiter=delimiter)
        elif file_extension == 'pdf':
            data_array = read_pdf(file_path, num_columns=num_columns)
        else:
            raise ValueError(f"Unsupported text file type: {file_extension}")

        return data_array
    except Exception as e:
        raise ValueError(f"Error reading text file: {e}")
    

def get_file_extension(file_path):
    """
    Get the file extension from the file path.

    Parameters:
    - file_path (str): The path to the file.

    Returns:
    - extension (str): The file extension.
    """
    return file_path.split('.')[-1].lower()


def read_pdf(file_path, num_columns=None):
    """
    Read data from a PDF file using PyPDF2.

    Parameters:
    - file_path (str): The path to the PDF file.
    - num_columns (int, optional): The expected number of columns in the resulting data. Default is None.

    Returns:
    - data_array (numpy.ndarray): NumPy array containing the data.
    """
    try:
        if num_columns is None:
            # Default to a reasonable number of columns if not specified
            num_columns = 10

        with open(file_path, 'rb') as file:
            pdf_reader = PdfReader(file)
            num_pages = len(pdf_reader.pages)

            # Extract text from all pages
            text = ''
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()

            # Split the text into lines
            lines = text.split('\n')

            # Filter out lines that cannot be converted to float
            lines = [line.strip() for line in lines if is_float(line)]

            # Create a list of lists ensuring each row has the same number of elements
            data_list = [line.split(',')[:num_columns] for line in lines]

            # Pad or truncate lines to ensure uniform length
            data_list = [line + [''] * (num_columns - len(line)) if len(line) < num_columns else line[:num_columns] for line in data_list]

            # Convert the list of lists into a NumPy array
            data_array = np.array(data_list, dtype=np.float)

        return data_array
    except Exception as e:
        raise ValueError(f"Error reading PDF file: {e}")
    

def is_float(value):
    """
    Check if a string can be converted to a float.

    Parameters:
    - value (str): The string to check.

    Returns:
    - is_float (bool): True if the string can be converted to a float, False otherwise.
    """
    try:
        float(value)
        return True
    except ValueError:
        return False

