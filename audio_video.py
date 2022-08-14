from moviepy.editor import (
    VideoFileClip,
    AudioFileClip,
)


def merging(video_path: str, audio_path: str, output_name: str = ''):

    video = VideoFileClip(video_path).set_duration(10)
    audio = AudioFileClip(audio_path).set_duration(10)

    end = video.set_audio(audio)
    end.write_videofile(output_name)
