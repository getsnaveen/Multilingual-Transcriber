import os 
from abc import ABC, abstractmethod
from typing import Optional, Any
from audio_extract import extract_audio

class Extraction(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def AudioExtraction(self, inputpath:str, outputpath:str, *args, **kwargs):
        pass

class AudioExtractor(Extraction):
    def __init__(self):
        super().__init__()
        pass
    
    def AudioExtraction(inputpath:str, outputpath:str, *args, **kwargs):
        extract_audio(input_path= inputpath, output_path= outputpath) 
  
    

        