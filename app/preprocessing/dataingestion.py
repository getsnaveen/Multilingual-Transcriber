import os 
from abc import ABC, abstractmethod
from typing import Optional, Any
import yt_dlp

class Loader(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def Video_Loader(self,filepath:str, *args, **kwargs):
        pass

    @abstractmethod
    def Downloader(self,filepath:str, *args, **kwargs):
        pass

class VideoLoader(Loader):
    def __init__(self):
        super().__init__()
        pass

    def Video_Loader(self, filepath, *args, **kwargs):
        pass
    
    def Downloader(self, filepath, *args, **kwargs):
        ydl_opts = {}    
        video_url = filepath.strip()    
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])

        