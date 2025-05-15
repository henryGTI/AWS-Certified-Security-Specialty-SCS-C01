import boto3

s3 = boto3.client('s3')
s3.upload_file(
    'local_file.txt',           # EC2에 있는 파일
    'my-bucket',                # S3 버킷 이름
    'uploaded_file.txt',        # S3에 저장될 이름
    ExtraArgs={'ServerSideEncryption': 'AES256'}  # 서버측 암호화
)
