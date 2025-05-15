import boto3

s3 = boto3.client('s3')
response = s3.list_buckets()
print(response)

# 코드 분석
# EC2 인스턴스에 부여된 IAM 역할이 S3 읽기 권한을 가지고 있어야 함
# 이 API 호출은 CloudTrail에 자동으로 기록됨 (누가, 언제, 어떤 API를 호출했는지 추적 가능)
