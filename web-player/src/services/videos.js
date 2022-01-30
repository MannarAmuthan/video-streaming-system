
export const VIDEO_SERVICE_URL=process.env.STORAGE_SERVER_URL || process.env.REACT_APP_STORAGE_SERVER_URL;

export const thumbnail_url=(video_id)=>{
    return `${VIDEO_SERVICE_URL}/processed/${video_id}/thumbnail.png`
}

export const video_url=(video_id)=>{
    return `${VIDEO_SERVICE_URL}/processed/${video_id}/master.m3u8`;
}

async function fetch_videos() {
    try{
    console.log(VIDEO_SERVICE_URL);
    let response = await fetch(VIDEO_SERVICE_URL+"/videos");
    let jsonVideos = await response.json();
    return jsonVideos['videos'];
    }
    catch(e){
        console.log("Something wrong while fetching videos");
    }
}
  
export default fetch_videos;