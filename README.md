# YouTube Video Downloader

This Python script provides a simple graphical user interface (GUI) for downloading YouTube videos. It utilizes the pytube library for handling YouTube video downloads and tkinter for creating the GUI. The user can specify the video URL, save path, and select the desired resolution for the downloaded video.

## Dependencies

Make sure you have the necessary libraries installed before running the script. You can install them using the following:

bash

pip install pytube

## Usage

### 1. Clone the Repository:

git clone https://github.com/your-username/your-repo.git
cd your-repo

### 2. Run the Script:

    python youtube_downloader.py

### 3. GUI Interface:
        Upon running the script, a Tkinter window will open.
        Enter the YouTube video URL in the provided field.
        Specify the save path for the downloaded video.
        Choose the desired resolution from the dropdown menu.

### 4. Click Download:
        After configuring the settings, click the "Download" button to initiate the download process.
        The script will attempt to download the video with the specified parameters.

### 5. Success/Failure Messages:
        If the download is successful, a message will be printed indicating the resolution and success status.
        If no suitable stream is found for the selected resolution, an appropriate message will be displayed.

### 6. Closing the Application:
        The Tkinter window will close automatically after the download process, or you can manually close it.

## Important Note

    The script uses the pytube library to interact with YouTube and download videos. Make sure your internet connection is stable.

    The available resolutions for download are '720p', '480p', and '360p'. You can customize the resolutions in the resolutions dictionary if needed.

    The Tkinter GUI provides a user-friendly interface for interacting with the script.

    The script handles exceptions during the download process and prints relevant error messages.

    After a successful download, the Tkinter window will be closed.

## Customization

    You can modify the script to include additional features or adapt it to your specific requirements.

    Explore the pytube documentation for more options and functionalities: pytube Documentation

    Customize the default video URL and save path in the script according to your preferences.

Feel free to experiment and enhance the functionality based on your needs.