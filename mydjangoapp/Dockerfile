# Use the official Python image from the Docker Hub
FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /code

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY .. .

# Specify the command to run on container start
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "mydjangoapp.wsgi:application"]
