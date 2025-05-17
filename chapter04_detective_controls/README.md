# Chapter 04. Detective Controls

AWS 환경에서 이상 징후 탐지, 감사, 모니터링을 위한 탐지 제어(Detective Controls)의 개념과 실습을 다룹니다.  
CloudTrail, Config, GuardDuty, Security Hub 등 다양한 탐지 서비스의 활용법을 정리합니다.

---

## 1. 탐지 제어(Detective Controls)란?

- **탐지 제어**란 시스템 내에서 발생하는 이벤트, 변경, 이상 행위를 실시간 또는 사후에 탐지하는 보안 통제
- AWS에서는 로그, 이벤트, 규정 준수 상태, 위협 탐지 등 다양한 방식으로 제공

---

## 2. 주요 서비스 및 실습 코드

### 2.1 AWS Config: 리소스 상태 및 변경 추적

**`config_rule_example.py`**
```python
import boto3

config = boto3.client('config')

# Config Recorder 활성화
config.put_configuration_recorder(
    ConfigurationRecorder={
        'name': 'default',
        'roleARN': 'arn:aws:iam::123456789012:role/aws-config-role'
    }
)
config.put_delivery_channel(
    DeliveryChannel={
        'name': 'default',
        's3BucketName': 'my-config-bucket'
    }
)
config.start_configuration_recorder(
    ConfigurationRecorderName='default'
)
```
- 리소스 변경 사항을 S3에 기록, 규정 준수 상태 추적

---

### 2.2 CloudTrail: API 호출 기록 및 감사

**`cloudtrail_event_check.py`**
```python
import boto3

cloudtrail = boto3.client('cloudtrail')

# 최근 이벤트 조회
events = cloudtrail.lookup_events(MaxResults=5)
for event in events['Events']:
    print(event['EventName'], event['Username'], event['EventTime'])
```
- 누가, 언제, 어떤 API를 호출했는지 추적 가능

---

### 2.3 GuardDuty: 위협 탐지

**`guardduty_example.py`**
```python
import boto3

gd = boto3.client('guardduty')

# GuardDuty 활성화(최초 1회)
response = gd.create_detector(Enable=True)
detector_id = response['DetectorId']
print("GuardDuty Detector ID:", detector_id)
```
- GuardDuty는 VPC Flow Logs, CloudTrail, DNS Logs를 분석해 위협을 자동 탐지

---

## 3. Security Hub, Inspector, Trusted Advisor

- **Security Hub**: 여러 보안 서비스의 결과를 통합하여 대시보드로 제공
- **Inspector**: EC2 인스턴스의 취약점 자동 진단
- **Trusted Advisor**: AWS 환경의 보안, 비용, 성능, 가용성 등 종합 점검

---

## 4. 실무 팁

- **CloudTrail, Config, GuardDuty, Security Hub**는 반드시 활성화하고, 정기적으로 모니터링
- **Config Rule**을 활용해 리소스가 규정에 맞게 운영되는지 자동 검사
- **이상 징후 탐지 시 SNS, Lambda 등으로 자동 알림/대응 연동 가능**

---

## 5. 참고 자료

- [AWS Config 공식 문서](https://docs.aws.amazon.com/ko_kr/config/latest/developerguide/WhatIsConfig.html)
- [AWS CloudTrail 공식 문서](https://docs.aws.amazon.com/ko_kr/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)
- [AWS GuardDuty 공식 문서](https://docs.aws.amazon.com/ko_kr/guardduty/latest/ug/what-is-guardduty.html)
- [AWS Security Hub 공식 문서](https://docs.aws.amazon.com/ko_kr/securityhub/latest/userguide/what-is-securityhub.html)

---

## 6. 복습 문제

1. AWS Config와 CloudTrail의 차이점은?
2. GuardDuty가 탐지하는 위협의 예시는?
3. Security Hub의 주요 기능은?
4. 탐지 제어를 실무에서 어떻게 자동화할 수 있는가?
