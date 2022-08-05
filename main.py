from numpy import sort
from pytube import YouTube, Playlist
from checks import check_link, res_itags
from downloads import (download_audio,
download_video,
download_playlist_videos,
download_playlist_audios,
clean_up)
import os

'''
                ---- This page simulates a GUI with options to be chosen ---
'''

clean_up()

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

    resolutions_sets = []
    resolution_dicts = []
  

    print('----------THATS A PLAYLIST---------')
    type_download = input("    1) To download the videos\n    2) To download the audios only ")


    if type_download == "1":

        #check all the videos for the resolution that eachone has.
        playlist = Playlist(link)
        for video in playlist:
            
            #Save the link of video
            video_link = video

            #res_itags return a dict with the resolutions and the itags
            res_dict  = res_itags(YouTube(link).streams)

            #Save a list with dictionarys with reolution and itags for each video
            resolution_dicts.append((res_dict, video_link))
            
            #transform the resolutions list in a set separate the intersecton between all of them
            resolutions_sets.append(set(res_dict.keys()))
   
    #separate the intersecton between all of resolutions sets
    resolutions_sets = set.intersection(*resolutions_sets)
    #change the intersection to a list and sort them
    resolutions = sorted(list(resolutions_sets))

    #Dict with the possible choices from a user
    dict_resolution = {}

    #Show the resolutions 
    print("Choose the option of yor resolution")
    for count, item in enumerate(resolutions):
        dict_resolution[count] = item
        print(count,":",item)

    #Get the option for a  resolution chose by the user and check wich is it in dict_resolution
    #It will have to change with a GUI
    user_choice = input(">")
    user_res = dict_resolution[int(user_choice)]  
    
    #create a list with the playlist link, and tuples for each video with the video link and the itag
    #for the resolution chosed by the user
    itag_link = [link]
    for dict in resolution_dicts:
        itag_link.append((dict[0][user_res],dict[1]))
    
    print(itag_link)

    #download_playlist_videos(itag_link)
    
        
    
    
else:
    print("Invalid link")



      
       
   



 
    

    
    
    