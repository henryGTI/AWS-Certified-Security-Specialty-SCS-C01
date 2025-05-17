import boto3

gd = boto3.client('guardduty')

# GuardDuty 활성화(최초 1회)
response = gd.create_detector(Enable=True)
detector_id = response['DetectorId']
print("GuardDuty Detector ID:", detector_id)
