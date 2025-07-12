import boto3

def create_table():
    glue = boto3.client('glue')
    glue.create_table(
        DatabaseName='banking_db',
        TableInput={
            'Name': 'transactions',
            'StorageDescriptor': {
                'Columns': [
                    {'Name': 'transaction_id', 'Type': 'string'},
                    {'Name': 'customer_id', 'Type': 'string'},
                    {'Name': 'amount', 'Type': 'double'},
                    {'Name': 'timestamp', 'Type': 'timestamp'}
                ],
                'Location': 's3://your-bucket/transactions/',
                'InputFormat': 'org.apache.hadoop.mapred.TextInputFormat',
                'OutputFormat': 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat',
                'SerdeInfo': {
                    'SerializationLibrary': 'org.openx.data.jsonserde.JsonSerDe'
                }
            }
        }
    )