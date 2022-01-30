import os

from flask import request, Flask, make_response, send_from_directory
from flask_cors import cross_origin

flask_app = Flask(__name__)


processed_directory = "processed_storage"
source_directory = "source_storage"


@flask_app.route("/uploadSource", methods=['POST'])
@cross_origin(origin='*')
def uploadSource():
    # check if the post request has the file part
    if 'file' not in request.files:
        make_api_response("No File found in the request",400)
    if 'video_id' not in request.form:
        make_api_response("Video id found in the request", 400)
    file = request.files['file']
    if file.filename == '':
        make_api_response("No File found in the request",400)
    if file:
        video_id = request.form['video_id']
        filename_with_ext = str(file.filename).split(".")
        filename= video_id
        if len(filename_with_ext) == 2:
            filename += "." + filename_with_ext[1]

        __create_disk_folder(source_directory + "/" + video_id)
        file.save(source_directory + "/" + video_id + "/" + filename)
        return make_api_response(f"File uploaded {filename}")


@flask_app.route("/uploadProcessed", methods=['POST'])
@cross_origin(origin='*')
def uploadProcessed():
    # check if the post request has the file part
    if 'file' not in request.files:
        make_api_response("No File found in the request",400)
    if 'video_id' not in request.form:
        make_api_response("Video id found in the request", 400)
    file = request.files['file']
    if file.filename == '':
        make_api_response("No File found in the request",400)
    if file:
        video_id = request.form['video_id']
        file_name = file.filename
        __create_disk_folder(processed_directory + "/" + video_id)
        file.save(processed_directory + "/" + video_id + "/" + file_name)
        return make_api_response(f"Processed File uploaded {file_name}")


@flask_app.route('/processed/<path:path>')
@cross_origin(origin='*')
def send_processed(path):
    return send_from_directory(processed_directory, path)


@flask_app.route('/source/<path:path>')
@cross_origin(origin='*')
def send_source(path):
    return send_from_directory(source_directory, path)


@flask_app.route("/videos", methods=['GET'])
@cross_origin(origin='*')
def get_video_list():
    sub_folders = [f.path.split("/")[1] for f in os.scandir(processed_directory) if f.is_dir()]
    return make_response({"videos":sub_folders},200)


@flask_app.route("/uploadForm", methods=['GET'])
@cross_origin(origin='*')
def upload_video_form():
    return """<html>
   <body>
      <form action = "http://localhost:5000/uploadSource" method = "POST"
         enctype = "multipart/form-data">
         <input type= "text" name ="video_id"/>
         <input type = "file" name = "file" />
         <input type = "submit"/>
      </form>
   </body>
</html>"""


def __create_disk_folder(directory):
    if not os.path.exists(f"{directory}/"):
        os.makedirs(f"{directory}/")
    return directory


def make_api_response(message: str, status_code=200):
    print(message)
    response = make_response({"message": message}, status_code)
    response.headers.add_header("content-type", "application/json")
    return response


__create_disk_folder(processed_directory)
__create_disk_folder(source_directory)

if __name__ == "__main__":
    flask_app.run(host='0.0.0.0', threaded=True)