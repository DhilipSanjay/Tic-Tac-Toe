FROM python:3.13.0a2-slim

WORKDIR /usr/src/app

COPY client/requirements.txt ./
RUN pip install -r requirements.txt 

COPY client/player.py .

COPY client/images/ ./images

CMD ["python", "./player.py", "172.17.0.1"]
