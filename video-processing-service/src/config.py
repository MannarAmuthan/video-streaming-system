import os

from gateway.simple_storage import download_blob
from gateway.simple_storage import upload_blob


def source_videos_bucket():
    return "streamer-source-videos" #os.environ["SOURCE_VIDEOS_BUCKET"]


def processed_video_bucket():
    return "post-processed-videos"
    # return os.environ["PROCESSED_VIDEOS_BUCKET"]


def get_uploader():
    return upload_blob


def get_downloader():
    return download_blob