from aws_cdk import (
    # Duration,
    Duration,
    RemovalPolicy,
    Stack,
    # aws_sqs as sqs,
    aws_s3 as s3,
    CfnOutput
)
from constructs import Construct

class PythonStarterStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(self, "MyFirstBucket",
            versioned=True,
            removal_policy=RemovalPolicy.DESTROY,
            lifecycle_rules=[
                s3.LifecycleRule(
                    expiration=Duration.days(10)
                )
            ]
        ) 

        CfnOutput( self,"MyFirstBucketOutput",
            value=bucket.bucket_name,
            description="My First Bucket Name",
            export_name="MyFirstBucket"
        )

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "PythonStarterQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
