#!/usr/bin/env python3
import os
from ..model import VideoFile
import firebase_admin
from firebase_admin import storage


class VideoFileRepository:

    # The download url's endpoint and bucket name
    # see https://cloud.google.com/storage/docs/request-endpoints?hl=ja

    def add(self, file: VideoFile) -> str:
        """Upload video to cloud storage."""
        bucket = storage.bucket()
        # Instantiate blob object by file name
        blob = bucket.blob(file.name)
        # Upload blob's contents from file
        blob.upload_from_filename(file.path)
        # Remove uploaded file from disk
        os.remove(file.path)
        # Set the accessibility to public
        blob.make_public()
        # Return public url
        return blob.public_url
