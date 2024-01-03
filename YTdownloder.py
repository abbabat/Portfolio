from pytube import YouTube
from sys import argv



link = argv[1]

yt = YouTube(link)
    
print("Title: ", yt.title)
    
print("Views: ", yt.views)
    
print("Uploded on: ", yt.publish_date)
    
print("Video leghnt: ", yt.length/60)


yd = yt.streams.get_highest_resolution()
    
yd.download("/Users/abbabatoure/Documents/Projects/Youtube downlowder")  #Proovide a forder we the video goes


#run : python3 /Users/abbabatoure/Documents/Projects/Youtube\ downlowder/YTdownloder.py "https://www.youtube.com/watch?v=K_CbgLpvH9E&t=324s"






      