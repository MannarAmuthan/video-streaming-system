import os


class ChunkException(Exception):
    def __init__(self, message):
        self.message = message

resolution_bit_rates={
"1080" : 4500000,
"720" : 2500000,
"480" : 1250000,
"360" : 700000,
"240" : 400000,
"144" : 250000
}


resolution_dimensions={
"1080" : [1920,1080],
"720" : [1280,720],
"480" : [854,480],
"360" : [640,360],
"240" : [426,240],
"144" : [256,144]
}


def make_chunks(input_video_path,output_video_path,resolution):
    try:
        if not os.path.exists(f"{output_video_path}/"):
            os.makedirs(f"{output_video_path}/")

        command =  f"ffmpeg -y -i {input_video_path} -codec: copy -start_number 0 -hls_time 10 -hls_list_size 0 -f hls {output_video_path}/{resolution}.m3u8"
        exit_code = os.system(command)
        if exit_code != 0:
            raise Exception(f"FFMPEG Exit code : {exit_code}")
    except Exception as e:
        raise ChunkException(f"Something wrong while chunking {str(e)}")


def create_master_hls(video_path):

    file_template = "#EXTM3U\n#EXT-X-VERSION:3\n"

    resolution_template = "#EXT-X-STREAM-INF:BANDWIDTH={},RESOLUTION={}x{}\n{}.m3u8\n"

    for file in os.listdir(video_path):
        if file.endswith(".m3u8"):
            resolution = file.split(".")[0]
            bandwidth = resolution_bit_rates[resolution]
            width = resolution_dimensions[resolution][0]
            height = resolution_dimensions[resolution][1]
            file_template+=resolution_template.format(bandwidth,width,height,resolution)

    text_file = open(f"{video_path}/master.m3u8", "w")

    text_file.write(file_template)

    text_file.close()




