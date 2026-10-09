import boto3

# Create EC2 client
ec2 = boto3.client("ec2", region_name="us-east-1")

# Create EC2 instance
response = ec2.run_instances(
    ImageId="ami-081b0a6eac00b4f53",
    InstanceType="t3.micro",
    MinCount=1,
    MaxCount=1
)

# Get created instance ID
instance_id = response["Instances"][0]["InstanceId"]

print("EC2 instance created successfully!")
print("Instance ID:", instance_id)