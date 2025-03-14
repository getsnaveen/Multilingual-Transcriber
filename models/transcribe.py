import os 
from abc import ABC, abstractmethod
from typing import Optional, Any
from datetime import timedelta
from faster_whisper import WhisperModel

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
        counter = 0
        for segment in segments:
            startTime = segment.start 
            endTime = segment.end
            text = segment.text
            segmentId = counter
            counter += 1
            segment = f"{segmentId}\n{startTime} --> {endTime}\n{text[1:] if text[0] is ' ' else text}\n\n"

            # srtFilename = os.path.join(outputpath, f"1.srt")
            with open(outputpath, 'a', encoding='utf-8') as srtFile:
                srtFile.write(segment)


    