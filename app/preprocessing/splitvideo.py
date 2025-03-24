import os 
from abc import ABC, abstractmethod
from typing import Optional, Any
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.video.io import VideoFileClip

class Splitter(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def Video_Splitter(self,filepath:str, segment_length, output_dir, *args, **kwargs):
        pass


class VideoSplitter(Splitter):
    def __init__(self):
        super().__init__()
        pass

    def Video_Splitter(self,filename:str, segment_length, output_dir, *args, **kwargs):
        clip = VideoFileClip(filename)
        duration = clip.duration

        start_time = 0
        end_time = segment_length
        i = 1

        # Extract the filename without extension
        basename = os.path.basename(filename).split('.')[0]

        # Extract directory path
        dir_path = os.path.dirname(filename)

        output_path = os.path.join(dir_path, output_dir)

        # Create output directory if it doesn't exist
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        while start_time < duration:
            output = os.path.join(output_path, f"{basename}_part{i}.mp4")
            ffmpeg_extract_subclip(filename, start_time, min(end_time, duration), targetname=output)
            start_time = end_time
            end_time += segment_length
            i += 1
        print(f'Video split into {i-1} parts.')
    