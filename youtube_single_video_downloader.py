from pytube import YouTube

# Video where to save
save_path ="C:/Users/vivek/OneDrive/Desktop/New folder/youtube_video_downloader/"

# Take video link
link = input("Enter Video Link: ")

try:
    yt = YouTube(link)
except:
    print("Connection Error")

resolution = input('''Select Resolution of Video
1 for 360p
2 for 720p
''')

if resolution=="1":
    mp4files = yt.streams.get_by_resolution('360p')

elif resolution=="2":
    mp4files = yt.streams.get_by_resolution('720p')

else:
    print("Incorrect input")



try:
    mp4files.download(save_path)
    print('Task Completed')
    
except:
    print("Some Error Occured!")

