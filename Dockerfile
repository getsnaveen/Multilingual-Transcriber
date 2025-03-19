FROM python:3.11.11
# install app dependencies
# RUN apt install ffmpeg
RUN apt-get update && apt-get install -y python3 python3-pip
COPY . ./multilingual-transcriber/
RUN pip install --upgrade pip 
RUN pip install -r /multilingual-transcriber/requirements.txt
EXPOSE 8501
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health
# CMD ["streamlit", "run", "/multilingual-transcriber/main.py", "--host", "0.0.0.0", "--port", "8501"]
ENTRYPOINT ["streamlit", "run", "/multilingual-transcriber/main.py", "--server.port=8501", "--server.address=0.0.0.0"]
