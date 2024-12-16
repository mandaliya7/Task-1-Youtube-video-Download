# youtube video download by link are user input
import yt_dlp # import module for video download
import os # this module is use for interact with operating system

# link by user
yt_link = input("Enter the YouTube link: ")

# quality input by user
while True:
    try:
        quality = int(input("Enter the desired video quality (e.g., 720, 1080): "))
        if quality >= 0:
            break
        #if user are enter incorrect value than error are show
        else:
            print("enter a valid quality")
    except ValueError:
        print("Please enter a valid quality e.g : 720 , 1080.")

# path for video download
download_directory = os.path.join(os.path.expanduser("~"), "Desktop")

# conditions for video quality
if quality >= 0 and quality <= 192:
    format_quality = '144p'
elif quality >= 193 and quality <= 360:
    format_quality = '240p'
elif quality >= 361 and quality <= 600:
    format_quality = '480p'
elif quality >= 601 and quality <= 900:
    format_quality = '720p'
elif quality >= 901:
    format_quality = '1080p'
else:
    format_quality = 'best'

# file name and download quality
ydl_opts = {
    'format': f'bestvideo[height<={format_quality}]+bestaudio/best[height<={format_quality}]',
    'outtmpl': os.path.join(download_directory, f'%(title)s.%(ext)s'),
}

# download video
try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([yt_link])
    # massage of video download successfully
    print(f"The video has been downloaded successfully to {download_directory}.")
# error for problem
except Exception as e:
    print("An error occurred:", e)
