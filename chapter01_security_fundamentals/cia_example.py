import boto3

s3 = boto3.client('s3')
s3.upload_file(
    'local_file.txt',           # EC2에 있는 파일
    'my-bucket',                # S3 버킷 이름
    'uploaded_file.txt',        # S3에 저장될 이름
    ExtraArgs={'ServerSideEncryption': 'AES256'}  # 서버측 암호화
)

코드 분석

ExtraArgs={'ServerSideEncryption': 'AES256'}: S3에 저장되는 파일을 자동으로 암호화(기밀성 보장)

EC2에서 실행 시, IAM 역할이 S3 접근 권한을 가지고 있어야 함
