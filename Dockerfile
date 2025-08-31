# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file into the container
COPY requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application and test files into the container
COPY app.py ./
COPY test_app.py ./

# Expose port 5000 for the Flask app
EXPOSE 5000

# Run the Pytest tests
CMD ["pytest", "test_app.py"]

# To run the Flask application, use this command instead of the above one:
# CMD ["python", "app.py"]