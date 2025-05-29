import React, { useEffect } from "react";
import "./VideoPlayer.css";

const VideoPlayer = ({ lesson, onWatch }) => {
  useEffect(() => {
    if (lesson) {
      onWatch(lesson);
    }
  }, [lesson]);

  if (!lesson) return <div className="video-area">Select a lesson</div>;

  return (
    <div className="video-area">
      <h2>{lesson.title}</h2>
      <video controls autoPlay src={`/course/${lesson.path}`} />
    </div>
  );
};

export default VideoPlayer;