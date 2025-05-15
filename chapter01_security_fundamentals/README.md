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
