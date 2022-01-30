import React from 'react';
import "video.js/dist/video-js.css";
import VideoPlayer from './VideoPlayer';
import VideoList from './VideoList/VideoList';
import './VideoApp.css'
import { useState, useEffect} from 'react';
import { useSelector,useDispatch } from 'react-redux'
import fetch_videos, {video_url} from '../services/videos';
  
  const VideoApp = () =>{

    const [videolist, setVideolist] = useState([]);
    const currentVideo = useSelector((state) => state.currentVideo);
    const dispatch = useDispatch();
    console.log(currentVideo);

    useEffect(() => {
      fetch_videos().then(res=>{
        setVideolist(res);
        dispatch({ type: 'setVideo',payload:res[0] })
      }
      ).catch(e=>{
        console.log(e);
      })
    },[dispatch]);

    if(videolist?.length>0 || currentVideo!==""){

      return(
        <div className="video-app-container">
          <div>
            <div className="up">
            <VideoPlayer url={video_url(currentVideo)} />
            <p className="video-title">{currentVideo}</p>
            </div>
          
            <p className="more-videos">More videos</p>
            <div className="down">
            <VideoList videoIds={videolist}></VideoList>
            </div>
  
          </div>
        </div>
      )
    }
    else{
      return(
      <div className="video-app-container">
        <p>Loading</p>
      </div>
      )
    }
  }

export default VideoApp;