# AWS CloudHSM 실무 요약 및 활용 예시

AWS CloudHSM은 하드웨어 기반의 키 관리 및 암호화 연산을 제공하는  
클라우드 전용 HSM(Hardware Security Module) 서비스입니다.

---

## 1. CloudHSM이란?

- **HSM(Hardware Security Module)**:  
  암호화 키를 안전하게 생성, 저장, 관리, 사용하도록 설계된 하드웨어 장치
- **AWS CloudHSM**:  
  FIPS 140-2 Level 3 인증을 받은 HSM을 클라우드에서 온디맨드로 제공  
  사용자는 HSM 클러스터를 직접 소유/운영하며, 키에 대한 완전한 제어권을 가짐

---

## 2. CloudHSM 주요 특징

- **고성능 하드웨어 암호화**: 대칭/비대칭 암호화, 디지털 서명, 키 생성 등
- **완전한 키 소유권**: AWS도 키에 접근 불가(고객이 직접 관리)
- **FIPS 140-2 Level 3 인증**
- **VPC 내에 배치**: 네트워크 격리 및 보안 강화
- **PKCS#11, JCE, OpenSSL 등 표준 API 지원**

---

## 3. CloudHSM vs KMS

| 구분         | CloudHSM                        | KMS                        |
|--------------|---------------------------------|----------------------------|
| 키 소유권    | 고객 완전 소유                  | AWS가 관리, 고객 위임      |
| 사용 목적    | 고성능, 규제 준수, 커스텀 암호화 | 일반적 암호화, 통합 관리   |
| API          | PKCS#11, JCE, OpenSSL           | AWS SDK, KMS API           |
| 비용         | 시간당 과금(클러스터 단위)       | 사용량 기반 저렴           |

---

## 4. CloudHSM 실습 흐름

> **참고:** CloudHSM은 콘솔/CLI에서 클러스터 생성 후,  
> EC2 인스턴스에서 클라이언트 소프트웨어를 설치해 연동합니다.  
> (boto3로 직접 암호화 연산을 수행하지 않고, PKCS#11 등 라이브러리 사용)

### 1) CloudHSM 클러스터 생성 (콘솔/CLI)
- AWS 콘솔 → CloudHSM → 클러스터 생성 → VPC/서브넷 지정

### 2) 클러스터 활성화 및 HSM 인스턴스 프로비저닝
- 클러스터가 "Active" 상태가 되면 HSM 인스턴스 자동 생성

### 3) EC2에서 CloudHSM 클라이언트 설치 및 연결
```bash
# Amazon Linux 예시
sudo yum install -y aws-cloudhsm-client
sudo service cloudhsm-client start
```
- 클러스터 IP, 인증서 등으로 HSM에 연결

### 4) 키 생성 및 암호화 연산 (PKCS#11, OpenSSL 등)
```bash
# 예시: PKCS#11 라이브러리로 키 생성/암호화
# (자세한 코드는 AWS 공식 문서 참고)
```

---

## 5. 실무 활용 예시

- **고객 관리 키(CMK) 직접 운영**이 필요한 금융, 공공, 규제 산업
- **HSM 기반 SSL/TLS 오프로드, 디지털 서명, 커스텀 암호화**
- **BYOK(Bring Your Own Key)**: 외부에서 생성한 키를 HSM에 업로드

---

## 6. 참고 자료

- [AWS CloudHSM 공식 문서](https://docs.aws.amazon.com/ko_kr/cloudhsm/latest/userguide/what-is-cloudhsm.html)
- [CloudHSM 시작하기](https://docs.aws.amazon.com/ko_kr/cloudhsm/latest/userguide/getting-started.html)
- [CloudHSM vs KMS 비교](https://aws.amazon.com/ko/cloudhsm/faqs/)

---

## 7. 복습 문제

1. CloudHSM과 KMS의 차이점은?
2. CloudHSM을 사용해야 하는 대표적인 상황은?
3. CloudHSM에서 키를 생성/관리하는 방식은?

---

더 궁금한 점이나 실습 코드가 필요하면 언제든 질문해 주세요!
