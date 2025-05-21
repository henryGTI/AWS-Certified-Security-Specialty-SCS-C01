# Chapter 08. Security Automation

AWS에서 보안 작업을 자동화하는 방법과 실습 예시를 다룹니다.

---

## 1. 보안 자동화 개요

- 이벤트 기반 자동화(CloudWatch Events, EventBridge, Lambda)
- 반복 작업 자동화(IaC, 배포 자동화, 키 회전 등)

---

## 2. Lambda를 활용한 자동화 예시

**`lambda_automation.py`**
```python
import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    # 예시: S3 버킷 퍼블릭 차단 자동화
    bucket = event['detail']['requestParameters']['bucketName']
    s3.put_public_access_block(
        Bucket=bucket,
        PublicAccessBlockConfiguration={
            'BlockPublicAcls': True,
            'IgnorePublicAcls': True,
            'BlockPublicPolicy': True,
            'RestrictPublicBuckets': True
        }
    )
    return "퍼블릭 차단 완료"
```

---

## 3. EventBridge로 보안 이벤트 자동 대응

**`eventbridge_example.py`**
```python
# EventBridge 규칙은 콘솔/CLI에서 생성, Lambda와 연동
# 예시: S3 퍼블릭 변경 이벤트 발생 시 Lambda 자동 실행
```

---

## 4. 실무 팁

- **자동화는 반드시 테스트 후 운영 환경에 적용**
- **모든 자동화 작업은 CloudTrail로 로깅**
- **자동화 실패 시 알림 체계 구축(SNS, Slack 등)**

---

## 5. 참고 자료

- [AWS Lambda 공식 문서](https://docs.aws.amazon.com/ko_kr/lambda/latest/dg/welcome.html)
- [AWS EventBridge 공식 문서](https://docs.aws.amazon.com/ko_kr/eventbridge/latest/userguide/what-is-amazon-eventbridge.html)

---

## 6. 복습 문제

1. Lambda와 EventBridge를 활용한 보안 자동화 예시는?
2. 자동화 작업의 실패/오류를 어떻게 감지하고 대응할 수 있는가?

---
