import './VideoList.css';
import VideoCard from '../VideoCard';

function VideoList({videoIds}) {
  return (
    <div>
    <div className="video-list">
      {
          videoIds?.map(element => {
            return <VideoCard videoId={element}></VideoCard>
          })
      }
    </div>
    </div>
  );
}

export default VideoList;