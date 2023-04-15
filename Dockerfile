# Use an official Python runtime as a base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the script to the working directory
COPY script.py /app/script.py

# Install OpenCV and other dependencies
RUN pip install opencv-python-headless numpy

# Set the entry point to the script
ENTRYPOINT ["python", "/app/script.py"]