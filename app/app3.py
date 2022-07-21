import json
import csv
import boto3
import os
from datetime import datetime, timezone, timedelta

s3 = boto3.client('s3')

def lambda_handler(event, context):
    
    print("Lambdaが呼ばれたよ！！！！！！")
    print(json.dumps(event)) 
    print('event: {}'.format(event))
    print('context: {}'.format(context))
    
    print("bucket_name:" + event['Records'][0]['s3']['bucket']['name'])
    print("object_name:" + event['Records'][0]['s3']['object']['key'])
    
    json_data = []

    # TZを日本に変更
    JST = timezone(timedelta(hours=+9), 'JST')
    timestamp = datetime.now(JST).strftime('%Y%m%d%H%M%S')

    # 一時的な読み書き用ファイル（後で消す）
    tmp_csv = '/tmp/test_{ts}.csv'.format(ts=timestamp)
    tmp_json = '/tmp/test_{ts}.json'.format(ts=timestamp)

    # 最終的な出力ファイル
    outputted_json = 'output/test_{ts}.json'.format(ts=timestamp)

    for record in event['Records']:
        bucket_name = record['s3']['bucket']['name']
        key_name = record['s3']['object']['key']

    s3_object = s3.get_object(Bucket=bucket_name, Key=key_name)
    data = s3_object['Body'].read()
    contents = data.decode('utf-8')