import boto3

cloudtrail = boto3.client('cloudtrail')

# 최근 이벤트 조회
events = cloudtrail.lookup_events(MaxResults=5)
for event in events['Events']:
    print(event['EventName'], event['Username'], event['EventTime'])
