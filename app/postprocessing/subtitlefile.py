import ffmpeg


def main():
    #define globals
    RAW_TEXT_LIST : List[tuple[str,str,int]]   # you should assing to RAW_TEXT_LIST each section of the text
    # RAW_TEX_LIST =            # right here
    NAME_OF_FILE : str = "THE_NAME_OF_THE_SUB_FILE_TO_WRITE" #change this

    currentSection : int = 0

    def convertMillisToTc(millis: int) -> str:
        #utility function to convert miliseconds to timeCode hh:mm:ss,mmm
        miliseconds,seconds=divmod(int(millis/1000),60)
        minutes=int(millis/(1000*60))%60
        hours=int(millis/(1000*60*60))%24
        return f"{hours:02d}:{minutes:02d}:{seconds:02d},{miliseconds:03d}"

    def makeSubRipStr(rawText : str, initialTimeCode: str, durationInMiliseconds : int ) -> str: 
        currentSection+=1 # we add 1 to the currentSection counter, starting in 1.
        
        initialTimeCodeInMilis : int = sum((3600000 * int(hours), 60000 * int(minutes),1000 * int(seconds), int(miliseconds)) for hours,minutes,seconds,miliseconds in initialTimeCode.split(":"))
        finalTimeCode : str = convertMillisToTC(initialTimeCodeInMilis + durationInMiliseconds);
        formatedText : str = f'{currentSection}\n{initialTimeCodetimeCode} --> {finalTimeCode}\n{rawText}\n\n'
        return formatedText


    #Create the file and do nothing with it
    with open(file=f"./subfiles/{NAME_OF_FILE}.srt",mode="w",encoding="utf-8") as subFile: pass

    #open the file in "append mode and add each entry formated"
    with open(file=f"./subfiles/{NAME_OF_FILE}.srt",mode="a+",encoding="utf-8") as subFile: 
        for sourceTuple in RAW_TEX_LIST:
            text, initialTC, duration = sourceTuple
            subFile.write(makeSubRipStr(text,initialTC,duration)) 

def add_subtitle_to_video(soft_subtitle, subtitle_file,  subtitle_language):

    video_input_stream = ffmpeg.input(input_video)
    subtitle_input_stream = ffmpeg.input(subtitle_file)
    output_video = f"output-{input_video_name}.mp4"
    subtitle_track_title = subtitle_file.replace(".srt", "")

    if soft_subtitle:
        stream = ffmpeg.output(
            video_input_stream, subtitle_input_stream, output_video, **{"c": "copy", "c:s": "mov_text"},
            **{"metadata:s:s:0": f"language={subtitle_language}",
            "metadata:s:s:0": f"title={subtitle_track_title}"}
        )
        ffmpeg.run(stream, overwrite_output=True)