import boto3
import json

iam = boto3.client('iam')

policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:GetObject"],
            "Resource": "arn:aws:s3:::my-bucket/*"
        }
    ]
}

iam.put_user_policy(
    UserName='test-user',
    PolicyName='S3ReadOnly',
    PolicyDocument=json.dumps(policy)
)
