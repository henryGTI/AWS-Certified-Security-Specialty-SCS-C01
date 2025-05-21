# Chapter 09. Security Troubleshooting on AWS

AWS 환경에서 보안 문제를 진단하고 해결하는 방법을 다룹니다.

---

## 1. 문제 진단 도구

- **CloudTrail**: API 호출 추적
- **CloudWatch Logs**: 애플리케이션/시스템 로그 분석
- **VPC Flow Logs**: 네트워크 트래픽 분석
- **EventBridge**: 이벤트 기반 문제 감지

---

## 2. 실습 코드 예시

**`cloudwatch_logs_check.py`**
```python
import boto3

logs = boto3.client('logs')
# 로그 그룹 목록 조회
response = logs.describe_log_groups()
for group in response['logGroups']:
    print(group['logGroupName'])
```

**`vpc_flowlog_analysis.py`**
```python
import boto3

ec2 = boto3.client('ec2')
# VPC Flow Logs 목록 조회
response = ec2.describe_flow_logs()
for flowlog in response['FlowLogs']:
    print(flowlog['FlowLogId'], flowlog['LogGroupName'])
```

---

## 3. 실무 팁

- **CloudTrail, VPC Flow Logs, CloudWatch Logs**를 항상 활성화
- **문제 발생 시 로그를 먼저 확인**하고, 원인 분석 후 대응
- **네트워크 문제는 보안 그룹, NACL, 라우팅 테이블 등도 함께 점검**

---

## 4. 참고 자료

- [AWS CloudWatch 공식 문서](https://docs.aws.amazon.com/ko_kr/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html)
- [AWS VPC Flow Logs 공식 문서](https://docs.aws.amazon.com/ko_kr/vpc/latest/userguide/flow-logs.html)

---

## 5. 복습 문제

1. CloudTrail과 CloudWatch Logs의 차이점은?
2. VPC Flow Logs를 활용한 네트워크 문제 진단 방법은?
3. 보안 문제 발생 시 우선적으로 점검해야 할 항목은?

---
