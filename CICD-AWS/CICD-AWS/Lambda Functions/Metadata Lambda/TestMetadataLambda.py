import pytest
from unittest.mock import patch
from metadata_lambda import lambda_handler

@patch('metadata_lambda.s3_client.get_object')
@patch('metadata_lambda.dynamodb_client.put_item')
def test_metadata_lambda(mock_put_item, mock_get_object):
    # Mock S3 response with a fake image
    mock_get_object.return_value = {
        'Body': b'fakeimagebytes'  # Placeholder for image bytes
    }

    # Mock DynamoDB response (we don't need a return value here)
    mock_put_item.return_value = {}

    event = {
        'Records': [{
            's3': {
                'bucket': {'name': 'test-bucket'},
                'object': {'key': 'test-image.jpg'}
            }
        }]
    }

    context = {}

    # Call the lambda function
    response = lambda_handler(event, context)

    # Assert that DynamoDB put was called
    mock_put_item.assert_called_once()

    # Check the Lambda response
    assert response['statusCode'] == 200
    assert 'Metadata stored' in response['body']
