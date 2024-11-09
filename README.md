# AWS Lambda CI/CD Project

## Overview
This project demonstrates the implementation of a fully automated CI/CD pipeline using AWS Lambda functions, AWS CodePipeline, and AWS SDK for Python (Boto3). The solution is designed to showcase how to build, test, deploy, and update AWS Lambda functions using a CI/CD pipeline, making use of AWS services like Lambda, S3, DynamoDB, and API Gateway.

## Key Features
Lambda Functions: Two AWS Lambda functions are implemented — one for image metadata extraction (MetadataLambda.py) and another for resizing images (ResizeLambda.py).
CI/CD Pipeline: The project includes an automated CI/CD pipeline using AWS CodePipeline, which builds, tests, and deploys Lambda functions whenever changes are made to the repository.
Automated Testing: The Lambda functions include unit tests written in Python using the pytest framework, ensuring the functions are correctly processing data before deployment.

## How the CI/CD Pipeline Works
### 1. Lambda Functions
ResizeLambda.py: This function resizes an image uploaded to an S3 bucket. The image’s new size is logged, and the resized image is saved to another S3 bucket.
MetadataLambda.py: This function extracts metadata (such as dimensions and file type) from an image uploaded to an S3 bucket and stores this information in a DynamoDB table.
### 2. Automated Testing
Both Lambda functions have corresponding test files:

TestResizeLambda.py: This file contains unit tests for the ResizeLambda.py function using the pytest framework and mocks AWS services like S3.
TestMetadataLambda.py: This file contains unit tests for the MetadataLambda.py function, also using pytest and mocking S3 and DynamoDB services.

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
S3Setup.py: A Python script to automate the creation of the necessary S3 buckets for storing images.
DynamoDBSetup.py: A Python script to automate the creation of the DynamoDB table where image metadata will be stored.
APIGatewaySetup.py: A Python script to configure the API Gateway, if you plan to invoke the Lambda functions via HTTP endpoints.

## Detailed Explanation of Files
### 1. Lambda Functions/Resize Lambda/ResizeLambda.py
This Lambda function resizes an uploaded image. It listens for S3 events and resizes the image, saving it to another bucket.

ResizeLambda.py: Main logic for image resizing.
TestResizeLambda.py: Unit tests for the resizing functionality.

### 2. Lambda Functions/Metadata Lambda/MetadataLambda.py
This Lambda function extracts metadata from an uploaded image (like width, height, and file type) and stores it in DynamoDB.

MetadataLambda.py: Main logic for image metadata extraction.
TestMetadataLambda.py: Unit tests for the metadata extraction functionality.

### 3. CloudFormation.yaml
Defines the AWS infrastructure, including S3 buckets, Lambda functions, DynamoDB table, and API Gateway (if used).

### 4. CodePipeline.yml
Defines the stages of the CI/CD pipeline:

Install: Install dependencies for the Lambda functions.
Build: Package the Lambda functions into .zip files.
Post-Build: Deploy the packaged Lambda functions to AWS.

### 5. S3Setup.py
Sets up S3 buckets using Boto3. This is necessary for storing the images that trigger the Lambda functions.

### 6. DynamoDBSetup.py
Sets up the DynamoDB table using Boto3. This table stores the metadata of images processed by the Lambda functions.

### 7. APIGatewaySetup.py
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

Use the CloudFormation.yaml file to provision the necessary AWS resources. You can either use the AWS Management Console or deploy using the AWS CLI:

aws cloudformation create-stack --stack-name aws-cicd-stack --template-body file://CloudFormation.yaml

#### 3. Set Up S3 Buckets and DynamoDB Table

Run the S3Setup.py and DynamoDBSetup.py scripts to create the S3 buckets and DynamoDB table:

python S3Setup.py
python DynamoDBSetup.py

#### 4. Configure API Gateway (Optional)

If you're using API Gateway to invoke the Lambda functions, run the APIGatewaySetup.py script.

#### 5. Deploy with CodePipeline

Set up your CodePipeline using the codepipeline.yml file. The pipeline will automatically build, test, and deploy the Lambda functions.


## Conclusion
This project demonstrates how to implement a complete CI/CD pipeline using AWS Lambda and AWS CodePipeline, leveraging tools like CloudFormation for infrastructure provisioning, S3 for image storage, and DynamoDB for metadata storage. The pipeline automates testing and deployment, ensuring continuous integration and delivery of AWS Lambda-based applications.
