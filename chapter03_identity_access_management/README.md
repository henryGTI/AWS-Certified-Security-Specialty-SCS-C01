# Chapter 03. Identity and Access Management (IAM)

AWS 리소스에 대한 인증, 인가, 계정 관리의 핵심인 IAM(Identity and Access Management)에 대해 다룹니다.  
실무에서 자주 사용하는 IAM 정책, 역할, SSO, Federation, Secrets Manager 등도 함께 정리합니다.

---

## 1. IAM 개요

- **IAM(Identity and Access Management)**: AWS 리소스에 대한 접근 제어 및 권한 관리 서비스
- **주요 개념**
  - **User(사용자)**: AWS 리소스에 접근하는 개별 계정
  - **Group(그룹)**: 여러 사용자를 묶어서 동일한 권한 부여
  - **Role(역할)**: AWS 서비스/사용자에게 임시 권한 부여
  - **Policy(정책)**: JSON 형식의 권한 규칙(허용/거부)

---

## 2. IAM 정책 실습

**`iam_user_role_example.py`**
```python
import boto3

iam = boto3.client('iam')

# 사용자 생성
iam.create_user(UserName='test-user')

# 역할 생성 예시
assume_role_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {"Service": "ec2.amazonaws.com"},
            "Action": "sts:AssumeRole"
        }
    ]
}
iam.create_role(
    RoleName='EC2S3ReadOnlyRole',
    AssumeRolePolicyDocument=json.dumps(assume_role_policy)
)
```

---

## 3. S3 접근 정책 예시

**`s3_policy_example.py`**
```python
import boto3
import json

iam = boto3.client('iam')

policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:GetObject"],
            "Resource": "arn:aws:s3:::my-bucket/*"
        }
    ]
}

iam.put_user_policy(
    UserName='test-user',
    PolicyName='S3ReadOnly',
    PolicyDocument=json.dumps(policy)
)
```
- 특정 S3 버킷에만 읽기 권한을 부여하는 최소 권한 정책

---

## 4. Federation & SSO

- **Federation(연동 인증)**: 외부 IdP(Active Directory, Google, SAML 등)와 연동하여 AWS 접근
- **AWS SSO(Single Sign-On)**: 여러 AWS 계정/서비스에 한 번에 로그인

---

## 5. Secrets Manager & Parameter Store

- **AWS Secrets Manager**: 데이터베이스 비밀번호, API 키 등 민감 정보 안전하게 저장/관리
- **AWS Systems Manager Parameter Store**: 설정값, 시크릿 등 안전하게 저장

**`cognito_federation_example.py`**  
(예시: Cognito를 통한 연동 인증)
```python
import boto3

cognito = boto3.client('cognito-idp')
# 사용자 풀 생성, 연동 등은 AWS 콘솔에서 주로 설정

# 예시: 사용자 풀 목록 조회
response = cognito.list_user_pools(MaxResults=10)
print(response)
```

---

## 6. 실무 팁

- **IAM 정책은 최소 권한 원칙(Least Privilege)**을 반드시 적용
- **IAM 역할을 EC2, Lambda 등 서비스에 부여**하면 키 없이 안전하게 리소스 접근 가능
- **MFA(다중 인증)**를 활성화하여 계정 보안 강화
- **정기적으로 IAM 사용자/정책/키 사용 현황 점검**

---

## 7. 참고 자료

- [AWS IAM 공식 문서](https://docs.aws.amazon.com/ko_kr/IAM/latest/UserGuide/introduction.html)
- [AWS SSO 공식 문서](https://docs.aws.amazon.com/ko_kr/singlesignon/latest/userguide/what-is.html)
- [AWS Secrets Manager](https://docs.aws.amazon.com/ko_kr/secretsmanager/latest/userguide/intro.html)
- [AWS Cognito](https://docs.aws.amazon.com/ko_kr/cognito/latest/developerguide/cognito-user-identity-pools.html)

---

## 8. 복습 문제

1. IAM 정책과 역할의 차이점은?
2. Federation과 SSO의 차이점은?
3. Secrets Manager와 Parameter Store의 차이점과 사용 예시는?
4. IAM 최소 권한 정책을 적용하는 이유는?

---

더 궁금한 점이나 실습 코드가 필요하면 언제든 질문해 주세요!
