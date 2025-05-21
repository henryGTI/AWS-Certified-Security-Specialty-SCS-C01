import boto3

logs = boto3.client('logs')
# 로그 그룹 목록 조회
response = logs.describe_log_groups()
for group in response['logGroups']:
    print(group['logGroupName'])
