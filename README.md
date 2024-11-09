# Header 1 (Largest)

# #AWS Lambda CI/CD Project
Overview
This project demonstrates the implementation of a fully automated CI/CD pipeline using AWS Lambda functions, AWS CodePipeline, and AWS SDK for Python (Boto3). The solution is designed to showcase how to build, test, deploy, and update AWS Lambda functions using a CI/CD pipeline, making use of AWS services like Lambda, S3, DynamoDB, and API Gateway.

Key Features
Lambda Functions: Two AWS Lambda functions are implemented — one for image metadata extraction (metadata_lambda.py) and another for resizing images (resize_lambda.py).
CI/CD Pipeline: The project includes an automated CI/CD pipeline using AWS CodePipeline, which builds, tests, and deploys Lambda functions whenever changes are made to the repository.
Automated Testing: The Lambda functions include unit tests written in Python using the pytest framework, ensuring the functions are correctly processing data before deployment.
