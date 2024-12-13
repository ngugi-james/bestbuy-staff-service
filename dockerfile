# Use the official Python 3.11 slim image as the base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file first for dependency installation
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application code into the container
COPY . .

# Expose the service port (8080 in this case)
EXPOSE 8080

# Set the command to run the application
CMD ["python", "app/main.py"]
