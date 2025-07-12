import boto3

def enable_cloudtrail():
    client = boto3.client('cloudtrail')
    client.create_trail(
        Name='BankingTrail',
        S3BucketName='your-cloudtrail-bucket'
    )
    client.start_logging(Name='BankingTrail')

# infrastructure/terraform/main.tf
provider "aws" {
  region = "us-east-1"
}

resource "aws_kinesis_stream" "transaction_stream" {
  name        = "transaction-stream"
  shard_count = 1
}

resource "aws_s3_bucket" "raw_bucket" {
  bucket = "your-raw-transaction-bucket"
}