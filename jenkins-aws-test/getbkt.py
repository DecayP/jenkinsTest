import boto3
import pprint

# Create an S3 client
s3 = boto3.client('s3')

# Call to S3 to retrieve the policy for the given bucket
result = s3.get_bucket_acl(Bucket='s3bucket-dk')
pprint.pprint(result)