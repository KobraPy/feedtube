
from pytube import *


def res_itags(stream):
    '''
    Receive the return of Youtube(url).streams object(A list with the streams avaliable in a video)
    and return a dictionary with the itags an the resolutions.
    ATENTION! Any other filtering must be done before with the function "Youtube(url).steams.filter".
    
    '''
    itags = {}

    for linha in stream:
        

        l = str(linha).split(" ")

        if 'res="2160p"' in l:
            itag = "".join(x for x in l[1] if x.isdigit())
            itags[2160] = itag

        if 'res="1440p"' in l:
            itag = "".join(x for x in l[1] if x.isdigit())
            itags[1440] = itag
    
        if 'res="1080p"' in l:
            itag = "".join(x for x in l[1] if x.isdigit())
            itags[1080] = itag
            
        elif 'res="720p"' in l:
            itag = "".join(x for x in l[1] if x.isdigit())
            itags[720] = itag
        
        elif 'res="480p"' in l:
            itag = "".join(x for x in l[1] if x.isdigit())
            itags[480] = itag

        elif 'res="360p"' in l:
            itag = "".join(x for x in l[1] if x.isdigit())
            itags[360] = itag
            
        elif 'res="240p"' in l:
            itag = "".join(x for x in l[1] if x.isdigit())
            itags[240] = itag
        
        elif 'res="144p"' in l:
            itag = "".join(x for x in l[1] if x.isdigit())
            itags[144] = itag
        else:
            pass

  
    return itags

def check_link(link: str) -> int:
    '''
    Check if a link is a single video or a playlist trying to get proprities 
    from it that only video, or playlist will have
    if none of this, will return invalid value
    '''
    try:
        Playlist(link).playlist_id
        return 2
    except:
        try:
            YouTube(link).streams.filter(only_video=True)
            return 1

        except :
            return 3


    

            


