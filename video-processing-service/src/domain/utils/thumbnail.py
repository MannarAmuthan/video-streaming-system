import os


def create_thumbnail(video_id,video_format,video_path):
    try:
        exit_code = os.system(f"ffmpeg -i {video_id}.{video_format} -ss 00:00:01.000 -vframes 1 {video_path}/thumbnail.png")
        if exit_code != 0:
            raise Exception(f"FFMPEG Exit code : {exit_code}")
    except Exception as e:
        raise Exception(f"Could not create thumbnail for {video_id} : {e}")

