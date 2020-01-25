#!/usr/bin/env python3

from celery import Celery
from .config import load_config
from .cloud_storage.repository import VideoFileRepository
from .download.repository import DownloadRepository
from .firestore.repository import VideoDetailRepository, DownloadTaskRepository
from .model import DownloadTask, VideoDetail

# For firebase authentication
import firebase_admin
from firebase_admin import credentials

config = load_config()

# Start celery worker
# TODO: change module name
module_name = 'main'
celery = Celery(module_name, broker=config['CELERY_BROKER'])

# Initialize firebase application
firebase_admin.initialize_app(options={
    'storageBucket': f"{config['CLOUD_STORAGE_BUCKET_NAME']}.appspot.com"
})

# Instantiate repositories
download_repository = DownloadRepository()
video_file_repository = VideoFileRepository()


@celery.task
def download(user_id: str, task_id: str, task: DownloadTask):
    "Perform an scheduled download task."
    # Instantiate user-associated repositories by user id
    video_detail_repository = VideoDetailRepository(user_id)
    download_task_repository = DownloadTaskRepository(user_id)

    # Update task status to "RUNNING"
    task = DownloadTask("RUNNING", task.url, task.start_time)
    download_task_repository.update(task_id, task)

    # Perform download
    file = download_repository.get(task.url)
    # TODO: handle errors when download failed
    download_url = video_file_repository.add(file)

    # Add new VideoDetail record
    video_detail_repository.add(
        VideoDetail(
            name=file.name,
            origin_url=task.url,
            download_url=download_url
        )
    )

    # Update task status to "COMPLETE"
    task = DownloadTask("COMPLETE", task.url, task.start_time)
    download_task_repository.update(task_id, task)
