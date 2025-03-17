import os, math 
from abc import ABC, abstractmethod
from typing import Optional, Any
from datetime import timedelta
from faster_whisper import WhisperModel
from utils import format_time

class Transcribe(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def AudioTranscriptiontoFile(self, inputpath:str, languatetoconvert:str, outputpath:str, *args, **kwargs):
        pass

class AudioTranscriptor(Transcribe):
    def __init__(self):
        super().__init__()
        pass   
    
    def AudioTranscriptiontoFile(inputpath:str, languatetoconvert:str, outputpath:str, *args, **kwargs):
        model = WhisperModel('large-v3') 
                
        transcribe,info = model.transcribe(audio= inputpath, 
                                          language= languatetoconvert)
        segments = list(transcribe)
        text = ""
        for index, segment in enumerate(segments):
            segment_start = format_time(segment.start)
            segment_end = format_time(segment.end)
            text += f"{str(index+1)} \n"
            text += f"{segment_start} --> {segment_end} \n"
            text += f"{segment.text} \n"
            text += "\n"
            
        f = open(outputpath, "w")
        f.write(text)
        f.close()
            

    