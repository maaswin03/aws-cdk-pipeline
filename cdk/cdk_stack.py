from aws_cdk import (
    # Duration,
    Stack,
    RemovalPolicy,
)
from constructs import Construct
from aws_cdk.aws_s3 import Bucket
from aws_cdk.aws_sns import Topic

class CdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # create a s3 bucket
        Bucket(self, "s3-aswin-bucket",removal_policy=RemovalPolicy.DESTROY)

        Topic(self, "Topic",display_name="Customer subscription topic")

        Topic(self, "Topic",display_name="Customer subscription topic - 1")


