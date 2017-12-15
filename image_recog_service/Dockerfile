# Use an official Python runtime as a parent image
FROM python:3.6.2

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Make port 7777 available to the world outside this container
EXPOSE 7777

# Install any needed packages specified in requirements.txt
RUN pip install -r /app/requirements.txt

# Define environment variable
ENV NAME World

# Run app when the container launches
CMD ["python3", "/app/__main__.py"]