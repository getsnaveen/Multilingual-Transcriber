import os 
from abc import ABC, abstractmethod
from typing import Optional, Any
from faster_whisper import WhisperModel
from datetime import timedelta

class Transcribe(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def AudioTranscription(self, inputpath:str, outputpath:str, *args, **kwargs):
        pass

class AudioTranscriptor(Transcribe):
    def __init__(self):
        super().__init__()
        pass
    
    def AudioTranscriptiontoFile(self, inputpath:str, languatetoconvert:str, *args, **kwargs):
        model = WhisperModel('large-v3')         
        transcribe = model.transcribe(audio= inputpath, 
                                          language= languatetoconvert)
        segments = transcribe['segments']
        for segment in segments:
            startTime = str(0)+str(timedelta(seconds=int(segment['start'])))+',000'
            endTime = str(0)+str(timedelta(seconds=int(segment['end'])))+',000'
            text = segment['text']
            segmentId = segment['id']+1
            segment = f"{segmentId}\n{startTime} --> {endTime}\n{text[1:] if text[0] is ' ' else text}\n\n"

            srtFilename = os.path.join("SrtFiles", f"VIDEO_FILENAME.srt")
            with open(srtFilename, 'a', encoding='utf-8') as srtFile:
                srtFile.write(segment)
