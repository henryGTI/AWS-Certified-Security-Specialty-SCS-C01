2.1 Introduction (소개)

  이론

    클라우드 보안은 기존 온프레미스 보안과 달리, 공유 책임 모델(Shared Responsibility Model)을 기반으로 합니다.

    즉, AWS와 사용자가 각각 책임져야 할 보안 영역이 다릅니다.

2.2 Cloud Security Principles Overview (클라우드 보안 원칙 개요)

  이론

    공유 책임 모델

      AWS: 인프라, 하드웨어, 네트워크, 가상화 계층 등 “클라우드의 보안” 책임

      고객(사용자): 데이터, 애플리케이션, IAM, 네트워크 설정 등 “클라우드 내의 보안” 책임

  핵심 원칙

    데이터 보호, 접근 제어, 암호화, 모니터링, 규정 준수

2.3 The Shared Responsibility Model (공유 책임 모델)

  실습/정리

    chapter02_cloud_security_principles/shared_responsibility.md

  AWS 공식 문서 요약,

    내가 책임져야 할 영역(예: S3 버킷 퍼블릭 차단, IAM 정책 관리 등) 정리

2.4 AWS Compliance Programs & Artifact

  이론

    AWS Artifact: 규정 준수 관련 문서(감사 리포트 등) 제공

    AWS Compliance Program: ISO, SOC, PCI 등 다양한 국제 표준 준수

2.5 AWS Well-Architected Framework

  이론

    AWS에서 권장하는 5가지 핵심 원칙

      보안(Security)

      신뢰성(Reliability)

      성능 효율성(Performance Efficiency)

      비용 최적화(Cost Optimization)

      운영 우수성(Operational Excellence)

      보안(Security) 원칙

      IAM 최소 권한, 데이터 암호화, 모니터링, 자동화된 보안, 사고 대응 등

  실습/정리

    chapter02_cloud_security_principles/well_architected_framework.md

    Well-Architected Framework의 각 Pillar 요약

    실제 AWS Well-Architected Tool 사용 경험/캡처 정리

2.6 IAM 최소 권한 원칙 실습

  실습 코드 예시

    chapter02_cloud_security_principles/iam_policy_minimum.py

2.7 S3 데이터 암호화 실습

  실습 코드 예시

    chapter06_data_protection/s3_encryption_example.py

    (챕터6에도 연계됨)

2.8 CloudTrail로 감사 활성화

  실습 코드 예시

    chapter01_security_fundamentals/cloudtrail_setup.py

    (1장과 연계)

2.9 Summary (요약)

    클라우드 보안의 핵심은 공유 책임 모델과 최소 권한, 암호화, 모니터링 등 실무 원칙

    EC2에서 IAM, S3, CloudTrail을 활용해 실제로 보안 원칙을 코드로 구현해볼 수 있음

2.10 Review Questions (복습 문제)

    공유 책임 모델에서 AWS와 사용자의 책임 구분

    Well-Architected Framework의 5가지 Pillar

    IAM 최소 권한 정책 예시
