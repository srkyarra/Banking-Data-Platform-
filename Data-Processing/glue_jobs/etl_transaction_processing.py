import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Sample read from S3
input_data = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": ["s3://your-bucket/transactions/"]},
    format="json"
)

# Write to Redshift
glueContext.write_dynamic_frame.from_jdbc_conf(
    frame=input_data,
    catalog_connection="redshift-conn",
    connection_options={"dbtable": "transactions", "database": "banking"},
    redshift_tmp_dir="s3://your-temp-dir/"
)

job.commit()