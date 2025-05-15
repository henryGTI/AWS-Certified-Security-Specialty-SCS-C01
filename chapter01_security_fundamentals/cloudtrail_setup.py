import boto3

cloudtrail = boto3.client('cloudtrail')
cloudtrail.create_trail(
    Name='my-trail',
    S3BucketName='my-cloudtrail-logs'
)
cloudtrail.start_logging(Name='my-trail')

# 코드 분석
# CloudTrail 트레일을 생성하고, S3에 로그를 저장
# 이후 모든 AWS API 호출이 기록됨
