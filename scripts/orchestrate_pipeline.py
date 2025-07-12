import subprocess

def run():
    subprocess.run(['python3', 'data_ingestion/kinesis/create_kinesis_stream.py'])
    subprocess.run(['python3', 'data_catalog/glue_catalog/create_glue_catalog_table.py'])
    subprocess.run(['python3', 'data_governance/audit_logs/enable_cloudtrail_logging.py'])

if __name__ == '__main__':
    run()
