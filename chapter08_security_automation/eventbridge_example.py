import boto3

def lambda_handler(event, context):
    # S3 버킷 이름 추출 (EventBridge 이벤트 구조에 따라 경로가 다를 수 있음)
    bucket_name = event['detail']['requestParameters']['bucketName']
    
    s3 = boto3.client('s3')
    
    # S3 버킷 퍼블릭 접근 차단
    s3.put_public_access_block(
        Bucket=bucket_name,
        PublicAccessBlockConfiguration={
            'BlockPublicAcls': True,
            'IgnorePublicAcls': True,
            'BlockPublicPolicy': True,
            'RestrictPublicBuckets': True
        }
    )
    print(f"{bucket_name} 버킷의 퍼블릭 접근이 차단되었습니다.")
    return {
        'statusCode': 200,
        'body': f"{bucket_name} 버킷의 퍼블릭 접근이 차단되었습니다."
    }
