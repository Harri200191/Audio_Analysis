import tkinter as tk
from tkinter import filedialog
import os
from pydub import AudioSegment
import shutil

def select_audio_file():
    root = tk.Tk()
    root.withdraw()  
 
    audio_file_path = filedialog.askopenfilename(
        title="Select an audio file",
        filetypes=[("Audio Files", "*.mp3 *.wav *.flac *.ogg *.m4a")]
    )

    if audio_file_path:
        return audio_file_path
    else:
        return None
    
def extract_extension(input_string): 
    last_period_index = input_string.rfind(".")
 
    if last_period_index != -1: 
        extension = input_string[last_period_index + 1:]
        return extension
    else: 
        return input_string

def convert_audio_to_mp3(input_path, output_path): 
    audio = AudioSegment.from_file(input_path) 
    audio.export(output_path, format="mp3")
    
def copy_to_current_directory(source_path, destination_directory):
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    file_name = os.path.basename(source_path)
    extens = extract_extension(file_name)
    destination_path = os.path.join(destination_directory, "MainAudio."+extens)
    shutil.copy2(source_path, destination_path)
    input_path = "MainAudio."+extens  
    output_path = "MainAudio.mp3"
    convert_audio_to_mp3(input_path, output_path)
    
    return destination_path

if __name__ == "__main__":
    selected_audio_file = select_audio_file()

    if selected_audio_file:
        current_directory = os.getcwd()
        copied_file_path = copy_to_current_directory(selected_audio_file, current_directory)
        print(f"Selected audio file: {selected_audio_file}")
        print(f"Audio file copied to the current directory: {copied_file_path}")
        print(f"Selected audio file: {selected_audio_file}")
    else:
        print("No audio file selected.")