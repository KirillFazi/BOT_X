#FROM python:3.9-aplpine
#
#WORKDIR /app
#
#ENV PYTHONDONTWRITEBYTECODE=1\
#    PYTHONUNBUFFERED=1
#
#MAINTAINER Madhuri Koushik "[email protected]"
#
#RUN apt-get update -y \
#    apt-get install -y python3-pip python3-dev
#
#COPY .. .
#
#RUN pip install --no-cache-dir -r requirements.txt
#
#ENTRYPOINT [ "python3" ]
#
#CMD [ "app/app.py" ]

# установка базового образа (host OS)
FROM python:3.8
# установка рабочей директории в контейнере
WORKDIR /bot
# копирование файла зависимостей в рабочую директорию
COPY requirements.txt .
# установка зависимостей
RUN pip install -r requirements.txt
# копирование содержимого локальной директории src в рабочую директорию
COPY src/ .
# команда, выполняемая при запуске контейнера
CMD [ "python", "./app.py" ]