import boto3

ec2 = boto3.client('ec2')

# NACL 생성
response = ec2.create_network_acl(VpcId='vpc-xxxxxxxx')
nacl_id = response['NetworkAcl']['NetworkAclId']

# 인바운드 규칙 추가 (예: 80번 포트 HTTP 허용)
ec2.create_network_acl_entry(
    NetworkAclId=nacl_id,
    RuleNumber=100,
    Protocol='6',  # TCP
    RuleAction='allow',
    Egress=False,
    CidrBlock='0.0.0.0/0',
    PortRange={'From': 80, 'To': 80}
)
