# Use an official Python runtime as a parent image
# python:3.9-slim-buster is a good choice for smaller image size
FROM python:3.9-slim-buster

# Set the working directory in the container to /app
# All subsequent commands will run from this directory
WORKDIR /app

# Copy the Python web server script into the container at /app
# The 'hello_server.py' here should match the name of your Python file.
COPY hello.py .

# Expose the port that the application will listen on
# This informs Docker that the container will listen on port 8000 at runtime
EXPOSE 8000

# Define the command to run the application when the container starts
# This command executes your Python web server script
CMD ["python", "hello.py"]
