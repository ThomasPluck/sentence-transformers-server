# Use an official Python runtime as the base image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the local package files to the container
COPY . /app

# Install the required pip packages
RUN pip install --no-cache-dir bottle==0.12.25 sentence-transformers==2.2.2 cheroot==10.0.0

# Document that the application inside the container listens on port 9012
EXPOSE 9012

# Specify the command to run on container start
CMD ["python", "server.py", "--port", "9012", "--model", "intfloat/e5-small-v2"]
