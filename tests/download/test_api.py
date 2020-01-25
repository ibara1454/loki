import unittest
from unittest.mock import MagicMock

from loki.download.api import DownloadApi


@unittest.mock.patch("youtube_dl.YoutubeDL")
class TestDownloadApi(unittest.TestCase):
    def test_get(self, mock):
        url = "https://dummy"
        instance = mock()
        instance.__enter__.return_value = instance
        instance.download.return_value = 0

        api = DownloadApi()
        result = api.get(url)
        print(result)

        self.assertEqual(result.result, 0)
