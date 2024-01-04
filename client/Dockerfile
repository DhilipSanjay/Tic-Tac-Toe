# Use an official Python runtime as a base image
FROM python:3.8

# Set the working directory in the container
WORKDIR /usr/src/app

# Install Pygame
COPY requirements.txt ./
RUN pip install -r requirements.txt 

# Copy the player script into the container at /usr/src/app
COPY player.py .

# Copy the images directory if necessary
COPY images/ ./images

# Run player.py when the container launches
CMD ["python", "./player.py"]
