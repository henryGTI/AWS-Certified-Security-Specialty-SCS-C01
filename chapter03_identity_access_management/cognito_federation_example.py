import boto3

cognito = boto3.client('cognito-idp')
# 사용자 풀 생성, 연동 등은 AWS 콘솔에서 주로 설정

# 예시: 사용자 풀 목록 조회
response = cognito.list_user_pools(MaxResults=10)
print(response)
