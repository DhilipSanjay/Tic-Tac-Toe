FROM python:latest

WORKDIR /usr/src/app

COPY client/requirements.txt ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt 

COPY client/player.py .

COPY client/images/ ./images

CMD ["python", "./player.py", "172.17.0.1"]
