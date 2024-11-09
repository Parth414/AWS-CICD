import boto3
from PIL import Image
import io

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    # Extract S3 bucket and key from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    # Get the image from S3
    image_obj = s3_client.get_object(Bucket=bucket, Key=key)
    image_data = image_obj['Body'].read()

    # Open image and resize
    image = Image.open(io.BytesIO(image_data))
    image = image.resize((100, 100))  # Example resize to 100x100

    # Save the resized image back to S3
    resized_key = f"resized/{key}"
    resized_image_data = io.BytesIO()
    image.save(resized_image_data, format='PNG')
    resized_image_data.seek(0)

    s3_client.put_object(Body=resized_image_data, Bucket=bucket, Key=resized_key)

    return {
        'statusCode': 200,
        'body': f"Resized image saved to {resized_key}"
    }
