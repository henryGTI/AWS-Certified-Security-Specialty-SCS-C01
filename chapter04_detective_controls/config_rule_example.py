import boto3

config = boto3.client('config')

# Config Recorder 활성화
config.put_configuration_recorder(
    ConfigurationRecorder={
        'name': 'default',
        'roleARN': 'arn:aws:iam::123456789012:role/aws-config-role'
    }
)
config.put_delivery_channel(
    DeliveryChannel={
        'name': 'default',
        's3BucketName': 'my-config-bucket'
    }
)
config.start_configuration_recorder(
    ConfigurationRecorderName='default'
)
