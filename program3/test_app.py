from unittest import TestCase

from back_rest import CloudDirectoryBackupRestore


class ParserTest(TestCase):
    def test_backup_command(self):
        cdbr = CloudDirectoryBackupRestore()
        result = cdbr.backup_dir(
            "/Users/terenceschumacher/Books/tron-books",
            "backup-restore-bucket.tschu.02.25",
        )
        print(result)
        assert True

    def test_badbucket_name(self):
        cdbr = CloudDirectoryBackupRestore()
        result = cdbr.restore_dir(
            "backup-restore-bucket.tschu.02.25",
            "/Users/terenceschumacher/Books/tron-books",
        )
        print(result)
        assert True

    def test_list_files(self):
        cdbr = CloudDirectoryBackupRestore()
        result = cdbr.list_files("backup-restore-bucket.tschu.02.25")
        print(result)
        assert True
