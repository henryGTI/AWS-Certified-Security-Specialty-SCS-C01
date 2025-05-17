# Chapter 02. Cloud Security Principles and Frameworks

클라우드 보안의 핵심 원칙과 AWS에서의 실무 적용 방법을 다룹니다.  
공유 책임 모델, Well-Architected Framework, 최소 권한 원칙, 컴플라이언스 등  
클라우드 환경에서 반드시 알아야 할 보안 프레임워크를 정리합니다.

---

## 1. 공유 책임 모델 (Shared Responsibility Model)

- **AWS**: 클라우드 인프라(물리, 네트워크, 하드웨어, 가상화 계층) 보안 책임
- **고객(사용자)**: 데이터, 애플리케이션, 네트워크 설정, IAM, 암호화, 접근제어 등 클라우드 내 보안 책임
- 책임 경계를 명확히 이해하고, 내 역할에 맞는 보안 조치를 반드시 수행해야 함

**자세한 요약:**  
[shared_responsibility.md](./shared_responsibility.md)

---

## 2. AWS Well-Architected Framework

- AWS에서 권장하는 5가지 핵심 Pillar(기둥)
  1. **보안(Security)**: 데이터 보호, 권한 최소화, 모니터링, 사고 대응
  2. **신뢰성(Reliability)**: 장애 복구, 자동 복구, 백업 전략
  3. **성능 효율성(Performance Efficiency)**: 적절한 리소스, 오토스케일링, 최신 기술 활용
  4. **비용 최적화(Cost Optimization)**: 불필요한 리소스 제거, 비용 분석
  5. **운영 우수성(Operational Excellence)**: 자동화, 모니터링, 반복적 개선

**자세한 요약 및 실사용 경험:**  
[well_architected_framework.md](./well_architected_framework.md)

---

## 3. 컴플라이언스와 감사

- **AWS Artifact**: 규정 준수 관련 문서(감사 리포트 등) 제공
- **AWS Compliance Program**: ISO, SOC, PCI 등 다양한 국제 표준 준수
- **CloudTrail**: 모든 API 호출을 기록하여 감사 및 추적 가능

---

## 4. 최소 권한 원칙 실습

**`iam_policy_minimum.py`**
```python
import boto3
import json

iam = boto3.client('iam')

policy_document = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetObject", "s3:PutObject"],
            "Resource": [
                "arn:aws:s3:::my-bucket",
                "arn:aws:s3:::my-bucket/*"
            ]
        }
    ]
}

response = iam.create_policy(
    PolicyName='S3AccessOnlyMyBucket',
    PolicyDocument=json.dumps(policy_document)
)
print(response)
```
- 특정 S3 버킷에만 접근 가능한 최소 권한 정책 예시

---

## 5. S3 데이터 암호화 실습

**`chapter06_data_protection/s3_encryption_example.py`**  
(챕터6과 연계)

```python
import boto3

s3 = boto3.client('s3')
s3.upload_file(
    'local_file.txt',
    'my-bucket',
    'uploaded_file.txt',
    ExtraArgs={'ServerSideEncryption': 'AES256'}
)
```
- S3에 업로드되는 파일을 서버 측에서 자동으로 암호화

---

## 6. CloudTrail로 감사 활성화

**`chapter01_security_fundamentals/cloudtrail_setup.py`**  
(1장과 연계)

```python
import boto3

cloudtrail = boto3.client('cloudtrail')
cloudtrail.create_trail(
    Name='my-trail',
    S3BucketName='my-cloudtrail-logs'
)
cloudtrail.start_logging(Name='my-trail')
```
- 모든 AWS API 호출을 S3에 기록

---

## 7. 실무 팁

- **공유 책임 모델**을 반드시 숙지하고, 내 책임 영역의 보안은 직접 챙길 것
- **Well-Architected Tool**을 활용해 내 환경을 정기적으로 진단하고 개선
- **IAM 최소 권한 정책**을 항상 적용하여 불필요한 권한 남용 방지
- **CloudTrail**을 통해 모든 작업을 로깅하고, 정기적으로 감사

---

## 8. 참고 자료

- [AWS Shared Responsibility Model 공식 문서](https://aws.amazon.com/ko/compliance/shared-responsibility-model/)
- [AWS Well-Architected Framework 공식 문서](https://docs.aws.amazon.com/ko_kr/wellarchitected/latest/framework/welcome.html)
- [AWS Artifact](https://aws.amazon.com/ko/artifact/)
- [AWS Security Best Practices](https://docs.aws.amazon.com/ko_kr/wellarchitected/latest/security-pillar/)

---

## 9. 복습 문제

1. 공유 책임 모델에서 AWS와 고객의 책임은 어떻게 구분되는가?
2. Well-Architected Framework의 5가지 Pillar를 설명하라.
3. IAM 최소 권한 정책을 적용하는 이유와 방법은?
4. CloudTrail을 활성화하면 얻을 수 있는 이점은?

---

더 궁금한 점이나 실습 코드가 필요하면 언제든 질문해 주세요!
