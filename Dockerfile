# Dockerfile
FROM python:3.9-slim

# Create the directory for logs
RUN mkdir -p /var/log

# Copy the Python script into the container
COPY time_logger.py /app/time_logger.py

# Set the working directory
WORKDIR /app

# Run the Python script
CMD ["python", "time_logger.py"]
