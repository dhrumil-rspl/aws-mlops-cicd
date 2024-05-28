# Use a base image with a minimal Linux distribution
FROM ubuntu:latest

# Install necessary packages (e.g., Nginx, Python for handling data)
RUN apt-get update && apt-get install -y \
    nginx \
    python3 \
    python3-pip

# Set working directory
WORKDIR /app

# Copy static website files (HTML, CSS, JS) to the appropriate location
COPY static /var/www/html

# Copy data file to the application directory
COPY data/raw/data.csv /app/data.csv

# Expose port 80 for serving web traffic
EXPOSE 80

# Start Nginx server and keep the container running
CMD service nginx start && tail -f /dev/null
