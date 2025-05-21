# AWS Security Journey Plan (보안 여정 단계별 계획)

AWS 환경에서 체계적으로 보안을 강화하기 위한  
단계별 보안 여정(Security Journey) 설계 예시입니다.

---

## 1. Phase 1: Infrastructure Protection (인프라 보호)

- **VPC, Subnet, Security Group, NACL 등 네트워크 보안 기본 설정**
- **IAM 최소 권한 원칙 적용**
- **S3, EBS, RDS 등 데이터 암호화 활성화**
- **CloudTrail, Config, VPC Flow Logs 등 로깅 및 모니터링 활성화**
- **WAF, Shield 등 웹/네트워크 공격 방어 도구 적용**

---

## 2. Phase 2: Security Insights and Workload Protection (보안 인사이트 및 워크로드 보호)

- **GuardDuty, Security Hub, Inspector 등 위협 탐지 서비스 활성화**
- **Config Rule, Trusted Advisor 등 규정 준수 및 보안 상태 점검**
- **CloudWatch, SNS, Lambda 등으로 실시간 경보 및 자동화 대응**
- **정기적인 취약점 진단 및 보안 점검 수행**
- **운영 워크로드의 보안 정책 및 표준화**

---

## 3. Phase 3: Security Automation (보안 자동화)

- **EventBridge, Lambda, SSM 등으로 이벤트 기반 자동화 대응**
- **IAM, S3, 네트워크 등 주요 리소스의 변경 감지 및 자동 조치**
- **DevSecOps 파이프라인 구축(Infrastructure as Code, 자동 보안 테스트 등)**
- **보안 정책/설정의 코드화 및 형상 관리**
- **정기적인 보안 자동화 점검 및 개선**

---

## 4. 실무 적용 팁

- **Well-Architected Tool**로 정기적으로 보안 상태 진단
- **Security Hub 대시보드**로 전체 보안 현황 한눈에 파악
- **팀 단위 보안 교육 및 모의 훈련** 정기 실시
- **최신 AWS 보안 서비스/기능**을 적극 도입

---

## 5. 참고 자료

- [AWS Well-Architected Framework](https://docs.aws.amazon.com/ko_kr/wellarchitected/latest/framework/welcome.html)
- [AWS Security Hub](https://docs.aws.amazon.com/ko_kr/securityhub/latest/userguide/what-is-securityhub.html)
- [AWS Security Best Practices](https://docs.aws.amazon.com/ko_kr/wellarchitected/latest/security-pillar/)

---

## 6. 복습 문제

1. AWS 보안 여정의 3단계(Phase)는 무엇인가?
2. 각 단계별로 반드시 적용해야 할 핵심 보안 조치는?
3. 보안 자동화의 실무적 이점은?

---

더 궁금한 점이나 실무 적용 사례가 필요하면 언제든 질문해 주세요!
