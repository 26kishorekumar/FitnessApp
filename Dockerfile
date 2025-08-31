# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Install system dependencies required by Tkinter and for running tests in a headless environment
# xvfb is a virtual framebuffer that allows GUI apps to run without a physical display
RUN apt-get update && apt-get install -y \
    tk-dev \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory.
# This step is placed here so it can be cached.
COPY requirements.txt .

# Install any needed packages specified in requirements.txt.
# This expensive step will only be re-run if requirements.txt changes.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory.
# This is the last step that will be rebuilt on every code change.
COPY . .

# The command to run tests will be provided by the GitHub Actions workflow.
# This keeps the image flexible for other uses (e.g., running the app).
