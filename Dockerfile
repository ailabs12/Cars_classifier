# Use an official Python runtime as a parent image
FROM python:3.6.5-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

RUN pip install --upgrade pip

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

RUN apt-get update
RUN apt-get install -y --no-install-recommends \
libsm6 libxrender1 libfontconfig1 libice6 \
libglib2.0-0 libxext6 libgl1-mesa-glx

COPY boot.sh ./
RUN chmod +x boot.sh

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV FLASK_APP routes.py

# Run app.py when the container launches
# CMD ["python", "routes.py"]
CMD ["/bin/bash", "./boot.sh"]
