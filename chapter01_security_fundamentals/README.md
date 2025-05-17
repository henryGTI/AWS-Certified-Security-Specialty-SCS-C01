# Chapter 01. Security Fundamentals

AWS 보안의 기초 개념과 실무 적용 방법을 다룹니다.  
기본 이론, 주요 공격 유형, AWS에서의 실습 예시를 함께 정리합니다.

---

## 1. 보안의 3요소 (CIA Triad)

- **기밀성(Confidentiality)**: 허가된 사용자만 데이터에 접근 가능  
- **무결성(Integrity)**: 데이터가 변조되지 않고 정확하게 유지  
- **가용성(Availability)**: 필요할 때 언제든 접근 가능

---

## 2. 주요 보안 개념

- **취약점(Vulnerability)**: 시스템의 약점(예: 패치되지 않은 소프트웨어)
- **위협(Threat)**: 취약점을 악용하려는 시도(예: 해커, 악성코드)
- **위험(Risk)**: 위협이 취약점을 통해 실제로 피해를 줄 가능성

---

## 3. 인증, 인가, 회계 (AAA)

- **인증(Authentication)**: 사용자가 누구인지 확인 (ex. AWS IAM 사용자, MFA)
- **인가(Authorization)**: 인증된 사용자가 무엇을 할 수 있는지 결정 (ex. IAM 정책)
- **회계(Accounting/Auditing)**: 사용자의 행동을 기록 (ex. CloudTrail)

---

## 4. 네트워크 보안 기초

- **OSI 7계층**: 물리, 데이터링크, 네트워크, 전송, 세션, 표현, 응용
- **TCP/IP 스택**: 네트워크 통신의 실제 구현

---

## 5. 주요 공격 유형

- **Reconnaissance(정찰)**: 정보 수집
- **Password Attacks(비밀번호 공격)**: brute force, dictionary
- **Eavesdropping(도청)**: 네트워크 트래픽 감청
- **IP Spoofing(위장)**, **Man-in-the-Middle(중간자 공격)**
- **DoS/DDoS(서비스 거부 공격)**
- **Malware(악성코드)**, **Phishing(피싱)**

---

## 6. AWS 실습 코드 예시

### 6.1 S3 파일 업로드 시 암호화 적용 (기밀성)

**`cia_example.py`**
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

---

### 6.2 S3 버킷 목록 조회 & CloudTrail로 기록 확인 (AAA)

**`aaa_example.py`**
```python
import boto3

s3 = boto3.client('s3')
response = s3.list_buckets()
print(response)
```

---

### 6.3 S3 버킷 퍼블릭 차단 (기밀성, 무결성 강화)

**`s3_public_block.py`**
```python
import boto3

s3 = boto3.client('s3')
s3.put_public_access_block(
    Bucket='my-bucket',
    PublicAccessBlockConfiguration={
        'BlockPublicAcls': True,
        'IgnorePublicAcls': True,
        'BlockPublicPolicy': True,
        'RestrictPublicBuckets': True
    }
)
```

---

### 6.4 CloudTrail 트레일 생성 및 시작 (로깅과 감사)

**`cloudtrail_setup.py`**
```python
import boto3

cloudtrail = boto3.client('cloudtrail')
cloudtrail.create_trail(
    Name='my-trail',
    S3BucketName='my-cloudtrail-logs'
)
cloudtrail.start_logging(Name='my-trail')
```

---

## 7. 실무 팁

- **IAM 역할을 EC2에 부여**하면 Access Key/Secret Key 없이 안전하게 AWS 리소스 접근 가능
- **CloudTrail**을 항상 활성화하여 모든 API 호출을 기록하고, 사고 발생 시 추적 가능
- **S3 버킷은 기본적으로 퍼블릭 차단**을 설정하여 데이터 유출 위험을 최소화

---

## 8. 참고 자료

- [AWS Security Best Practices](https://docs.aws.amazon.com/ko_kr/wellarchitected/latest/security-pillar/)
- [AWS CloudTrail 공식 문서](https://docs.aws.amazon.com/ko_kr/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)
- [AWS IAM 공식 문서](https://docs.aws.amazon.com/ko_kr/IAM/latest/UserGuide/introduction.html)

---

## 9. 복습 문제

1. 보안의 3요소(CIA Triad)는 무엇인가요?
2. AWS에서 인증, 인가, 회계(AAA)는 각각 어떤 서비스/기능과 연관되나요?
3. S3 버킷을 퍼블릭으로 열어두면 어떤 위험이 있나요? 이를 방지하는 방법은?
4. CloudTrail을 활성화하면 얻을 수 있는 이점은?

---

