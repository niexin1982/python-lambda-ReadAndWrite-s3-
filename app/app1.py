import json

import boto3

# バケット名,オブジェクト名
BUCKET_NAME = 'testxxx'  #自分のs3のバケットに変更
OBJECT_KEY_NAME = 'hello.json'

s3 = boto3.resource('s3')


def lambda_handler(event, context):
    bucket = s3.Bucket(BUCKET_NAME)
    obj = bucket.Object(OBJECT_KEY_NAME)

    response = obj.get()    
    body = response['Body'].read()

    return json.loads(body.decode('utf-8'))