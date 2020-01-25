#!/usr/bin/env python3

# Copyright (c) 2020 Chiajun Wang
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from datetime import datetime


class DownloadTask:
    "The scheduled download task."
    status: str
    url: str
    start_time: datetime

    def __init__(self, status: str, url: str, start_time: datetime):
        self.status = status
        self.url = url
        self.start_time = start_time

    def to_dict(self):
        return {
            "status": self.status,
            "url": self.url,
            "start_time": self.start_time,
        }

    @staticmethod
    def from_dict(d):
        return DownloadTask(d.status, d.url, d.start_time)


class VideoFile:
    """Model class for video files.

    This class is an alternate of the actual video data instead of containing
    the whole data in memory.
    """

    name: str
    path: str

    def __init__(self, name, path):
        self.name = name
        self.path = path

    def __repr__(self):
        return f"VideoFile(name={self.name},path={self.path})"


class VideoDetail:
    ""
    name: str
    status: str
    origin_url: str
    download_url: str

    def __init__(
        self,
        name: str,
        origin_url: str,
        download_url: str,
    ):
        self.name = name
        self.origin_url = origin_url
        self.download_url = download_url

    def to_dict(self):
        return {
            "name": self.name,
            "origin_url": self.origin_url,
            "download_url": self.download_url,
        }

    @staticmethod
    def from_dict(d):
        return VideoDetail(d.name, d.origin_url, d.download_url)
