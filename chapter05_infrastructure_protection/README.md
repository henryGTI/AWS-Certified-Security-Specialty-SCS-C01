# Chapter 05. Infrastructure Protection

AWS 인프라(네트워크, 서버 등)의 보안 설계와 실무 적용 방법을 다룹니다.  
VPC, Security Group, NACL, WAF, Shield 등 네트워크 및 인프라 보호의 핵심 개념과 실습 예시를 정리합니다.

---

## 1. 네트워크 보안 기본 개념

- **VPC(Virtual Private Cloud)**: AWS 내에서 논리적으로 격리된 네트워크 공간
- **Subnet**: VPC 내에서 IP 대역을 분할한 네트워크
- **NAT Gateway**: 프라이빗 서브넷의 인스턴스가 인터넷에 접근할 수 있도록 중계
- **VPN/Direct Connect**: 온프레미스와 AWS 간의 안전한 연결

---

## 2. 접근 제어

- **Security Group**: 인스턴스 단위의 가상 방화벽(상태 저장)
- **NACL(Network ACL)**: 서브넷 단위의 트래픽 제어(상태 비저장)
- **VPC Endpoints**: AWS 서비스에 프라이빗 네트워크로 안전하게 접근

---

## 3. 인프라 보호 실습 코드

### 3.1 Security Group 생성 및 인바운드 규칙 추가

**`vpc_security_group.py`**
```python
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
```

---

### 3.2 NACL 생성 및 규칙 추가

**`nacl_example.py`**
```python
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
```

---

### 3.3 WAF & Shield

- **AWS WAF(Web Application Firewall)**: 웹 공격(SQLi, XSS 등) 방어
- **AWS Shield**: DDoS 공격 자동 방어(기본 제공)

**`waf_shield_example.py`**  
(실제 WAF/Shield 설정은 콘솔에서 주로 진행, boto3로도 일부 가능)

---

## 4. 실무 팁

- **Security Group은 인스턴스 단위, NACL은 서브넷 단위**로 적용됨을 기억
- **최소 권한 원칙**: 꼭 필요한 포트/대역만 허용
- **VPC Flow Logs**로 네트워크 트래픽을 모니터링하고 이상 징후 탐지
- **WAF/Shield**로 웹 공격 및 DDoS 방어를 자동화

---

## 5. 참고 자료

- [AWS VPC 공식 문서](https://docs.aws.amazon.com/ko_kr/vpc/latest/userguide/what-is-amazon-vpc.html)
- [AWS Security Group 공식 문서](https://docs.aws.amazon.com/ko_kr/vpc/latest/userguide/VPC_SecurityGroups.html)
- [AWS NACL 공식 문서](https://docs.aws.amazon.com/ko_kr/vpc/latest/userguide/vpc-network-acls.html)
- [AWS WAF 공식 문서](https://docs.aws.amazon.com/ko_kr/waf/latest/developerguide/what-is-aws-waf.html)
- [AWS Shield 공식 문서](https://docs.aws.amazon.com/ko_kr/waf/latest/ddos-ug/ddos-overview.html)

---

## 6. 복습 문제

1. Security Group과 NACL의 차이점은?
2. VPC Endpoints의 보안적 이점은?
3. WAF와 Shield의 역할과 차이점은?
4. VPC Flow Logs를 활용한 보안 모니터링 방법은?

---
