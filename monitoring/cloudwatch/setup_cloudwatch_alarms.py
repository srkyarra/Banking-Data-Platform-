import boto3

def setup_alarm():
    cloudwatch = boto3.client('cloudwatch')
    cloudwatch.put_metric_alarm(
        AlarmName='HighKinesisPutRecordsErrors',
        MetricName='PutRecords.FailedRecords',
        Namespace='AWS/Kinesis',
        Statistic='Sum',
        Period=300,
        EvaluationPeriods=1,
        Threshold=5,
        ComparisonOperator='GreaterThanThreshold',
        AlarmActions=[],
        Dimensions=[{'Name': 'StreamName', 'Value': 'transaction-stream'}]
    )