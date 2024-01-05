from pytube import YouTube

# 物件
# YouTube('https://youtu.be/n1ND3bNnJcg?si=3h0d9XH5zo__4egz').streams.first().download()

yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()