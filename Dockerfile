#pull the python 3.9.10 image from dockerhub
FROM python:3.9.10-slim-buster

#copy every file in current directory to /app container
COPY . /app

#make the dockera-app directory as the wokring directory
WORKDIR /app


#install the required libraries and modules
RUN pip3 install -r requirments.txt

#run the application
CMD ["python3","app.py"]
