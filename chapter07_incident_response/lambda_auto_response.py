import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    # 예시: 감염된 인스턴스 격리
    instance_id = event['detail']['instance-id']
    ec2.modify_instance_attribute(
        InstanceId=instance_id,
        Groups=['sg-격리용-보안그룹-ID']
    )
    return "격리 완료"
