import boto3

ec2 = boto3.client('ec2')

# Security Group 생성
response = ec2.create_security_group(
    GroupName='my-sec-group',
    Description='My security group',
    VpcId='vpc-xxxxxxxx'
)
sg_id = response['GroupId']

# 인바운드 규칙 추가 (예: 22번 포트 SSH 허용)
ec2.authorize_security_group_ingress(
    GroupId=sg_id,
    IpPermissions=[
        {
            'IpProtocol': 'tcp',
            'FromPort': 22,
            'ToPort': 22,
            'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
        }
    ]
)
