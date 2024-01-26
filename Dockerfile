
    #syntax=docker/dockerfile:1

    FROM python

    WORKDIR /app

    COPY requirements.txt /app

    RUN pip install -r requirements.txt

    COPY . .

    EXPOSE 8000

    CMD ["py","manage.py","runserver","0.0.0.0:8000"]