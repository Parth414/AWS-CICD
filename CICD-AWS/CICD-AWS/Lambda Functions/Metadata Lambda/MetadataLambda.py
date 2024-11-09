import boto3
import json
from PIL import Image
import io
import logging

# Initialize clients
s3_client = boto3.client('s3')
dynamodb_client = boto3.client('dynamodb')

# Set up logging
logging.basicConfig(level=logging.INFO)

def lambda_handler(event, context):
    try:
        # Extract the S3 bucket and key from the event
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']
        logging.info(f"Processing metadata for image in bucket {bucket}, key {key}")

        # Get the image from S3
        image_obj = s3_client.get_object(Bucket=bucket, Key=key)
        image_data = image_obj['Body'].read()

        # Open the image to get its metadata
        image = Image.open(io.BytesIO(image_data))
        width, height = image.size
        file_type = image.format

        # Store metadata in DynamoDB
        table_name = 'ImageMetadata'
        metadata = {
            'image_id': {'S': key},
            'width': {'N': str(width)},
            'height': {'N': str(height)},
            'file_type': {'S': file_type}
        }

        dynamodb_client.put_item(TableName=table_name, Item=metadata)

        logging.info(f"Metadata stored in DynamoDB for image {key}")

        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': f"Metadata stored for image {key}",
                'image_id': key,
                'width': width,
                'height': height,
                'file_type': file_type
            })
        }

    except Exception as e:
        logging.error(f"Error processing metadata: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': f"Error processing metadata: {str(e)}"
            })
        }
