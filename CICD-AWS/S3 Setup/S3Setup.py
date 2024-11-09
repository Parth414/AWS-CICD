import boto3

s3_client = boto3.client('s3')

def create_bucket(bucket_name):
    response = s3_client.create_bucket(Bucket=bucket_name)
    print(f"Bucket {bucket_name} created: {response}")

# Example usage
create_bucket('my-image-processing-bucket')
