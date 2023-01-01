import boto3

client = boto3.client('dynamodb', region_name='us-west-1') #choose client & region

try: 
    resp = client.create_table( 
    TableName="Books", 

# Declare primary key and schema
    KeySchema=[ 
    { 
    "AttributeName": "Author", 
    "KeyType": "HASH" 
    }, 
    { 
    "AttributeName": "Title", 
    "KeyType": "RANGE" 
    } 
    ],
# attributes declared in AttributeDefinitions 
    AttributeDefinitions=[ 
    { 
    "AttributeName": "Author", 
    "AttributeType": "S" 
    }, 
    { 
    "AttributeName": "Title", 
    "AttributeType": "S" 
    } 
    ],
# controls the amount of data read/write to DynamoDB per second. 

    ProvisionedThroughput={ 
    "ReadCapacityUnits": 1, 
    "WriteCapacityUnits": 1 
    } 
    ) 
    
    print("Table created successfully!")

except Exception as e: 
    print("Error creating table:") 
    print(e)