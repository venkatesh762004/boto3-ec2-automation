import boto3

s3 = boto3.client("s3")

bucket_name = "my-portfolio-bucket"
file_name = "test.txt"
s3_key = "test.txt"

s3.upload_file(
    file_name,
    bucket_name,
    s3_key
)

print("File uploaded successfully!")