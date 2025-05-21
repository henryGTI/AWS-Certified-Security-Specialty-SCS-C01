# Chapter 06. Data Protection

AWS에서 데이터 보호(암호화, 키 관리, 접근제어 등)의 원칙과 실무 적용 방법을 다룹니다.

---

## 1. 데이터 암호화

- **대칭키 암호화**: 하나의 키로 암호화/복호화 (예: AES)
- **비대칭키 암호화**: 공개키/개인키 쌍 사용 (예: RSA)
- **해시 알고리즘**: 데이터 무결성 검증 (예: SHA-256)

---

## 2. AWS Key Management Service (KMS)

- **KMS**: 암호화 키 생성, 저장, 관리, 회전, 감사 기능 제공
- **CloudHSM**: 하드웨어 기반 키 관리(고급 보안 요구 시)

---

## 3. S3, EBS, RDS 등 데이터 암호화 실습

**`s3_encryption_example.py`**
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

**`kms_encrypt_example.py`**
```python
import boto3

kms = boto3.client('kms')
response = kms.encrypt(
    KeyId='alias/my-key',
    Plaintext=b'Hello, World!'
)
print(response['CiphertextBlob'])
```

---

## 4. S3 버킷, RDS, EBS 암호화 옵션

- S3: 서버측 암호화(SSE-S3, SSE-KMS, SSE-C)
- EBS: 볼륨 생성 시 암호화 옵션 선택
- RDS: 인스턴스 생성 시 암호화 활성화

---

## 5. 실무 팁

- **KMS 키는 주기적으로 회전**하고, 접근 권한을 최소화
- **S3, EBS, RDS 등 모든 저장소는 암호화 기본 적용**
- **CloudTrail로 KMS 키 사용 이력 감사**

---

## 6. 참고 자료

- [AWS KMS 공식 문서](https://docs.aws.amazon.com/ko_kr/kms/latest/developerguide/overview.html)
- [AWS S3 암호화 공식 문서](https://docs.aws.amazon.com/ko_kr/AmazonS3/latest/userguide/serv-side-encryption.html)
- [AWS CloudHSM 공식 문서](https://docs.aws.amazon.com/ko_kr/cloudhsm/latest/userguide/what-is-cloudhsm.html)

---

## 7. 복습 문제

1. 대칭키와 비대칭키 암호화의 차이점은?
2. KMS와 CloudHSM의 차이점은?
3. S3, EBS, RDS에서 암호화를 적용하는 방법은?
4. KMS 키 관리 시 주의할 점은?

---
