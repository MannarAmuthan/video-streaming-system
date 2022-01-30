import shutil
import traceback

from Logger import log
from data.video import DataException, download_video, upload_video
import os

from domain.utils.chunks import make_chunks, ChunkException, create_master_hls
from domain.utils.resolution import create_resolutions, ResolutionException
from domain.utils.thumbnail import create_thumbnail

CHUNK_DURATION = 3


class ProcessException(Exception):
    def __init__(self, message):
        self.message = message


def process_video(video_id, video_format):
    try:
        original_directory = os.getcwd()
        file_directory = __create_disk_folder(video_id)

        os.chdir(file_directory)

        download_video(video_id,video_format)
        log(f"Download {video_id} for processing ", "INFO")

        create_resolutions(video_id,video_format)

        log(f"Created resolutions for {video_id}", "INFO")

        resolutions = os.listdir("resolutions")

        chunk_videos_path = f"stream"

        for res_file in resolutions:
            resolution_string = res_file.split(".")[0]
            input_source_video = f"resolutions/{res_file}"
            make_chunks(input_source_video,chunk_videos_path,resolution_string)
            log(f"Created stream_files for {video_id}", "INFO")

        create_master_hls(f"{chunk_videos_path}/")
        create_thumbnail(video_id,video_format,f"{chunk_videos_path}/")
        stream_files = os.listdir(chunk_videos_path)
        for file in stream_files:
            upload_video(video_id,f"{chunk_videos_path}/{file}")
            log(f"Uploaded stream_files for {video_id} from {chunk_videos_path}/{file}", "INFO")

        __remove_disk_folder_if_exists(original_directory,file_directory)

    except ResolutionException as e:
        traceback.print_exc()
        __remove_disk_folder_if_exists(original_directory, file_directory)
        raise ProcessException(f"Could not create resolutions for video {video_id} : {e.message}")
    except ChunkException as e:
        traceback.print_exc()
        __remove_disk_folder_if_exists(original_directory, file_directory)
        raise ProcessException(f"Could not create stream_files for video {video_id} : {e.message}")
    except DataException as e:
        traceback.print_exc()
        __remove_disk_folder_if_exists(original_directory, file_directory)
        raise ProcessException(f"Could not download/upload stream_files for video {video_id} : {e.message}")
    except Exception as e:
        traceback.print_exc()
        __remove_disk_folder_if_exists(original_directory, file_directory)
        raise ProcessException(f"Could not process video {video_id}")


def __create_disk_folder(video_id):
    root_directory = f"{video_id}"

    if not os.path.exists(f"{root_directory}/"):
        os.makedirs(f"{root_directory}/")
    return root_directory


def __remove_disk_folder_if_exists(original_directory,file_directory):
    print("Deleting temp folder .....")
    os.chdir(original_directory)
    if os.path.exists(f"{file_directory}"):
        shutil.rmtree(file_directory)
