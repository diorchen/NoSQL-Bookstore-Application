import boto3

client = boto3.client('dynamodb', region_name='us-west-1')

try:
    resp = client.update_table(
        TableName="Books",
        # Declare primary key
        AttributeDefinitions=[
            {
                "AttributeName": "Category",
                "AttributeType": "S"
            },
        ],
        # Add, update, or delete any global secondary indexes on table.
        GlobalSecondaryIndexUpdates=[
            {
                "Create": {
                    "IndexName": "CategoryIndex",
                    "KeySchema": [
                        {
                            "AttributeName": "Category",
                            "KeyType": "HASH"
                        }
                    ],
                    "Projection": {
                        "ProjectionType": "ALL"
                    },
                    # Global secondary indexes read and write capacity separate from the underlying table.
                    "ProvisionedThroughput": {
                        "ReadCapacityUnits": 1,
                        "WriteCapacityUnits": 1,
                    }
                }
            }
        ],
    )
    print("Secondary index added successfully!")
except Exception as e:
    print("Error updating table:")
    print(e)