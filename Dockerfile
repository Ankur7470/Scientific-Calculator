# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the Python files into the container
COPY calculator.py /app/calculator.py
COPY test.py /app/test.py

# Set the default command to run the calculator
CMD ["python", "calculator.py"]
