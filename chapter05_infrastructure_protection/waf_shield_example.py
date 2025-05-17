import boto3

# WAFv2 클라이언트 생성 (리전 주의: WAF는 us-east-1, global 등에서 동작)
waf = boto3.client('wafv2', region_name='us-east-1')

# 1. Web ACL 생성
response = waf.create_web_acl(
    Name='my-web-acl',
    Scope='REGIONAL',  # 'REGIONAL' for ALB, API Gateway, 'CLOUDFRONT' for CloudFront
    DefaultAction={'Allow': {}},
    Description='My sample WAF Web ACL',
    Rules=[
        {
            'Name': 'BlockSpecificIP',
            'Priority': 1,
            'Action': {'Block': {}},
            'Statement': {
                'IPSetReferenceStatement': {
                    'ARN': 'arn:aws:wafv2:us-east-1:123456789012:regional/ipset/my-ip-set/abcd1234-5678-90ab-cdef-EXAMPLE11111'
                }
            },
            'VisibilityConfig': {
                'SampledRequestsEnabled': True,
                'CloudWatchMetricsEnabled': True,
                'MetricName': 'BlockSpecificIP'
            }
        }
    ],
    VisibilityConfig={
        'SampledRequestsEnabled': True,
        'CloudWatchMetricsEnabled': True,
        'MetricName': 'myWebACL'
    }
)
print("Web ACL 생성 완료:", response['Summary']['ARN'])

# 2. (선택) IPSet 생성 예시
# 실제로는 먼저 IPSet을 만들어야 위의 ARN을 사용할 수 있습니다.
# 아래 코드는 참고용입니다.
ipset_response = waf.create_ip_set(
    Name='my-ip-set',
    Scope='REGIONAL',
    Description='Block this IP',
    IPAddressVersion='IPV4',
    Addresses=['1.2.3.4/32'],  # 차단할 IP
    Tags=[]
)
print("IPSet 생성 완료:", ipset_response['Summary']['ARN'])

# 3. Shield Advanced는 콘솔에서 활성화(구독) 후, 보호 대상 리소스(예: ALB, CloudFront 등)를 추가
print("AWS Shield Advanced는 콘솔에서 활성화 및 관리하세요.")
