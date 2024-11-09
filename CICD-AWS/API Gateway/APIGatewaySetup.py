import boto3

api_client = boto3.client('apigateway')

def create_api():
    response = api_client.create_rest_api(
        name='ImageProcessingAPI',
        description='API for image processing via Lambda',
        endpointConfiguration={'types': ['REGIONAL']}
    )
    api_id = response['id']
    print(f"API created with ID: {api_id}")
    return api_id

# Example usage
create_api()
