#!/usr/bin/env python3

import uuid
import os
import youtube_dl
from ..model import VideoFile


class DownloadRepository:
    """Video-download APIs."""
    # options for youtube_dl
    __options: dict

    def __init__(self, options={}):
        """Create a video download API instance with given options."""
        self.__options = options

    def get(self, url: str) -> VideoFile:
        """Download video from given url.
        Note that downloading may block thread a long time.

        Parameters
        ==========
        url: string
            The url of video.

        Returns
        =======
        Result of execution.
        """
        # TODO: choose format dynamically
        # force using MPEG-4
        ext_format = 'mp4'
        # generate a unique filename
        file_name = f"{uuid.uuid4()}.{ext_format}"
        # set template of output file name
        # see: https://github.com/ytdl-org/youtube-dl#output-template
        self.__options['format'] = ext_format
        self.__options['outtmpl'] = file_name
        with youtube_dl.YoutubeDL(self.__options) as ydl:
            # blocking call
            ret_code = ydl.download([url])
            # TODO: error handling
            return VideoFile(
                name=file_name,
                path=os.path.join(os.getcwd(), file_name),
            )
