import boto3

def create_stream(stream_name):
    client = boto3.client('kinesis')
    client.create_stream(StreamName=stream_name, ShardCount=1)
    print(f"Stream {stream_name} created")