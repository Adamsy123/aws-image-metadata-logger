import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ImageMetadata')

def lambda_handler(event, context):

    record = event['Records'][0]
    bucket = record['s3']['bucket']['name']
    key = record['s3']['object']['key']
    size = record['s3']['object']['size']

    image_id = str(uuid.uuid4())

    table.put_item(
        Item={
            'image_id': image_id,
            'file_name': key,
            'bucket': bucket,
            'file_size': size
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Metadata stored successfully')
    }