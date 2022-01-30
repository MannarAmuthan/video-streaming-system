import os
import json


resolutions={
"p_1080" : [1920,1080],
"p_720" : [1280,720],
"p_480" : [854,480],
"p_360" : [640,360],
"p_240" : [426,240],
"p_144" : [256,144]
}


class ResolutionException(Exception):
    def __init__(self, message):
        self.message = message


def get_resolution(video_path):
    response_string=os.popen(f"ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of json {video_path}").read()
    response=json.loads(response_string)
    if "streams" in response:
        width=response["streams"][0]["width"]
        height=response["streams"][0]["height"]
        return {"width":width,"height":height}
    return {}


def get_duration(video_path):
    try:
        response = os.popen(f"ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 {video_path}")
        return response.read()
    except Exception as e:
        raise ResolutionException(f"Something wrong while get duration for {video_path} : {str(e)}")


def create_resolutions(video_id,video_format):
    try:
        if not os.path.exists(f"resolutions/"):
            os.makedirs(f"resolutions/")
        video_path = f"{video_id}.{video_format}"

        for res in resolutions:
            width = resolutions[res][0]
            height = resolutions[res][1]
            exit_code = os.system(f"ffmpeg -y -i {video_path} -vf scale=\"{width}:{height}\" resolutions/{height}.{video_format}")
            if exit_code != 0:
                raise Exception(f"FFMPEG Exit code : {exit_code}")
    except Exception as e:
        raise ResolutionException(f"Something wrong while create resolutions for {video_id} : {str(e)}")
