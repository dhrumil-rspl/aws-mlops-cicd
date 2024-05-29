# MLOps Project

This repository contains an example MLOps pipeline using AWS CodePipeline, CodeBuild, and GitHub.

## Project Structure

- `Dockerfile`: Dockerfile to create the training environment.
- `app.py`: Simple Flask application to serve the dataset.
- `buildspec.yml`: AWS CodeBuild build specification file.
- `ml_script.py`: Script for training the machine learning model.
- `requirements.txt`: Python dependencies.
- `static/index.html`: Static HTML file to display the dataset.
- `datasets/dataset.csv`: Example dataset.

## Instructions

1. Set up AWS CodePipeline and CodeBuild as described in the project documentation.
2. Push any changes to the `datasets/dataset.csv` file to trigger the pipeline.
3. The trained model will be uploaded to S3, and the new Docker image will be deployed to an EC2 instance.
