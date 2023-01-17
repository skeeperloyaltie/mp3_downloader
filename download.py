import os
import glob
import youtube_dl

# directory containing the mp3 files
directory = '/path/to/mp3/files'

# get a list of all mp3 files in the directory
mp3_files = glob.glob(os.path.join(directory, '*.mp3'))

# create a list to store the file names without the extension
file_names = []

# iterate through the list of mp3 files
for file in mp3_files:
    # get the file name without the extension
    file_name, _ = os.path.splitext(os.path.basename(file))
    file_names.append(file_name)

# directory to save downloaded files
download_directory = '/path/to/save/files'

# download files using youtube-dl
ydl_opts = {'outtmpl': download_directory + '/%(title)s.%(ext)s'}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    for file_name in file_names:
        ydl.download(['https://www.youtube.com/watch?v='+file_name])
