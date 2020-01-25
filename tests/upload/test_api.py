import unittest
from unittest.mock import MagicMock

from loki.upload.api import UploadApi


@unittest.mock.patch("google.cloud.storage.Client")
class TestUploadApi(unittest.TestCase):
    def test_post(self, mock):
        src, dest = "dummy", "dummy"
        instance = mock()

        api = UploadApi()
        url = api.post(src=src, dest=dest)

        instance. \
            get_bucket.return_value. \
            blob.return_value. \
            upload_from_filename.assert_called()
        self.assertEqual(url, f"{api.ENDPOINT}/{api.BUCKET_NAME}/{dest}")
