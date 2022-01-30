from flask import Flask
from flask import request
from flask import make_response

import json

from Logger import log
from domain.process_video import process_video, ProcessException

flask_app = Flask(__name__)


@flask_app.route("/health")
def health_check():
    return {'message': 'Healthy'} 


@flask_app.route("/process-video", methods=['POST'])
def process():
    try:

        payload: dict = json.loads(request.data)

        if "video_id" not in payload or "video_format" not in payload:
            return make_api_response("video_id or video_format is missing", 400)

        video_id: str = payload["video_id"]
        video_format: str = payload["video_format"]
        log(f"Started video processing for {video_id}","INFO")
        process_video(video_id,video_format)
        log(f"Completed video processing for {video_id}", "INFO")
        return make_api_response("Video processed successfully", 201)
    except ProcessException as e:
        return make_api_response(e.message, 500)
    except Exception as e:
        return make_api_response(str(e), 500)


def make_api_response(message: str, status_code=200):
    response = make_response({"message": message}, status_code)
    response.headers.add_header("content-type", "application/json")
    return response


if __name__ == "__main__":
    flask_app.run(host='0.0.0.0',port=8080)