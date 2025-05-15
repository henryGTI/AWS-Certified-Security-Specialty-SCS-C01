import boto3

s3 = boto3.client('s3')
s3.upload_file(
    'local_file.txt',
    'my-bucket',
    'uploaded_file.txt',
    ExtraArgs={'ServerSideEncryption': 'AES256'}
)

# 코드 분석
# S3에 업로드되는 파일을 서버 측에서 자동으로 암호화
# 데이터 보호 원칙 실습
