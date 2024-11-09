import boto3

dynamodb = boto3.resource('dynamodb')

def create_table():
    table = dynamodb.create_table(
        TableName='ImageMetadata',
        KeySchema=[
            {
                'AttributeName': 'image_id',
                'KeyType': 'HASH'  # Partition key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'image_id',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    table.wait_until_exists()
    print(f"Table {table.table_name} created.")

# Example usage
create_table()
