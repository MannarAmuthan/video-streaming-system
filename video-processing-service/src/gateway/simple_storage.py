import os
import shutil
import requests

from Logger import log

video_server_url = os.environ["STORAGE_SERVER_URL"]


def upload_blob(file_name, destination_blob_name):
    dest_file_path=destination_blob_name.split("/")
    video_id=dest_file_path[0]
    files = {'file': open(file_name, 'rb')}
    response = requests.post(f'{video_server_url}/uploadProcessed', files=files,data={"video_id":video_id})
    if response.status_code<200 or response.status_code>299:
        raise Exception(f"Not able to upload {response.content}")


def download_blob(source_blob_name, destination_file_name):
    url = f'{video_server_url}/source/{source_blob_name}'
    log(f"Downloading... {source_blob_name} for processing ", "INFO")
    response = requests.get(url, stream=True)
    with response as r:
        with open(destination_file_name, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
    log(f"Downloaded... {source_blob_name} for processing ", "INFO")
    return destination_file_name