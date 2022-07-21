import boto3

# localに保存するファイルパス
LocalFilePath = r'C:\Users\niexin\workspace\python-lambda-write-s3\app\data\local.csv'
#S3の保存先バケット名
DEST_BUCKET_NAME = "testforcsvupload" 
#バケット内のファイルパス
DEST_OBJECT_KEY_NAME = "test1/local.csv" 

#元データの指定とアップロード先を指定してアップロード
s3 = boto3.resource('s3')
s3.meta.client.upload_file(LocalFilePath, DEST_BUCKET_NAME, DEST_OBJECT_KEY_NAME) 