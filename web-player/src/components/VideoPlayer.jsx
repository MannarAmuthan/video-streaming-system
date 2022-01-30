// taken from https://github.com/videojs/video.js/blob/master/docs/guides/react.md
import React from 'react';
import videojs from 'video.js';

export default class VideoPlayer extends React.Component {
  componentDidMount() {

    const videoJsOptions = {
      autoplay: true,
      playbackRates: [0.5, 1, 1.25, 1.5, 2],
      width: 1280,
      height: 720,
      controls: true,
      sources: [
        {
          src: this.props.url,
        },
      ],
    };

    // instantiate video.js
    this.player = videojs(this.videoNode,videoJsOptions,this.props, function onPlayerReady() {
      console.log('onPlayerReady', this);
    });
  }

  // destroy player on unmount
  componentWillUnmount() {
    if (this.player) {
      this.player.dispose();
    }
  }

  componentWillReceiveProps(nextProps) {
    if (nextProps.url !== this.props.url) {
      this.player.src({src: nextProps.url});
    }
  
  }

  // wrap the player in a div with a `data-vjs-player` attribute
  // so videojs won't create additional wrapper in the DOM
  // see https://github.com/videojs/video.js/pull/3856
  render() {
    return (
      <div data-vjs-player>
        <video ref={node => (this.videoNode = node)} className="video-js" />
      </div>
    );
  }
}