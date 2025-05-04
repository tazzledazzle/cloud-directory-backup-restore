import subprocess

from aws_cdk import Stack, aws_s3 as s3, aws_s3_deployment as s3deploy, App
from constructs import Construct


class S3Uploader:
    def __init__(self):
        subprocess.run(["aws", "configure"])

    def backup_dir(self, dir, bucket_name):
        bucket = s3.Bucket.from_bucket_name(self, "Program3Bucket", bucket_name)

        # Upload the directory to the cloud
        s3deploy.BucketDeployment(
            self,
            "DeployFiles",
            sources=[s3deploy.Source.asset(dir)],
            destination_bucket=bucket,
            # optional prefix in destination bucket
        )

        app = App()
        S3Uploader(app, "S3UploaderStack")
        app.synth()
