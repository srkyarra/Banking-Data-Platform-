## Step1 .Customer Transactions
A customer initiates a transaction (e.g., funds transfer, payment) using a mobile or web banking app.

## step2. Amazon Kinesis (Data Stream)
   The transaction is sent in real-time to Amazon Kinesis, a streaming service that handles high-throughput event data.

Kinesis ensures real-time data is captured as soon as the transaction occurs.

## Step3. AWS Lambda (optional preprocessing)
   A Lambda function (e.g., process_transaction_lambda.py) can be triggered by Kinesis to:

Enrich or validate data

Format it to JSON

Send to S3 and Glue

## Step 4. Amazon S3 (Raw Storage)
   Raw transaction data is stored in Amazon S3 (object storage) for long-term and replayable storage.

## Step 5. AWS Glue (ETL Engine)
   Glue picks up the raw data, performs ETL (Extract, Transform, Load):

Extracts records from S3

Transforms data (e.g., cleans, aggregates)

Loads cleaned data into Amazon Redshift

## Step 6. Amazon Redshift (Data Warehouse)
   Structured, clean transaction data is stored here for:

Business Intelligence (BI) reporting

Ad hoc SQL queries

Trend analysis

## Step 7. Fraud Detection Layer (Glue or Redshift Job)
   A fraud detection job (e.g., Glue script or Redshift SQL logic) scans for anomalies like:

High-value transfers at night

Unusual transaction patterns

Flagged transactions are written to S3 or a fraud_alerts table.

## Step 8. Amazon CloudWatch (Monitoring)
   CloudWatch is used for:

Tracking custom metrics (e.g., FraudAlertsGenerated)

Setting alarms on failures or spikes in fraudulent activity

Sending notifications to ops or security teams