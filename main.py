from pytube import YouTube, Playlist
from checks import check_link, res_itags
from downloads import (download_audio,
download_video,
download_playlist_videos,
download_playlist_audios,
clean_up)
import os


#Check if a link is a playlist or a video
link = input("Paste your link and we will see ....")
check = check_link(link)

clean_up()


# If is a video link
if check == 1:

    print('----------THATS A VIDEO---------')
    type_download = input("    1) To download the video\n    2) To download the audio only ")
    if type_download == "1":
        res_dict ={}
        a = res_itags(YouTube(link).streams)
        for count , item in enumerate(sorted(a.keys())):
            res_dict[count] = item
            print(count, ":", item)
        choice_res = input("Choose the resolution for yor video")
        # Here I have to create a dictionary "res_dict" with the possibilites of choice
        # for the user, thats temporary while I can't implement a GUI for the user to choose.
        chosen_itag = a[res_dict[int(choice_res)]]
        download_video(link=link, itag_video=chosen_itag)
        

    elif type_download == "2":
        download_audio(link)
    else:
        print("Opção invalida")

# if is a playlist
elif check == 2:

    print('----------THATS A PLAYLIST---------')
    type_download = input("    1) To download the videos\n    2) To download the audios only ")
    if type_download == "1":
        #check all the videos for the resolution that everyone has.
        playlist = Playlist(link)
        for video in playlist:
            
            resolutions = (res_itags(YouTube(link).streams)).keys()
        
        

        
    elif type_download == "2":
        download_playlist_audios(link)
    else:
        print("Opção invalida")
    
else:
    print("Invalid link")



      
       
   



 
    

    
    
    