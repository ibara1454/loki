#!/usr/bin/env python3

import os


def load_config() -> dict:
    "Load configurations."
    # Get environment variables
    CLOUD_STORAGE_BUCKET_NAME = os.getenv(
        'CLOUD_STORAGE_BUCKET_NAME',
        "CLOUD_STORAGE_BUCKET_NAME")
    CELERY_BROKER = os.getenv('CELERY_BROKER', 'file://')
    return {
        'CLOUD_STORAGE_BUCKET_NAME': CLOUD_STORAGE_BUCKET_NAME,
        'CELERY_BROKER': CELERY_BROKER,
    }
