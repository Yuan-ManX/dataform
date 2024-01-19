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


import wave
import os
import numpy as np
from pydub import AudioSegment


def read_audio_file(file_path):
    """
    Read audio file and return the audio data as a NumPy array.

    Parameters:
    - file_path (str): The path to the audio file.

    Returns:
    - audio_data (numpy.ndarray): NumPy array containing the audio data.
    """
    try:
        # Determine file type based on extension
        file_extension = file_path.split('.')[-1].lower()
        if file_extension not in ['wav', 'mp3', 'ogg']:
            raise ValueError("Unsupported audio file type. Supported types are: 'wav', 'mp3', 'ogg'")

        # Read audio data based on file type
        if file_extension == 'wav':
            with wave.open(file_path, 'rb') as wf:
                frames = wf.getnframes()
                audio_data = wf.readframes(frames)
            audio_data = np.frombuffer(audio_data, dtype=np.int16)

        else:
            audio = AudioSegment.from_file(file_path, format=file_extension)
            audio_data = np.array(audio.get_array_of_samples(), dtype=np.int16)

        return audio_data
    except Exception as e:
        raise ValueError(f"Error reading audio file: {e}")


def write_audio_file(output_file, audio_data, channels=1, sample_width=2, frame_rate=44100):
    """
    Write audio data to a file in the specified format.

    Parameters:
    - output_file (str): The path to the output audio file.
    - audio_data (numpy.ndarray): NumPy array containing the audio data.
    - channels (int, optional): Number of audio channels. Default is 1 (mono).
    - sample_width (int, optional): Sample width in bytes. Default is 2 (16-bit).
    - frame_rate (int, optional): Frame rate in Hz. Default is 44100.

    Returns:
    - None
    """
    try:
        # Determine output file type based on extension
        file_extension = output_file.split('.')[-1].lower()
        if file_extension not in ['wav', 'mp3', 'ogg']:
            raise ValueError("Unsupported audio file type. Supported types are: 'wav', 'mp3', 'ogg'")

        # Write audio data based on file type
        if file_extension == 'wav':
            with wave.open(output_file, 'wb') as wf:
                wf.setnchannels(channels)
                wf.setsampwidth(sample_width)
                wf.setframerate(frame_rate)
                wf.writeframes(audio_data.astype(np.int16).tobytes())

        else:
            audio = AudioSegment(audio_data.astype(np.int16).tobytes(), sample_width=sample_width, frame_rate=frame_rate, channels=channels)
            audio.export(output_file, format=file_extension)
    except Exception as e:
        raise ValueError(f"Error writing audio file: {e}")


def read_audio_folder(folder_path):
    """
    Read audio files from a folder and return a dictionary.

    Parameters:
    - folder_path (str): The path to the folder containing audio files.

    Returns:
    - audio_data_dict (dict): Dictionary with file names as keys and NumPy arrays as values.
    """
    audio_data_dict = {}

    try:
        # Iterate through files in the folder
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)

            # Check if the file is a regular file
            if os.path.isfile(file_path):
                try:
                    # Use the read_audio_file function to read audio data
                    audio_data = read_audio_file(file_path)
                    audio_data_dict[file_name] = audio_data
                except ValueError as e:
                    print(f"Error reading {file_name}: {e}")

        return audio_data_dict

    except Exception as e:
        raise ValueError(f"Error reading audio folder: {e}")

