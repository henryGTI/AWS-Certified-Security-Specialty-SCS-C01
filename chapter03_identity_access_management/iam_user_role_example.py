import boto3

iam = boto3.client('iam')

# 사용자 생성
iam.create_user(UserName='test-user')

# 역할 생성 예시
assume_role_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {"Service": "ec2.amazonaws.com"},
            "Action": "sts:AssumeRole"
        }
    ]
}
iam.create_role(
    RoleName='EC2S3ReadOnlyRole',
    AssumeRolePolicyDocument=json.dumps(assume_role_policy)
)
