# AWS Shared Responsibility Model (공유 책임 모델)

AWS Shared Responsibility Model(공유 책임 모델)은  
클라우드 환경에서 **AWS와 고객(사용자)**이 각각 어떤 보안 책임을 가지는지 명확하게 구분해주는 모델입니다.

---

## 1. 책임의 구분

### 1) AWS의 책임 (Security "of" the Cloud)
- **AWS가 클라우드 인프라 자체의 보안을 책임집니다.**
- 주요 항목:
  - 데이터 센터의 물리적 보안
  - 하드웨어, 소프트웨어, 네트워크, 가상화 계층의 보안
  - AWS 서비스(EC2, S3 등)의 운영 및 유지보수
  - 인프라의 가용성, 내결함성, 확장성

### 2) 고객(사용자)의 책임 (Security "in" the Cloud)
- **고객이 클라우드 내에서의 보안을 책임집니다.**
- 주요 항목:
  - 데이터 암호화 및 무결성 관리
  - 애플리케이션 보안, OS/미들웨어 패치
  - 네트워크 구성(VPC, 서브넷, 보안그룹 등)
  - IAM 사용자/권한 관리
  - S3 버킷 접근 정책, 데이터 백업 및 복구
  - 로깅 및 모니터링(CloudTrail, CloudWatch 등)

---

## 2. 예시

- **EC2 인스턴스**
  - AWS: 물리 서버, 하이퍼바이저, 네트워크 인프라 보안
  - 고객: OS 패치, 방화벽 설정, 애플리케이션 보안, 데이터 암호화

- **S3 버킷**
  - AWS: S3 서비스의 인프라 보안
  - 고객: 버킷 접근 정책, 데이터 암호화, 퍼블릭 접근 차단

---

## 3. 공식 문서 참고

- [AWS Shared Responsibility Model 공식 문서(한글)](https://aws.amazon.com/ko/compliance/shared-responsibility-model/)
- [AWS Security Best Practices](https://docs.aws.amazon.com/ko_kr/wellarchitected/latest/security-pillar/)

---

## 4. 핵심 요약

- **AWS는 클라우드의 보안(물리, 인프라)을 책임지고,**
- **고객은 클라우드 내의 보안(데이터, 애플리케이션, 접근제어 등)을 책임진다.**
- 책임 경계를 명확히 이해하고, 내 역할에 맞는 보안 조치를 반드시 수행해야 한다.
