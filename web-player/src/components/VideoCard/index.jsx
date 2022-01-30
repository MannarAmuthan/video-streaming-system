import { Card } from 'antd';
import './index.css';
import {thumbnail_url} from '../../services/videos'
import { useDispatch } from 'react-redux'

function VideoCard({videoId}) {
    const dispatch = useDispatch()

    return (
        <Card onClick={()=>{
          dispatch({ type: 'setVideo',payload:videoId })
        }}>
          <img
            width="262" 
            height="180"
            alt="example"
            src={thumbnail_url(videoId)}
          />
          <h4>{videoId}</h4>
      </Card>
    );
}

export default VideoCard;