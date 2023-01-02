# Use an official Python runtime as a base image
FROM python:3.10-slim

# Set the working directory to /app
WORKDIR /app

# Create directory /app/data
RUN mkdir -p /app/data

# Copy Python modules from the current directory into the container at /app
COPY *.py /app

# Install any needed packages
RUN pip install pandas

# Run app.py when the container launches
CMD ["python", "word_counter.py"]