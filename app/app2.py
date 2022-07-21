def lambda_handler(event, context):
    print("Lambdaが呼ばれたよ！！！！！！")
    input_bucket = event['Records'][0]['s3']['bucket']['name']
    input_key = event['Records'][0]['s3']['object']['key']
    print("bucket =", input_bucket)
    print("key =", input_key)