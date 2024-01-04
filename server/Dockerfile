# Use an official Python runtime as a base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the server script into the container at /usr/src/app
COPY server.py .

# Expose port 9999 for the server
EXPOSE 9999

# Run server.py when the container launches
CMD ["python", "./server.py"]
