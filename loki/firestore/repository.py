#!/usr/bin/env python3

from ..model import VideoDetail, DownloadTask
from firebase_admin import firestore
from firebase_admin.firestore import CollectionReference, DocumentReference


class VideoDetailRepository:
    __collection: CollectionReference

    def __init__(self, username: str):
        db = firestore.client()
        # FIXME: A collection must have an odd number of path elements
        self.__collection = db.collection(f"users/{username}/videos")

    def get(self, id_str: str) -> VideoDetail:
        doc_ref: DocumentReference = self.__collection.document(id_str)
        doc = doc_ref.get()
        # returns the data in snapshot
        # returns None if reference does not exist
        return doc.to_dict()

    def add(self, video: VideoDetail) -> str:
        update_time, doc_ref = self.__collection.add(video.to_dict())
        return doc_ref.id

    def update(self, id_str: str, video: VideoDetail) -> str:
        doc_ref: DocumentReference = self.__collection.document(id_str)
        doc_ref.set(video.to_dict())
        return id_str

    def delete(self, id_str: str):
        doc_ref: DocumentReference = self.__collection.document(id_str)
        doc_ref.delete()


class DownloadTaskRepository:
    __collection: CollectionReference

    def __init__(self, username: str):
        db = firestore.client()
        # FIXME: A collection must have an odd number of path elements
        self.__collection = db.collection(f"users/{username}/download_tasks")

    def get(self, id_str: str) -> DownloadTask:
        doc_ref: DocumentReference = self.__collection.document(id_str)
        doc = doc_ref.get()
        # returns the data in snapshot
        # returns None if reference does not exist
        return doc.to_dict()

    def add(self, task: DownloadTask) -> str:
        update_time, doc_ref = self.__collection.add(task.to_dict())
        return doc_ref.id

    def update(self, id_str: str, task: DownloadTask) -> str:
        doc_ref: DocumentReference = self.__collection.document(id_str)
        doc_ref.set(task.to_dict())
        return id_str

    def delete(self, id_str: str):
        doc_ref: DocumentReference = self.__collection.document(id_str)
        doc_ref.delete()
