# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the Python script to the working directory
COPY samba.py .
# Define the command to run the Python script
CMD ["python", "samba.py"]
