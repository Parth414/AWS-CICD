# AWS Lambda CI/CD Project

## Overview
This project demonstrates the implementation of a fully automated CI/CD pipeline using AWS Lambda functions, AWS CodePipeline, and AWS SDK for Python (Boto3). The solution is designed to showcase how to build, test, deploy, and update AWS Lambda functions using a CI/CD pipeline, making use of AWS services like Lambda, S3, DynamoDB, and API Gateway.

## Key Features
Lambda Functions: Two AWS Lambda functions are implemented — one for image metadata extraction (metadata_lambda.py) and another for resizing images (resize_lambda.py).
CI/CD Pipeline: The project includes an automated CI/CD pipeline using AWS CodePipeline, which builds, tests, and deploys Lambda functions whenever changes are made to the repository.
Automated Testing: The Lambda functions include unit tests written in Python using the pytest framework, ensuring the functions are correctly processing data before deployment.

## How the CI/CD Pipeline Works
### 1. Lambda Functions
resize_lambda.py: This function resizes an image uploaded to an S3 bucket. The image’s new size is logged, and the resized image is saved to another S3 bucket.
metadata_lambda.py: This function extracts metadata (such as dimensions and file type) from an image uploaded to an S3 bucket and stores this information in a DynamoDB table.
### 2. Automated Testing
Both Lambda functions have corresponding test files:

test_resize_lambda.py: This file contains unit tests for the resize_lambda.py function using the pytest framework and mocks AWS services like S3.
test_metadata_lambda.py: This file contains unit tests for the metadata_lambda.py function, also using pytest and mocking S3 and DynamoDB services.

### 3. CI/CD Pipeline with AWS CodePipeline
The CI/CD pipeline is defined using a YAML file (codepipeline.yml). This pipeline automates the following tasks:

Install Dependencies: During the pipeline's install phase, Python dependencies are installed from requirements.txt files in each Lambda function directory.
Build: The pipeline then packages both Lambda functions into .zip files for deployment.
Post-Build/Deployment: The pipeline deploys the Lambda functions to AWS using the aws lambda update-function-code command.

### 4. CloudFormation
The cloudformation.yaml file defines the infrastructure resources for the project. This includes the creation of:

S3 Buckets: For image storage.
DynamoDB Table: To store metadata about the images.
Lambda Functions: For image resizing and metadata extraction.
API Gateway: (Optional, if implementing an API).

### 5. Supporting Scripts
s3_setup.py: A Python script to automate the creation of the necessary S3 buckets for storing images.
dynamodb_setup.py: A Python script to automate the creation of the DynamoDB table where image metadata will be stored.
api_gateway_setup.py: A Python script to configure the API Gateway, if you plan to invoke the Lambda functions via HTTP endpoints.

## Detailed Explanation of Files
### 1. lambda_functions/resize_lambda/resize_lambda.py
This Lambda function resizes an uploaded image. It listens for S3 events and resizes the image, saving it to another bucket.

resize_lambda.py: Main logic for image resizing.
requirements.txt: Lists the Python dependencies for this Lambda (e.g., Pillow for image processing).
test_resize_lambda.py: Unit tests for the resizing functionality.
### 2. lambda_functions/metadata_lambda/metadata_lambda.py
This Lambda function extracts metadata from an uploaded image (like width, height, and file type) and stores it in DynamoDB.

metadata_lambda.py: Main logic for image metadata extraction.
requirements.txt: Lists the Python dependencies for this Lambda.
test_metadata_lambda.py: Unit tests for the metadata extraction functionality.
### 3. cloudformation.yaml
Defines the AWS infrastructure, including S3 buckets, Lambda functions, DynamoDB table, and API Gateway (if used).

### 4. codepipeline.yml
Defines the stages of the CI/CD pipeline:

Install: Install dependencies for the Lambda functions.
Build: Package the Lambda functions into .zip files.
Post-Build: Deploy the packaged Lambda functions to AWS.
### 5. s3_setup.py
Sets up S3 buckets using Boto3. This is necessary for storing the images that trigger the Lambda functions.

### 6. dynamodb_setup.py
Sets up the DynamoDB table using Boto3. This table stores the metadata of images processed by the Lambda functions.

### 7. api_gateway_setup.py
(Optional) This script sets up API Gateway if you wish to expose your Lambda functions as HTTP endpoints.

## Getting Started
### Prerequisites
AWS Account: Ensure you have an active AWS account and the necessary permissions to create Lambda functions, S3 buckets, DynamoDB tables, and API Gateway (if needed).
Python 3.x: The Lambda functions are written in Python. Make sure you have Python 3.x installed.
AWS CLI: Install and configure the AWS CLI with your credentials.
### Steps

#### 1. Clone the Repository

Clone this repository to your local machine:

git clone https://github.com/Parth414/AWS-CICD.git
cd AWS-CICD

#### 2. Set Up AWS Resources

Use the cloudformation.yaml file to provision the necessary AWS resources. You can either use the AWS Management Console or deploy using the AWS CLI:

aws cloudformation create-stack --stack-name aws-cicd-stack --template-body file://cloudformation.yaml

#### 3. Set Up S3 Buckets and DynamoDB Table

Run the s3_setup.py and dynamodb_setup.py scripts to create the S3 buckets and DynamoDB table:

python s3_setup.py
python dynamodb_setup.py

#### 4. Configure API Gateway (Optional)

If you're using API Gateway to invoke the Lambda functions, run the api_gateway_setup.py script.

#### 5. Deploy with CodePipeline

Set up your CodePipeline using the codepipeline.yml file. The pipeline will automatically build, test, and deploy the Lambda functions.


## Conclusion
This project demonstrates how to implement a complete CI/CD pipeline using AWS Lambda and AWS CodePipeline, leveraging tools like CloudFormation for infrastructure provisioning, S3 for image storage, and DynamoDB for metadata storage. The pipeline automates testing and deployment, ensuring continuous integration and delivery of AWS Lambda-based applications.
