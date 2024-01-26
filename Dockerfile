
    #syntax=docker/dockerfile:1

    FROM python:3.12.1-windowsservercore-ltsc2022

    WORKDIR /app

    COPY requirements.txt requirements.txt

    RUN pip install requirements.txt

    COPY . .

    CMD ["py","manage.py","runserver","0.0.0.0:8000","--noreload"]