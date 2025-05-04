from unittest import TestCase

from aws_connection import S3Uploader


class TestS3UploaderStack(TestCase):
    def test_backup_dir(self):
        aws = S3Uploader()
        result = aws.backup_dir("test", "test_bucket")
        # check for existing bucket
