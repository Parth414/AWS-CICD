import pytest
from resize_lambda import lambda_handler
from unittest.mock import patch

@patch('resize_lambda.s3_client.get_object')
@patch('resize_lambda.s3_client.put_object')
def test_resize_lambda(mock_put_object, mock_get_object):
    # Mock S3 response
    mock_get_object.return_value = {
        'Body': b'fakeimagebytes'  # This is just a placeholder for actual image bytes
    }
    
    mock_put_object.return_value = {}
    
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
    
    # Assert that S3 put was called (i.e., image was resized and saved)
    mock_put_object.assert_called_once()
    assert response['statusCode'] == 200
    assert 'Resized image saved' in response['body']
