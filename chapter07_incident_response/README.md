# Chapter 07. Incident Response

AWS 환경에서 보안 사고 발생 시 대응 절차와 자동화 방법을 다룹니다.

---

## 1. 사고 대응 프로세스

- **탐지(Detect)** → **분석(Analyze)** → **대응(Respond)** → **복구(Recover)**
- CloudTrail, GuardDuty, Security Hub 등으로 이상 징후 탐지

---

## 2. 사고 대응 자동화 실습

**`lambda_auto_response.py`**
```python
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
```

---

## 3. 실무 팁

- **사고 대응 Runbook**을 미리 작성하고, 정기적으로 모의 훈련
- **CloudWatch Events, Lambda**로 자동화된 대응 체계 구축
- **사고 발생 시 로그, 스냅샷 등 증거 보존**

---

## 4. 참고 자료

- [AWS Incident Response 공식 문서](https://docs.aws.amazon.com/ko_kr/whitepapers/latest/aws-security-incident-response-guide/welcome.html)
- [AWS Lambda 공식 문서](https://docs.aws.amazon.com/ko_kr/lambda/latest/dg/welcome.html)

---

## 5. 복습 문제

1. 사고 대응 프로세스의 4단계는?
2. Lambda를 활용한 자동화 대응 예시는?
3. 사고 발생 시 증거 보존의 중요성은?

---
