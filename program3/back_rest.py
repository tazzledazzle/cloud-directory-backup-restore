import argparse
import os
import subprocess


class CloudDirectoryBackupRestore:
    def __init__(self):
        pass

    def backup_dir(self, dir, bucket_name):
        print(f"Backing up {dir}")
        if not os.path.isdir(dir):
            raise argparse.ArgumentTypeError(f"{dir} is not a valid directory")

        # check bucket exists
        result = subprocess.run(["aws", "s3", "ls", f"s3://{bucket_name}"])
        # print(result)

        # only copy the directory that was passed in

        dir_name = dir.split("/")[-1]
        if result.returncode == 0:
            print(f"Bucket {bucket_name} exists")
            return subprocess.run(
                ["aws", "s3", "sync", dir, f"s3://{bucket_name}/{dir_name}"]
            )
        else:
            subprocess.run(["aws", "s3", "mb", f"s3://{bucket_name}"])
            print(f"Bucket {bucket_name} created")

        return subprocess.run(
            ["aws", "s3", "sync", dir, f"s3://{bucket_name}/{dir_name}"]
        )

    def restore_dir(self, bucket_name, dir):
        print(f"Restoring {self.restore_dir}")
        dir_name = dir.split("/")[-1]
        return subprocess.run(
            ["aws", "s3", "sync", f"s3://{bucket_name}/{dir_name}", dir]
        )

    def list_files(self, bucket_name):
        result = subprocess.run(["aws", "s3", "ls", f"s3://{bucket_name}"])
        print(result)

    def create_parser(self):
        arg_parser = argparse.ArgumentParser(
            prog="back_rest", description="Back_Rest: Backup and Restore Directories to the Cloud"
        )
        arg_parser.add_argument("--version", action="version", version="%(prog)s 1.0")
        subparsers = arg_parser.add_subparsers(
            dest="backup",
            help="uploads the specified directory for backup in the cloud",
        )
        backup = subparsers.add_parser("backup", help="Backup files to a bucket")
        backup.add_argument("src_dir", help="the directory to backup")
        backup.add_argument(
            "bucket_name", help="the name of the bucket to store the backup"
        )
        restore = subparsers.add_parser(
            "restore", help="restores the specified directory from the cloud"
        )
        restore.add_argument(
            "bucket_name", help="the name of the bucket to restore from"
        )
        restore.add_argument("src_dir", help="the directory to restore")

        subparsers.add_parser("list", help="lists the files in the specified directory")

        return arg_parser


if __name__ == "__main__":
    cdbr = CloudDirectoryBackupRestore()
    parser = cdbr.create_parser()
    args = parser.parse_args()
    if args.backup:
        cdbr.backup_dir(args.src_dir, args.bucket_name)
    elif args.restore:
        cdbr.restore_dir(args.bucket_name, args.src_dir)
    elif args.list:
        cdbr.list_files()
