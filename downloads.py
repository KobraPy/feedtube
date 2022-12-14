from pytube import Playlist, YouTube
import os
from checks import res_itags
from tempfile import mkdtemp
from audio_video import merging
import shutil
from time import sleep


def clean_up():
    """
    Since i am using moviepy to merge audio em video files
    its very dificult to create a temporary directory...the
    library dont finish the processes immediately after the merging
    so a context manager an even shutil.rmtree cant be used.
    Tham I create this function to be executed in the begining of the process
    and delete the temporary directory if it exists
    """

    if 'temporary' in os.listdir():
        print('cleaning temporary')
        shutil.rmtree('.\\temporary')
    else:
        print('Creating temporary directory')
        os.mkdir('temporary')


def download_video(link: str, itag_video: int):
    """
                --- Download just one video ----
    This function receives a link and a itag from the stream with
    the epecific resolution chosed by the user.
    With the link it dowloads th audio chanel , and with the itag it
    downloads the video, tham merge them using the function "merging"

    """

    data = YouTube(link)
    video_name = data.title

    data.streams.get_by_itag(140).download(
        filename='audio', output_path='.\\temporary'
    )
    print('audio ok')
    data.streams.get_by_itag(itag_video).download(
        filename='video', output_path='.\\temporary'
    )
    print('video ok')

    audio_path = '.\\temporary' + '\\audio'
    video_path = '.\\temporary' '\\video'
    # Merge audio and video an put the video name back
    merging(
        audio_path=audio_path,
        video_path=video_path,
        output_name=video_name + '.mp4',
    )


def download_audio(link: str):
    """
                        ---  Download a audio of a single video ---
    This function receive just a link, and since youtube uses just one stream for audio/only in
    mp4 format, we can use a trick to extract the itag by using string slicing

    """
    data = YouTube(link)
    data_filtered = data.streams.filter(
        file_extension='mp4', only_audio=True, abr='128kbps'
    )
    itag = int(str(data_filtered[0])[15:18])
    print('Downloading...')
    data.streams.get_by_itag(itag).download()
    print('Download finished ...')


def download_playlist_videos(links_and_itag: list):

    # get the playlist link to extrac informations
    link = links_and_itag[0]
    playlist = Playlist(link)
    playlist_name = playlist.title
    print(playlist_name)

    # Create a directory with the playlist name
    if playlist_name not in os.listdir():
        os.mkdir(path=playlist_name)
    else:
        pass

    # Moviepy uses the absolut path and uses the "\\" pattern, so we have to get the path an change the pattern
    dir_path = os.path.abspath(playlist_name).replace('\\', '\\\\')

    # Iterate inside the Playlist object to get the isoleted links and itags
    for itag, video_link in links_and_itag[1:]:

        data = YouTube(video_link)
        video_name = (data.title).strip()

        # Set the name for temporary files of audio e video
        name_audio = video_name.replace('"', '') + 'video'
        name_video = video_name.replace('"', '') + 'audio'

        # Download the audio and video on temporary directory
        data.streams.get_by_itag(140).download(
            filename=name_audio, output_path='temporary'
        )
        print('audio ok')

        data.streams.get_by_itag(itag).download(
            filename=name_video, output_path='temporary'
        )
        print('video ok')

        # get the path to temporary files
        audio_path = 'temporary\\\\' + name_audio
        video_path = 'temporary\\\\' + name_video

        print(audio_path, '\n', video_path)

        merging(
            audio_path=audio_path,
            video_path=video_path,
            output_name=dir_path + '\\\\' + video_name + '.mp4',
        )
        


def download_playlist_audios(link):

    """
            ---Download audios of a playlist---
    This function uses the same trick of the one to download a single audio, it iterates
    for the videos, for each video it iterates for the streams, filter the streams for the
    ones with only_audio/mp4, and extract the itag to download, creates a directory with
    the playlist's name a save the audios there.

    """

    data = Playlist(link)
    playlist_name = data.title

    # Create a directory with the name of the playlist
    if playlist_name not in os.listdir():
        os.mkdir(path=playlist_name)
    else:
        pass

    # Iterate inside the Playlist object to get the isoleted links
    for link in data:

        # Use the links to create a Youtube object
        data = YouTube(link)

        video_name = data.title
        video_publi = data.publish_date

        print(' -------------------------------------------------------')
        print(video_publi, video_name)

        # Filter the stremas of the video to get the ones with a audio_only chanel and a 128kbps
        audio_mp4 = data.streams.filter(
            file_extension='mp4', only_audio=True, abr='128kbps'
        )
        # Using a gambiarra to separete the itag value from the stream we gonna use
        itag_music = int(str(audio_mp4[0])[15:18])

        if video_name + '.mp4' not in os.listdir(playlist_name):
            print(' -- - Downloading - --')
            download = data.streams.get_by_itag(itag_music)
            download.download(output_path=playlist_name)
        else:
            print(video_name('Allready downloaded !! '))
            pass

        print('\n')
