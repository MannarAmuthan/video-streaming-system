from gateway.simple_storage import upload_blob, download_blob


class DataException(Exception):
    def __init__(self, message):
        self.message = message


def upload_video(video_id,video_file_path):
    try:
        destination_file_path= video_id + "/" + video_file_path
        upload_blob( video_file_path, destination_file_path)
    except Exception as e:
        raise DataException(f"Could not upload video {video_id} : {str(e)}")


def download_video(video_id,video_format):
    try:
        input_file_path = video_id+"/"+video_id+f".{video_format}"
        destination_file_path = video_id+f".{video_format}"
        download_blob( input_file_path, destination_file_path)
    except Exception as e:
        raise DataException(f"Could not download video {video_id} : {str(e)}")