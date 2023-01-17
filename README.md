## Music Downloader
This script is designed to download music files from YouTube.

## Requirements
  Python 3.x
  youtube-dl library
  os,glob library
  concurrent.futures library
## How to use
  Replace the directory variable with the path of the directory containing the mp3 files
  Replace the download_directory variable with the path of the directory where you want to save the downloaded files.
  Run the script python 
      downloader.py
## Features
- Downloads multiple files in parallel using ThreadPoolExecutor to minimize the time it takes to download the files.
- Handles network errors by retrying the download a few times.
- Continues the download if it failed before.
- Replaces spaces and special characters in the file name with underscores to avoid invalid URL.
- Downloads the best available audio format of the video, which is usually in mp3 format.
- Can download the video if the file name is the title of the video.
- Hides warning messages generated by youtube-dl
## Note
Please be careful while using this code if you have a large number of files to download and a low-bandwidth internet connection, as it may cause the network to be saturated, and download speed may be affected.
Downloading copyrighted material without permission may be illegal in your country.
## Dependency
  - youtube-dl: https://github.com/ytdl-org/youtube-dl

  - os: https://docs.python.org/3/library/os.html

  - glob: https://docs.python.org/3/library/glob.html

  - concurrent.futures: https://docs.python.org/3/library/concurrent.futures.html