# Dockerfile

# Base image: Python 3.9 slim version
# This image contains Python 3.9 and is a smaller version of the official Python image,
# making it more efficient for container usage where minimal dependencies are needed.
FROM python:3.9-slim

# Set the working directory inside the container
# This command sets the current working directory to '/app'.
# Any subsequent commands (COPY, RUN, etc.) will be executed relative to this directory.
WORKDIR /app

# Copy the Python script to the container's working directory
# This command copies the 'app.py' file from the host machine's directory
# into the '/app' directory inside the container.
COPY app.py /app/

# Install dependencies listed in the 'requirements.txt' file
# This command runs pip to install the Python dependencies inside the container,
# using the '-r' flag to install the packages listed in 'requirements.txt'.
# '--no-cache-dir' ensures that pip doesn't store downloaded package files, keeping the image smaller.
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the Python script when the container starts
# This specifies the default command that will run when the container is started.
# It tells the container to run the Python interpreter with 'app.py' as the argument.
CMD ["python", "app.py"]
