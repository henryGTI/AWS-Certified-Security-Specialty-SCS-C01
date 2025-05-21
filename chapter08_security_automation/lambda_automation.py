import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    # 예시: S3 버킷 퍼블릭 차단 자동화
    bucket = event['detail']['requestParameters']['bucketName']
    s3.put_public_access_block(
        Bucket=bucket,
        PublicAccessBlockConfiguration={
            'BlockPublicAcls': True,
            'IgnorePublicAcls': True,
            'BlockPublicPolicy': True,
            'RestrictPublicBuckets': True
        }
    )
    return "퍼블릭 차단 완료"
