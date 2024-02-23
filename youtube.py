# Import necessary libraries
from pytube import YouTube
import tkinter as tk
from tkinter import filedialog, ttk

# Function to download video based on the provided URL, save path, and resolution
def download_video(url, save_path, resolution):
    try:
        # Create a YouTube object for the given URL
        yt = YouTube(url)
        
        # Filter available video streams for progressive streams with MP4 extension
        streams = yt.streams.filter(progressive=True, file_extension="mp4")

        # Filter streams based on the selected resolution
        selected_streams = streams.filter(res=resolutions[resolution])

        if selected_streams:
            # Get the first stream from the selected streams
            chosen_stream = selected_streams.first()
            
            # Download the video to the specified save path
            chosen_stream.download(output_path=save_path)
            
            # Print success message with the selected resolution
            print(f"Video downloaded Successfully! - Resolution: {resolution}")
            
            # Close the Tkinter window after download
            root.destroy()
        else:
            # Print a message if no stream is found for the selected resolution
            print(f"No stream found for resolution: {resolution}")

    except Exception as e:
        # Print any exception that occurs during the download process
        print(e)

# Provide available resolutions in a dictionary
resolutions = {
    '720p': '720p',
    '480p': '480p',
    '360p': '360p',
}

# Set the default YouTube video URL and save path
url = "" # Put your YouTube video URL here
save_path = "" # Put your File location here

# Create a simple Tkinter GUI with a dropdown menu to select resolution
root = tk.Tk()
root.title("YouTube Video Downloader")

# Create a label for resolution selection
resolution_label = tk.Label(root, text="Select Resolution:")
resolution_label.pack(pady=10)

# Create a StringVar to store the selected resolution, and set it to the default resolution
resolution_var = tk.StringVar(root)
resolution_var.set('720p')

# Create a Combobox (dropdown menu) for resolution selection
resolution_menu = ttk.Combobox(root, textvariable=resolution_var, values=list(resolutions.keys()))
resolution_menu.pack(pady=10)

# Function to start the download when the button is clicked
def start_download():
    resolution_choice = resolution_var.get()
    download_video(url, save_path, resolution_choice)

# Create a button for starting the download
download_button = tk.Button(root, text="Download", command=start_download)
download_button.pack(pady=10)

# Run the Tkinter main loop
if __name__ == "__main__":
    root.mainloop()
