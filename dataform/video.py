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


import cv2
import numpy as np


def read_video_file(file_path):
    """
    Read video file and return the video frames as a NumPy array.

    Parameters:
    - file_path (str): The path to the video file.

    Returns:
    - video_data (numpy.ndarray): NumPy array containing the video frames.
    """
    # Supported video file types
    supported_video_types = ['mp4', 'avi', 'mov']

    try:
        # Determine file type based on extension
        file_extension = file_path.split('.')[-1].lower()
        if file_extension not in supported_video_types:
            raise ValueError(f"Unsupported video file type. Supported types are: {', '.join(supported_video_types)}")

        # Read video data
        cap = cv2.VideoCapture(file_path)
        frames = []
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            frames.append(frame)
        cap.release()

        video_data = np.array(frames)
        return video_data
    except Exception as e:
        raise ValueError(f"Error reading video file: {e}")
    

def write_video_file(output_file, video_array, fps=30, codec='mp4v'):
    """
    Write video frames to a file in the specified format.

    Parameters:
    - output_file (str): The path to the output video file.
    - video_array (numpy.ndarray): NumPy array containing the video frames.
    - fps (int, optional): Frames per second. Default is 30.
    - codec (str, optional): Video codec to use (e.g., 'mp4v', 'xvid', 'MJPG', 'DIVX', etc.). Default is 'mp4v'.

    Returns:
    - None
    """
    # Supported video file types
    supported_video_types = ['mp4', 'avi', 'mov']

    try:
        # Determine output file type based on extension
        file_extension = output_file.split('.')[-1].lower()
        if file_extension not in supported_video_types:
            raise ValueError(f"Unsupported video file type. Supported types are: {', '.join(supported_video_types)}")

        if video_array.size == 0 or video_array.shape[0] == 0:
            raise ValueError("Empty video array. Cannot write an empty video.")

        # Write video data
        fourcc = cv2.VideoWriter_fourcc(*codec)
        height, width, _ = video_array[0].shape
        out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

        for frame in video_array:
            out.write(frame)
        out.release()
    except Exception as e:
        raise ValueError(f"Error writing video file: {e}")


