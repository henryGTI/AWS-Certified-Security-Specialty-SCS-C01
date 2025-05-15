import boto3

s3 = boto3.client('s3')
s3.put_public_access_block(
    Bucket='my-bucket',
    PublicAccessBlockConfiguration={
        'BlockPublicAcls': True,
        'IgnorePublicAcls': True,
        'BlockPublicPolicy': True,
        'RestrictPublicBuckets': True
    }
)

# 코드 분석
# S3 버킷의 퍼블릭 접근을 완전히 차단
# 실수로 공개되는 것을 방지하여 데이터 유출 위험 감소
