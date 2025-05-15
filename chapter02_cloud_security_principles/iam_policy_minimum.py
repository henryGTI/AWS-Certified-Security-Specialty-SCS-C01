import boto3
import json

iam = boto3.client('iam')

# 정책 문서: 특정 S3 버킷에만 접근 허용
policy_document = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetObject", "s3:PutObject"],
            "Resource": [
                "arn:aws:s3:::my-bucket",
                "arn:aws:s3:::my-bucket/*"
            ]
        }
    ]
}

# 정책 생성
response = iam.create_policy(
    PolicyName='S3AccessOnlyMyBucket',
    PolicyDocument=json.dumps(policy_document)
)
print(response)

# 코드 분석
# "Action": S3 버킷 조회, 객체 업로드/다운로드만 허용
# "Resource": 특정 버킷과 그 안의 객체만 지정
# 최소 권한 원칙을 코드로 실습
