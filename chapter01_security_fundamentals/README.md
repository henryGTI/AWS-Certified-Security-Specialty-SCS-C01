1.1 Introduction (소개)

이론

보안(Security)이란 정보, 시스템, 자산을 무단 접근, 변경, 파괴, 노출로부터 보호하는 모든 활동을 의미합니다.

클라우드 환경(AWS)에서는 물리적 보안부터 데이터, 네트워크, 애플리케이션, 사용자까지 다양한 계층에서 보안이 필요합니다.

1.2 Understanding Security (보안의 이해)

이론

보안의 3요소(CIA Triad)

기밀성(Confidentiality): 허가된 사용자만 데이터에 접근 가능

무결성(Integrity): 데이터가 변조되지 않고 정확하게 유지

가용성(Availability): 필요할 때 언제든 접근 가능

1.3 Basic Security Concepts (기본 보안 개념)

이론

취약점(Vulnerability): 시스템의 약점(예: 패치되지 않은 소프트웨어)

위협(Threat): 취약점을 악용하려는 시도(예: 해커, 악성코드)

위험(Risk): 위협이 취약점을 통해 실제로 피해를 줄 가능성

1.4 Security Countermeasures and Enforcement (보안 대책 및 집행)

이론

대책 예시: 방화벽, 암호화, 접근제어, 모니터링, 백업 등

AWS 예시: Security Group, KMS, IAM, CloudTrail

1.5 Confidentiality, Integrity, and Availability (기밀성, 무결성, 가용성)

실습 코드 예시 (S3 파일 업로드 시 암호화 적용: 기밀성)

chapter01_security_fundamentals/cia_example.py

1.6 Accountability and Nonrepudiation (책임추적성, 부인방지)

이론

책임추적성(Accountability): 누가, 언제, 무엇을 했는지 추적 가능 (ex. CloudTrail 로그)

부인방지(Nonrepudiation): 행위자가 자신의 행동을 부인할 수 없음 (ex. 디지털 서명)

1.7 Authentication, Authorization, and Accounting (인증, 인가, 회계)

실습 코드 예시 (S3 버킷 목록 조회 & CloudTrail로 기록 확인)

chapter01_security_fundamentals/aaa_example.py

1.8 Visibility and Context (가시성 및 맥락)

이론

가시성: 시스템 상태, 로그, 이벤트를 실시간으로 파악

맥락: 이벤트가 발생한 배경, 원인, 영향 등 파악

1.9 Foundational Networking Concepts (네트워크 기초 개념)

이론

OSI 7계층: 물리, 데이터링크, 네트워크, 전송, 세션, 표현, 응용

TCP/IP 스택: 네트워크 통신의 실제 구현

AWS에서는 주로 3~7계층(네트워크~응용)을 많이 다룸

1.10 Main Classes of Attacks (주요 공격 유형)

이론

Reconnaissance(정찰): 정보 수집

Password Attacks(비밀번호 공격): brute force, dictionary

Eavesdropping(도청): 네트워크 트래픽 감청

IP Spoofing(위장), Man-in-the-Middle(중간자 공격)

DoS/DDoS(서비스 거부 공격)

Malware(악성코드), Phishing(피싱)

실습 코드 예시 (S3 버킷 퍼블릭 차단: 기밀성, 무결성 강화)

chapter01_security_fundamentals/s3_public_block.py

1.11 Logging & Auditing (로깅과 감사)

실습 코드 예시 (CloudTrail 트레일 생성 및 시작)

chapter01_security_fundamentals/cloudtrail_setup.py

1.12 Risk Management (위험 관리)

이론

위험 식별 → 평가 → 완화 → 모니터링

AWS에서는 IAM 최소 권한, 네트워크 분리, 암호화, 모니터링 등으로 위험 관리

1.13 Well-Known Security Frameworks and Models (주요 보안 프레임워크 및 모델)

이론

NIST, ISO 27001, CIS, Zero-Trust Model

AWS Well-Architected Framework: 보안, 신뢰성, 성능, 비용, 운영

1.14 Sample Practical Models for Guiding Security Design and Operations (실무 보안 모델)

이론

Security Wheel: 준비 → 탐지 → 대응 → 복구 → 반복

Attack Continuum Model: 공격 전/중/후 단계별 대응

Zero-Trust Model: 기본적으로 아무도 신뢰하지 않고, 모든 접근을 검증

1.15 Summary & Exam Essentials (요약 & 시험 포인트)

보안의 3요소(CIA), 인증/인가/회계, 주요 공격 유형, 위험 관리, AWS의 보안 서비스와 프레임워크를 반드시 숙지

1.16 Review Questions (복습 문제)

각 개념별로 예시 문제를 풀어보며 이해도를 점검
