# Base Image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy the app file into container
COPY app.py .

# Install Flask
RUN pip install flask

# Command to run app
CMD ["python", "app.py"]
