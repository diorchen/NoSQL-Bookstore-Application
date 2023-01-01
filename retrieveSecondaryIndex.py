import boto3
 
dynamodb = boto3.client('dynamodb', region_name='us-west-1') 
resp = dynamodb.execute_statement(Statement='SELECT * FROM Books.CategoryIndex WHERE Category = \'Technology\'')
print(resp['Items'])