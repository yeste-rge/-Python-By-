# from pytube import YouTube

# def Download(link):
#     youtube_video = YouTube(link)
#     youtube_video = youtube_video.streams.get_highest_resolution();
#     youtube_video.download() # type: ignore
#     print("YouTube download has been download")

#     link = input("enter the install link you want to install: ")
#     Download(link)
from pytube import YouTube

def download_video(link):
    try:
        # Create a YouTube object
        youtube_video = YouTube(link)
        
        # Get a progressive stream (contains both video and audio)
        stream = youtube_video.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
        
        # Download the video
        stream.download()
        print(f"Download completed for: {youtube_video.title}")
        
    except Exception as e:
        print(f"Error occurred: {e}")

# Get the video link from the user
link = input("Enter the YouTube link you want to download: ")

# Call the function to download the video
download_video(link)