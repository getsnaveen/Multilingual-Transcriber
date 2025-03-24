import sys
import pysrt
from moviepy import TextClip

def time_to_seconds(time_obj):
    return time_obj.hours * 3600 + time_obj.minutes * 60 + time_obj.seconds + time_obj.milliseconds / 1000


def create_subtitle_clips(subtitles, videosize,fontsize=24, font='Arial', color='white', debug = False):
    subtitle_clips = []
    font = "Arial.ttf"
    for subtitle in subtitles:
        start_time = time_to_seconds(subtitle.start)
        end_time = time_to_seconds(subtitle.end)
        duration = end_time - start_time

        video_width, video_height = videosize
        
        text_clip = TextClip(font=font,
                             text = subtitle.text, 
                             color=color, 
                             bg_color = 'black',
                             size=(int(video_width*3/4), None)).with_start(start_time).with_duration(duration)
        subtitle_x_position = 'center'
        subtitle_y_position = video_height* 4 / 5 

        text_position = (subtitle_x_position, subtitle_y_position)                    
        subtitle_clips.append(text_clip.with_position(text_position))

    return subtitle_clips

