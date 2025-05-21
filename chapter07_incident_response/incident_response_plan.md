# AWS Incident Response Plan (사고 대응 계획)

AWS 환경에서 보안 사고 발생 시 신속하고 체계적으로 대응하기 위한  
사고 대응 프로세스와 실무 적용 예시를 정리합니다.

---

## 1. 사고 대응 프로세스(Incident Response Process)

1. **탐지(Detect)**
   - 이상 징후, 경보, 로그 분석(CloudTrail, GuardDuty, Security Hub 등)
2. **분석(Analyze)**
   - 사고 범위, 영향, 원인 파악
   - 관련 로그, 스냅샷, 네트워크 트래픽 등 증거 수집
3. **대응(Respond)**
   - 악성 인스턴스 격리, 권한 회수, 네트워크 차단 등 즉각적 조치
   - 자동화된 Lambda, SSM, EventBridge 활용 가능
4. **복구(Recover)**
   - 정상 서비스 복구, 데이터 복원, 시스템 재배포
   - 보안 패치, 설정 개선 등 재발 방지 조치
5. **사후 분석(Post-Incident Review)**
   - 사고 보고서 작성, 원인 분석, 대응 프로세스 개선

---

## 2. AWS 사고 대응 실무 예시

### 2.1 탐지 및 경보

- **CloudTrail**: API 호출 기록, 이상 행위 탐지
- **GuardDuty**: 위협 인텔리전스 기반 자동 탐지
- **Security Hub**: 여러 보안 서비스 결과 통합

### 2.2 자동화된 대응 예시

**Lambda로 EC2 인스턴스 격리**
```python
import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    instance_id = event['detail']['instance-id']
    ec2.modify_instance_attribute(
        InstanceId=instance_id,
        Groups=['sg-격리용-보안그룹-ID']
    )
    return "격리 완료"
```

### 2.3 증거 보존

- 로그, 스냅샷, 네트워크 트래픽 등 사고 당시 증거를 S3 등에 안전하게 저장
- CloudTrail, VPC Flow Logs, CloudWatch Logs 등 활용

---

## 3. 사고 대응 Runbook(실행 절차서) 예시

1. **경보 발생 시 담당자에게 즉시 알림(SNS, Slack 등)**
2. **사고 인스턴스 격리 및 권한 회수**
3. **관련 로그, 스냅샷, 네트워크 트래픽 증거 수집**
4. **사고 원인 분석 및 영향 범위 파악**
5. **서비스 복구 및 재발 방지 조치**
6. **사고 보고서 작성 및 대응 프로세스 개선**

---

## 4. 실무 팁

- **사고 대응 Runbook을 미리 작성**하고, 정기적으로 모의 훈련 실시
- **자동화 도구(Lambda, SSM, EventBridge 등)와 연계**하여 신속 대응
- **모든 사고 대응 활동은 CloudTrail 등으로 로깅**하여 추후 감사 가능하게 유지

---

## 5. 참고 자료

- [AWS Incident Response 공식 문서](https://docs.aws.amazon.com/ko_kr/whitepapers/latest/aws-security-incident-response-guide/welcome.html)
- [AWS GuardDuty 공식 문서](https://docs.aws.amazon.com/ko_kr/guardduty/latest/ug/what-is-guardduty.html)
- [AWS Security Hub 공식 문서](https://docs.aws.amazon.com/ko_kr/securityhub/latest/userguide/what-is-securityhub.html)

---

## 6. 복습 문제

1. AWS 사고 대응 프로세스의 5단계는?
2. Lambda를 활용한 자동화 대응 예시는?
3. 사고 발생 시 증거 보존의 중요성은?
4. 사고 대응 Runbook의 필요성과 주요 항목은?

---
