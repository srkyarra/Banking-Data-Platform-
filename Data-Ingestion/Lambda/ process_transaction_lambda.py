import json
import base64

def lambda_handler(event, context):
    for record in event['Records']:
        payload = base64.b64decode(record["kinesis"]["data"]).decode('utf-8')
        transaction = json.loads(payload)
        print(f"Processing transaction ID: {transaction['transaction_id']}")
    return {'statusCode': 200, 'body': 'Processed transactions'}