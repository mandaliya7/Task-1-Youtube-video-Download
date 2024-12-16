from pytube import YouTube

# Ask the user for the YouTube link
youtube_link = input("Enter the YouTube link: ")

# Create a YouTube object
yt = YouTube(youtube_link)

# Ensure the YouTube object is created before accessing streams
if isinstance(yt, YouTube):
    # Get the highest resolution stream available
    stream = yt.streams.get_highest_resolution()

    # Download the video
    stream.download()

    print(f"The video has been downloaded successfully: {yt.title}")
else:
    print("Failed to create YouTube object. Please check the link.")
