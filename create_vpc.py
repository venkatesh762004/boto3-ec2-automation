import boto3

# Create EC2 client
ec2 = boto3.client("ec2", region_name="us-east-1")

# Create VPC
response = ec2.create_vpc(
    CidrBlock="10.0.0.0/16"
)

# Get VPC ID
vpc_id = response["Vpc"]["VpcId"]

print("VPC created successfully!")
print("VPC ID:", vpc_id)