from moviepy.editor import (
    VideoFileClip,
    AudioFileClip,
)


video = VideoFileClip(
    "temporary\\Chizuru's crying over Kazuya motivating her - Rent a Girlfriend Season 2 Episode 1video"
).set_duration(10)
audio = AudioFileClip(
    "temporary\\Chizuru's crying over Kazuya motivating her - Rent a Girlfriend Season 2 Episode 1audio"
).set_duration(10)

end = video.set_audio(audio)
end.write_videofile(
    'C:\\Users\\outho\\Desktop\\yotube\\teste_video\\teste.mp4'
)
