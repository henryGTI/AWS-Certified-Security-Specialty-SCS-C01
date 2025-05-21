import boto3

kms = boto3.client('kms')
response = kms.encrypt(
    KeyId='alias/my-key',
    Plaintext=b'Hello, World!'
)
print(response['CiphertextBlob'])
