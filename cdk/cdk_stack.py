from aws_cdk import (
    # Duration,
    Stack,
    RemovalPolicy,
    aws_s3 as s3
)
from constructs import Construct

class CdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # create a s3 bucket
        bucket = s3.Bucket(self, "s3-aswin-bucket",removal_policy=RemovalPolicy.DESTROY,)

