import boto3

ec2 = boto3.client('ec2')
# VPC Flow Logs 목록 조회
response = ec2.describe_flow_logs()
for flowlog in response['FlowLogs']:
    print(flowlog['FlowLogId'], flowlog['LogGroupName'])
