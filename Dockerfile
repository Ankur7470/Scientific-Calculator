# # Use the official Python image as the base image
# FROM python:3.9-slim

# # Set the working directory
# WORKDIR /app

# # Copy the Python files into the container
# COPY calculator.py /app/calculator.py
# COPY test.py /app/test.py

# # Set the default command to run the calculator
# CMD ["python", "calculator.py"]

# Use a base image with CMake and GCC
FROM ubuntu:20.04

# Install dependencies
RUN apt-get update && \
    apt-get install -y cmake gcc build-essential

# Set the working directory
WORKDIR /app

# Copy the source code
COPY . .

# Build the application
RUN mkdir build && \
    cd build && \
    cmake .. && \
    make

# Set the default command to run the calculator
CMD ["./build/calculator"]
