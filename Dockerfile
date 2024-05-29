# Dockerfile
FROM python:3.8-slim

# Install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the application code
COPY . /app
WORKDIR /app

# Command to run the application
CMD ["python", "app.py"]
