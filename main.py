import os

import pysrt
from moviepy import VideoFileClip
from moviepy import  CompositeVideoClip

from models.transcribe import AudioTranscriptor
from preprocessing.audioextraction import AudioExtractor
from postprocessing.integrating_srtfile import create_subtitle_clips
# from faster_whisper import WhisperModel
import streamlit as st
import warnings
warnings.filterwarnings("ignore")

# model = WhisperModel('large-v3') 

# st.title(" Multilingual transcriber ")
# with st.form("my_form"):
if __name__ == "__main__":
    # uploaded_file = st.text_input(label = "video path for movie title creation" ,
    #                                 value = "")  
    uploaded_file = r"F:\Data Science Pro\Multilingual-Transcriber\Input\9.mp4"
    print("#######", uploaded_file)
    # submitted = st.form_submit_button("Submit")    
    base_name = os.path.basename(uploaded_file)
    file_name_without_extension, _ = os.path.splitext(base_name)
    print("#######",file_name_without_extension)
    
    # if submitted:        
    output_filename = file_name_without_extension+ "_audiofile"
    output_filename = "output\\audiofiles\\"+output_filename        
    # st.info("Audio extraction is in progress")
    print("Audio extraction is in progress")
    output_filename = output_filename+".mp3"
    AudioExtractor.AudioExtraction(inputpath = uploaded_file, outputpath = output_filename)     
    print("Transcribe is inprogress ")
    srtfilename = file_name_without_extension+"_SRTfile"  
    srtfilename = "output\\srtfiles\\"+srtfilename+".srt"                        
    AudioTranscriptor.AudioTranscriptiontoFile(inputpath=output_filename, languatetoconvert= "en",outputpath = srtfilename)
    print("SRT file Generated ")
    video = VideoFileClip(uploaded_file)
    subtitles = pysrt.open(srtfilename)
    output_final = file_name_without_extension+ "_subtitled.mp4"
    output_final = "output\\final\\"+output_final 
    
    print ("Output file name: ",output_final)

    # Create subtitle clips
    subtitle_clips = create_subtitle_clips(subtitles,video.size)

    # Add subtitles to the video
    final_video = CompositeVideoClip([video] + subtitle_clips)

    # Write output video file
    final_video.write_videofile(output_final)

        