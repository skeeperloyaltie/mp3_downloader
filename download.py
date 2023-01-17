import os
import glob
import youtube_dl
import concurrent.futures

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

# function to download a file using youtube-dl
def download_file(file_name):
    ydl_opts = {
        'outtmpl': download_directory + '/%(title)s.%(ext)s',
        'quiet': True,
        'retries': 3,
        'continuedl': True
    }
    url = 'https://www.youtube.com/watch?v='+file_name
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f'Successfully downloaded {file_name}')
    except Exception as e:
        print(f'Error downloading {file_name}: {e}')

# use concurrent.futures to download files in parallel
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(download_file, file_name) for file_name in file_names]
    for f in concurrent.futures.as_completed(results):
        pass
