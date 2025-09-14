'''
This single file, cdk_example.py, contains the complete definition for your AWS resources. 
You can run this program with the AWS CDK to deploy the resources to your AWS account. 
To use it, simply save the code, install the necessary dependencies (aws-cdk-lib and constructs), and then run cdk deploy in your terminal.
'''

import aws_cdk as cdk
from constructs import Construct
from aws_cdk.aws_s3 import Bucket
from aws_cdk.aws_lambda import Function, Code, Runtime
from aws_cdk.aws_ec2 import Vpc, Instance, InstanceType, MachineImage, SubnetSelection, SubnetType

class MyCdkStack(cdk.Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # 1. Create an S3 Bucket
        # This creates a new S3 bucket with default settings.
        # The bucket name will be generated automatically.
        s3_bucket = Bucket(self, "MySimpleBucket",
            removal_policy=cdk.RemovalPolicy.DESTROY
        )
        # Output the bucket name for easy reference
        cdk.CfnOutput(self, "BucketName", value=s3_bucket.bucket_name)

        # 2. Create an AWS Lambda Function
        # This creates a basic Python 3.9 Lambda function with inline code.
        lambda_function = Function(self, "MySimpleLambda",
            runtime=Runtime.PYTHON_3_9,
            handler="index.handler",
            code=Code.from_inline(
                "def handler(event, context):\n"
                "    print('Hello from Lambda!')\n"
                "    return {'statusCode': 200, 'body': 'Success'}"
            ),
            timeout=cdk.Duration.seconds(30)
        )

        # 3. Create an EC2 Instance
        # This creates a new EC2 instance in the default VPC.
        # We'll use a standard t2.micro instance type.
        # It's important to select a Vpc and a MachineImage (AMI).
        vpc = Vpc(self, "Vpc")
        
        ec2_instance = Instance(self, "MySimpleEc2Instance",
            vpc=vpc,
            instance_type=InstanceType.of(
                ec2.InstanceClass.T2, 
                ec2.InstanceSize.MICRO
            ),
            machine_image=MachineImage.latest_amazon_linux2(),
            vpc_subnets=SubnetSelection(subnet_type=SubnetType.PUBLIC)
        )
        # Output the instance ID for easy reference
        cdk.CfnOutput(self, "InstanceId", value=ec2_instance.instance_id)

app = cdk.App()
MyCdkStack(app, "MySimpleStack")
app.synth()
