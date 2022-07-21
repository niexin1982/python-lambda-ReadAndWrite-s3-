# AWS　LambdaのPythonでS3の操作入門　　　

## 固定のS3オブジェクトを取得する
AWS LambdaのPythonで決まりのS3バケットからオブジェクトを取得するの一番シンプルなサンプルです。   

app1.py
```
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
```

以下のウエブページを参考して、Lambdaの構築方法を理解する。    
https://dev.classmethod.jp/articles/get-s3-object-with-python-in-lambda/   
---- 
## S3へのファイル投入のトリガーイベントでLambda起動
トリガーイベントでLambdaを起動し、S3にアップロードファイルの情報を取得する。    
app2.py
```
def lambda_handler(event, context):
    print("Lambdaが呼ばれたよ！！！！！！")
    input_bucket = event['Records'][0]['s3']['bucket']['name']
    input_key = event['Records'][0]['s3']['object']['key']
    print("bucket =", input_bucket)
    print("key =", input_key)
```

以下のウエブページを参考して、Lambdaのトリガーイベントを理解する。   
※該当ページ内容を少し古かったので、最新のマニュアルをご参考ください。   
https://dev.classmethod.jp/articles/lambda-my-first-step/    

## S3にアップロードされたCSVファイルをAWS LambdaでJSONファイルに変換する

app3.py
```
import json
import csv
import boto3
import os
from datetime import datetime, timezone, timedelta

s3 = boto3.client('s3')

def lambda_handler(event, context):
    
    print("Lambdaが呼ばれたよ！！！！！！")
    print(json.dumps(event))   #event内容をわかりやすくになるために、event内容をlogに出力する。
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
```

eventのサンプル
```
{
    "Records": [
        {
            "eventVersion": "2.1",
            "eventSource": "aws:s3",
            "awsRegion": "ap-northeast-1",
            "eventTime": "2022-07-21T07:37:07.456Z",
            "eventName": "ObjectCreated:Put",
            "userIdentity": {
                "principalId": "AWS:AIDAUH5FHYL7RDNTLUGP7"
            },
            "requestParameters": {
                "sourceIPAddress": "121.111.247.108"
            },
            "responseElements": {
                "x-amz-request-id": "MYPZJ0MQCJHH42X6",
                "x-amz-id-2": "0GivdGXTu/ARJQfw7yiQKy+svIpA5XZkLXarC1q1Xt2NzfvzGpohywGW0+HKeuDGwAo47ypOwPQ/oWwGEZHGn1dQMWPfEH5MJo3cJ2U29M4="
            },
            "s3": {
                "s3SchemaVersion": "1.0",
                "configurationId": "518d06a5-2446-4f28-8288-45ffe6e2b71b",
                "bucket": {
                    "name": "testforcsvupload",
                    "ownerIdentity": {
                        "principalId": "AWV8ORBZFH2RI"
                    },
                    "arn": "arn:aws:s3:::testforcsvupload"
                },
                "object": {
                    "key": "test2/test.csv",
                    "size": 74,
                    "eTag": "f4441d21f6371f2be8e1cf5f145de0ba",
                    "sequencer": "0062D9022369C475DC"
                }
            }
        }
    ]
}

```

以下のウエブページを参考して、Lambdaでcsvファイルの読取、JSONファイルへの書込みを理解する。  
※該当ページ内容を少し古かったので、最新のマニュアルをご参考ください。   
https://dev.classmethod.jp/articles/lambda-my-first-step/