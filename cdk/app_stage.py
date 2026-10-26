import aws_cdk as cdk
from constructs import Construct
from cdk.cdk_stack import CdkStack

class MyPipelineAppStage(cdk.Stage):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        S3Stack = CdkStack(self, "S3Stack")