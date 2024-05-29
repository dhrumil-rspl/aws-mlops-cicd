#!/bin/bash

set -e

# Update packages and install nginx
sudo apt-get update -y
sudo apt-get install -y nginx

# Start nginx service
sudo service nginx start

# Copy static files to nginx html directory
sudo cp -r static/* /var/www/html/

# Docker commands to pull the latest image and run the container
aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin <your ECR repository URI>
docker pull <your ECR repository URI>:latest
docker stop mlops-project || true
docker rm mlops-project || true
docker run -d --name mlops-project -p 80:5000 <your ECR repository URI>:latest
